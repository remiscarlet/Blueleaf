$(document).ready(function () {

    // Run this after one second because all on-load CSS animations are <1 second
    setTimeout(function () {
        // Remove any classes that are on-load only
        $('[class^="on-load-"], [class*=" on-load-"]').each(function () {
            parentThis = this;
            console.log($(this));
            var classes = $(this).attr('class').split(" ");
            if (classes.length > 0) {
                classes.forEach(function (className) {
                    if (className.indexOf('on-load') === 0) {
                        //$(parentThis).removeClass(className);
                    }
                });
            }
        });
    }, 1000);
});
