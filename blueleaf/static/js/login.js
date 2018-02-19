$(window).load(function () {

    $('#login-button').on('click', function () {
        $('#error_notices').removeClass('visible');
        var email = $('input#email').val();
        var password = $('input#password').val();

        var params = {
            email: email,
            password: password,
        };

        $.post(Flask.url_for("base.login"), params).done(function (data) {
            // Proceed to main page
            console.log("On success:");

        }).fail(function (data) {
            console.log("On failure:");
            $('#error_notices').html("Unknown username or password")
                               .addClass('background-error')
                               .addClass('visible').addClass('shake');
            setTimeout(function () { 
                $('#error_notices').removeClass('shake');
            }, 300);
        });
    });
});
