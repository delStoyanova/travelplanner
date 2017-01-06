/**
 * Created by Delyana on 26.11.2016 .
 */


function validate() {
    var messages = []; // an array to store the messages of invalid input
    //storing the content from the input fields
    var username = document.getElementById("name").value;
    var password = document.getElementById("password").value;

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





