(function () {
  const toggle = document.querySelector(".menu-toggle");
  const nav = document.querySelector(".nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      const open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", String(open));
    });
  }

  document.querySelectorAll(".nav-drop > button").forEach(function (btn) {
    btn.addEventListener("click", function (event) {
      event.stopPropagation();
      btn.parentElement.classList.toggle("is-open");
    });
  });

  document.addEventListener("click", function () {
    document.querySelectorAll(".nav-drop.is-open").forEach(function (el) {
      el.classList.remove("is-open");
    });
  });

  const lightbox = document.querySelector(".lightbox");
  const lightboxImg = document.querySelector(".lightbox img");
  if (lightbox && lightboxImg) {
    document.querySelectorAll("[data-full]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        lightboxImg.src = btn.getAttribute("data-full");
        lightboxImg.alt = btn.querySelector("img")?.alt || "";
        lightbox.classList.add("is-open");
      });
    });
    lightbox.addEventListener("click", function () {
      lightbox.classList.remove("is-open");
      lightboxImg.src = "";
    });
    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape") {
        lightbox.classList.remove("is-open");
        lightboxImg.src = "";
      }
    });
  }
})();
