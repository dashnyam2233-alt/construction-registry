/* CR changelist: Collapsible FILTER (▲/▼) + HARD remove "white space"
   - Uses inline styles on #main to defeat any existing CSS (even !important conflicts)
   - Default collapsed => main table full width
   - Remembers state in localStorage per path
*/
(function () {
  function ready(fn) {
    if (document.readyState !== "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  }

  function el(tag, attrs) {
    var e = document.createElement(tag);
    if (attrs) {
      Object.keys(attrs).forEach(function (k) {
        if (k === "class") e.className = attrs[k];
        else if (k === "text") e.textContent = attrs[k];
        else e.setAttribute(k, attrs[k]);
      });
    }
    return e;
  }

  function storageKey() {
    return "cr_filter_collapsed:" + window.location.pathname;
  }

  function getSavedCollapsedDefaultTrue() {
    try {
      var v = localStorage.getItem(storageKey());
      if (v === "0") return false;
      if (v === "1") return true;
    } catch (e) {}
    return true; // default collapsed
  }

  function setMainPadding(px) {
    var main = document.getElementById("main");
    if (!main) return;

    // Inline style = strongest. Also set marginRight to kill any gap.
    main.style.paddingRight = px;
    main.style.marginRight = "0px";
    main.style.boxSizing = "border-box";
  }

  function applyState(isCollapsed) {
    var b = document.body;
    if (!b) return;

    if (isCollapsed) {
      b.classList.add("cr-filter-collapsed");
      b.classList.remove("cr-filter-open");
      setMainPadding("0px");        // ✅ white space kill
    } else {
      b.classList.add("cr-filter-open");
      b.classList.remove("cr-filter-collapsed");
      setMainPadding("390px");      // ✅ reserve space for fixed filter
    }

    try { localStorage.setItem(storageKey(), isCollapsed ? "1" : "0"); } catch (e) {}
  }

  ready(function () {
    if (!document.body || !document.body.classList.contains("change-list")) return;

    var filter = document.getElementById("changelist-filter");
    if (!filter) return;

    // Already processed?
    if (filter.querySelector(".cr-filter-head")) {
      applyState(getSavedCollapsedDefaultTrue());
      return;
    }

    // Build header + body wrapper inside #changelist-filter
    var head = el("div", { class: "cr-filter-head" });
    head.appendChild(el("div", { text: "ШҮҮЛТҮҮР" }));

    var btn = el("button", { type: "button", class: "cr-filter-toggle" });
    head.appendChild(btn);

    var bodyWrap = el("div", { class: "cr-filter-body" });

    // Move existing children into bodyWrap
    while (filter.firstChild) bodyWrap.appendChild(filter.firstChild);

    filter.appendChild(head);
    filter.appendChild(bodyWrap);

    function syncButton() {
      var collapsed = document.body.classList.contains("cr-filter-collapsed");
      btn.textContent = collapsed ? "\u25BC" : "\u25B2"; // ▼ / ▲
      btn.setAttribute("aria-expanded", collapsed ? "false" : "true");
    }

    btn.addEventListener("click", function () {
      var collapsed = document.body.classList.contains("cr-filter-collapsed");
      applyState(!collapsed);
      syncButton();
    });

    // Initial state
    applyState(getSavedCollapsedDefaultTrue());
    syncButton();

    // Safety: if window resized small, remove inline padding so Django responsive works
    window.addEventListener("resize", function () {
      if (window.innerWidth <= 1200) {
        setMainPadding("0px");
      } else {
        // restore according to current state
        var collapsed2 = document.body.classList.contains("cr-filter-collapsed");
        setMainPadding(collapsed2 ? "0px" : "390px");
      }
    });
  });
})();