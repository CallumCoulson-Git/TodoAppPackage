import { createWebHashHistory , createRouter } from 'vue-router'

import MainContent from './components/MainContent.vue'
import LoginForm from './components/LoginForm.vue'
import Manage from './components/Manage/Manage.vue'
import Database from './components/LoginForm.vue'
import RegisterForm from './components/RegisterForm.vue'

const routes = [
  { path: '/', component: MainContent },
  { path: '/login', component: LoginForm },
  { path: '/manage', component: Manage },
  { path: '/database', component: Database },
  { path: '/register', component: RegisterForm },
]

const router = createRouter({
  history: createWebHashHistory (),
  routes,
})

export default router