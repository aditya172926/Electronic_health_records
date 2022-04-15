var modal = document.getElementById("myModal");
var modalbtn = document.getElementById("myBtn");
var modalspan = document.getElementsByClassName("btn-close")[0];

modalbtn.onclick = function() {
    modal.style.display = "block";
}
modalspan.onclick = function() {
    modal.style.display = "none";
}
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display == "none";
    }
}