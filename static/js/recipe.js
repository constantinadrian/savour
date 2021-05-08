$(".rating-form input").on('change', function() {
    
    $(".rating-stars").addClass("rating--not-allowed")
    $(".star").addClass("disabled");
    let stars = document.querySelectorAll(".ratings");
    for (let i = 0, l = stars.length; i < l; i++){
        if(stars[i].checked) {
            console.log(stars[i].value)
        }
    }
})