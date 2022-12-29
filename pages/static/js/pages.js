// $(document).ready(function() {
//     $('#example').DataTable( {
//         "language": {
//             "lengthMenu": "Показывать _MENU_ записей на странице",
//             "zeroRecords": "Ничего не найдено",
//             "info": "Показанно _PAGE_ из _PAGES_",
//             "infoEmpty": "Нет записей",
//             "infoFiltered": "(Фильтр _MAX_ из всех)",
//             "sSearch": "Поиск",
//             "oPaginate": {
//             "sFirst":    "Первая",
//             "sLast":    "Последняя",
//             "sNext":    "Следующая",
//             "sPrevious": "Предидущая"
//         },
//             "pageLength": {
//             "_": "Show 5 rows"
//         },
//             order: [[2, 'desc']],
//
//         }
//     } );
// } );

$(document).ready(function () {
    $('#example').DataTable({
        searching: false,
        paging: false,
        ordering: false,
        info: false,
        search: false
    });
});

const addMoreImg = document.getElementById('add-more-img')
const totalImgForms = document.getElementById('id_img-TOTAL_FORMS')

addMoreImg.addEventListener('click',add_img_form)

function add_img_form(event){
    if (event){
        console.log(event)
        event.preventDefault()
    }
    const currentImgForms = document.getElementsByClassName('img-item')
    const currentFormCount = currentImgForms.length
    const formCopyTarget = document.getElementById('img-list')
    const emptyFormElement = document.getElementById('empty-form-img').cloneNode(true)
    emptyFormElement.setAttribute('class', 'img-item')
    emptyFormElement.setAttribute('id', `form-${currentFormCount}`)
    const regex = new RegExp('__prefix__', 'g')
    emptyFormElement.innerHTML = emptyFormElement.innerHTML.replace(regex, currentFormCount)
    totalImgForms.setAttribute('value', currentFormCount + 1)
    formCopyTarget.append(emptyFormElement)
}


function download(input){
    console.log(input.id)
    let file = input.files[0];
    let reader = new FileReader();
    reader.readAsDataURL(file);
    let image = $(`#${input.id}`);
    console.log(image.attr('src'))
    reader.onload = function (){
        image.attr('src', reader.result);
    }
}


function hidePhoto(event, element) {
    $(element).parent().css('display', 'none');
    let photoID = ($(element).parent().attr('id')).replace('-item', '-DELETE');
    console.log(photoID)
    $(`#${photoID}`).prop('checked', true);

}

function hideBack(event, element) {
    console.log(element)
    $('.img-page').attr('src', '/static/dist/img/empty-photo.png')
    $('.page').attr('value', 'delete')

}

function hideEmptyForm(event, element) {
    $(element).parent().remove()
}


function hideCinemaLogo(prefix, element) {
    console.log(element)
    console.log(event)
    $('#id_'+prefix+'-logo').attr('src', '/static/dist/img/empty-photo.png')
    $('.delete_logo').attr('value', prefix)
}

function hideCinemaBanner(event, element) {
    console.log(element)
    $('.img-banner_up').attr('src', '/static/dist/img/empty-photo.png')
    $('.delete_banner').attr('value', 'delete')
}


