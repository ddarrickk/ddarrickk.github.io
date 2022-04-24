const navSlide = () => {
    const hideNav = document.querySelector('.hideNav');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');
    
    hideNav.addEventListener('click', ()=> {
        nav.classList.toggle('nav-active');

        navLinks.forEach((link,index) => {
            if(link.style.animation){
                link.style.animation = ''
            }else {
                link.style.animation = 'navLinkFade 0.5s ease forwards ${index / 7 + 0.3}s';
            }
            console.log(index/7);
        });
        hideNav.classList.toggle('toggle');
    });
}

navSlide();

