$(document).ready(function () {
    // ������ �����, ������ � ���������� �� ��
    $('#menu_5').bind('click', headMenu);
    $('#show_panel').bind('click', showMenu);
    $('#menu_1').on('click', function () {
        if (!$('#menu_1').hasClass('clicked')) { // ���� ������ ���
            $('#menu_1').addClass('clicked'); // ��������� �����
            onIn();// ��� ��� ������� �����
        } else { // ���� ����
            $('#menu_1').removeClass('clicked'); // ������� �����
            console.log('Second click'); // ��� ��� ������� �����
            onOut();
        }
    });
    setInterval(new_data_for_poup_menu, 0);
    //setInterval(form_alert);

});

function headMenu() {
    //������ �����, ������
    $('#head').slideUp(3000, function () {
        $('#Popup_menu').slideUp(2000);
        $('#show_panel').slideDown(2000);
    });
}

function showMenu() {
    //������ �����, ������
    $('#head').slideDown(3000, function () {
        $('#Popup_menu').slideDown(2000);
        $('#show_panel').slideUp(2000);
    });
}


// ������� ������� ���������� ��� ��������� ������� �� �������
function onIn() {
    //$('#popup_m').fadeIn();
    coordinates = $("#Popup_menu").offset();
    coordinates = coordinates.left;
    coordinates = parseInt(coordinates);
    coordinates = coordinates + 1;
    coordinates += 'px';
    $('#popup_m_external').css({
        'padding-left': coordinates,
    });
    $('#popup_m').fadeIn();

    $('#Popup_menu').css({
        'border-bottom-left-radius': '0px',
    });
}

// ������� ������� ���������� ��� ������ ������� �� �������
function onOut() {
    $('#popup_m').fadeOut();
    $('#Popup_menu').css({
        'border-bottom-left-radius': '10px',
    });
}

// ������� ��� post.html ��������� ��������� ���������

// �������� ������ ��� ����������� ����������� ������������ ����, �� �� ������� ���
function new_data_for_poup_menu() {
    coordinates = $("#Popup_menu").offset();
    coordinates = coordinates.left;
    coordinates = parseInt(coordinates);
    coordinates = coordinates + 1
    coordinates += 'px';
    $('#popup_m_external').css({
        'padding-left': coordinates,
    });
};


// function form_alert () {
//     $("form").submit(function(event){
//         //alert('1');
//         $(this).find("#form").each(function(){
//             //alert('2');
//             if (!$(this).val().length) {
//                 alert("Заполните пожалуйста все поля!");
//                 $(this).focus();
//                 return false;
//         }
//         });
//     });
// }