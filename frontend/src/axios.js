import axios from "axios";

axios.defaults.baseURL="http:localhost:8000/";

let Jwt_token=localStorage.getItem('access_token')

axios.defaults.headers.common["Authorization"]='Bearer '+Jwt_token;