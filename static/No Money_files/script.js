function generate() {
    fetch('/case_api/No money', {
    method: 'GET',
    headers: {
        'Content-Type': 'application/json'
    },
})
.then(response => response.json())
.catch(error => {
    console.error('Ошибка:', error);
});
}
