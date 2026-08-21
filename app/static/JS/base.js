console.log("Js File is Load");

console.log("admin Js is load");

counter = 0;
console.log(counter)
let logo =  document.querySelector('.logo');
let showAdminLogin = document.querySelector('.container');



logo.addEventListener('click',function(event){
    counter++;
    console.log(counter);
  if(counter > 6){
    window.location.href = "/adminlogin_views/";
  }

})
