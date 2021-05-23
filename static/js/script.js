$(document).ready(function(){
    // Change the recipe title display if lenght is to long
    $(".js-card-title").each(function() {
        let cardRecipeTitle = this.textContent
        if (cardRecipeTitle.length > 57) {
            cardRecipeTitle = cardRecipeTitle.substring(0,53) + "..."
            this.innerHTML = cardRecipeTitle
        }
    })

    // Hide flash message
    $(".js-flash-message").delay(5000).fadeOut();

    // Update the modal content with information that has to be deleted
    // Credit code https://getbootstrap.com/docs/4.6/components/modal/
    $('#deleteModal').on('show.bs.modal', function (event) {
        // Button that triggered the modal
        let button = $(event.relatedTarget);

        // Extract info from data-* attributes
        let item = button.data('item');
        let item_id = button.data('id');

        // Update the modal's content
        let modal = $(this)
        modal.find('.modal-title-item').text(item);
        modal.find('#delete-item-id').val(item_id);
        modal.find('#delete-item').val(item);
    })

    // Clear the fields from the modal when the modal is hidden / close
    $('#deleteModal').on('hidden.bs.modal', function () {
        var modal = $(this);
        modal.find('.modal-title-item').text('');
        modal.find('#delete-item-id').val('');
        modal.find('#delete-item').val('');
    });
    // End Credit code

       // Update the modal content with information that has to be deleted
    // Credit code https://getbootstrap.com/docs/4.6/components/modal/
    $('#editModal').on('show.bs.modal', function (event) {
        // Button that triggered the modal
        let button = $(event.relatedTarget);

        // Extract info from data-* attributes
        let type = button.data('type');
        let item_id = button.data('id');
        let item = button.data('item');

        // Update the modal's content
        let modal = $(this)
        modal.find('.modal-title').text(type);
        modal.find('#category-id').val(item_id);
        modal.find('#category-name').val(item);
        modal.find('#category-type').val(type);
    })

    // Clear the fields from the modal when the modal is hidden / close
    $('#editModal').on('hidden.bs.modal', function () {
        var modal = $(this);
        modal.find('.modal-title').text('');
        modal.find('#category-id').val('');
        modal.find('#category-name').val('');
        modal.find('#category-type').val('');
    });
    // End Credit code
});

// Get all the images tag from the page
let img = $('img');

/**
 * Change the brocken image links from the page
 * @param {Object} img - All images fields from the page 
 */
function changeImage(img) {
    img.each(function (){}).one('error', function() {
        this.src = '../static/img/pexels-chimene-gaspar-1464880.jpg';
    }); 
}

changeImage(img)

/**
 * Function to make the AJAX call to server
 * @param {Object} event - Submit event for subscribe form
 */
$("#subscribe-form").submit(function(event) {
    // prevent from submitting a form
    event.preventDefault()

    // clear the previous message is the user it trying to submit again
    $(".subscribe-ajax-response").html("")

    // make an AJAX call to server side
    $.ajax({
        url: $(event.target).prop("action"),
        data: $("#subscribe-form").serialize(),
        type: 'POST',
        success: function(response) {
            // reset the form
            $("#subscribe-form").trigger("reset");

            responseObj = JSON.parse(response)

            if (responseObj.status == "success"){
                subscribedSuccessMessage();
            }
            else if (responseObj.status == "already subscribed") {
                subscribedDeniedMessage();
            }
            else {
                subscribedErrorMessage();
            }
        },
        error: function(){
            subscribedErrorMessage();
        }
    });
})

/**
 * Function to handle the success response from AJAX call
 */
function subscribedSuccessMessage() {
    displayResponse = `
                        <p class="mt-3">Thank you for subscribing!</p>
                      `;
    $(".subscribe-ajax-response").append(displayResponse);
}

/**
 * Function to handle the reject response from AJAX call
 */
function subscribedDeniedMessage() {
    displayResponse = `
                        <p class="mt-3">This email address is already subscribed.</p>
                      `;
    $(".subscribe-ajax-response").append(displayResponse);
}

/**
 * Function to handle the error response from AJAX call
 */
function subscribedErrorMessage() {
    displayResponse = `
                        <p class="mt-3">Sorry, we could not process your request.</p>
                        <p>If the problem persists please <a class="contact-ancor-tag" href="/contact">contact us</a></p>
                      `;
    $(".subscribe-ajax-response").append(displayResponse);
}