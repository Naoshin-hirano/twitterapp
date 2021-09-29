<template>
  <div id="app">
    <div class="header">
        <h3>Daily Notes</h3>
    </div>
    <div class="menu">
        <div class="user-info">
            <h4>Naoya Hirano</h4>
            <img src="https://www.newsweekjapan.jp/stories/assets_c/2021/04/webs210427_climate-thumb-720xauto-249046.jpeg" alt="">
        </div>
        <div>
            <ul>
                <li>投稿</li>
                <li>ユーザー</li>
                <li>プロフィール</li>
                <li>Daily Notesへようこそ</li>
                <li>ログアウト</li>
                <li>アカウントを削除</li>
                <li>利用規約</li>
                <li>プライバシーポリシー</li>
                <li>アプリの脆弱性を報告する</li>
            </ul>
        </div>
    </div>
    <div class="container">
      <router-view class="router"/>
    </div>
  </div>
</template>

<style scoped>
.header{
  background-color:#0095d9;
  color:white;
  padding:1px 50px;
  width:100%;
}

.menu{
    background-color:#1E90FF;
    width:30%;
    float:left;
    height:900px;
    color:white;
}
.container{
  float:right;
  width:70%;
}
.user-info{
    text-align: center;
    margin-top:50px;
    margin-bottom:50px;
}
.user-info img{
  vertical-align: middle;
  width: 100px;
  height: 100px;
  border-radius: 50%;
}
ul li{
    list-style: none;
    padding-top:40px;
}
</style>