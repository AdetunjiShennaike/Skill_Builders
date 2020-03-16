<template>
  <div>
    <button @click="isOpen = !isOpen">
      My Profile
    </button>

    <transition
      @before-enter = 'beforeEnter'
      @enter = 'enter'
      @leave = 'leave'
      :css="false"
    >
      <div v-if="isOpen" class="drawer">
        <img src="../assets/avatar.png" alt="avatar" />
        <div></div>
        <div></div>
        <div></div>
        <div></div>
      </div>
    </transition>
  </div>
</template>

<script>
// library for sliding animations, with controlled velocity
import Velocity from 'velocity-animate'
export default {
  data() {
    return {
      isOpen: false
    }
  },
  methods: {
    beforeEnter(e) {
      e.style.opacity = 0
      e.style.width = '0em'
    },
    enter(e, done) {
      Velocity(
        e,
        {opacity: 1, width: '12em'},
        // just an Array in velocity makes a spring effect/physics
        {duration: 1000, easing: [60,10], complete: done}
      )
    },
    leave(e, done) {
      Velocity(
        e,
        {opacity: 0, width: '0em'},
        {duration: 500, easing: 'easeInCubic', complete: done}
      )
    }
  }
}
</script>

<style scoped>
  img {
    height: 2.5em;
    width: 2.5em;
    border-radius: 50%;
  }

  .drawer {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 12em;
    height: 20em;
    border-radius: 1%;
    background-color: #e0e0e0;
    box-shadow: 0.08em 0.03em 0.4em #ababab;
    padding-top: 0.7em;
  }
  .drawer div {
    height: 3.5em;
    width: 95%;
    margin-top: 0.6em;
    background-color: #f0f0f0;
    border: 0.02em solid #ababab;
    border-radius: 1%;
  }
</style>

//  Example of all the types of trigger methods that can be called
// <transition
//   @before-enter="beforeEnter"
//   @enter="enter"
//   @after-enter="afterEnter"
//   @enter-cancelled="enterCancelled"

//   @before-leave="beforeLeave"
//   @leave="leave"
//   @after-leave="afterLeave"
//   @leave-cancelled="leaveCancelled"
// >
//   <!-- ... -->
// </transition>