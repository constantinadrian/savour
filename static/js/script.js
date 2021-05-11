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
    $("#flashMessage").delay(5000).fadeOut();
});