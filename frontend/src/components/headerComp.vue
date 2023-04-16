<template>
    <div class="header">
        <h2 class="companyLogo">DarkVault</h2>
        
   </div>

</template>
<style>
.header{
    position:fixed;
    top:0;
    background: #FFFFFF;
    left:0;
    width:100%;
    height:9%;
    text-align:center;
    display:flex;
    flex-direction:row;
    justify-content:space-between;
    align-items:center;
    border-bottom: 1px solid rgb(115, 137, 152);
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