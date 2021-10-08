<template>
    <div>
      <div class="container">
          <div class="overlay" v-show="opened" @click="toggle"></div>
          <div class="gray-overlay" v-show="editOpened" @click="editToggle"></div>
          <div class="gray-overlay" v-show="removeOpened" @click="removeToggle"></div>
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
                <div @click.prevent="toggle(post.id, post.content)" class="down-icon">
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
              @click-delete="removeToggle"
              @click-edit="editToggle"
              class="list-modal"/>
              <EditModal
              :editContent="editContent"
              v-if="editOpened"
              @click-update="onUpdate"
              class="edit-modal"/>
              <RemoveModal
              v-if="removeOpened"/>
          </div>
      </div>
    </div>
</template>

<script>
import { apiService } from '../../common/api.service.js'
import ListModal from '../../components/ListModal.vue'
import EditModal from '../../components/EditModal.vue'
import RemoveModal from '../../components/RemoveModal.vue'

export default {
  name: "list",
  components: {
    ListModal, EditModal, RemoveModal
  },
  data(){
    return {
      posts: [],
      content: null,
      opened: false,
      editOpened: false,
      removeOpened: true,
      id:null,
      editContent: null
    }
  },
  methods: {
    toggle(pk, editContent){
        this.opened =! this.opened
        this.id = pk
        this.editContent = editContent
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
          console.log("投稿できました")
        })
    },
    onUpdate(updatedContent){
      let endpoint = `/api/tweets/${this.id}/`;
      let method = "PUT";
      this.content = updatedContent
      apiService(endpoint, method, {
        content: this.content
      }).then(data => {
        const post = this.posts.find(post => post.id === data.id)
        post.content = data.content
        this.editOpened = false
        console.log("更新できました")
      })
    },
    deleteData(id){
      let endpoint = `/api/tweets/${id}/`;
      apiService(endpoint, "DELETE")
      .then(() => {
        const post = this.posts.find(post => post.id === id)
        const index = this.posts.indexOf(post)
        this.posts.splice(index, 1)
        console.log("削除できました")
      })
      .then(() =>{
        this.opened = false
      })
    },
    editToggle(){
      this.editOpened =! this.editOpened
    },
    removeToggle(){
      this.removeOpened =! this.removeOpened
    },
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
.edit-modal{
  position: absolute;
  z-index:11;
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
  background: rgba(0, 0, 255, 0);
  z-index: 2;
}
.gray-overlay{
  position: absolute;
  left: 0; 
  top: 0;
  width: 100%; height: 100%;
  background: rgba(100, 100, 100, .8);
  z-index: 4;
}

</style>