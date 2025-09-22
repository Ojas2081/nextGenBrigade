// Small animation when clicking buttons
document.querySelectorAll(".btn, .btn-outline").forEach(btn => {
  btn.addEventListener("click", () => {
    btn.style.transform = "scale(0.95)";
    setTimeout(() => btn.style.transform = "scale(1)", 200);
  });
});
