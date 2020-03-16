import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import List from "./views/List.vue";
import Drawer from "./views/Drawer.vue";
import Simple from "./views/Simple.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/list",
      name: "list",
      component: List
    }, 
    {
      path: "/drawer",
      name: "drawer",
      component: Drawer
    }, 
    {
      path: "/simple",
      name: "simple",
      component: Simple
    }, 
    {
      path: "/stagger",
      name: "stagger",
      component: () =>
        import(/* webpackChunkName: "about" */ "./views/Stagger.vue")
    }, 
    {
      path: "/card",
      name: "card",
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () =>
        import(/* webpackChunkName: "about" */ "./views/Card.vue")
    },
    {
      path: "/about",
      name: "about",
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () =>
        import(/* webpackChunkName: "about" */ "./views/About.vue")
    }
  ]
});
