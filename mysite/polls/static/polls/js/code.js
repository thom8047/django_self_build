function closeNav() {
    var navBar = document.getElementById("side-nav")
    var spanOfNavBar = document.getElementById("span-left-side-nav")

    spanOfNavBar.setAttribute('data-open', 'true')
    navBar.style.width = "0px";
    document.getElementById("content").style.marginLeft= "0px";
}

function openNav() {
    var navBar = document.getElementById("side-nav")
    var spanOfNavBar = document.getElementById("span-left-side-nav")
    if(spanOfNavBar.getAttribute('data-open') === "true") {
        spanOfNavBar.setAttribute('data-open', '');
        
        navBar.style.width = "200px";
        document.getElementById("content").style.marginLeft = "200px";
    }
    else {
        closeNav()
    }
}
