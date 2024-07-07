let slideindex = 1;
function setslide(input , index){
    slideindex = index
    let item = document.querySelector(`#${input}`)
    let slides = [...document.querySelector('.slides').children];
    slides.forEach((element)=>{
        element.classList.remove('active');
    })
    item.classList.add('active');
}

setInterval(()=>{
    slideindex +=1;
    if(slideindex==5){
        slideindex=1;
    }
    setslide(`slide${slideindex}` , slideindex)
} , 3000)