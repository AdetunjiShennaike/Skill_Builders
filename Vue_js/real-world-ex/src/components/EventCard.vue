<template>
  <router-link :to="{ name: 'show', params: { id: '1' } }" class="event-link">
    <div class="event-card -shadow">
      <span class="eyebrow">@{{ event.time }} on {{ event.date }}</span>
      <h4 class="title">{{ event.title }}</h4>
      <span>{{ event.attendees.length }} attending</span>
    </div> 
  </router-link>
</template>

<script>

export default {
  data() {
    return{
      event: {
        id: 1,
        title: 'Park Cleanup',
        date: 'Tues Aug 12, 2019',
        time: '9:00',
        attendees: [
          { id: 'something', name: 'James Bond'},
          { id: 'somethingelse', name: 'Craig'}
        ]
      }
    }
  }
  
}
</script>

<style scoped>
/* scoped prevents the styles from flowing to other components */
h4 {
  color: green
}
.event-card {
  padding: 20px;
  margin-bottom: 24px;
  transition: all 0.2s linear;
  cursor: pointer;
}
.event-card:hover {
  transform: scale(1.01);
  box-shadow: 0 3px 12px 0 rgba(0, 0, 0, 0.2), 0 1px 15px 0 rgba(0, 0, 0, 0.19);
}
.event-card > .title {
  margin: 0;
}

.event-link {
  color: black;
  text-decoration: none;
  font-weight: 100;
}
</style>