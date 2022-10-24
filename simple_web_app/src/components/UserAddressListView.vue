<script>
import axios from 'axios';
import xml2js from 'xml2js';

export default {
  name: 'UserAddressListView',
  data() {
    return {
      user: this.$root.$data?.selectedUser,
      addresses: [],
      loading: false,
    }
  },
  mounted() {
    this.loadUserAddressList()
  },
  methods: {
    loadUserAddressList() {
      const userId = this.user?.id
      const url = `http://0.0.0.0:1234/rss/users/${userId}/addresses/`
      this.loading = true;

      axios.get(url).then(response => {
        console.log(`Parsing RSS addresses belongs to User - ${userId}...`)
        this.parseRSS(response.data).then(result => {
          this.addresses = result
          this.loading = false;
        })
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
          let root = result.addresses;

          for (tag in root.address) {
            let item = root.address[tag];

            to_return.push({
              id: item.id[0],
              username: item.username[0],
              address: item.address[0]
            });
          }

          console.log("Asigning data to the component's state ... ", to_return)
          resolve(to_return);  
        });
      })
    },
    returnToUserList() {
      this.$emit("setSelectedUser", null);
    }
  }
};
</script>

<template>
  <div>
    <h2>{{ user.first_name }}'s address list</h2>
    <p>
      XML retrieved from <b><a :href="'http://localhost:1234/rss/users/' + user.id + '/addresses/'">{{ "http://localhost:1234/rss/users/" + user.id + "/addresses/" }}</a></b> endpoint
    </p>
    <table>
      <thead>
        <td>ID</td>
        <td>Username</td>
        <td>Address</td>
      </thead>
      <tbody>
        <tr v-if="loading">Load user's address list...</tr>
        <tr v-for="address in addresses" :key="address.id">
          <td>{{ address.id }}</td>
          <td>{{ address.username }}</td>
          <td>{{ address.address }}</td>
        </tr>
      </tbody>
      <tfoot>
        <td colspan="3">
          <a @click="returnToUserList()">Back to user list</a>
        </td>
      </tfoot>
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