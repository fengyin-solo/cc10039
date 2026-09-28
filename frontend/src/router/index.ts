import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const Aircraft = () => import('@/views/aircraft/index.vue')
const Ad = () => import('@/views/ad/index.vue')
const Timeditem = () => import('@/views/timeditem/index.vue')
const Linemaint = () => import('@/views/linemaint/index.vue')
const Checkpack = () => import('@/views/checkpack/index.vue')
const Card = () => import('@/views/card/index.vue')
const Material = () => import('@/views/material/index.vue')
const License = () => import('@/views/license/index.vue')
const Record = () => import('@/views/record/index.vue')
const Defecthold = () => import('@/views/defecthold/index.vue')
const Release = () => import('@/views/release/index.vue')
const Enginetest = () => import('@/views/enginetest/index.vue')
const Ndt = () => import('@/views/ndt/index.vue')
const Cabin = () => import('@/views/cabin/index.vue')
const Borescope = () => import('@/views/borescope/index.vue')
const Gear = () => import('@/views/gear/index.vue')
const Error = () => import('@/views/error/index.vue')
const Org = () => import('@/views/org/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/aircraft', name: 'aircraft', component: Aircraft },
    { path: '/ad', name: 'ad', component: Ad },
    { path: '/timeditem', name: 'timeditem', component: Timeditem },
    { path: '/linemaint', name: 'linemaint', component: Linemaint },
    { path: '/checkpack', name: 'checkpack', component: Checkpack },
    { path: '/card', name: 'card', component: Card },
    { path: '/material', name: 'material', component: Material },
    { path: '/license', name: 'license', component: License },
    { path: '/record', name: 'record', component: Record },
    { path: '/defecthold', name: 'defecthold', component: Defecthold },
    { path: '/release', name: 'release', component: Release },
    { path: '/enginetest', name: 'enginetest', component: Enginetest },
    { path: '/ndt', name: 'ndt', component: Ndt },
    { path: '/cabin', name: 'cabin', component: Cabin },
    { path: '/borescope', name: 'borescope', component: Borescope },
    { path: '/gear', name: 'gear', component: Gear },
    { path: '/error', name: 'error', component: Error },
    { path: '/org', name: 'org', component: Org },
  ],
})

export default router
