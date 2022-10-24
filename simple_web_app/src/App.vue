<template>
  <div v-if="selectedUser === null">
    <UserView @setSelectedUser="selectedUser = $event" />
  </div>
	<div v-else>
    <UserAddressListView @setSelectedUser="selectedUser = $event"/>
  </div>
</template>

<script>
import UserView from './components/UserView.vue'
import UserAddressListView from './components/UserAddressListView.vue'

export default {
  name: 'App',
  components: {
    UserView,
    UserAddressListView,
  },
  data() {
    return {
      selectedUser: null
    }
  },
  methods: {
    setSelectedUser(user) {
      this.selectedUser = user;
    },
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
