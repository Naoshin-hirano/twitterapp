<template>
  <div>
    <Menu class="menu"/>
    <div class="container">
      <div class="header">
        <h3>Daily Notes</h3>
      </div>
      <div v-for="post in posts" :key="post.pk" class="post">
        <router-link
          :to="{ name: 'tweet', params: { id: post.id } }"
          class="tweet-link">
          <p>ユーザー: {{ post.creator }}</p>
          <p>ツイート内容: {{ post.content }}</p>
        </router-link>
      </div>
    </div>
</div>
</template>

<script>
import { apiService } from '../../common/api.service.js'
import Menu from './Menu.vue'
export default {
  name: "list",
  components: {
    Menu
  },
  data(){
    return {
      posts: []
    }
  },
  methods: {
    getPost(){
      let endpoint = `api/tweets/`
      apiService(endpoint).then(data => {
        this.posts.push(...data.results)
      })
    }
  },
  created(){
    this.getPost()
    console.log(this.posts)
  }
};
</script>

<style scoped>
.container{
  float:right;
  width:70%;

}
.menu{
  float:left;
  width:30%;
  height:900px;
  color:white;
}
.header{
  background-color:#0095d9;
  color:white;
  padding:1px 50px;
}
.post{
  border: 1px black solid;
}
</style>