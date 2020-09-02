<template>
<div class="header">
  <div id="container">
    <b-navbar toggleable="lg" type="dark" >
    <b-navbar-brand href="/home">
      <img class="icon" src="../assets/pom_logo.png" alt="PoM Logo">
    </b-navbar-brand>
    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      
    <b-collapse id="nav-collapse" is-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
      <b-nav-form>
        <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
        <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
      </b-nav-form>

      <b-nav-item-dropdown v-if="userData.isLogged" right>
        <!-- Using 'button-content' slot -->
        <template v-slot:button-content>
        <img class="icon" v-bind:src="userData.profilePicture" alt="Anonymous User Icon">
        </template>
        <b-dropdown-item v-bind:href="userData.profileUrl">
        Profile
        </b-dropdown-item>
        <b-dropdown-item href="#">Sign Out</b-dropdown-item>
      </b-nav-item-dropdown>
      <b-nav-item-dropdown v-else right>
        <!-- Using 'button-content' slot -->
        <template v-slot:button-content>
          <img class="icon" src="../assets/anonymousUser.png" alt="Anonymous User Icon">
        </template>
        <!-- <b-button v-b-modal.modal-1>Launch demo modal</b-button> -->
        
        <b-dropdown-item v-b-modal.modal-1>Sign in</b-dropdown-item>
        <b-modal id="modal-1" title="Registro!">
          <LoginForm/>
        </b-modal>

      </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
    </b-navbar>
  </div>
</div>
</template>

<script>
import LoginForm from './LoginForm.vue'

export default {
  components: {
    LoginForm
  },
  props: {
    userData: Object
  }
}
</script>

<style scoped>

  .header {
    background-color: #582525;
    margin-bottom: 2.4rem;
  }

  .icon {
    width: 50px;
    margin-left: 1.2rem;
    border-radius: 0.6rem;
  }
</style>