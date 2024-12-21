// static/script.js

document.addEventListener('DOMContentLoaded', function () {
    const loginForm = document.querySelector('form');
    const signUpLink = document.querySelector('.forget a');

    if (loginForm) {
        loginForm.addEventListener('submit', function (event) {
            event.preventDefault();

            // Assuming you have a route named 'subjects' in Flask
            window.location.href = '/subjects';
        });
    }

    if (signUpLink) {
        signUpLink.addEventListener('click', function (event) {
            event.preventDefault();

            // Assuming you have a route named 'register' in Flask
            window.location.href = '/register';
        });
    }
});
