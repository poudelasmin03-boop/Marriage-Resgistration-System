console.log("load admin file on admin section");

/*showing and hinding a password*/

  let show  = document.querySelector('.show');
 let password1 = document.getElementById('password');
 show.innerHTML = "Show";
function ShowPassword(){

  console.log('clicked show btn')
  if (password1.type === "password"){
    password1.type = "text";
    show.innerHTML = "Hide";
    
  }
  else{
     password1.type = "password";
    show.innerHTML = "Show";
  }

} 

/* Validation of form to stop submmiting */
function AdminForm(){
  console.log("call function");
  let username =document.getElementById('username').value.trim();
  let password = document.getElementById('password').value.trim();


  let usernameError = document.querySelector('.usernameError');

  let passwordError = document.querySelector('.passwordError');



  usernameError.innerHTML = "";
  passwordError.innerHTML = "";
  
  is_submit = true;

  if(username === ""){
    usernameError.innerHTML = "Username is required";
    is_submit = false;
  }
  if(password === ""){
    passwordError.innerHTML = "Passwords is required";
    is_submit = false;
  }
  
   return is_submit;
   
  

}


/* Testing */


let  p   = document.querySelector('.para')
p.addEventListener('click',()=>{
  console.log("p is clicked");
})



