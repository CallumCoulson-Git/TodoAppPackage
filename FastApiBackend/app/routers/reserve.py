from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from typing_extensions import Annotated
from app.database import get_session
from app.models import Reserve, User
from dateutil.parser import isoparse

router = APIRouter()

@router.post("/reserve/")
def create_reserve(reserve: Reserve, user_id: int, session: Annotated[Session, Depends(get_session)]) -> Reserve:
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if isinstance(reserve.set_for, str):
        reserve.set_for = isoparse(reserve.set_for)
    reserve.owner = user
    session.add(reserve)
    session.commit()
    session.refresh(reserve)
    return reserve

@router.get("/reserve/")
def read_reserves(
    session: Annotated[Session, Depends(get_session)],
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[Reserve]:
    reserves = session.exec(select(Reserve).offset(offset).limit(limit)).all()
    return reserves

@router.get("/reserve/{reserve_id}")
def read_reserve(reserve_id: int, session: Annotated[Session, Depends(get_session)]) -> Reserve:
    reserve = session.get(Reserve, reserve_id)
    if not reserve:
        raise HTTPException(status_code=404, detail="Reserve not found")
    return reserve

@router.get("/user/{user_id}/reserves")
def read_user_reserves(user_id: int, session: Annotated[Session, Depends(get_session)]) -> list[Reserve]:
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user.reserves

@router.put("/reserve/{reserve_id}")
def update_reserve(reserve_id: int, updated_reserve: Reserve, session: Annotated[Session, Depends(get_session)]) -> Reserve:
    reserve = session.get(Reserve, reserve_id)
    if not reserve:
        raise HTTPException(status_code=404, detail="Reserve not found")
    reserve_data = updated_reserve.dict(exclude_unset=True)
    if 'set_for' in reserve_data and isinstance(reserve_data['set_for'], str):
        reserve_data['set_for'] = isoparse(reserve_data['set_for'])
    for key, value in reserve_data.items():
        setattr(reserve, key, value)
    session.add(reserve)
    session.commit()
    session.refresh(reserve)
    return reserve

@router.delete("/reserve/{reserve_id}")
def delete_reserve(reserve_id: int, session: Annotated[Session, Depends(get_session)]):
    reserve = session.get(Reserve, reserve_id)
    if not reserve:
        raise HTTPException(status_code=404, detail="Reserve not found")
    session.delete(reserve)
    session.commit()
    return {"message": "Reserve deleted successfully"}
