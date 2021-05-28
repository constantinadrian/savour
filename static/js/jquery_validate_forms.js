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
                pattern: /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
            },
            password: {
                required: true
            },
            passwordConfirmation: {
                required: true,
                equalTo: "#password"
            }
        },
        messages: {
            username: {required: "Please fill out this field", pattern: "Name must be between 3 and 20 characters long, and can contain letters and numbers only."},
            email: {required: "Please fill out this field", pattern: "Please enter a valid email address" },
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
        let checkFields = $('#login-register').find(":input");

        // if fields are invalid prevent submit form
        if (!checkFields.valid()){
            e.preventDefault();
        }
    });

    // Use jQuery validate for add recipe form
    // https://jqueryvalidation.org/documentation/
    $("#add-recipe").validate({
        rules: {
            ["recipe-category"]: {
                required: true
            },
            ["recipe-title"]: {
                required: true
            },
            ["recipe-description"]: {
                required: true,
                maxlength: 150
            },
            ["recipe-ingredient"]: {
                required: true
            },
            ["recipe-methods"]: {
                required: true,
                maxlength: 320
            },
            ["recipe-image-url"]: {
                required: true,
                url: true
            },
            ["recipe-cook-time"]: {
                required: true,                
                number: true,
                min: 1,
                max: 1440
            },
            ["recipe-serve"]: {
                required: true,
                number: true,
                min: 1,
                max: 24
            },
            ["recipe-tips"]: {
                required: true,
            }
        },
        messages: {
            ["recipe-category"]: {
                required: "Please choose a category"
            },
            ["recipe-title"]: {
                required: "Please add recipe title"
            },
            ["recipe-description"]: {
                required: "Please add a recipe description"
            },
            ["recipe-ingredient"]: {
                required: "Please fill out ingredient field"
            },
            ["recipe-methods"]: {
                required: "Please fill out step field"
            },
            ["recipe-image-url"]: {
                required: "Please add recipe image",
                url: "Please enter a valid URL (e.g https://images.pexels.com/photos/1070850/pexels-photo-1070850.jpeg)"
            },
            ["recipe-cook-time"]: {
                required: "Please fill out the cooking time"
            },
            ["recipe-serve"]: {
                required: "Please fill out people serve"
            },
            ["recipe-tips"]: {
                required: "Please fill out the tips field"
            } 
        },
        errorElement: 'span',
        highlight: function(element) {
            $(element).addClass('has-error');
        },
        unhighlight: function(element) {
            $(element).removeClass('has-error');
        },
        errorPlacement: function(error, element) {
            if (element.parent('.ingredient').length || element.parent('.methods').length)
            {
                if (element.next().length) {
                    error.insertAfter(element.next());
                }
                else {
                    error.insertAfter(element);
                }
            }
            else
            {
                error.insertAfter(element.next());
            }  
        },
        submitHandler: function(form) {
            removeIngredientsNumbers();
            removeMethodsNumbers();
            form.submit();
        }   
    });

    // After validation rename the ingredients fields with same name 
    // as we use request.form.getlist to get the array on ingredients
    function removeIngredientsNumbers() {
        $(".js-recipe-ingredient").each(function(){
            $(this).attr("name", "recipe-ingredient");
        });
    }

    function removeMethodsNumbers() {
        $(".js-recipe-methods").each(function(){
            $(this).attr("name", "recipe-methods");
        });
    }

    // Click event to call jQuery validate
    $('#btn-submit-add-recipe').click(function(e) {
        // get all input field for validate
        let checkFields = $('#add-recipe').find(":input");

        // add rules for ingredients created dynamically
        $(".js-recipe-ingredient").each(function(){
            $(this).rules("add", {
                required: true,

                messages: {
                    required: "Please fill out ingredient field"
                }
            });
        });

        // add rules for methods created dynamically
        $(".js-recipe-methods").each(function(){
            $(this).rules("add", {
                required: true,

                messages: {
                    required: "Please fill out step field"
                }
            });
        });

        // if fields are invalid prevent submit form
        if (!checkFields.valid()){
            // prevent the form from submitting
            e.preventDefault();

            // define variable to error scroll position
            let scrollNewPosition;

            // check if the error is on ingredients fields
            if ($('.has-error:visible:first').parent().prop('className') == "ingredient") {
                // if only one ingredients call the function to get the right position for the scroll
                // this is because the first ingredient has the label
                if ($(".ingredient").length == 1) {
                    scrollNewPosition = scrollPosition();
                }
                // if the error is on any ingredients were created dynamically
                // calculate the scroll position without the label position 
                // (as this fields don't have labels) 
                else {
                    scrollNewPosition = $('.has-error:visible:first').offset().top- $('.create-recipes-section').offset().top; 
                }
            }
            // check if the error is on methods fields
            else if ($('.has-error:visible:first').parent().prop('className') == "methods") {
                if ($(".methods").length == 1) {
                    scrollNewPosition = scrollPosition();
                }
                else {
                    scrollNewPosition = $('.has-error:visible:first').offset().top - $('.create-recipes-section').offset().top; 
                }
            }
            // for all other fileds with error call the function to get the exact position for the scroll
            else {
                scrollNewPosition = scrollPosition();
            }
            
            // scroll to first element on top that has the error
            $('html, body').animate({
                scrollTop: scrollNewPosition
            }, 1200);
             
            
        }
    });

    /**
     * Function that moves the scoll position to first element
     * that fails the jquery validation
     */
    function scrollPosition() {
        // get the node of each element
        let formContainer = $('.create-recipes-section');
        let scrollToError = $('.has-error:visible:first');
        let labelError = $('.has-error:visible:first + label span');

        // declare the variable for scroll new position
        let positionScrollError;

        // check if position of label didn't change 
        // this happens when the .has-error class is being added
        if (scrollToError.offset().top < labelError.offset().top) {
            positionScrollError = scrollToError.offset().top - formContainer.offset().top - (labelError.offset().top - scrollToError.offset().top);
        }
        // by default the label position is not change
        else {
            positionScrollError = scrollToError.offset().top - formContainer.offset().top + (labelError.offset().top - scrollToError.offset().top);
        }
        return positionScrollError;
    }

    // Use jQuery validate for add/edit categories form
    // https://jqueryvalidation.org/documentation/
    $("#add_categories").validate({
        rules: {
            ["category-name"]: {
                required: true
            }
        },
        messages: {
            ["category-name"]: {required: "Please fill out this field"} 
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
    $('#btn-submit-add_categories').click(function(e) {
        // get input field for validate 
        // the hidden fields are ignored by default
        let checkField = $('#add_categories').find(":input");

        // if fields are invalid prevent submit form
        if (!checkField.valid()){
            e.preventDefault();
        }
    });

    // Use jQuery validate for Contact form and return form to emailjs for submit
    // https://jqueryvalidation.org/documentation/
    $("#contact-form").validate({
        rules: {
            name: {
                required: true
            },
            email: {
                required: true,
                pattern: /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
            },
            query: {
                required: true
            },
            message: {
                required: true
            }
        },
        messages: {
            name: {required: "Please fill out this field"},
            email: {required: "Please fill out this field", pattern: "Please enter a valid email address" },
            query: {required: "Please fill out this field"},
            message: {required: "Please fill out this field"}
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
            // form is submited with emailjs
            return sendMail(form);
        }   
    });

    // Click event  call jQuery validate
    $('#btn-submit-contact-form').click(function(e) {
        // get input field for validate 
        // the hidden fields are ignored by default
        let checkField = $('#contact-form').find(":input");

        // if fields are invalid prevent submit form
        if (!checkField.valid()){
            e.preventDefault();
        }
    });


    // Use jQuery validate for Contact form and return form to emailjs for submit
    // https://jqueryvalidation.org/documentation/
    $("#subscribe-form").validate({
        rules: {
            email: {
                required: true,
                pattern: /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
            }
        },
        messages: {
            email: {required: "Please fill out this field", pattern: "Please enter a valid email address" }
        },
        errorElement: 'span',
        highlight: function(element) {
            $(element).addClass('has-error');
        },
        unhighlight: function(element) {
            $(element).removeClass('has-error');
        },
        errorPlacement: function(error, element) {
            error.insertAfter(element);
        }
    });

    // Click event  call jQuery validate
    $('#btn-submit-subscribe').click(function(e) {
        // get input field for validate 
        // the hidden fields are ignored by default
        let checkField = $('#subscribe-form').find(":input");

        // if fields are invalid prevent submit form
        if (!checkField.valid()){
            e.preventDefault();
        }
    });
});