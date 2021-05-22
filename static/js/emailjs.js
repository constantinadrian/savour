/**
 * Set user ID for emailjs service
 */
(function(){
    emailjs.init("user_ApCzStsJvY0Nwtp3I4YST");
})();

// Credit Function Emailjs adapted from Code Institute - Interactive Frontend Development - Resume
/**
 * Send user feedback thru emailjs service
 * @param {Object} contactForm - Contact form values
 */
function sendMail(contactForm) {
    emailjs.send("gmail", "savour", {
        "to_name": "Savour",
        "from_name": contactForm.name.value,
        "from_email": contactForm.email.value,
        "subject": contactForm.query.value,
        "message": contactForm.message.value
    })
    .then(
        function(response) {
            $("#contact-form").trigger("reset");

            // Credit code SweetAlert2 - https://sweetalert2.github.io/#download
            Swal.fire({
                icon: 'success',
                title: 'Thank you',
                text: 'Your message has successfully been sent.'
            });
            // End Credit
        },
        function(error) {
            $("#contact-form").trigger("reset");

            // Credit code SweetAlert2 - https://sweetalert2.github.io/#download
            Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'Something went wrong your message could not be sent. Try again later.',
            });
            // End Credit
        }
    );
    return false;
}
// End Credit Function Emailjs