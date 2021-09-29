<template>
  <div class="container">
    <h2>ツイート</h2>
    <p>ツイート: {{ post.content }}</p>
  </div>
</template>

<script>
import { apiService } from '../../common/api.service.js'
export default {
  name: 'tweet',
  props: {
    id: {
      type: Number,
      required: true,
      default: 0
    }
  },
  data(){
    return {
      post: {}
    }
  },
  methods: {
    setPageTitle(title){
      document.title = title;
    },
    getPostData(){
      let endpoint = `/api/tweets/${this.id}/`;
      console.log("id:" + this.id)
      apiService(endpoint).then(data => {
        this.post = data;
        this.setPageTitle(data.content)
      })
    }
  },
  created(){
    this.getPostData()
  }
}
</script>