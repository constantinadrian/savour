$(document).ready(function () {

    // Use jQuery validate for register/login form
    // https://jqueryvalidation.org/documentation/
    $("#login-register").validate({
        rules: {
            username: {
                required: true,
                pattern: /^([a-zA-Z0-9]){3,20}?$/
            },
            email: {
                required: true,
                email: true 
            },
            password: {
                required: true,
            },
            passwordConfirmation: {
                required: true,
                equalTo: "#password"
            }
        },
        messages: {
            username: {required: "Please fill out this field", pattern: "Name must be between 3 and 20 characters long, and can contain letters and numbers only."},
            email: {required: "Please fill out this field", email: "Please enter a valid email address" },
            password: {required: "Please fill out this field" },
            passwordConfirmation: {required: "Please fill out this field", equalTo: "Please enter the same password again" }   
        },
        errorElement: 'span',
        highlight: function(element) {
            $(element).addClass('has-error');
        },
        unhighlight: function(element) {
            $(element).removeClass('has-error');
        },
        errorPlacement: function(error, element) {
            error.insertAfter(element.next());
        },
        submitHandler: function(form) {
            form.submit();
        }
             
    });

    // Click event  call jQuery validate
    $('#btn-submit-form').click(function(e) {
        // get all input field for validate
        var checkFields = $('#login-register').find(":input");

        // if fields are invalid prevent submit form
        if (!checkFields.valid()){
            e.preventDefault();
        }
    });
});