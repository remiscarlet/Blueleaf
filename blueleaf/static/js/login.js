window.onload = function () {


    $('#login-button').on('click', function () {
        var email = $('input#email').val();
        var password = $('input#password').val();

        var params = {
            email: email,
            password: password,
        };

        $.post(Flask.url_for("base.login"), params).done(function (data) {
            console.log("On success:");
            console.log(data);
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


    // Run this after one second because all on-load CSS animations are <1 second
    setTimeout(function () {
        // Remove any classes that are on-load only
        $('[class^="on-load-"], [class*=" on-load-"]').each(function () {
            parentThis = this;
            var classes = $(this).attr('class');
            classes.split(" ").forEach(function (className) {
                if (className.indexOf('on-load') === 0) {
                    $(parentThis).removeClass(className);
                }
            });
        });
    }, 1000);
};
