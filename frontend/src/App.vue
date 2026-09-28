<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">民航机务航线维护平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向航空器适航状态、时控项目到期、定检工作包编排、维修放行签署与维修差错整改的一体化机务维修后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "航空器", path: "/aircraft" }, { label: "适航指令", path: "/ad" }, { label: "时控项目", path: "/timeditem" }, { label: "航线维护", path: "/linemaint" }, { label: "定检工作包", path: "/checkpack" }, { label: "维修工卡", path: "/card" }, { label: "航材领用", path: "/material" }, { label: "维修人员执照", path: "/license" }, { label: "维修记录", path: "/record" }, { label: "缺陷保留", path: "/defecthold" }, { label: "放行签署", path: "/release" }, { label: "试车检查", path: "/enginetest" }, { label: "无损探伤", path: "/ndt" }, { label: "客舱维护", path: "/cabin" }, { label: "发动机孔探", path: "/borescope" }, { label: "起落架维护", path: "/gear" }, { label: "维修差错", path: "/error" }, { label: "维修单位资质", path: "/org" }]
</script>
