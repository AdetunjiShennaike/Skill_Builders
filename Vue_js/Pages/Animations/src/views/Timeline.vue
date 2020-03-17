<template>
  <div>
    <img class="runner first" src="../assets/runner.png" alt="runner" />
    <img class="runner second" src="../assets/runner.png" alt="runner" />
    <img class="runner third" src="../assets/runner.png" alt="runner" />
  </div>
</template>
<script>
import gsap from 'gsap'
export default {
  mounted() {
    // create a timeline to make sequenced movements with animations
    // you can add options to the timeline such as repeat in the timeline method
    let timeline = gsap.timeline({ repeat: -3 })
    // adding a number after the object tells it when to start the animation 
    timeline.to('.first', { x: 200, duration: 4, ease: 'expo.out' })
    // -= on th eoutside of the object moves it back into the previous animation by that amount
    timeline.to('.second', { x: 450, duration: 3, ease: 'expo.out' }, '-=3')
    // < makes the animation start at the same time as the previous animation 
    timeline.to('.third', { x: 700, duration: 2, ease: 'expo.out' }, '<')
    // adding a number after < you can add a delay
  }
}
</script>
<style scoped>
.runner {
  display: block;
  height: 5em;
  width: 5em;
  margin-top: 1.5em;
}
</style>