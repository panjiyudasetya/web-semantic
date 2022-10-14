<script>
import axios from 'axios';
import xml2js from 'xml2js';

export default {
  name: 'UserView',
  data() {
    return {
      users: [],
      loading: false,
    }
  },
  mounted() {
    // Setting `isRss` parameter to `false` for rendering JSON data.
    // this.loadUsers(
    //   "http://0.0.0.0:1234/api/users/",
    //   false
    // )

    // Setting `isRss` parameter to `true` for rendering XML data.
    this.loadUsers(
      "http://0.0.0.0:1234/rss/users/",
      true
    )
  },
  methods: {
    loadUsers(url, isRss) {
      this.content = null;
      this.loading = true;

      axios.get(url).then(response => {
        if (isRss) {
          console.log("Parsing RSS ... ")
          this.parseRSS(response.data).then(result => {
            this.users = result
            this.loading = false;
          })
        } else {
          console.log("Asigning JSON data to the component's state ... ", response.data)
          this.users = response.data;
          this.loading = false;
        }
      }).catch((reason) => {
        this.loading = false;
        console.error(reason)
      });
    },
    parseRSS(rssUser) {
      return new Promise(resolve => {
        let tag ="";
        let to_return = [];

        let parser = new xml2js.Parser({
          trim: true,
          explicitArray: true
        });

        parser.parseString(rssUser, function (err, result) {
          if (err) {
            console.error(err)
          }
          console.log(result);
          let root = result.users;

          for (tag in root.user) {
            let item = root.user[tag];

            to_return.push({
              identifier: item.identifier[0],
              first_name: item.first_name[0],
              last_name: item.last_name[0],
              email: item.email[0],
              is_active: item.is_active[0],
            });
          }

          resolve(to_return);  
        });
      })
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