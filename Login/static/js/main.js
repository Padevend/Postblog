function addStyle(element, attribute){
    for(key in attribute){
        value = attribute[key]
        element.style.setProperty(key, value)
    }
}

screen = document.querySelector('body')
window.onload = ()=>{
    const{clientHeight, clientWidth} = document.documentElement;
    addStyle(screen, {
        'height': clientHeight+'px',
        'width': clientWidth+'px',
    })

    background = document.querySelectorAll("[bg]")
    background.forEach(element => {
        addStyle(element, {
            'background': element.getAttribute("bg"),
        })
    });
}


window.onresize = ()=>{
    const{clientHeight, clientWidth, offsetWidth} = document.documentElement;
    addStyle(screen, {
        'height': clientHeight+'px',
        'width': clientWidth+'px',
    })

}


// head_link = document.querySelectorAll('header ul li a')
// const activeLink = (link)=>{
//     head_link.forEach(element =>{
//         element.classList.remove('active')
//     })
//     link.classList.add('active')
// }
// head_link.forEach(item => {
//     item.onclick = ()=>{
//         activeLink(item)
//     }
// })
