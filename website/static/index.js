$(function() {
    $('a#test').bind('click', function() {
        $.getJSON('/run', // << HERE
            function(data) {
                // do nothing
            });
        return false;
    });
});