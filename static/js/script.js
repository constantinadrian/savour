// Change the recipe title display if lenght is
$(".card-recipe-title").each(function() {
    let cardRecipeTitle = this.textContent
    if (cardRecipeTitle.length > 57) {
        cardRecipeTitle = cardRecipeTitle.substring(0,53) + "..."
        this.innerHTML = cardRecipeTitle
    }
})