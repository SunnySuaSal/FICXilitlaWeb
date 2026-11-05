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

  const hero = document.querySelector("[data-hero-carousel]");
  if (hero) {
    const slides = Array.prototype.slice.call(hero.querySelectorAll(".hero-slide"));
    const dots = Array.prototype.slice.call(hero.querySelectorAll(".hero-dots button"));
    const copy = hero.querySelector(".hero-copy");
    const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    let index = 0;
    let timer = 0;

    function show(next) {
      index = (next + slides.length) % slides.length;
      slides.forEach(function (slide, i) {
        const on = i === index;
        slide.classList.toggle("is-active", on);
        slide.setAttribute("aria-hidden", on ? "false" : "true");
      });
      dots.forEach(function (dot, i) {
        dot.setAttribute("aria-selected", i === index ? "true" : "false");
      });
      const poster = slides[index].classList.contains("hero-slide--poster");
      hero.classList.toggle("is-poster", poster);
      if (copy) copy.setAttribute("aria-hidden", poster ? "true" : "false");
    }

    function stop() {
      window.clearInterval(timer);
      timer = 0;
    }

    function start() {
      stop();
      if (reduce || slides.length < 2) return;
      timer = window.setInterval(function () {
        show(index + 1);
      }, 7000);
    }

    dots.forEach(function (dot, i) {
      dot.addEventListener("click", function () {
        show(i);
        start();
      });
    });

    hero.addEventListener("mouseenter", stop);
    hero.addEventListener("mouseleave", start);
    document.addEventListener("visibilitychange", function () {
      if (document.hidden) stop();
      else start();
    });

    show(0);
    start();
  }

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
