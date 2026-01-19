const btn = document.getElementById("interactiveBtn");
const menu = document.getElementById("interactivesMenu");

// Toggle dropdown on click
btn.addEventListener("click", (e) => {
    e.preventDefault();
    menu.style.display = menu.style.display === "block" ? "none" : "block";
});

// Close dropdown when clicking outside
document.addEventListener("click", (e) => {
    if (!btn.contains(e.target) && !menu.contains(e.target)) {
        menu.style.display = "none";
    }
});
