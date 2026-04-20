// Wait until page loads
document.addEventListener("DOMContentLoaded", function () {

    let name = document.getElementById("name");
    let email = document.getElementById("email");
    let message = document.getElementById("message");
    let submitBtn = document.getElementById("submitBtn");


    // A) Key Press Validation (onkeyup)
    name.onkeyup = function () {
        if (name.value.length < 3) {
            name.style.border = "2px solid red";
        } else {
            name.style.border = "2px solid green";
        }
    };

    email.onkeyup = function () {
        if (email.value.includes("@")) {
            email.style.border = "2px solid green";
        } else {
            email.style.border = "2px solid red";
        }
    };


    // B) Mouse Hover Highlight
    message.onmouseover = function () {
        message.style.backgroundColor = "lightyellow";
    };

    message.onmouseout = function () {
        message.style.backgroundColor = "white";
    };


    // C) Double Click Confirmation
    submitBtn.ondblclick = function () {
        let result = confirm("Are you sure?");

        if (result) {
            alert("Form Submitted!");
        } else {
            alert("Submission Cancelled!");
        }
    };

});