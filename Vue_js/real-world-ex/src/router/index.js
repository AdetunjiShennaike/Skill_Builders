import Vue from "vue";
import VueRouter from "vue-router";
import EventCreate from '../views/EventCreate'
import EventList from '../views/EventList'
import EventShow from '../views/EventShow'
Vue.use(VueRouter);

const routes = [
  {
    path: '/event',
    name: 'show',
    component: EventShow
  },
  {
    path: '/',
    name: 'list',
    component: EventList
  },
  {
    path: '/event/create',
    name: 'create',
    component: EventCreate
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
