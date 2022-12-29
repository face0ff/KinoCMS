$(document).ready(function() {

    let oTable = $('#example').DataTable({

        "language": {
            "lengthMenu": "Показывать _MENU_ записей на странице",
            "zeroRecords": "Ничего не найдено",
            "info": "Показанно _PAGE_ из _PAGES_",
            "infoEmpty": "Нет записей",
            "infoFiltered": "(Фильтр _MAX_ из всех)",
            "sSearch": "Поиск",
            "oPaginate": {
                "sFirst": "Первая",
                "sLast": "Последняя",
                "sNext": "Следующая",
                "sPrevious": "Предидущая"
            },
            "pageLength": {
                "_": "Show 5 rows"
            },
            order: [[2, 'desc']],

        }
    })

} );

$(document).ready(function() {
   oTable = $('#example').dataTable();

   $('form').submit(function(){
      $(oTable.fnGetHiddenNodes()).find('input:checked').appendTo(this);
   });

});

function allUsers(){
    $(`#baton`).css('display', 'none');
}

function oneUsers(){
    $(`#baton`).css('display', '');
}


function checkValue(value){
    console.log(value)
    test1 = document.getElementById('HtmlFile').value = value;
    console.log(test1)
    let name = $(`#template_name`);
    name.text(value);
}

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
function show_name(input){
    console.log(input.value)
    let file = (input.value).substr(12)
    let name = $(`#file_name`);
    name.text(file)
    checkValue(file)
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




