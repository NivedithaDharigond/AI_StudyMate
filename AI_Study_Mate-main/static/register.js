// static/script.js

document.addEventListener('DOMContentLoaded', function () {
    const registerForm = document.querySelector('form');

    if (registerForm) {
        registerForm.addEventListener('submit', function (event) {
            event.preventDefault();

            // Assuming you have a route named 'login' in Flask
            window.location.href = '/login';
        });
    }
});
