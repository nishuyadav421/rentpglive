const inputSearch = document.querySelector('.inputSearch');
const loginBtn = document.getElementById('loginBtn');


inputSearch.addEventListener('click', () => {
    inputSearch.style.backgroundColor = 'red';
});

loginBtn.addEventListener('click', () => {
    window.location.href = "/login";

});
