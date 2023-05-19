<template>
    <div class="container">
        <Header />
        <div class="row">
            <div class="col Input" >
                <div  style="display:flex; justify-content:flex-start; align-item:center; color:white;"> 
                    <h3>Register</h3>
                </div>
                
                <form @submit.prevent="submitHandler" style="width:350px; margin:20px; color:white">
                    <div class="mb-3" style="margin-bottom:30px">
                        <div style="display:flex; justify-content:start; align-item:center;">
                            <label for="InputEmail" class="form-label">Email</label>
                        </div>
                        <input type="email" class="form-control" id="InputEmail" aria-describedby="emailHelp" placeholder="Lucy@google.com" v-model="state.email">
                        
                        
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
                    <div class="mb-3" style="justify-content:flex-start">
                        <div style="display:flex; justify-content:start; align-item:center;">
                            <label for="InputConfirmPassword" class="form-label">Confirm Password</label>
                        </div>
                        <input type="password" class="form-control" id="InputConfirmPassword" placeholder="**********" v-model="state.confirm">
                    </div>
                    <button type="submit" class="btn btn-primary" style="width:100%; background:#800020" >Submit</button>
                    
                </form>
                <div class="errors">
                        <div style="display:flex; justify-content:start; align-item:center;">
                            <p v-if="v$.email.$error" style="font-size:x-small; color:#800020">
                                Enter a valid email address
                        </p>
                        </div>
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
                        <div style="display:flex; justify-content:start; align-item:center;">
                            <p v-if="v$.confirm.$error" style="font-size:x-small; color:#800020">
                                        Confirm password should be same as password
                        </p>
                        </div>
                    </div>
            </div>
            <div class="col QR_code"  >
                <div class="False_QR" v-if="!state.display">
                    <p>Please download the Google Authenticator app from playstore or app store to scan this QR for OTP</p>
                </div>
                <img class="QR_image" v-if="state.display"  :src="state.qrcodeimage" alt="QR Code" > 
                <div v-if="state.display"  class="otp_input"  style="display:flex; flex-direction:column; justify-content:center; align-items:center; margin-bottom:10px">
                    <div class="otp-input">
                        <input class="boxes" v-for="(field, index) in otpFields" :key="index" v-model="field.value" type="text" maxlength="1" minlength="1" @input="onInput(index)" />
                    </div>
                    <button class="btn btn-primary" v-on:click="verifyOtp" style="background:#800020">Verify OTP</button>
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
import { required, email, minLength, sameAs } from '@vuelidate/validators'
import {reactive, computed} from 'vue';
import axios from 'axios';
import QRCode from 'qrcode';
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
            email:"",
            username:"",
            password:"",
            confirm:"",
            framedata:0,
            error:"",
            qrcodeimage:'',
            display:false,
            errorSignUp:false,
            errorOtp:false,
            

        });
        const rules = computed(() => {
            return{
            email:{ required, email },
            username:{ required },
            password:{ required ,minLength:minLength(8)},
            confirm:{ required , sameAs:sameAs(state.password)}
            }

        });
        const v$ = useValidate(rules, state);



        async function submitHandler(){
            console.log("submitted")
            const isFormCorrect =await this.v$.$validate()
            if(!isFormCorrect)return
            console.log("hahahahhah")
            await axios.post('http://localhost:8000/signup',{
                email: this.state.email,
                username: this.state.username,
                password:this.state.password,
            })
            .then(res=>{
                
                QRCode.toDataURL(res.data)
                    .then(qrCodeSrc => {
                        
                    this.state.qrcodeimage = qrCodeSrc
                    this.state.display=true
                    
                    })
                    .catch(err => {
                    console.error(err)
                    this.state.errorSignUp=true
                    })

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
            window.location='/signin'
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
    background: black;
    font-family: 'Playguard', sans-serif;
    
    
}
.container{
    background: black;
    margin:0%;
    padding: 0%;
    max-width:100%;
}
.container .row{
    background: black;
    padding: 0%;
    margin:0%;
    max-width:100%;
}
.container .row .col{
    background:rgb(20, 20, 20); width:50%; height:100vh;
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
    color:#00FFFF; font-weight: bold;
}

</style>