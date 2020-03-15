<template>
  <div class="home">
    <button @click="toggleModal">Open</button>
    <!-- adding fade as a name, makes it so that you can just use fade as the transistion name in the styling -->
    <transition name="fade">
      <div v-if="isOpen" class="modal">
        <button @click="toggleModal">Close</button>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isOpen: false
    }
  },
  methods: {
    toggleModal() {
      this.isOpen = !this.isOpen
    }
  }
}
</script>

