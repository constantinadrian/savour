$(document).ready(function () {

    // Use jQuery validate for register/login form
    // https://jqueryvalidation.org/documentation/
    $("#login").validate({
        rules: {
            email: {
                required: true,
                email: true 
            },
            password: {
                required: true,
            }
        },
        messages: {
            email: {required: "Please fill out this field", email: "Please enter a valid email address" },
            password: {required: "Please fill out this field" }  
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
        var checkFields = $('#login').find(":input");

        // if fields are invalid prevent submit form
        if (!checkFields.valid()){
            e.preventDefault();
        }
    });
});