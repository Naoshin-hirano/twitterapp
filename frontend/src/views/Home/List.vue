<template>
  <div>
    <div class="container">
      <Post key=""/>
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
import Post from './Post.vue'
export default {
  name: "list",
  components: {
    Post
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
.post{
  border: 1px black solid;
}
</style>