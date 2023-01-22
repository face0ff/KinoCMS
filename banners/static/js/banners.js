$(document).ready ( function(){
 $('.color-back').hide();
 var clean_ground = $('.img-back-banner').attr('src')
    console.log(clean_ground)
    if (clean_ground === '/media/static/dist/img/white.png'){
        $('.img-back-banner').attr('src', '/static/dist/img/empty-photo.png')
    }
});
$('#id_background_0').change(function () {
    var valueSelected = $(this).val()

    if (valueSelected === '1') {
    $('.color-back').hide();
    $('.image-back').show()
    }
    });

$('#id_background_1').change(function () {
    var valueSelected = $(this).val()

    if (valueSelected === '2') {
    $('.image-back').hide();
    $('.color-back').show();
    }
    });




const addMoreNews = document.getElementById('add-more-news')
const totalNewForms = document.getElementById('id_news-TOTAL_FORMS')

addMoreNews.addEventListener('click',add_new_form)

function add_new_form(event){
    if (event){
        console.log(event)
        event.preventDefault()
    }
    const currentNewsForms = document.getElementsByClassName('news-banner-item')
    const currentFormCount = currentNewsForms.length
    const formCopyTarget = document.getElementById('news-banner-list')
    const emptyFormElement = document.getElementById('empty-form-news').cloneNode(true)
    emptyFormElement.setAttribute('class', 'news-banner-item')
    emptyFormElement.setAttribute('id', `form-${currentFormCount}`)
    const regex = new RegExp('__prefix__', 'g')
    emptyFormElement.innerHTML = emptyFormElement.innerHTML.replace(regex, currentFormCount)
    totalNewForms.setAttribute('value', currentFormCount + 1)
    formCopyTarget.append(emptyFormElement)
}

const addMoreMain = document.getElementById('add-more-main')
const totalMainForms = document.getElementById('id_main-TOTAL_FORMS')

addMoreMain.addEventListener('click',add_main_form)

function add_main_form(event){
    if (event){
        console.log(event)
        event.preventDefault()
    }
    const currentMainForms = document.getElementsByClassName('main-banner-item')
    const currentFormCount = currentMainForms.length
    const formCopyTarget = document.getElementById('main-banner-list')
    const emptyFormElement = document.getElementById('empty-form-main').cloneNode(true)
    emptyFormElement.setAttribute('class', 'main-banner-item')
    emptyFormElement.setAttribute('id', `form-${currentFormCount}`)
    const regex = new RegExp('__prefix__', 'g')
    emptyFormElement.innerHTML = emptyFormElement.innerHTML.replace(regex, currentFormCount)
    totalMainForms.setAttribute('value', currentFormCount + 1)
    formCopyTarget.append(emptyFormElement)
}



// function download(input, id) {
//
//     let image = $(`#${id}-image`);
//     image.attr('src', URL.createObjectURL(input.target.files[0]));
//     image.onload = function() {
//         URL.revokeObjectURL(image.src);
//     };
// }

function download(input){

    let file = input.files[0];
    let reader = new FileReader();
    reader.readAsDataURL(file);
    let image = $(`#${input.id}`)
    console.log(image.attr('src'))
    console.log(reader.result)
    reader.onload = function (){
        image.attr('src', reader.result);
    }
}

function downloadBack(input){
    let file = input.files[0];
    let reader = new FileReader();
    reader.readAsDataURL(file);
    let image = $(`#${input.id}`);
    console.log(input.id)
    reader.onload = function (){
        console.log(reader.result)
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
    $('.img-back-banner').attr('src', '/static/dist/img/empty-photo.png')
    $('.background_banner').attr('value', 'delete')
}

function hideEmptyForm(event, element) {
    $(element).parent().remove()
}

