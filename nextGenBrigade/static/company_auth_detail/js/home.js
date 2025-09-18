window.addEventListener("pageshow", (event) => {
  const token = localStorage.getItem("token");
  if (!token) {
    window.location.href = "/";
    return;
  }
});

document.addEventListener("DOMContentLoaded", async () => {
  const token = localStorage.getItem("token");
  console.log(token)
  if (!token) {
    window.location.href = "/";
    return;
  }
  console.log("inside")
  // Show “Edit” & “Logout” buttons if present
  const editBtn   = document.getElementById("edit_btn");
  const logoutBtn = document.getElementById("logout_btn");

editBtn.classList.remove("d-none");
logoutBtn.classList.remove("d-none");
});

document.addEventListener('DOMContentLoaded', () => {
  const cards = document.querySelectorAll('.card');
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if(e.isIntersecting) {
        e.target.style.opacity = 1;
        e.target.style.transform = 'translateY(0)';
        io.unobserve(e.target);
      }
    });
  }, { threshold: 0.12 });

  cards.forEach(c => {
    c.style.opacity = 0;
    c.style.transform = 'translateY(12px)';
    io.observe(c);
  });
});

var swiper = new Swiper(".mySwiper", {
    loop: true, // infinite loop
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    autoplay: {
      delay: 7000, // auto slide every 3s
      disableOnInteraction: false,
    },
  });

