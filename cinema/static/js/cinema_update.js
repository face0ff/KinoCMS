
const addMoreCinema = document.getElementById('add-more-cinema')
const totalCinemaForms = document.getElementById('id_cinema-TOTAL_FORMS')

addMoreCinema.addEventListener('click',add_cinema_form)

function add_cinema_form(event){
    if (event){
        console.log(event)
        event.preventDefault()
    }
    const currentCinemaForms = document.getElementsByClassName('cinema-item')
    const currentFormCount = currentCinemaForms.length
    const formCopyTarget = document.getElementById('cinema-list')
    const emptyFormElement = document.getElementById('empty-form-cinema').cloneNode(true)
    emptyFormElement.setAttribute('class', 'cinema-item')
    emptyFormElement.setAttribute('id', `form-${currentFormCount}`)
    const regex = new RegExp('__prefix__', 'g')
    emptyFormElement.innerHTML = emptyFormElement.innerHTML.replace(regex, currentFormCount)
    totalCinemaForms.setAttribute('value', currentFormCount + 1)
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
    $('.img-main_film').attr('src', '/static/img/empty-photo.png')
    $('.films').attr('value', 'delete')


}








function hideCinemaLogo(event, element) {
    console.log(element)
    $('.img-main_cinema').attr('src', '/static/img/empty-photo.png')
    $('.cinema').attr('value', 'delete')
}

function hideCinemaBanner(event, element) {
    console.log(element)
    $('.img-main_cinema').attr('src', '/static/img/empty-photo.png')
    $('.cinema').attr('value', 'delete')
}