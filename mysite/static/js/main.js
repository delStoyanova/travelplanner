$(document).ready(main);
function main() {

    //focus on user name fields both in login and register
    $("#name").focus(function () {
        $(this).css("outline-color", "#000000");
    });
    //focus on password in login
    $("#password").focus(function () {
        $(this).css("outline-color", "#000000");
    });
    //focus on password in register
    $("#reg_password").focus(function () {
        $(this).css("outline-color", "#000000");
    });
    //focus on confirm password in register
    $("#conf_password").focus(function () {
        $(this).css("outline-color", "#000000");
    });
    //focus on My To Do list input
    $("#todoitem").focus(function () {
        $(this).css("outline-color", "#000000");
    });
    // the below functions add class "active" when the mouse hovers on the navbar
    $(".home").hover(function () {
        $(this).addClass("active");
    }, function () {
        $(this).removeClass("active");
    });
    $(".btn-default").hover(function () {
        $(this).addClass("active");
    }, function () {
        $(this).removeClass("active");
    });
    $(".login").hover(function () {
        $(this).addClass("active");
    }, function () {
        $(this).removeClass("active");
    });
    $(".dropdown-toggle").hover(function () {
        $(this).css("background-color", "black");
    }, function () {
        $(this).css("background-color", "#f1f1f2");
    });

    $(".register").hover(function () {
        $(this).addClass("active");
    }, function () {
        $(this).removeClass("active");
    });

    //for the drop down menu of My Profile we need .css
    $(".todo").hover(function () {
        $(".dropdown-toggle").css("background-color", "black");
    }, function () {
        $(".dropdown-toggle").css("background-color", "#f1f1f2");
    });

    $(".dropdown-header").hover(function () {
        $(".dropdown-toggle").css("background-color", "black");
    }, function () {
        $(".dropdown-toggle").css("background-color", "#f1f1f2");
    });

    $(".places").hover(function () {
        $(".dropdown-toggle").css("background-color", "black");
    }, function () {
        $(".dropdown-toggle").css("background-color", "#f1f1f2");
    });
    $(".place").hover(function () {
        $(".dropdown-toggle").css("background-color", "black");
    }, function () {
        $(".dropdown-toggle").css("background-color", "#f1f1f2");
    });
    $(".art").hover(function () {
        $(".dropdown-toggle").css("background-color", "black");
    }, function () {
        $(".dropdown-toggle").css("background-color", "#f1f1f2");
    });
    $(".divider").hover(function () {
        $(".dropdown-toggle").css("background-color", "black");
    }, function () {
        $(".dropdown-toggle").css("background-color", "#f1f1f2");
    });


}

