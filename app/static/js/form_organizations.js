$(document).ready(function () {
    fetch('/api/geo')
        .then(response => response.json())
        .then(data => {
            data.forEach(city => {
                $("#city").append(`<option value="${city.fields.name}">${city.fields.name}</option>`)
            })
        })
        .catch(error => console.error(error))
});
