(function () {
  function makeIndexAccordion() {
    const contentMain = document.querySelector("#content-main");
    if (!contentMain) return;

    const tables = contentMain.querySelectorAll(".module table");
    if (!tables.length) return;

    tables.forEach((table) => {
      const caption = table.querySelector("caption");
      if (!caption) return;

      if (caption.querySelector(".registry-app-toggle")) return;

      const link = caption.querySelector("a");
      const titleText = (link ? link.textContent : caption.textContent || "").trim();

      caption.textContent = "";

      const toggle = document.createElement("span");
      toggle.className = "registry-app-toggle";
      toggle.setAttribute("role", "button");
      toggle.setAttribute("tabindex", "0");
      toggle.innerHTML = `<span class="registry-caret"></span><span>${titleText}</span>`;

      // Default: COLLAPSED
      table.classList.add("registry-app-collapsed");
      caption.classList.remove("registry-app-open");

      function toggleOpen() {
        const collapsed = table.classList.toggle("registry-app-collapsed");
        if (!collapsed) caption.classList.add("registry-app-open");
        else caption.classList.remove("registry-app-open");
      }

      toggle.addEventListener("click", function (e) {
        e.preventDefault();
        e.stopPropagation();
        toggleOpen();
      });

      // ✅ KEYDOWN — зөвхөн toggle өөрөө focus дээр байх үед л ажиллана
      toggle.addEventListener("keydown", function (e) {
        if (document.activeElement !== toggle) return;

        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          e.stopPropagation();
          toggleOpen();
        }
      });

      caption.appendChild(toggle);
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    makeIndexAccordion();
  });
})();
