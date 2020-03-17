"use strict";
$('.carousel').carousel('pause');
(function ($) {
    // manual carousel controls
    $('.next').click(function () {
        $('.carousel').carousel('next');
        return false;
    });
    $('.prev').click(function () {
        $('.carousel').carousel('prev');
        return false;
    });
})(jQuery);

$.each($('.carousel-inner').find('a'), function (indexInArray, valueOfElement) { 
     $($($($('.carousel-inner').find('a')[indexInArray]).parent())).click(function (e) { 
       window.open($(valueOfElement).attr('href'), '_blank');
     });
});

$($('#services div.col-md-6')).each(function (index, element) {
    $(element).on('hover',function () {
        $(element).find('h5').removeClass('border-white')
    })
});