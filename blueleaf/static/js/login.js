window.onload = function () {
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

    $('#login-button').on('click', function () {
        var email = $('input#email').val();
        var password = $('input#password').val();

        var params = {
            email: email,
            password: password,
        };

        $.post(Flask.url_for("login"), params).done(function (data) {
            console.log("On success:");
            console.log(data);
        });
    });
};
