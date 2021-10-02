<template>
    <div class="modal">
        <div class="menu">
          <ul>
            <li class="delete">削除</li>
            <li>プロフィールに固定する</li>
            <li>naoyaさんをリストに追加/削除</li>
            <li>返信できるユーザーを変更</li>
            <li>ツイートを埋め込む</li>
            <li>ツイートアクティビティを表示</li>
          </ul>
        </div>
    </div>
</template>

<style scoped>
.modal{
    width:300px;
    height:330px;
    border:1px solid black;
    z-index:5;
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 600px;
    margin: auto;
    background-color:white;
}
.delete{
  color:red;
}
ul{
   list-style: none;
}
ul li{
  padding-top:20px;
}
/* .entry a{
    width:200px;
    background-color:#1E90FF;
    color:white;
    padding:20px 65px;
    text-decoration: none;
    border-radius: 5px;
}
.entry{
    text-align:right;
}
.entry a:hover{
    background-color:#4169E1;
}
label{
    margin-left:20px;
} */
</style>