




function validate(){
    let name=document.querySelector('#name').value
    let age=document.querySelector('#age').value
    let city=document.querySelector('#city').value
    let salary=document.querySelector('#salary').value
    let sub=document.querySelector('#sub').value
    let contact=document.querySelector('#contact').value
    let email=document.querySelector('#email').value
    let pass=document.querySelector('#pass').value
    let cpass=document.querySelector('#cpass').value



if(name=="") {
    document.querySelector('#error').innerHTML="please fill the detail"
    document.querySelector('#name').focus()
    return false
}
else if(city=="") {
    alert("fill your city")
    document.querySelector('#city').focus()
    return false
}

// else if(age=="") {
//     alert("fill your age")
//     document.querySelector('#age').focus()
//     return false
// }

// else if(isNaN(age)) {
//     alert("fill your age in numbers")
//     document.querySelector('#age').focus()
//     return false
// }
else if(age=="") {
 document.querySelector('#age').focus()
 alert("fill your age")
    return false
 }
 else if(age.length >3 ) {
     alert("fill your age")
 document.querySelector('#age').focus()

    return false
 }




else if(isNaN(salary)) {
    alert("fill your salary inn numbers")
    document.querySelector('#salary').focus()
    return false
}

// else if(sub=="") {
//     alert("fill your sub")
//     document.querySelector('#sub').focus()
//     return false
// }

 else if(contact==""){
    alert("enter contact number")
    document.querySelector('#contact').focus()
    return false
 }
 else if(contact.length <10 || contact.length>10){
    alert("enter 10 digit number")
    document.querySelector('#contact').focus()
    return false
 }

else if(email==""){
    alert("enter your email")
    document.querySelector('#email').focus()
    return false
 }

 else if(! (email.includes('@gmail.com'))){
    alert("write in correct format")
    document.querySelector('#email').focus()
    return false
 }

 else if(pass==""){
    alert("enter your password")
    document.querySelector('#pass').focus()
    return false
 }

  else if(!(pass.match(/[~!#$@%^&*() 0123456789]/))){
     alert("pleaase enter seccial character")
     document.querySelector('#pass').focus()
    return false
  }

 else if(pass.length <8 || pass.length>15){
    alert("enter correct length password")
    document.querySelector('#pass').focus()
    return false
 }

  else if(cpass==""){
    alert("enter your password")
    document.querySelector('#cpass').focus()
    return false
 }

 else if (!(cpass==pass)){
    alert("password does not match")
    document.querySelector('#cpass').focus()
    return false
 }

}



