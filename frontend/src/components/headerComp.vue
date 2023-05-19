<template>
    <div class="header">
        <h1 class="companyLogo">DARKVAULT</h1>
        
   </div>

</template>
<style>
.header{
    font-family: 'Playguard', sans-serif;
    position:fixed;
    top:0;
    background: #005A5B ;
    left:0;
    width:100%;
    height:9%;
    text-align:center;
    display:flex;
    flex-direction:row;
    justify-content:space-between;
    align-items:center;
    color:#C0C0C0;
}
.header .companyLogo{
    margin-left:5px;
    height:40px;
}
.header .companyLogo img{
    width: 160px;
    height: 100%;
    font-weight: bold;
}
.header .logout button{
    margin-right:5px;
    background-color: rgb(12, 119, 190);
    border-radius: 5px;
    border: none;
    color: white;
    font-size: 16px;
}
</style>