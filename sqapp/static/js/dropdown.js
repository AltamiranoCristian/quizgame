document.addEventListener("DOMContentLoaded", function() {
    var miElemento = document.getElementById("menu");
    var boton = document.getElementById("user-menu-button");
    boton.addEventListener("click", function() {
        miElemento.classList.toggle("hidden");
    });
});