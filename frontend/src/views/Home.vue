<template>
  <div class="container">
    <h1>Twitter App</h1>
    <div v-for="post in posts" :key="post.pk" class="post">
      <p>ユーザー: {{ post.creator }}</p>
      <p>ツイート内容: {{ post.content }}</p>
    </div>
  </div>
</template>

<script>
import { apiService } from '../common/api.service.js'
export default {
  name: "Home",
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
.post{
  border: 1px black solid;
}
</style>