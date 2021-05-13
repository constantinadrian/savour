/**
 * Add ingredients fields for recipe
 */
function addIngredients() {
    let ingredietsList = document.querySelector(".ingredients-list");
    let ingredients = document.querySelectorAll(".ingredient");


    if (ingredients.length == 1) {
        $(".btn-remove-ingredients").css("display", "inline-block");
    }

    if (ingredients.length != 5) {
        let listItem = document.createElement('li');
        
        inputField = `
                        <input type="text" class="form-control" name="recipe-ingredient" required>
                    `;   

        listItem.setAttribute("class", "ingredient");
        listItem.innerHTML = inputField;

        ingredietsList.insertBefore(listItem, ingredietsList.lastChild.nextSibling);

    }
    else {
        console.log("You reach maximum of ingredients fields");
    }
}

/**
 * Remove ingredients fields from recipe
 */
function removeIngredients() {
    let ingredietsList = document.querySelector(".ingredients-list");

    // remove last child from ingredients list
    ingredietsList.removeChild(ingredietsList.lastElementChild);

    // get all the nodes of ingredients list
    let ingredients = document.querySelectorAll(".ingredient");

    // check if is more than one otherwise hide the remove btn
    if (ingredients.length == 1) {
        $(".btn-remove-ingredients").css("display", "none")
    }
}

// Add more ingredients fields
$(".btn-add-ingredients").click(function(){
    addIngredients()
});

// Remove ingredients fields
$(".btn-remove-ingredients").click(function(){
    removeIngredients()
});

