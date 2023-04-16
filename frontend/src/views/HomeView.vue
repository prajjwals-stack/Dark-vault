<template>
    <div class="main" >
        <headerComp />
        <div class="container" style="margin-top:60px">
            <div class="row">
                <div class="col" style="display:flex; flex-direction:row; justify-content:space-evenly; align-items:center">
                    <div class="password" style="margin-top:100px;  ">
                        <h3>Credential</h3>
                        <div v-for="x in list" :key="x" style="display:flex;   justify-content:flex-start; align-items:center; width:50%">
                            <p>{{ x.name.toUpperCase() }}</p>
                        </div>
                    </div>
                    <div class="password" style="margin-top:100px; ">
                        <h3>Password</h3>
                        <div v-for="x in list" :key="x" style="display:flex;   justify-content:flex-start; align-items:center; width:50%">
                            <p>********</p>
                        </div>
                    </div>
                </div>
                <div class="col">
                    <h1>PINs</h1>
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
            list:""
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
            })
            .catch(err=>{   
                console.log(err)
            })

        }
        return { getList}
    }
}
</script>

<style scoped>
.main{
    width:100%;
    height:100vh;
    background: black !important;
}

</style>