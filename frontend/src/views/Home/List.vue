<template>
    <div>
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
        <div
        class="down-icon"
        @click="toggle">
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
      v-if="opened"
      @hide-modal="hide"
      class="list-modal"/>
    </div>
</template>

<script>
import { apiService } from '../../common/api.service.js'
// import ListModal from '../../components/ListModal.vue'
import ListModal from '../../components/ListModal2.vue'
// import ClickOutside from 'vue-click-outside'

export default {
  name: "list",
  components: {
    ListModal
  },
  // directives: {
  //     ClickOutside
  //   },
  // mounted () {
  //     // prevent click outside event with popupItem.
  //     this.popupItem = this.$el
  //   },
  data(){
    return {
      posts: [],
      content: null,
      opened: false
    }
  },
  methods: {
    toggle(){
        this.opened = true
      },
    hide() {
        this.opened = false
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
    }
  },
  created(){
    this.getPost()
  }
};
</script>

<style scoped>
/* .container{
  left: 0; 
  top: 0;
  width: 100%; 
  height: 100%;
  background: rgba(100, 100, 100, .8);
} */
.modal_opened {
    display:block;
}
h2{
  margin:5px;
}
.post{
  border: 1px black solid;
  height:150px;
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

</style>