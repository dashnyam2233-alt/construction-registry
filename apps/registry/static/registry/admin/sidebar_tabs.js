(function () {
  function ready(fn) {
    if (document.readyState !== "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  }

  ready(function () {
    if (window.location.pathname.indexOf("/admin/login") === 0) return;

    var sidebar = document.getElementById("cr-admin-right-sidebar");
    if (!sidebar) return;

    var djangoFilter = document.getElementById("changelist-filter");
    var hasFilter = !!djangoFilter;

    // ===== Tab header =====
    var tabHeader = document.createElement("div");
    tabHeader.id = "cr-sidebar-tabs";
    tabHeader.style.cssText =
      "display:flex;border-bottom:2px solid #e6e6e6;background:#fff;" +
      "position:sticky;top:0;z-index:10000;";

    function makeTabBtn(id, label) {
      var b = document.createElement("button");
      b.type = "button";
      b.id = id;
      b.innerHTML = label;
      b.style.cssText =
        "flex:1;padding:12px 8px;border:none;background:#fff;cursor:pointer;" +
        "font-weight:700;font-size:13px;color:#333;" +
        "border-bottom:3px solid transparent;transition:all 0.15s;";
      return b;
    }

    var btnChat = makeTabBtn("cr-tab-chat", "💬 Чат");
    var btnFilter = makeTabBtn("cr-tab-filter", "🔍 Шүүлтүүр");

    tabHeader.appendChild(btnChat);
    if (hasFilter) tabHeader.appendChild(btnFilter);

    // ===== Чат хэсэг (sidebar-ийн одоогийн агуулгыг хадгална) =====
    var chatSection = document.createElement("div");
    chatSection.id = "cr-chat-section";
    chatSection.style.padding = "0";

    var children = Array.prototype.slice.call(sidebar.children);
    for (var i = 0; i < children.length; i++) {
      chatSection.appendChild(children[i]);
    }

    // ===== Шүүлтүүр хэсэг =====
    var filterSection = document.createElement("div");
    filterSection.id = "cr-filter-section";
    filterSection.style.cssText = "padding:12px;display:none;";

    if (hasFilter) {
      var filterTitle = djangoFilter.querySelector("h2");
      if (filterTitle) filterTitle.style.display = "none";

      djangoFilter.style.cssText =
        "position:static !important;width:auto !important;float:none !important;" +
        "padding:0 !important;background:transparent !important;border:none !important;";

      filterSection.appendChild(djangoFilter);
    }

    // ===== Sidebar дотор шинээр угсрах =====
    sidebar.innerHTML = "";
    sidebar.appendChild(tabHeader);
    sidebar.appendChild(chatSection);
    sidebar.appendChild(filterSection);

    // ===== Tab солих =====
    function switchTab(tab) {
      if (tab === "filter" && hasFilter) {
        chatSection.style.display = "none";
        filterSection.style.display = "block";
        btnFilter.style.borderBottomColor = "#0d6efd";
        btnFilter.style.color = "#0d6efd";
        btnChat.style.borderBottomColor = "transparent";
        btnChat.style.color = "#333";
      } else {
        chatSection.style.display = "block";
        filterSection.style.display = "none";
        btnChat.style.borderBottomColor = "#0d6efd";
        btnChat.style.color = "#0d6efd";
        btnFilter.style.borderBottomColor = "transparent";
        btnFilter.style.color = "#333";
      }
      try { localStorage.setItem("cr_sidebar_tab", tab); } catch (e) {}
    }

    btnChat.addEventListener("click", function () { switchTab("chat"); });
    btnFilter.addEventListener("click", function () { switchTab("filter"); });

    // ===== Анхны tab =====
    var savedTab = "chat";
    try {
      var saved = localStorage.getItem("cr_sidebar_tab");
      if (saved) savedTab = saved;
      else if (hasFilter) savedTab = "filter";
    } catch (e) {}
    switchTab(savedTab);
  });
})();