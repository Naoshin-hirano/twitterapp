import Vue from "vue";
import VueRouter from "vue-router";
import List from "../views/Home/List.vue";
import Tweet from "../views/Tweet/Tweet.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "list",
    component: List,
  },
  {
    path: "/tweet/:id",
    name: "tweet",
    component: Tweet,
    props: true
  }
];

const router = new VueRouter({
  mode: "history",
  routes,
});

export default router;
