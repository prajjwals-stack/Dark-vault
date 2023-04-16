import axios from "axios";

axios.defaults.baseURL="http:localhost:8000/";
//http://35.200.136.144:5013/
// http://localhost:8001/
  
let Jwt_token=localStorage.getItem('access_token')
// localStorage.setItem('token',"")
axios.defaults.headers.common["Authorization"]='Bearer '+Jwt_token;