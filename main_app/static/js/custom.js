$('.ovon-main-menu li.ovon-sub>a').on('click', function () {
    $(this).removeAttr('href');
    var element = $(this).parent('li');
    if (element.hasClass('open')) {
        element.removeClass('open');
        element.find('li').removeClass('open');
        element.find('ul').slideUp();
    }
    else {
        element.addClass('open');
        element.children('ul').slideDown();
        element.siblings('li').children('ul').slideUp();
        element.siblings('li').removeClass('open');
        element.siblings('li').find('li').removeClass('open');
        element.siblings('li').find('ul').slideUp();
    }
});
$('.ovon-main-menu>ul>li.ovon-sub>a').append('<span class="holder"></span>');
// Document on load.
$(function () {
    contentWayPoint();
    burgerMenu();
    mobileMenuOutsideClick();
});
var wind = $(window);