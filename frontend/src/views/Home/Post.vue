<template>
    <div class="container">
        <textarea>
          いまどうしてる？
        </textarea>
        <div class="postMessage">
            <a href="#">投稿する</a>
        </div>
    </div>
</template>

<style scoped>
.container{
    margin-bottom:70px;
}
textarea{
    width:600px;
    font-size:17px;
}
.postMessage{
    text-align: center;
}
.postMessage a{
    background-color:#0095d9;
    text-decoration: none;
    color:white;
    width:200px;
    padding:10px 20px;
    float:right;
    border-radius:5px;
}
</style>