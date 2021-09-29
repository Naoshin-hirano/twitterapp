<template>
  <div>
    <div class="container">
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
export default {
  name: "list",
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