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
};
