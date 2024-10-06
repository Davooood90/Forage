$(document).ready(function() {
    $('.diet-button input[type="checkbox"]').change(function() {
        if ($(this).is(':checked')) {
            $(this).next('.btn').addClass('active');
        } else {
            $(this).next('.btn').removeClass('active');
        }
    });
});

function openModal(id) {
    console.log(id)
    var modal = document.getElementById(id);
    modal.style.display = "block";
}

function closeModal(id) {
    var modal = document.getElementById(id);
    modal.style.display = "none";
}

