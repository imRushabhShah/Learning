<template>
  <div>
    <h1>Register New User</h1><hr/>
    <form v-if="!submitted">
    USERNAME: <input type="text" v-model="user.username"/><br/>
    FIRST NAME: <input type="text" v-model="user.fname"/><br/>
    LAST NAME: <input type="text" v-model="user.lname"/><br/>
    EMAIL ID: <input type="text" v-model="user.email"/><br/>
    PASSWORD: <input type="password" v-model="user.password"/><br/>
    ROLE: <select v-model="user.role">
            <option v-for="userrole in roles" value="userrole.id">{{userrole.role}}</option>
          </select><br/>
      <button @click.prevent="registerUser">Register</button>
      <button @click.prevent="showusers">Show</button>
    </form>
    <div v-if="submitted">
      <h3>THank you for submittion</h3>
    </div>
    <div id="preview">
            <h3>Preview blog</h3>
            <p>name: {{ user.fname }}  {{user.lname}}</p>

    </div>
  </div>
</template>

<script>
export default {

  data(){
    return{
      user:{
        username:'',
        fname:'',
        lname:'',
        email:'',
        password:'',
        role:''
      },
      submitted:false,
      roles:[{role:'student',id:1},{role:'teacher',id:2}]

    }

  },
  methods:{
    registerUser(){
      this.$http.post("http://localhost:8000/paper/users/",{
        username:this.user.username,
        first_name:this.user.fname,
        last_name:this.user.lname,
        email:this.user.email,
        role:parseInt(this.user.role),
        password:this.user.password,
        dataType: "json",
        // type: 'GET'
      }).then(function (data){
        console.log(data);
        this.submitted=true;
      });

    },
    showusers() {
      this.$http.get("http://localhost:8000/paper/users/").then(function(data) {
        console.log(data);
        this.submitted = true;
      });
    }
  }
}


</script>
