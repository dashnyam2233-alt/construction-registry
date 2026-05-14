// registry/static/registry/public_modal.js
(function () {
  const modal = document.getElementById("authModal");
  const frame = document.getElementById("authFrame");
  if (!modal || !frame) return;

  const titleEl = document.getElementById("authModalTitle");

  const tabBtns = Array.from(document.querySelectorAll("[data-auth-tab]"));
  const openBtns = Array.from(document.querySelectorAll("[data-auth-open]"));
  const closeBtns = Array.from(document.querySelectorAll("[data-auth-close]"));

  const next = encodeURIComponent("/public/");

  function setActiveTab(kind) {
    tabBtns.forEach((b) => b.classList.toggle("is-active", b.dataset.authTab === kind));
    if (titleEl) titleEl.textContent = kind === "register" ? "Бүртгүүлэх" : "Нэвтрэх";
  }

  function urlFor(kind) {
    if (kind === "register") return `/register/?next=${next}`;
    return `/login/?next=${next}`;
  }

  function openModal(kind) {
    setActiveTab(kind);
    modal.classList.add("is-open");
    modal.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
    frame.src = urlFor(kind);
  }

  function closeModal() {
    modal.classList.remove("is-open");
    modal.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";
    frame.src = "about:blank";
  }

  openBtns.forEach((btn) => {
    btn.addEventListener("click", () => openModal(btn.dataset.authOpen || "login"));
  });

  tabBtns.forEach((btn) => {
    btn.addEventListener("click", () => openModal(btn.dataset.authTab || "login"));
  });

  closeBtns.forEach((btn) => btn.addEventListener("click", closeModal));

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && modal.classList.contains("is-open")) closeModal();
  });
})();
