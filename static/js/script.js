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