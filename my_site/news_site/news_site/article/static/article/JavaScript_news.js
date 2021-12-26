$(document).ready(function () {

    // Прячем комментарии
    $('#dom_comment').hide();
    $('#dom_comments_').hide();

    // При первом нажатии выводит блок с комментариями при втором нажатии убирает его
    $('#comments').bind('click', CommentShowHidden);

    // Прячем Шапку, панель и показываем их же
    $('#menu_5').bind('click', headMenu);

    $('#show_panel').bind('click', showMenu);

    $('#menu_1').on('click', function () {
        if (!$('#menu_1').hasClass('clicked')) { // если класса нет
            $('#menu_1').addClass('clicked'); // добавляем класс
            onIn();// код для первого клика

        } else { // если есть
            $('#menu_1').removeClass('clicked'); // убираем класс
            console.log('Second click'); // код для второго клика
            onOut();
        }
    });


    setInterval(new_data_for_poup_menu, 0);
    setInterval(title, 0);
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


// Функция которая отработает при наведении курсора на элемент
function onIn() {
    //$('#popup_m').fadeIn();
    coordinates = $("#Popup_menu").offset();
    coordinates = coordinates.left;
    coordinates = parseInt(coordinates);
    coordinates = coordinates
    coordinates += 'px';
    $('#popup_m_external').css({
        'padding-left': coordinates,
    });
    $('#popup_m').fadeIn();

    $('#Popup_menu').css({
        'border-bottom-left-radius': '0px',
    });
}

// Функция которая отработает при выходе курсора за элемент
function onOut() {
    $('#popup_m').fadeOut();
    $('#Popup_menu').css({
        'border-bottom-left-radius': '10px',
    });
}

// Функция для post.html размещяет правильно заголовок
function title() {
    //$('#popup_m').fadeIn();
    coordinates = $("#Articles").offset();
    coordinates = coordinates.left;
    coordinates = parseInt(coordinates);
    coordinates = coordinates + 1;
    coordinates += 'px';

    $('#boot_card').css({
        'padding-left': coordinates,
    });
};

// Получает данные для корректного отображения всплывающего окна, но не выводет его
function new_data_for_poup_menu(){
    coordinates = $("#Popup_menu").offset();
    coordinates = coordinates.left;
    coordinates = parseInt(coordinates);
    coordinates = coordinates + 1
    coordinates += 'px';
    $('#popup_m_external').css({
        'padding-left': coordinates,
    });
};

// При первом нажатии выводит блок с комментариями при втором нажатии убирает его
function CommentShowHidden(){
    if (!$('#comments').hasClass('clicked')) { // если класса нет
        $('#comments').addClass('clicked'); // добавляем класс
        $('#dom_comment').slideDown(1000);
        $('#dom_comments_').slideDown(1000);

      } else { // если есть
        $('#comments').removeClass('clicked'); // убираем класс
        $('#dom_comment').slideUp(1000);
        $('#dom_comments_').slideUp(1000);
      }
}

