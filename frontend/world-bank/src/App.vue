<template>
  <a-layout id="components-layout-top" class="layout">
    <a-layout-header>
      <div class="logo" />
      <a-menu
        theme="dark"
        mode="horizontal"
        :defaultSelectedKeys="['1']"
        :style="{ lineHeight: '64px' }"
      >
        <a-menu-item key="1"> <router-link to="/">World Bank Data</router-link></a-menu-item>
        <a-menu-item key="3"><router-link to="/about">About</router-link></a-menu-item>
      </a-menu>
    </a-layout-header>
    <a-layout-content style="padding: 0 50px">
      <router-view />
    </a-layout-content>
    <a-layout-footer style="text-align: center">Using data from <a href="https://data.worldbank.org/"  target="_blank">World Bank Data</a> | Created by Luccas Quadros</a-layout-footer>
  </a-layout>
</template>
