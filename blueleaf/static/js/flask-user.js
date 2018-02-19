$(document).ready(function () {
    $('input.form-control').each(function () {
        var name = $(this).attr('name');
        var fa_icon = "";
        if (name === "email") {
            fa_icon = "fa-envelope";
        } else if (name === "password") {
            fa_icon = "fa-key";
        } else if (name === "retype_password") {
            fa_icon = "fa-key";
        }

        $('i#icon-register-'+name).addClass("input-icon fas "+fa_icon+" fa-lg");
    });
    $('.register-buttons button').on('click', function (evnt) {
        evnt.preventDefault();
        console.log("setting window.href to "+$(this).parent().attr('href'));
        document.location.href = $(this).parent().attr('href');
    });
});
