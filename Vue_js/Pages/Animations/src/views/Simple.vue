<template>
  <transition 
    appear 
    @before-enter="beforeEnter" 
    @enter="enter" 
    :css="false"
  >
    <div class="card"></div>
  </transition>
</template>

<script>
import gsap from 'gsap'
export default {
  methods: {
    beforeEnter(elem) {
      elem.style.opacity = 0
      elem.style.transform = 'scale(0,0)'
    },
    // First input is what's being animated, second is an object of what type of animation to do
    // To method tells it where to go to
    enter(elem, done) {
      gsap.to(elem, {
        duration: 1,
        opacity: 1,
        scale: 1,
        ease: 'bounce.out',
        onComplete: done
      })
    }
  }
}
</script>

<style scoped>
  .card {
    display: block;
    margin: 0 auto 0 auto;
    height: 6.5em;
    width: 6.5em;
    border-radius: 1%;
    background-color: #16c0b0;
    box-shadow: 0.08em 0.03em 0.4em #ababab;
  }
</style>