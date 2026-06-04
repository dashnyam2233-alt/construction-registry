(function () {
  function ready(fn) {
    if (document.readyState !== "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  }

  ready(function () {
    var btn = document.getElementById("cr-filter-toggle");
    var panel = document.getElementById("changelist-filter");
    if (!btn || !panel) return;

    btn.addEventListener("click", function (e) {
      e.preventDefault();
      panel.classList.toggle("cr-filter-visible");
      btn.textContent = panel.classList.contains("cr-filter-visible")
        ? "▲ Шүүлтүүр"
        : "▼ Шүүлтүүр";
    });
  });
})();