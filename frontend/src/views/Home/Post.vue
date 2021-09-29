<template>
    <div class="container">
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
</template>

<script>
import { apiService } from "../../common/api.service.js"
export default {
    name: "TweetPost",
    data(){
        return {
            content: null,
            error: null
        }
    },
    methods: {
        onSubmit(){
            let endpoint = `/api/tweets/`;
            let method = "POST";
            apiService(endpoint, method, {
                content: this.content
            }).then( post_data =>{
                this.$router.push({
                    name: 'tweet',
                    params: {id: post_data.id }
                })
            })
        }
    }
}
</script>

<style scoped>
.container{
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
</style>