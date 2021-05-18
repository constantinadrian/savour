// Get all textarea fields from the page
let textarea = $("textarea");

/**
 * Add ingredients fields for recipe
 */
function addIngredients() {
    let ingredietsList = document.querySelector(".ingredients-list");
    let ingredients = document.querySelectorAll(".ingredient");

    // show remove btn once user has requested new field
    if (ingredients.length == 1) {
        $(".btn-remove-ingredients").css("display", "inline-block");
    }

    if (ingredients.length != 21) {
        let listItem = document.createElement('li');
        
        inputField = `
                        <input type="text" class="form-control" name="recipe-ingredient" required>
                     `;   

        listItem.setAttribute("class", "ingredient");
        listItem.innerHTML = inputField;

        ingredietsList.insertBefore(listItem, ingredietsList.lastChild.nextSibling);
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

/**
 * Add steps fields for recipe
 */
function addMethods() {
    let methodsList = document.querySelector(".methods-list");
    let methods = document.querySelectorAll(".methods");

    // show remove btn once user has requested new field
    if (methods.length == 1) {
        $(".btn-remove-steps").css("display", "inline-block");
    }

    if (methods.length != 15) {
        let stepItem = document.createElement('li');
        
        textareaField = `
                            <textarea class="form-control" name="recipe-methods" rows="1" maxlength="320" required></textarea>
                        `;   

        stepItem.setAttribute("class", "methods");
        stepItem.innerHTML = textareaField;

        methodsList.insertBefore(stepItem, methodsList.lastChild.nextSibling);

    }
    else {
        console.log("You reach maximum of steps fields");
    }

    // reasign the new numbers of fields
    textarea = $("textarea");

    resizeTextarea(textarea);
}

/**
 * Remove step fields from recipe
 */
function removeMethods() {
    let methodsList = document.querySelector(".methods-list");

    // remove last child from methods list
    methodsList.removeChild(methodsList.lastElementChild);

    // get all the nodes of methods list
    let methods = document.querySelectorAll(".methods");

    // check if is more than one otherwise hide the remove btn
    if (methods.length == 1) {
        $(".btn-remove-steps").css("display", "none")
    }
}

/**
 * Resize textarea on user input
 * @param {Object} textarea - All textarea fields from the page 
 */
function resizeTextarea(textarea) {
    textarea.each(function (){}).on("input", function () {
        $(this).css("height", "auto");
        $(this).css("height", this.scrollHeight);
    });
}

/**
 * Resize textarea on window resize
 * @param {Object} textarea - All textarea fields from the page 
 */
function windowResize(textarea) {
    textarea.each(function (){
        $(this).css("height", "auto");
        $(this).css("height", this.scrollHeight);
    });
}

// // Call the resize function 
resizeTextarea(textarea);

// Add more ingredients fields
$(".btn-add-ingredients").click(function(){
    addIngredients()
});

// Remove ingredients fields
$(".btn-remove-ingredients").click(function(){
    removeIngredients()
});

// Add more methods fields
$(".btn-add-steps").click(function(){
    addMethods()
});

// Remove methods fields
$(".btn-remove-steps").click(function(){
    removeMethods()
});

// Resize textarea on window resize
$(window).resize(function() {
    windowResize(textarea)
});

// If edit recipe was requested check if we need to show the remove ingredients and steps button
$(document).ready(function(){
    let ingredients = document.querySelectorAll(".ingredient");

    // show remove btn if more than one igredient in edit recipe
    if (ingredients.length > 1) {
        $(".btn-remove-ingredients").css("display", "inline-block");
    }

    let methods = document.querySelectorAll(".methods");
    // show remove btn if more than one step in edit recipe
    if ( methods.length > 1 ) {
        $(".btn-remove-steps").css("display", "inline-block");
    }
});