$(document).ready(function () {
    // Прячем Шапку, панель и показываем их же
    $('#menu_5').bind('click', headMenu);
    $('#show_panel').bind('click', showMenu);
    $('#comment').bind('click', comment);
});

function headMenu() {
    //Прячем Шапку, панель
    $('#head').slideUp(3000, function(){
        $('#Popup_menu').slideUp(2000);
        $('#show_panel').slideDown(2000);
    });
}

function showMenu() {
    //Прячем Шапку, панель
    $('#head').slideDown(3000, function () {
        $('#Popup_menu').slideDown(2000);
        $('#show_panel').slideUp(2000);
    });
}