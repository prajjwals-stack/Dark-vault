<template>
    <div class="main" >
        <headerComp />
        <div class="container" style="margin-top:60px">
            <div class="row" >
                <div >
                    <div style="display:flex; flex-direction:row; justify-content:flex-start;  margin-top:20px; color:#C0C0C0">
                        <h3>ADD CREDENTIALS</h3>
                    </div>
                    
                    <form @submit.prevent style="display:flex; flex-direction:row; justify-content:flex-start">
                        <input type="text" placeholder="Website Name" style="margin:10px; border-radius:10px; border:2px solid black" v-model="name">
                        <input type="password" placeholder="Password" style="margin:10px; border-radius:10px; border:2px solid black" v-model="password"> 
                        <button v-on:click="submit" class="btn btn-primary" style="margin:10px; border:2px solid black; background:#800020">Add Credentials</button>
                    </form> 
                    
                </div>
                <div class="container" >
                    <div class="row" style="margin-top:70px; width:100%; ">
                        
                        <div style="display:flex; flex-direction:row; justify-content:flex-start; margin-bottom:20px; color:#C0C0C0">
                            <h3>AVAILABLE CREDENTIALS</h3>
                            
                        </div>
                        <div v-if="Framedata==10" style="display:flex; flex-direction:row; justify-content:flex-start; margin-bottom:20px; color:#C0C0C0">
                                <h4> Website: {{ this.Website}}</h4> 
                                <h4>Password: {{ this.website_password }} <span><img src="" alt="">{{ Numbering }}</span></h4>
                        </div>
                        <div  v-for="x in list" :key="x" style="margin-bottom:10px" class="col-3" >
                            <div style="width:100%; height:100px;   background:#005A5B; border-radius:10px; display:flex; justify-content:center; align-items:center">
                                <p style="font-size: 100%; color:white" v-on:click="get_password(x['name'])" >{{ x['name'].toUpperCase() }}</p>
                                
                            </div>
                        </div>
                    </div>
                </div>
                
            </div>

        </div>

        

    



        <footerComp />
    </div>
</template>
<script>
import headerComp from '../components/headerComp.vue'
import footerComp from '../components/footerComp.vue'
import axios from 'axios'
// import {ref} from 'vue'
export default {
    components:{
        headerComp, footerComp
    },
    data(){
        return {
            list:"",
            name:"",
            password:"",
            Framedata:0,
            Website:'',
            website_password:"",
            Numbering:30,

        }
    },
    mounted(){
        this.getList()
    },
    setup(){
        
        async function getList(){
            console.log(localStorage.getItem("access_token"))
            axios.get(`http://localhost:8000/get_all_credentials`)
            .then(res=>{
                this.list=res.data
                console.log(this.list)
                console.log(res)
            })
            .catch(err=>{   
                console.log(err)
            })

        }
        
        return { getList}
    },
    methods: {
        async  submit(){
            console.log(this.name,this.password)
            axios.post(`http://localhost:8000/add_credentials`,{
                data: this.name,
                encrypted_password: this.password
            })
            .then(res=>{
                
                console.log(res)
                location.reload()
            })
            .catch(err=>{   
                console.log(err)
            })
        },
        async get_password(name){
            axios.post(`http://localhost:8000/get_credentials`,name)
            .then(res=>{
                this.Website=name;
                this.website_password=res.data;
                this.Framedata=10;
                console.log("hello");
                setInterval(function(){ this.Numbering--;},1000)
                console.log("hello again");
                console.log(res)
            })
            .catch(err=>{
                console.log(err)
            })
        }
    },
}
</script>

<style scoped>
*{
    padding: 0%;
    margin:0%; 
    font-family: 'Playguard', sans-serif;
    color:#C0C0C0;
}
body{
    font-family: 'Playguard', sans-serif;
    color:#C0C0C0;
    overflow:hidden;
}
.main{
    width:100%;
    height:100vh;
    background: #333333;
    overflow:hidden;
}
    


</style>