    $('document').ready(function() {
      $('#button').on('click', function() {
        if ($('#id_main_image').attr('src').split('/')[1] == 'static') {
            alert("Добавьте картинки")
            return false;
        }
        if ($('#id_name_ru').val() == '' || $('#id_description_ru').val() == '') {
            alert("Добавьте русский вариант ")
        }
        if ($('#id_name_uk').val() == '' || $('#id_description_uk').val() == '') {
            alert("Добавьте украинский вариант ")
        }
      });

    });