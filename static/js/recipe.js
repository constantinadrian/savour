// Check if the value of an element has been changed
$(".rating-form input").on('change', function() {
    // disable the rating form once user has rated
    $(".rating-stars").addClass("rating--not-allowed")
    $(".star").addClass("disabled");

    // Trigger the submit event manually
    $('#rating-form').submit();
})

/**
 * Function to make the AJAX call to server
 * @param {Object} event - Submit event from rating stars form
 */
$("#rating-form").submit(function(event) {
    // prevent from submitting a form
    event.preventDefault()
    // make an AJAX call to server side
    $.ajax({
        url: $(event.target).prop("action"),
        data: $('form').serialize(),
        type: 'POST',
        success: function(response) {
            responseObj = JSON.parse(response)

            if (responseObj.status == "success"){
                updateRecipeRating(responseObj.rating)
            }
            else if (responseObj.status == "denied") {
                displayDeniedMessage()
            }
            else if (responseObj.status == "not logged in") {
                displayRejectMessage()
            }
            else {
                displayErrorMessage();
            }
        },
        error: function(){
            displayErrorMessage();
        }
    });
})

/**
 * Function to handle the success response from AJAX call
 * @param {Object} Response - Object with updated ratings for recipe
 */
function updateRecipeRating(response) {
    let recipeRatingStar = document.querySelector(".js-rating-star-div");
    // remove all children from the parrent element in order to add new elements with updated rating
    while (recipeRatingStar.lastElementChild) {
        recipeRatingStar.removeChild(recipeRatingStar.lastElementChild);
    }
    // display recipe new rating after user rated
    $(".recipe-total-rating").html(response.toFixed(1))
    
    // get the updated rating 
    let ratedStar = response

    // use a for loop to display new rating 5 stars from response
    for (let i = 0; i < 5; i++) {
    
        // create new element and insert new children with the new rating
        let span = document.createElement('span');
        // add class to the element
        span.setAttribute("class", "rated-star");
        
        // declare variable that will dispay the star ratings
        let star;
        if (ratedStar >= 1) {
            star = `<i class="fas fa-star" aria-hidden="true"></i>`;
        }
        else if (ratedStar > 0 && ratedStar < 1) {
            star = `<i class="fas fa-star-half-alt" aria-hidden="true"></i>`;
        } 
        else {
            star = `<i class="far fa-star" aria-hidden="true"></i>`;
        }

        // set the span element content
        span.innerHTML = star;

        // if parrent elemnent has no children append the first child
        if (recipeRatingStar.children.length == 0) {
            recipeRatingStar.appendChild(span);
        }
        else {
        recipeRatingStar.insertBefore(span, recipeRatingStar.lastChild.nextSibling);
        }
        // decrement the actual rating value to check the next display for the star
        ratedStar -= 1;
    }
    // Display message to the user after successful rating
    $(".rating-ajax-response").html("Thank you for rating!")
}

/**
 * Function to handle the denied response from AJAX call
 */
function displayDeniedMessage() {
    $(".ratings:checked").prop("checked", false)
    displayResponse = `
                        <p>Sorry, the owner cannot rate it's own recipe.</p>
                      `;
    $(".rating-ajax-response").append(displayResponse);
}

/**
 * Function to handle the reject response from AJAX call
 */
function displayRejectMessage() {
    $(".ratings:checked").prop("checked", false)
    displayResponse = `
                        <p>Savour does not accept guest ratings.</p>
                        <p>Please <a class="login-ancor-tag" href="/login">Login</a> or <a class="register-ancor-tag" href="/register">Register</a></p>
                      `;
    $(".rating-ajax-response").append(displayResponse);
}

/**
 * Function to handle the error response from AJAX call
 */
function displayErrorMessage() {
    $(".ratings:checked").prop("checked", false)
    displayResponse = `
                        <p>Sorry, we could not process your request.</p>
                        <p>If the problem persists please <a class="contact-ancor-tag" href="/contact">contact us</a></p>
                      `;
    $(".rating-ajax-response").append(displayResponse);
}