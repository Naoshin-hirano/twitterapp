<template>
    <div 
    class="modal">
        <div class="xmark" @click.prevent="close">
            <svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="circle-xmark" class="svg-inline--fa fa-circle-xmark" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="currentColor" d="M336.1 175c-9.375-9.375-24.56-9.375-33.94 0L256 222.1L208.1 175c-9.375-9.375-24.56-9.375-33.94 0s-9.375 24.56 0 33.94l47.03 47.03L175 303c-9.375 9.375-9.375 24.56 0 33.94c9.373 9.373 24.56 9.381 33.94 0L256 289.9l47.03 47.03c9.373 9.373 24.56 9.381 33.94 0c9.375-9.375 9.375-24.56 0-33.94l-47.03-47.03l47.03-47.03C346.3 199.6 346.3 184.4 336.1 175zM256 0C114.6 0 0 114.6 0 256s114.6 256 256 256S512 397.4 512 256S397.4 0 256 0zM256 464c-114.7 0-208-93.31-208-208S141.3 48 256 48s208 93.31 208 208S370.7 464 256 464z"></path></svg>
        </div>
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
<script>
// import ClickOutside from 'vue-click-outside'
export default {
  // props: {
  //   id: {
  //     type: Number,
  //     required: true,
  //     default: 0
  //   }
  // },
//   directives: {
//       ClickOutside
//     },
//   mounted () {
//       // prevent click outside event with popupItem.
//       this.popupItem = this.$el
//     },
//   data(){
//     return {
//         opened: false
//     }
//   },
  methods: {
    close(){
        this.$emit('hide-modal')
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
    top: 0;
    right: 0;
    bottom: 0;
    left: 600px;
    margin: auto;
    background-color:white;
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