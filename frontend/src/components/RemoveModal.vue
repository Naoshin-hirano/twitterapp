<template>
    <div class="removeModal">
        <div class="container">
            <div class="message">
                <h3>投稿を削除しますか？</h3>
                <p>
                 この操作は取り消せません。プロフィール、あなたをフォローしているアカウントのタイムライン、Twitterの検索結果からツイートが削除されます。 
                </p>
            </div>
            <div class="btn-wrapper">
                <div class="btn remove">
                    削除
                </div>
                <div class="btn cancel">
                    キャンセル
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
h3{
    margin-bottom: 0px;
}
.container{
    margin:0 30px;
    padding-top:20px;
}
.removeModal{
    width:320px;
    height: 320px;
    border:1px solid black;
    z-index:5;
    position: absolute;
    left: 50%;
    top:50%;
    background-color:white;
    transform: translate(-50%, -50%);
    border-radius: 20px;
}
.message p{
    font-size: 0.9rem;
}
.btn-wrapper{
    text-align: center;
}
.remove{
    margin-top:30px;
    background: red;
    color:white;
}
.remove:hover{
    background:#dc143c;
}
.cancel{
    background:white;
    border:1px solid black;
    color:black;
}
.cancel:hover{
    background:#f5f5f5;
}
.btn{
    width:100%;
    height: 40px;
    border-radius:50px;
    text-decoration: none;
    line-height:40px;
    margin-bottom:13px;
    cursor : pointer;
}


</style>