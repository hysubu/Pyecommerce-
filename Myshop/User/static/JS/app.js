window.addEventListener('DOMContentLoaded', event => {

    // Toggle the side navigation
    const sidebarToggle = document.body.querySelector('#sidebarToggle');

    if (sidebarToggle) {
        // Uncomment Below to persist sidebar toggle between refreshes
        // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
        //     document.body.classList.toggle('sb-sidenav-toggled');
        // }
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }

});




// Image  validation >>>>>>>>>>>>>>>>>>>>
// const img1  = document.getElementById("img1")
// const imglink = img1.getAttribute("src")


// const btn = document.getElementById("click-btn")
// btn.addEventListener("click", function(){
//     alert(imglink)
// })



const btn =  document.getElementById("quantity_inc_button")
btn.addEventListener("click", ()=>{
    btn.textContent = +1
})







