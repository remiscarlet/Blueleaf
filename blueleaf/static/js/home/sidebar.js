'use strict';

$(document).ready(function () {
   $('.div-btn.dropdown-button.menu').on('click', function () {
        $(this).parent().find(".hidden").each(function () {
            console.log($(this));
            $(this).removeClass('hidden');
        });
        $(this).addClass('menu-open');
        console.log("Boop");
   });
   $('.div-btn.close-button-inner').on('click', function () {
        $('.hideable').each(function () {
            $(this).addClass('hidden');
        });
        $('.div-btn.dropdown-button.menu.menu-open').removeClass('menu-open');
   });
});
