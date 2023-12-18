
function scrollToSection(sectionId) {
    var targetSection = document.getElementById(sectionId);

    if (targetSection) {
        var offsetTop = targetSection.offsetTop;

        window.scrollTo({
            top: offsetTop,
            behavior: 'smooth'
        });
    }
}