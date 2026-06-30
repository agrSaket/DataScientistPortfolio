document.addEventListener("DOMContentLoaded", function () {
    const elements = document.querySelectorAll(".card, .skill");

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("show");
            }
        });
    });

    elements.forEach(el => {
        el.classList.add("hidden");
        observer.observe(el);
    });
});

function toggleMenu() {
    document.getElementById("menu").classList.toggle("active");
}