$(document).ready(function() {
    var $path = window.location.pathname;

    if($path.indexOf('post') != -1) {
        var $curr_menu = $('#post');
        $curr_menu.find('> a').css('color', 'white');
        $curr_menu.find('> i').css('color', 'white');
        $(this).css('border-bottom', '2px solid orange');
    }

    var $onDropdown = false;

    $(".menu").hover(function() {
        $(this).find('> a').css('color', 'white');
        $(this).find('> i').css('color', 'white');
        $(this).find('> .dropdown-area').css('display', 'block')
        $(this).css('border-bottom', '2px solid orange');
    }, function() {
        if(!$onDropdown) {
            $(this).find('> a').css('color', 'lightgray');
            $(this).find('> i').css('color', 'lightgray');
            $(this).find('> .dropdown-area').css('display', 'none')
            $(this).css('border-bottom', 'none');
        }
    });

    $(".dropdown-area").hover(function() {
        $onDropdown = true;
    }, function() {
        $onDropdown = false;
    });


    $('#photo-btn').click(function() {
        $('#list-view').hide();
        $('#photo-view').show();
    });

    $('#list-btn').click(function() {
        $('#list-view').show();
        $('#photo-view').hide();
    });

    $(document).keydown(function(e) {
        if(e.keyCode == '81') {
            $('#login').css('display', 'inline');
        }
    }).keyup(function(e) {
        if(e.keyCode == '81') {
            $('#login').hide();
        }
    });
})