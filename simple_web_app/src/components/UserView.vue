<script>
import axios from 'axios';

export default {
  name: 'UserView',
  data() {
    return {
      users: [],
      loading: false,
    }
  },
  mounted() {
    this.loadUsers(
      "http://0.0.0.0:1234/api/users/",
      false
    )
  },
  methods: {
    loadUsers(url, isRss) {
      this.content = null;
      this.loading = true;
      if (!isRss) {
        axios.get(url).then(response => {
          this.users = response.data;
          this.loading = false;
        }).catch((reason) => {
          console.error(reason)
          this.loading = false;
        });
      }
    }
  }
};
</script>

<template>
  <div>
    <h2>Users</h2>
    <table>
      <thead>
        <td>ID</td>
        <td>First Name</td>
        <td>Last Name</td>
        <td>Email</td>
        <td>Is Active</td>
      </thead>
      <tbody>
        <tr v-if="loading">Load list users...</tr>
        <tr v-for="user in users" :key="user.identifier">
          <td>{{ user.identifier }}</td>
          <td>{{ user.first_name }}</td>
          <td>{{ user.last_name }}</td>
          <td>{{ user.email }}</td>
          <td>{{ user.is_active }}</td>
        </tr>
      </tbody>
    </table>   
  </div>
</template>

<style>
  table, tr, td {
    border: 1px solid #eee;
  }
  table {
    margin: 0 auto;
  }
  td {
    padding: 5px;
  }
</style>