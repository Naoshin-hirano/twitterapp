<template>
    <div 
    class="modal">
        <div class="menu">
          <ul>
            <li class="delete" @click.prevent="remove">削除</li>
            <li @click.prevent="openEdit">編集</li>
            <li>プロフィールに固定する</li>
            <li>naoyaさんをリストに追加/削除</li>
            <li>返信できるユーザーを変更</li>
            <li>ツイートを埋め込む</li>
            <li>ツイートアクティビティを表示</li>
          </ul>
        </div>
    </div>
</template>

<script>
export default {
  props: {
      id: {
        type: Number,
        required: true,
        default: 0
    }
  },
  methods: {
    remove(){
      this.$emit('click-delete', this.id)
    },
    openEdit(){
      this.$emit('click-edit')
    }
  }
}
</script>

<style scoped>
.modal{
    width:300px;
    height:330px;
    border:1px solid black;
    z-index:5;
    position: absolute;
    top: 40%;
    left: 90%;
    background-color:white;
    transform: translate(-80%, -20%);
}
.xmark{
    text-align: right;
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

</style>