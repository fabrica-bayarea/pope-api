$(document).ready(function () {
    $('.dt-button').addClass('btn bg-poupex text-white')
    $('body').on('click', '.modalInfo', function () {
        $('#exampleModal').modal();
    });
});
