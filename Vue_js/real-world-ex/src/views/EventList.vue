<template>
<div>
  <h1>List</h1>
  <EventCard v-for="event in events" :key="event.id" :event="event" />  
</div>
</template>

<script>
import axios from "axios";
import EventCard from '@/components/EventCard';
export default {
  components: {
    EventCard
  },
  data() {
    return{
      events: []
    }
  },
  created() {
    axios
    .get('http://localhost:3000/events')
    .then( res => {
      console.log(res)
      this.events = res.data
    })
    .catch( err => {
      console.log(err)
    })
  }
}
</script>

<style scoped>

</style>