/**
 * Created by Delyana on 6.1.2017 .
 */
function validate() {
     var messages = [];// an array to store the messages of invalid input
    //storing the content from the input fields
    var item_text = document.getElementById("text").value;
     var item_date = document.getElementById("date").value;
    if (item_text.length == 0 || item_date.length == 0 ) {
        messages.push("Please fill the field in order to proceed.");
    }
    if (messages.length > 0) {
        alert(messages.join(" "));
        return false;
    }

}
