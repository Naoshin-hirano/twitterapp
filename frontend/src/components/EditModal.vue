<template>
    <div 
    class="modal">
      <div class="container">
        <div class="page-title">
            <h2>Daily Noteの編集</h2>
        </div>
        <div class="textField">
            <form @submit.prevent="onUpdate(content)">
                <textarea
                v-model="content"
                placeholder="いまどうしてる？">
                </textarea>
                <div class="postMessage">
                    <button type="onUpdate">更新する</button>
                </div>
            </form>
        </div>
      </div>
    </div>
</template>

<script>
export default {
    props: ["editContent"],
    data(){
        return{
            content: this.editContent    
        }
    },
    methods: {
        onUpdate(content){
            this.$emit('click-update', content)
        }
    }
}
</script>

<style scoped>
.container{
    margin:0 15px;
}
.modal{
    width:600px;
    height: 300px;
    border:1px solid black;
    z-index:5;
    position: absolute;
    left: 50%;
    top:30%;
    background-color:white;
    transform: translate(-50%, -50%);
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
textarea{
    width:100%;
    font-size:17px;
    z-index: 1;
}

ul{
   list-style: none;
}
ul li{
  padding-top:20px;
}

</style>