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
    this.loadUsers()
  },
  methods: {
    loadUsers() {
      const url = "http://0.0.0.0:1234/api/users/"
      this.loading = true;

      axios.get(url).then(response => {
        console.log("Asigning JSON data to the component's state ... ", response.data)
        this.users = response.data;
        this.loading = false;
      }).catch((reason) => {
        this.loading = false;
        console.error(reason)
      });
    },
    showAddressList(user) {
      this.$emit("setSelectedUser", user);
    }
  }
};
</script>

<template>
  <div>
    <h2>Users</h2>
    <p>JSON retrieved from <b><a href="http://localhost:1234/api/users/">http://localhost:1234/api/users/</a></b> endpoint</p>
    <table>
      <thead>
        <td>ID</td>
        <td>Username</td>
        <td>First Name</td>
        <td>Last Name</td>
        <td>Email</td>
        <td>Is Active</td>
        <td>Addresses</td>
      </thead>
      <tbody>
        <tr v-if="loading">Load list users...</tr>
        <tr v-for="user in users" :key="user.id">
          <td>{{ user.id }}</td>
          <td>{{ user.username }}</td>
          <td>{{ user.first_name }}</td>
          <td>{{ user.last_name }}</td>
          <td>{{ user.email }}</td>
          <td>{{ user.is_active }}</td>
          <td>
            <a @click="showAddressList(user)">Show</a>
          </td>
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
  /* unvisited link */
  a {
    color: #2c3e50;
    text-decoration: underline;
  }

  /* mouse over link */
  a:hover {
    color: hotpink;
    text-decoration: underline;
  }

  /* selected link */
  a:active {
    color: #2c3e50;
    text-decoration: underline;
  }
</style>