window.addEventListener("scroll", function () {
    let sticky = document.querySelector(".sticky-nav")
    let windowPosition = window.scrollY > 0;
    sticky.classList.toggle("scroll-active", windowPosition)
})
  