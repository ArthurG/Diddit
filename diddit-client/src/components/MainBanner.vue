<template>
  <div class="container">
    <div class="phone col-lg-4 col-md-6">
      <img src="../assets/phone.png">
    </div>
    <div class="ad-detail col-lg-8 col-md-6">
      <div class="ad-detail-text">
        <h1>Create seamless survey experiences</h1>
        <p><a href="#" class="learn-more">Learn More</a> How does Diddit work?</p>
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

.container{
  border: 1px solid red;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-flex-wrap: wrap;
  -ms-flex-wrap: wrap;
  flex-wrap: wrap;
  padding: 20px;
}

.phone{
  flex: 1;
  height: 100%;
}
.ad-detail{
  text-align: left;
  padding: auto;
  display: flex;
  display: -webkit-flex;
  display: -ms-flexbox;
  align-items: center;
}

.learn-more{
  color: white;
  background-color: black;
}


</style>
