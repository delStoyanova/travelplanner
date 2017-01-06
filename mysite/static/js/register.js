/**
 * Created by Delyana on 26.11.2016 .
 */


function validate() {
     var messages = [];// an array to store the messages of invalid input
    //storing the content from the input fields
    var username = document.getElementById("name").value;
    var password = document.getElementById("reg_password").value;
    var confirm_password=document.getElementById("conf_password").value;
    if(password!=confirm_password){
        alert("The password and confirm password do not match.");
        return false;
    }
    if (username.length < 6) {
        messages.push("User name should be longer than 6 characters.");
    }

    if (password.length < 6) {
        messages.push("Password should be longer than 6 characters.");
    }
    if (password.search(/[a-z]/) < 0) {
        messages.push("Password should contain at least one lowercase letter.");
    }
    if (password.search(/[A-Z]/) < 0) {
        messages.push("Password should contain at least one uppercase letter.");
    }
    if (password.search(/[0-9]/) < 0) {
        messages.push("Password should contain at least one digit.");
    }
    if (messages.length > 0) {
        alert(messages.join(" "));
        return false;
    }

}



