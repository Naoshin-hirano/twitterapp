<template>
    <div>
      <div class="container">
          <div class="overlay" v-show="opened" @click="toggle"></div>
          <div class="contents">
              <div class="page-title">
                <h2>ホーム</h2>
              </div>
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
                <div @click.prevent="toggle(post.id)" class="down-icon">
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
              <ListModal
              :id="id"
              v-if="opened"
              @click-delete="deleteData"
              class="list-modal"/>
          </div>
      </div>
    </div>
</template>

<script>
import { apiService } from '../../common/api.service.js'
import ListModal from '../../components/ListModal.vue'

export default {
  name: "list",
  components: {
    ListModal
  },
  data(){
    return {
      posts: [],
      content: null,
      opened: false,
      id:null
    }
  },
  methods: {
    toggle(pk){
        this.opened =! this.opened
        this.id = pk
        console.log("id:" + this.id)
      },
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
    },
    deleteData(id){
      let endpoint = `/api/tweets/${id}/`;
      apiService(endpoint, "DELETE")
      .then(() => {
        const post = this.posts.find(post => post.id === id)
        const index = this.posts.indexOf(post)
        this.posts.splice(index, 1)
        console.log("削除されてるid:" + index)
      })
      .then(() =>{
        this.opened = false
      })
    }
  },
  created(){
    this.getPost()
  }
};
</script>

<style scoped>
.post{
  position:relative;
  border: 1px black solid;
  height:150px;
}
.list-modal{
  position: absolute;
  z-index:5;
}
.modal_opened {
    display:block;
}
h2{
  margin:5px;
}
.textField{
    margin-bottom:70px;
}
textarea{
    width:70%;
    font-size:17px;
    z-index: 1;
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
  border-radius: 50%;
  background-color:white;
  opacity:0.8;
  color:#a9a9a9;
}
.down-icon:hover{
  background-color:#e0ffff;
}

.overlay{
  position: absolute;
  left: 0; 
  top: 0;
  width: 100%; height: 100%;
  background: rgba(100, 100, 100, .8);
  z-index: 2;
}

</style>