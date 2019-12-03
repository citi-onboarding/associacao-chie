// Coloque aqui os scripts relacionado a "Barra de navegação"
const openMenu = () => {
    document.getElementById("sidebar-mobile").style.width = "90%"
}

const closeMenu = () => {
    document.getElementById("sidebar-mobile").style.width = "0%";
}

const openInsta = () => {
    document.getElementById('instagram-link').click();
}
const openFace = () => {
    document.getElementById('facebook-link').click();
}

let nav = document.querySelector('#navbar');
let heightNavbar = nav.offsetHeight;

let heightSecondSection = $('#timeline').offset().top - heightNavbar;
let heightThirdSection = $('#goals').offset().top - heightNavbar;
let heightFourthSection = $('#contact').offset().top - heightNavbar;

const paint = (section) => {
    document.getElementById('markingSection1').style.background = 'none';
    document.getElementById('markingSection2').style.background = 'none';
    document.getElementById('markingSection3').style.background = 'none';
    document.getElementById('markingSection4').style.background = 'none';

    document.getElementById('markingSection' + section).style.background = '#FEE5DB';

}

document.addEventListener('scroll', () => {
    if($(document).scrollTop() > heightSecondSection) {
        document.getElementById('navbar').style.background = '#006EB3';
    } else {
        document.getElementById('navbar').style.background = 'none';
    }
    if($(document).scrollTop() < heightSecondSection) {
        paint('1');

    } else if($(document).scrollTop() < heightThirdSection) {
        paint('2');

    } else if($(document).scrollTop() < heightFourthSection) {
        paint('3');

    } else {
        paint('4');

    }

})

