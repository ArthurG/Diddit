<template>
  <div class="navbar navbar-default " role="navigation">
    <div class="container">
        <div class="navbar-header"><img class="navbar-brand" src="../assets/Logo.png">
        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-menubuilder"><span class="sr-only">Toggle navigation</span><span class="icon-bar"></span><span class="icon-bar"></span><span class="icon-bar"></span>
        </button>
      </div>
      <div class="collapse navbar-collapse navbar-menubuilder">
        <ul class="nav navbar-nav navbar-left">
          <li><router-link to="/home">Home</router-link></li>
          <li><router-link to="/home#about">About</router-link></li>
          <li><router-link to="/home#analytics">Analytics</router-link></li>
          <li><router-link to="/home#contact">Contact</router-link></li>
        </ul>
        <ul class="nav navbar-nav navbar-right">
          <li><router-link to="/signup">Signup</router-link></li>
          <li><router-link to="/login">Login</router-link></li>
        </ul>

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
.navbar-brand{
  background-image: url('../assets/Logo.png');
}

.navbar-nav > li > a, .navbar-brand {
  margin:8px 2px !important;
}

.navbar {min-height:30px !important;}
.navbar-nav > li > a:hover {
  border: 2px solid red;
}
.navbar-default .navbar-brand {
  color: rgba(119, 119, 119, 1);
}
.navbar-default {
  font-size: 1.5em;
  background-color: rgba(248, 248, 248, 0);
  border-width: 0px;
  border-radius: 0px;
}
.navbar-default .navbar-nav>li>a {
  color: rgba(119, 119, 119, 1);
  background-color: rgba(248, 248, 248, 0);
}
.navbar-default .navbar-nav>li>a:hover,
.navbar-default .navbar-nav>li>a:focus {
  border: 1px solid black;
}
.navbar-default .navbar-nav>.active>a,
.navbar-default .navbar-nav>.active>a:hover,
.navbar-default .navbar-nav>.active>a:focus {
  color: rgba(85, 85, 85, 1);
  border: 1px solid black;
}
.navbar-default .navbar-toggle {
  border-color: #ddd;
}
.navbar-default .navbar-toggle:hover,
.navbar-default .navbar-toggle:focus {
  border: 1px solid black;
}
.navbar-default .navbar-toggle .icon-bar {
  background-color: #888;
}
.navbar-default .navbar-toggle:hover .icon-bar,
.navbar-default .navbar-toggle:focus .icon-bar {
  border: 1px solid black;
}

</style>
