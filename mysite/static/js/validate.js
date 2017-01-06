/**
 * Created by Delyana on 4.12.2016 .
 */
function validate() {
    var messages = [];// an array to store the messages of invalid input
    //storing the content from the input fields
    var text = document.getElementById("share").value;
    if (text.length ==0){
         messages.push("Please fill the field in order to proceed.");
    }
   if (messages.length > 0) {
        alert(messages.join(" "));
        return false;
    }

}
