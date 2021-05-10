// Change the recipe title display if lenght is
$(".js-card-title").each(function() {
    let cardRecipeTitle = this.textContent
    if (cardRecipeTitle.length > 57) {
        cardRecipeTitle = cardRecipeTitle.substring(0,53) + "..."
        this.innerHTML = cardRecipeTitle
    }
})