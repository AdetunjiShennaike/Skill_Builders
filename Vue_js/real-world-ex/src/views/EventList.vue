<template>
<div>
  <h1>List</h1>
  <EventCard v-for="event in events" :key="event.id" :event="event" />  
</div>
</template>

<script>
import EventService from "@/services/EventService";
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
    EventService
    .getEvents()
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