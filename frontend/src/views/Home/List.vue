<template>
  <div>
    <h2>ホーム</h2>
    <div class="container">
      <div class="textField">
        <form @submit.prevent="onSubmit">
            <textarea
            v-model="content"
            placeholder="いまどうしてる？">
            </textarea>
            <div class="postMessage">
                <button type="onSubmit">投稿する</button>
            </div>
        </form>
      </div>
      <div v-for="post in posts" :key="post.pk" class="post">
        <div class="down-icon">
            <font-awesome-icon icon="angle-down" size="2x"/>
        </div>
        <div class="router-container">
          <router-link
          :to="{ name: 'tweet', params: { id: post.id } }"
          class="tweet-link">
          <p>ツイート内容: {{ post.content }}</p>
          </router-link>
        </div>
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
      posts: [],
      content: null
    }
  },
  methods: {
    getPost(){
      let endpoint = `api/tweets/`
      apiService(endpoint).then(data => {
        this.posts.push(...data.results)
      })
    },
    onSubmit(){
        let endpoint = `/api/tweets/`;
        let method = "POST";
        apiService(endpoint, method, {
            content: this.content
        }).then((data) => {
          this.posts.unshift(data)
          this.content = ''
        })
    }
  },
  created(){
    this.getPost()
  }
};
</script>

<style scoped>
h2{
  margin:5px;
}
.post{
  border: 1px black solid;
}

.textField{
    margin-bottom:70px;
}
textarea{
    width:70%;
    font-size:17px;
}
.postMessage{
    text-align: center;
}
.postMessage button{
    background-color:#0095d9;
    text-decoration: none;
    color:white;
    width:100px;
    padding:10px 20px;
    float:right;
    border-radius:20px;
}

.down-icon{
  float:right;
  padding:5px 20px;
}

</style>