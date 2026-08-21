console.log("Marraige files is loaded")


function marriageForm(){
let brideName = document.getElementById('brideName').value.trim();
let brideDob = document.getElementById('brideDOB').value.trim();
let brideFatherName = document.getElementById('brideFatherName').value.trim();
let brideMotherName =document.getElementById('brideMotherName').value.trim();
let brideAddress =document.getElementById('brideAddress').value.trim();
let brideNidNo = document.getElementById('brideNidNo').value.trim();
let brideEmail =document.getElementById('brideEmail').value.trim();
let brideImage =document.getElementById('brideImage');
let brideNidImage = document.getElementById('brideNidImage');



let groomName =document.getElementById('groomName').value.trim();
let groomDOB =document.getElementById('groomDOB').value.trim();
let groomFatherName =document.getElementById('groomFatherName').value.trim();
let groomMotherName =document.getElementById('groomMotherName').value.trim();
let groomAddress =document.getElementById('groomAddress').value.trim();
let groomNidNo =document.getElementById('groomNidNo').value.trim();
let groomImage =document.getElementById('groomImage');
let groomNidImage =document.getElementById('groomNidImage');


let marriageDate =document.getElementById('marriageDate').value.trim();
let registrationDate =document.getElementById('registrationDate').value.trim();
let MarriagePlace =document.getElementById('MarriagePlace').value.trim();

let is_valid = true;

let error  = document.querySelector('.error');
error.innerHTML = ""


if(brideName === "" || brideDob === "" ||brideFatherName === ""||brideMotherName === "" || brideNidNo ===""|| brideEmail === "" || brideAddress === ""|| groomName === ""|| groomDOB === ""||groomFatherName ===""|| groomMotherName ===""|| groomNidNo === ""||groomAddress === ""|| marriageDate === ""|| registrationDate === ""|| MarriagePlace === "" ){
  error.innerHTML = "All Field required";
  is_valid = false;
}

if(groomNidImage.files.length === 0 || groomImage.files.length === 0 || brideImage.files.length === 0 || brideNidImage.files.length === 0){
 error.innerHTML = "All Document is  required";
  is_valid = false;
}

if(registrationDate === marriageDate){
  error.innerHTML = "Registration date and Marraige date cann't be same";
}

 return is_valid;
}