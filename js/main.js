/* ==========================================================================
   Golf Resort Adendorf – Interaktion & Animation
   GSAP + ScrollTrigger + Lenis (CDN) · gleiche Scroll-Mechanik wie KomKom
   ========================================================================== */

(function () {
  "use strict";

  const prefersReduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const hasGsap = typeof gsap !== "undefined";

  document.documentElement.classList.remove("no-js");
  if (prefersReduced) document.documentElement.classList.add("reduced-motion");

  /* Smooth Scroll (Lenis) */
  let lenis = null;
  if (!prefersReduced && typeof Lenis !== "undefined") {
    lenis = new Lenis({ duration: 1.15, smoothWheel: true });
    function raf(time) { lenis.raf(time); requestAnimationFrame(raf); }
    requestAnimationFrame(raf);
    lenis.on("scroll", () => { if (typeof ScrollTrigger !== "undefined") ScrollTrigger.update(); });
  }

  /* Header */
  const header = document.querySelector(".site-header");
  let lastY = 0;
  function onScroll() {
    const y = window.scrollY;
    if (header) {
      header.classList.toggle("is-scrolled", y > 40);
      if (y > 320 && y > lastY + 6) header.classList.add("is-hidden");
      else if (y < lastY - 6 || y < 320) header.classList.remove("is-hidden");
    }
    lastY = y;
    const dock = document.querySelector(".cta-dock");
    if (dock) dock.classList.toggle("is-visible", y > window.innerHeight * (document.querySelector(".pov-stage") ? 4.4 : 0.7));
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* Burger */
  const burger = document.querySelector(".burger");
  const mobileNav = document.querySelector(".mobile-nav");
  if (burger && mobileNav) {
    burger.addEventListener("click", () => {
      const open = mobileNav.classList.toggle("is-open");
      burger.classList.toggle("is-open", open);
      burger.setAttribute("aria-expanded", open);
      document.body.style.overflow = open ? "hidden" : "";
      if (lenis) open ? lenis.stop() : lenis.start();
    });
    mobileNav.querySelectorAll("a").forEach((a, i) => {
      a.style.transitionDelay = (0.06 + i * 0.045) + "s";
    });
  }

  /* Aktiver Nav-Punkt */
  const path = location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll(".main-nav a, .mobile-nav a").forEach((a) => {
    if (a.getAttribute("href") === path) a.classList.add("is-active");
  });

  /* Page Transition */
  const pt = document.createElement("div");
  pt.className = "page-transition";
  document.body.appendChild(pt);
  if (sessionStorage.getItem("ga-transition") === "1") {
    sessionStorage.removeItem("ga-transition");
    pt.classList.add("is-out");
    setTimeout(() => pt.classList.remove("is-out"), 900);
  }
  if (!prefersReduced) {
    document.addEventListener("click", (e) => {
      const a = e.target.closest("a");
      if (!a) return;
      const href = a.getAttribute("href") || "";
      if (
        a.target === "_blank" || e.metaKey || e.ctrlKey ||
        href.startsWith("#") || href.startsWith("http") ||
        href.startsWith("mailto") || href.startsWith("tel") ||
        !href.endsWith(".html") && !href.includes(".html?") && !href.includes(".html#")
      ) return;
      e.preventDefault();
      sessionStorage.setItem("ga-transition", "1");
      pt.classList.add("is-in");
      setTimeout(() => { location.href = href; }, 480);
    });
  }

  /* Reveals – auch für nachträglich per JS eingefügte Elemente aufrufbar */
  window.gaInitReveals = function () {
    if (!hasGsap || typeof ScrollTrigger === "undefined" || prefersReduced) {
      document.querySelectorAll("[data-reveal]").forEach((el) => {
        el.style.opacity = 1; el.style.transform = "none";
      });
      return;
    }
    document.querySelectorAll("[data-reveal]:not([data-reveal-done])").forEach((el) => {
      el.setAttribute("data-reveal-done", "1");
      const type = el.getAttribute("data-reveal");
      const delay = parseFloat(el.getAttribute("data-delay") || 0);
      const from = { opacity: 0, y: 44, x: 0, scale: 1 };
      if (type === "left") { from.x = -54; from.y = 0; }
      if (type === "right") { from.x = 54; from.y = 0; }
      if (type === "scale") { from.scale = 0.9; from.y = 0; }
      gsap.fromTo(el, from, {
        opacity: 1, y: 0, x: 0, scale: 1,
        duration: 1.1, delay, ease: "power3.out",
        scrollTrigger: { trigger: el, start: "top 88%", once: true }
      });
    });
  };

  if (hasGsap && typeof ScrollTrigger !== "undefined" && !prefersReduced) {
    gsap.registerPlugin(ScrollTrigger);

    window.gaInitReveals();

    document.querySelectorAll(".split-lines").forEach((el) => {
      const text = el.textContent.trim();
      el.textContent = "";
      el.setAttribute("aria-label", text);
      const wrap = document.createElement("span");
      wrap.className = "line-wrap";
      const inner = document.createElement("span");
      inner.className = "line-inner";
      inner.textContent = text;
      wrap.appendChild(inner);
      el.appendChild(wrap);
      gsap.set(inner, { y: "110%" });
      gsap.to(inner, {
        y: 0, duration: 1.2, ease: "power4.out",
        scrollTrigger: { trigger: el, start: "top 90%", once: true }
      });
    });

    document.querySelectorAll(".blob").forEach((b, i) => {
      gsap.to(b, {
        y: (i % 2 ? -110 : 110), ease: "none",
        scrollTrigger: { trigger: b.parentElement, start: "top bottom", end: "bottom top", scrub: 1.2 }
      });
    });

    document.querySelectorAll("[data-count]").forEach((el) => {
      const target = parseFloat(el.getAttribute("data-count"));
      const suffix = el.getAttribute("data-suffix") || "";
      const obj = { v: 0 };
      gsap.to(obj, {
        v: target, duration: 2, ease: "power2.out",
        scrollTrigger: { trigger: el, start: "top 85%", once: true },
        onUpdate() { el.textContent = Math.round(obj.v) + suffix; }
      });
    });
  } else {
    document.querySelectorAll("[data-reveal]").forEach((el) => {
      el.style.opacity = 1; el.style.transform = "none";
    });
  }

  /* Marquee */
  document.querySelectorAll(".marquee").forEach((mq) => {
    const track = mq.querySelector(".marquee-track");
    if (!track) return;
    const base = track.innerHTML;
    while (track.scrollWidth < window.innerWidth * 2.2) track.innerHTML += base;
    if (prefersReduced) return;
    let x = 0;
    const speed = parseFloat(mq.getAttribute("data-speed") || 0.6);
    function step() {
      x -= speed;
      const half = track.scrollWidth / 2;
      if (-x >= half) x += half;
      track.style.transform = "translateX(" + x + "px)";
      requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  });

  /* Magnetic Buttons */
  if (!prefersReduced && window.matchMedia("(pointer: fine)").matches) {
    document.querySelectorAll(".btn").forEach((btn) => {
      btn.addEventListener("mousemove", (e) => {
        const r = btn.getBoundingClientRect();
        btn.style.transform = "translate(" + (e.clientX - r.left - r.width / 2) * 0.16 + "px," + ((e.clientY - r.top - r.height / 2) * 0.2 - 2) + "px)";
      });
      btn.addEventListener("mouseleave", () => { btn.style.transform = ""; });
    });
  }
})();
