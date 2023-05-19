<template>
    <div class="container">
        <Header />
        <div class="row">
            <div class="col Input" >
                
                
                <form @submit.prevent="submitHandler" style="width:350px; margin:20px; color:white;">
                    <div  style="display:flex; justify-content:flex-start; align-item:center; color:white; margin-bottom:20px"> 
                        <h2>LOGIN</h2>
                    </div>
                    <div class="mb-3">
                        <div style="display:flex; justify-content:start; align-item:center;">
                            <label for="InputName" class="form-label">Username</label>
                        </div>
                        <input type="text" class="form-control" id="InputName" aria-describedby="emailHelp" placeholder="Lucy" v-model="state.username">
                        
                    </div>
                    <div class="mb-3" style="justify-content:flex-start">
                        <div style="display:flex; justify-content:start; align-item:center;">
                            <label for="InputPassword" class="form-label">Password</label>
                        </div>
                        <input type="password" class="form-control" id="InputPassword" placeholder="**********" v-model="state.password">
                    </div>
                    
                    <button type="submit" class="btn btn-primary" style="width:100%; background:#800020" >Submit</button>
                    
                </form>
                <div class="errors">
                       
                        <div style="display:flex; justify-content:start; align-item:center;">
                            <p v-if="v$.username.$error" style="font-size:x-small; color:#800020">
                                        Enter a valid username
                        </p>
                        </div>
                        <div style="display:flex; justify-content:start; align-item:center;">
                            <p v-if="v$.password.$error" style="font-size:x-small; color:#800020">
                                        Enter a valid password(The password should be at least 8 characters long)
                        </p>
                        </div>
                        
                    </div>
            </div>
            <div class="col QR_code"  >
                <div v-if="state.display"  class="otp_input"  style="display:flex; flex-direction:column; justify-content:center; align-items:center; margin-bottom:10px">
                    <div class="otp-input">
                        <input class="boxes" v-for="(field, index) in otpFields" :key="index" v-model="field.value" type="text" maxlength="1" minlength="1" @input="onInput(index)" />
                    </div>
                    <button class="btn btn-primary" v-on:click="verifyOtp" style="background:#800020" >Verify OTP</button>
                </div>
                <div class="errors" v-if="state.errorOtp">
                    <div class="alert alert-danger" role="alert">
                        Enter Correct One time password
                    </div>
                </div>
                
            </div>
        </div>
        <Footer />
    </div>
</template>
<script>
import useValidate from '@vuelidate/core';
import { required, minLength } from '@vuelidate/validators'
import {reactive, computed} from 'vue';
import axios from 'axios';
import Header from '@/components/headerComp.vue';
import Footer from '@/components/footerComp.vue';
export default{
    props:['otps'],
    components:{
        Header,Footer
    },
    data() {
    return {
      otpFields: [
        { value: "" },
        { value: "" },
        { value: "" },
        { value: "" },
        { value: "" },
        { value: "" },
      ],
      OTPValue:""
    }
  },
    setup(){
        const state=reactive(
            {
            
            username:"",
            password:"",
            framedata:0,
            error:"",
            qrcodeimage:'',
            display:false,
            errorSignUp:false,
            errorOtp:false,
            

        });
        const rules = computed(() => {
            return{
            
            username:{ required },
            password:{ required ,minLength:minLength(8)},
            
            }

        });
        const v$ = useValidate(rules, state);



        async function submitHandler(){
            console.log("submitted")
            const isFormCorrect =await this.v$.$validate()
            const form=new FormData();
            if(!isFormCorrect)return
            console.log("hahahahhah")
            form.append("username",this.state.username)
            form.append("password",this.state.password)
            await axios.post('http://localhost:8000/login',
                 form
            )
            .then(res=>{
                
                localStorage.setItem("temp_access_token",res.data["access_token"])
                this.state.display=true


            })
            .catch(err=>{
                console.log(err)
            });
        }
    

            return { state, v$ ,submitHandler};
    
    },
    methods: {
    onInput(index) {
      const nextField = this.$refs[`otpField${index+1}`]
      if (nextField && this.otpFields[index].value !== "") {
        nextField.focus()
      }
      this.updateOtp()
    },
    updateOtp() {
      const otp = this.otpFields.map(field => field.value).join("")
      this.OTPValue=otp
      console.log(typeof(this.OTPValue))
    },
    async verifyOtp(){
        console.log(this.OTPValue)
        await axios.post(`http://localhost:8000/verify_otp?otp=${this.OTPValue}`)
        .then(res=>{
            console.log(res)
            localStorage.setItem("access_token",localStorage.getItem("temp_access_token"));
            localStorage.setItem("temp_access_token",null);   
            window.location='/Home'
        })
        .catch(err=>{
            console.log(err)
            this.state.errorOtp=true
        })
    }
  }
}



</script>
<style scoped>
*{
    padding: 0%;
    margin:0%; 
    font-family: 'Playguard', sans-serif;
}
body{
    padding: 0%;
    margin:0%;
    background: #333333;
    font-family: 'Playguard', sans-serif;
    
    
}
.container{
    background: #333333;
    margin:0%;
    padding: 0%;
    max-width:100%;
}
.container .row{
    background:#333333;
    padding: 0%;
    margin:0%;
    max-width:100%;
}
.container .row .col{
    background:#333333; width:50%; height:100vh;
}



.container .row .Input{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.container .row .col .otp_input .otp-input .boxes{
    width:40px;
    height: 40px;
    margin:5px;
  }
.container .row .QR_code{
    width:50%; height:100vh; display:flex; flex-direction:column; justify-content:center; align-items:center; 

  }
.container .row .QR_code .QR_image{
    width:300px; height:300px; border:2px solid black; padding: 3px; margin-bottom:5px;
    
}
.container .row .QR_code .False_QR{
    width:300px; height:300px; border:2px solid white; padding: 3px;
    display: flex; justify-content: center; align-items: center;
    background-position: center;   background-size:cover; background-image: linear-gradient(0deg,rgba(247, 4, 4, 0.721),rgba(247, 4, 4, 0.721)), url(@/assets/qr.png);
    color:white; font-weight: bold;
}

</style>