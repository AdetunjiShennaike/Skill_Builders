<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/list">List</router-link> |
      <router-link to="/about">About</router-link>
    </div>
    <!-- transistion modes help change the timing of a transition more easily -->
    <transition name='slide-fade' mode="out-in"> <!-- out-in makes the transition wait until the current transition finishes before allowing th enext to start -->
      <router-view />
    </transition>
  </div>
</template>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }

  button {
    height: 2.2em;
    margin: 0.5em;
    border-radius: .3em;
    background: linear-gradient(to right, #16c0b0, #84cf6a);
    color: white;
  }

  #nav {
    padding: 30px;
  }

  #nav a {
    font-weight: bold;
    color: #2c3e50;
  }

  #nav a.router-link-exact-active {
    color: #42b983;
  }

  input {
    display: inline-block;
    box-sizing: border-box;
    width: 30%;
    height: 1.8em;
    padding: 0.5em;
    margin: 0.2em;
    font: 0.8em 'Avenir', Helvetica, sans-serif;
  }

  p {
    font-size: .8em;
  }

  ::placeholder {
    color: #2c3e50;
  }
  ul {
    list-style-type: none;
  }

  .modal {
    width: 250px;
    height: 200px;
    padding: 10px;
    margin: 0 auto;
    margin-top: 20px;
    border-radius: 2%;
    background-color: #e0e0e0;
  }

  /* Transitions */

  /* everything titled fade-* is because we used the name fade in the vue transition */
  .fade-enter {
    opacity: 0;
  }
  /* since the values will be the same we can double them up here */
  .fade-enter-active,
  .fade-leave-active {
    transition: opacity 0.5s ease-out;
  }

  .fade-leave-to {
    opacity: 0;
  }

  .slide-fade-enter {
    transform: translateX(10px);
    opacity: 0;
  }
  /* since the values will be the same we can double them up here */
  .slide-fade-enter-active,
  .slide-fade-leave-active {
    transition: all 0.2s ease;
  }

  .slide-fade-leave-to {
    transform: translateX(-10px);
    opacity: 0;
  }

  .slide-up-enter {
    transform: translateY(10px);
    opacity: 0;
  }

  .slide-up-enter-active{
    transition: all 0.2s ease;
  }

  /* V-move helps ease creating transistions for default movement, like the sort thats done */
  .slide-up-move {
    transition: transform .5s ease-out;
  }
</style>
