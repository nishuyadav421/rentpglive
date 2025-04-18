const inputSearch = document.querySelector('.inputSearch');
const loginBtn = document.getElementById('loginBtn');
const registerBtn = document.getElementById('registerBtn');

inputSearch.addEventListener('click', () => {
    inputSearch.style.backgroundColor = 'red';
});

loginBtn.addEventListener('click', () => {
    alert('Login route hit successfully!')
   
});

registerBtn.addEventListener('click', () => {
    alert('Register route hit successfully!')
});

document.addEventListener("DOMContentLoaded", () => {
    console.log("Career page loaded");
});
