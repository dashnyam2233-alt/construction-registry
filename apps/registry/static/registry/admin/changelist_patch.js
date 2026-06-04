(function () {
  function ready(fn) {
    if (document.readyState !== "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  }
  ready(function () {
    var filter = document.getElementById("changelist-filter");
    if (filter) {
      filter.style.display = "block";
    }
  });
})();