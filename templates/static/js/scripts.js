// templates/static/js/scripts.js

document.addEventListener('DOMContentLoaded', function() {
    console.log('JavaScript is loaded and ready to go!');

    // Example: Add a click event to all alert close buttons
    const closeButtons = document.querySelectorAll('.btn-close');
    closeButtons.forEach(button => {
        button.addEventListener('click', function() {
            const alert = this.closest('.alert');
            if (alert) {
                alert.style.display = 'none'; // Hide the alert when close button is clicked
            }
        });
    });
});