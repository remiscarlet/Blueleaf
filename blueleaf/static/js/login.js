$(document).ready(function () {

    $('#login-button').on('click', function () {
        $('#error_notices').removeClass('visible');
        var email = $('input#email').val();
        var password = $('input#password').val();

        var error = false;

        if (email === undefined || email === "") {
            // Display error;
            $('input#email').parent().addClass('error shake');
            setTimeout(function () { 
                $('input#email').parent().removeClass('shake');
            }, 300);
            error = true;
        } else {
            $('input#email').parent().removeClass('error');
        }
        if (password === undefined || password === "") {
            //Display error;
            $('input#password').parent().addClass('error shake');
            setTimeout(function () { 
                $('input#password').parent().removeClass('shake');
            }, 300);
            error = true;
        } else {
            $('input#password').parent().removeClass('error');
        }

        if (error) {
            return;
        }


        var params = {
            email: email,
            password: password,
        };

        $.post(Flask.url_for("base.login"), params).done(function (data) {
            // Proceed to main page
            console.log("On success:");
            console.log(data);
            if (data["success"]) {
                window.location.href = data["url"];
            }
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
