<template>
  <div>
<input type="text" v-model="message"/> <br></br>
  HI there {{message}}
</div>
</template>

<script>
export default {
  data(){
    return{
      message:''
    }
  }
}
</script>
