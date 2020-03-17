<template>
  <div id="nav" class="nav
  ">
    <router-link to='/' class="brand">Real World Events </router-link>

    <nav>
      <router-link :to="{ name: 'list' }">List</router-link> |
      <router-link :to="{ name: 'create' }">Create</router-link> 

    </nav>
    </div>
</template>