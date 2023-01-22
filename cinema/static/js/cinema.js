
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
    $(`#${photoID}`).prop('checked', true)
}

function hideEmptyForm(event, element) {
    $(element).parent().remove()
}

function hideBack(event, element) {
    console.log(element)
    $('.img-main_film').attr('src', '/static/img/empty-photo.png')
    $('.films').attr('value', 'delete')

}


function hideCinemaLogo(event, element) {
    console.log(element)
    $('.img-logo').attr('src', '/static/img/empty-photo.png')
    $('.delete_logo').attr('value', 'delete')
}

function hideCinemaBanner(event, element) {
    console.log(element)
    $('.img-banner_up').attr('src', '/static/img/empty-photo.png')
    $('.delete_banner').attr('value', 'delete')
}

// if(document.getElementById('option1').checked) {
//     console.log('1')
// }else if(document.getElementById('option2').checked) {
//     console.log('2')
// }

$('.list-group-item').click(function(e) {
    e.preventDefault();
    $('.list-group-item').removeClass('active');
    $(this).addClass('active');
});

$('#list_ukr').click(function(e) {
    e.preventDefault();
    $('#uk').show();
    $('#ru').hide();
});
$('#list_rus').click(function(e) {
    e.preventDefault();
    $('#ru').show();
    $('#uk').hide();
});