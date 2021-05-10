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
            updateRecipeRating(response)
        },
        error: function(error){
            console.log("ajax error", error);
        }
    });
})

/**
 * Function to handle the response from AJAX call
 * @param {Object} Response - Object with updated ratings for recipe
 */
function updateRecipeRating(response) {
    let recipeRatingStar = document.querySelector(".js-rating-star-div");
    // remove all children from the parrent element
    while (recipeRatingStar.lastElementChild) {
        recipeRatingStar.removeChild(recipeRatingStar.lastElementChild);
    }
    responseObj = JSON.parse(response)

    // create and insert new children with the new rating
    let ratedStar = responseObj['rating']

    // display new rating 5 stars from response
    for (let i = 0; i < 5; i++) {
    
        // create new element
        let span = document.createElement('span');
        // add a class to the element
        span.setAttribute("class", "rated-star");
        
        // declare variable that will dispay the star ratings
        let star;
        if (ratedStar >= 1) {
            star = `
                    <i class="fas fa-star" aria-hidden="true"></i>
                  `;
        }
        else if (ratedStar > 0 && ratedStar < 1) {
            star = `
                    <i class="fas fa-star-half-alt" aria-hidden="true"></i>
                  `;
        } 
        else {
            star = `
                    <i class="far fa-star" aria-hidden="true"></i>
                  `;
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
        --ratedStar;
    }

    // Display message to the user after successful rating
    $(".rating-ajax-response").html("Thank you for rating!")
}