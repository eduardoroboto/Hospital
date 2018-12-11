(function ($) {
    $(function () {

        $('.sidenav').sidenav();

    }); // end of document ready
})(jQuery); // end of jQuery name space


$(document).ready(function () {
    $('.collapsible').collapsible();
});

$(document).ready(function () {
    $('.datepicker').datepicker({
        yearRange: [1950, 2018],
        format: 'dd-mm-yyyy'
    });
});

$(document).ready(function () {
    $('select').formSelect();
});


$(document).ready(function () {
    $('.timepicker').timepicker({
        twelveHour: false
    });
});