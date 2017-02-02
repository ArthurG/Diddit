<template>
  <div class="container-fluid">
    <div class="container" id="analytics">
      <h1>
        Your storefront console
      </h1>
      <div class="vid-placeholder">

      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: 'TopNav'
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

h1{
  color: white;
}

.container-fluid{
  background-color: black;
}
.container{
  border: 2px solid blue;
}

.vid-placeholder{
  height: 600px;
  background-color: white;
  margin: 5% 5%;
}



</style>
