// Get all textarea fields from the page
let textarea = $("textarea");

// declare the maximum number of ingredients and steps
const MAXINGREDIENTS = 21;
const MAXSTEPS = 15;

// declare variable to help enumerate future ingredients that will be created dynamic to the page
// we start at 22 because the maximum allowed is 21 and if user decide to edit the recipe by deleting 
// and adding multiple fields we need to keep a different name attribute within the input form for jquery 
// validation, because we need our name attribute to be unique for validation
let nameIngredientsCount = MAXINGREDIENTS + 1;

// declare variable to help enumerate future steps that will be created dynamic to the page
let stepsCount = MAXSTEPS + 1;

/**
 * Initialize all tooltips on a page
 */
function initializeToolip() {
    $('[data-toggle="tooltip"]').tooltip({
        trigger : 'hover'
    });
}

/**
 * Add ingredients fields for recipe
 * @param {Object} referenceNode - The node that was click on
 */
function addIngredients(referenceNode) {

    // after the current node we have to insert the next required field
    let currentNode = $($(referenceNode).parent().parent().parent().parent())[0];

    // get the parrent node that holds of all the ingrediets fields
    let ingredietsList = document.querySelector(".ingredients-list");
    
    // get all current ingredients nodes from the DOM
    let ingredients = document.querySelectorAll(".ingredient");

    // check if the number of fields does not exceed MAXINGREDIENTS fields
    if (ingredients.length != MAXINGREDIENTS) {
        let listItem = document.createElement('li');
        
        let inputField = `
                            <input type="text" class="form-control js-recipe-ingredient" name="recipe-ingredient-${nameIngredientsCount}" data-msg-required="Please fill out ingredient field" required>
                            <div class="ingredients-btn-container">
                                <div class="input-group-btn">
                                    <span class="input-group-remove-ingredients">
                                        <a class="btn-group-ingredients btn-remove-ingredients" role="button" data-toggle="tooltip" data-placement="top" title="Remove item"><i class="fas fa-minus-circle"></i></a>
                                    </span>
                                    <span class="input-group-add-ingredients">
                                        <a class="btn-group-ingredients btn-add-ingredients" role="button" data-toggle="tooltip" data-placement="top" title="Add item"><i class="fas fa-plus-circle"></i></a>
                                    </span>
                                </div>
                            </div>
                         `;

        listItem.setAttribute("class", "ingredient");
        listItem.innerHTML = inputField;

        // insert new field after the element that was clicked
        ingredietsList.insertBefore(listItem, currentNode.nextSibling);

        // Call the function to initiale all toolips on the page created dynamic
        initializeToolip();

        // increment the variable for next add ingredients call
        nameIngredientsCount += 1;
    }
}

/**
 * Remove ingredients fields from recipe
 * @param {Object} referenceNode - The node that was click on
 */
function removeIngredients(referenceNode) {

    // the current node that we have to remove
    let currentNode = $($(referenceNode).parent().parent().parent().parent())[0];

    // get the parrent node that holds of all the ingrediets fields
    let ingredietsList = document.querySelector(".ingredients-list");

    // destroy the tooltip for this node
    $(referenceNode).tooltip('dispose');

    // remove this child from ingredients list
    ingredietsList.removeChild(currentNode);
}

/**
 * Add steps fields for recipe
 * @param {Object} referenceNode - The node that was click on
 */
function addMethods(referenceNode) {

    // after the current node we have to insert the next required field
    let currentNode = $($(referenceNode).parent().parent().parent().parent())[0];

    // get the parrent node that holds of all the steps fields
    let methodsList = document.querySelector(".methods-list");

    // get all current steps nodes from the DOM
    let methods = document.querySelectorAll(".methods");

    // check if the number of steps does not exceed MAXSTEPS fields
    if (methods.length != MAXSTEPS) {
        let stepItem = document.createElement('li');
        
        let textareaField = `
                                <textarea class="form-control js-recipe-methods" name="recipe-methods-${stepsCount}" rows="1" maxlength="320" data-msg-required="Please fill out step field" required></textarea>
                                <div class="steps-btn-container">
                                    <div class="input-group-btn">
                                        <span class="input-group-remove-steps">
                                            <a class="btn-group-steps btn-remove-steps" role="button" data-toggle="tooltip" data-placement="top" title="Remove step"><i class="fas fa-minus-circle"></i></a>
                                        </span>
                                        <span class="input-group-add-steps">
                                            <a class="btn-group-steps btn-add-steps" role="button" data-toggle="tooltip" data-placement="top" title="Add step"><i class="fas fa-plus-circle"></i></a>
                                        </span>
                                    </div>
                                </div>
                            `;   

        stepItem.setAttribute("class", "methods");
        stepItem.innerHTML = textareaField;

        // insert new field after the element that was clicked
        methodsList.insertBefore(stepItem, currentNode.nextSibling);

        // Call the function to initiale all toolips on the page created dynamic
        initializeToolip();

        // reasign the new numbers of fields
        textarea = $("textarea");

        // Call the resize function 
        resizeTextarea(textarea);

        // increment the variable for next add steps call
        stepsCount += 1;
    }
}

/**
 * Remove step fields from recipe
 * @param {Object} referenceNode - The node that was click on
 */
function removeMethods(referenceNode) {

    // the current node that we have to remove
    let currentNode = $($(referenceNode).parent().parent().parent().parent())[0];

    // get the parrent node that holds of all the steps fields
    let methodsList = document.querySelector(".methods-list");

    // destroy the tooltip for this node
    $(referenceNode).tooltip('dispose');

    // remove this child from methods list
    methodsList.removeChild(currentNode);
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

// Call the resize function 
resizeTextarea(textarea);
windowResize(textarea);

// Call the function to initiale all toolips on the page 
initializeToolip();

// display the maximum numbers of ingredients fields
$(".max-ingredients-number").html(MAXINGREDIENTS);

// display the maximum numbers of ingredients fields
$(".max-steps-number").html(MAXSTEPS);


// Add more ingredients fields
$(".ingredients-list").on("click", ".btn-add-ingredients", function(){
    addIngredients($(this)[0]);
});

// Remove ingredients fields
$(".ingredients-list").on("click", ".btn-remove-ingredients", function(){
    removeIngredients($(this)[0]);
});

// Add more methods fields
$(".methods-list").on("click", ".btn-add-steps", function(){
    addMethods($(this)[0]);
});

// Remove methods fields
$(".methods-list").on("click", ".btn-remove-steps", function(){
    removeMethods($(this)[0]);
});

// Resize textarea on window resize
$(window).resize(function() {
    windowResize(textarea);
});
