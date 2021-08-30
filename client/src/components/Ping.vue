<template>
    <div>
      <p>{{msg}}</p>
      <p>Test message of Ping component</p>  
      <div style="margin: 10px">
        <p>
          <router-link :to="{name:'HelloWorld'}">To HelloWorld</router-link>
        </p>
    </div>
    </div>
</template>
<script>
export default {
    name: 'Ping',
    data() {
        return {
            msg:'Ping works!'
        }
    }
}
</script>
<style>
    
</style>