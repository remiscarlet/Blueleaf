'use strict';

$(document).ready(function () {
    $('button#logout').on('click', function () {
        var params = {

        }
        $.post(Flask.url_for('base.logout'), params).done(function (data) {
            console.log("On Success:");
            if (data["success"]) {
                window.location.href = data["url"];
            }
            console.log(data);
        }).fail(function (data) {
            console.log("On Failure:");
            console.log(data);
        });
    });
});
