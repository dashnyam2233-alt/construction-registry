(function () {
  function qs(sel, root) { return (root || document).querySelector(sel); }
  function qsa(sel, root) { return Array.from((root || document).querySelectorAll(sel)); }

  function getMainCodes() {
    return qsa('input[name="activity_directions"]').filter(b => b.checked).map(b => b.value);
  }

  function getSelectedValues(selectEl) {
    return Array.from(selectEl.options).filter(o => o.selected).map(o => o.value);
  }

  function setOptions(selectEl, values, selectedValues) {
    selectEl.innerHTML = "";
    values.forEach(v => {
      const opt = document.createElement("option");
      opt.value = v;
      opt.textContent = v;
      if (selectedValues.includes(v)) opt.selected = true;
      selectEl.appendChild(opt);
    });
  }

  function setPlaceholder(selectEl, text) {
    selectEl.innerHTML = "";
    const opt = document.createElement("option");
    opt.value = "";
    opt.textContent = text;
    opt.disabled = true;
    opt.selected = true;
    selectEl.appendChild(opt);
  }

  async function loadSubMap() {
    // admin/model url: /admin/registry/brigade/sub-map/
    const url = "/admin/registry/brigade/sub-map/";
    const res = await fetch(url, { credentials: "same-origin" });
    if (!res.ok) return {};
    return await res.json();
  }

  function enableToggleNoCtrl(selectEl) {
    // CTRL хэрэггүй болгож option дээр дархад toggle болгоно
    selectEl.addEventListener("mousedown", function (e) {
      const opt = e.target;
      if (!opt || opt.tagName !== "OPTION") return;
      // placeholder дээр toggle хийхгүй
      if (opt.disabled) return;

      e.preventDefault();
      opt.selected = !opt.selected;

      // Django form-д өөрчлөлт мэдэгдэх
      const ev = new Event("change", { bubbles: true });
      selectEl.dispatchEvent(ev);
    });
  }

  async function init() {
    const subSelect = qs("#id_activity_sub_directions");
    if (!subSelect) return;

    enableToggleNoCtrl(subSelect);

    // эхлээд placeholder
    setPlaceholder(subSelect, "Үндсэн чиглэл сонгоно уу...");
    subSelect.disabled = true;

    const subMap = await loadSubMap();

    const rebuild = () => {
      const mains = getMainCodes();

      if (!mains.length) {
        setPlaceholder(subSelect, "Үндсэн чиглэл сонгоно уу...");
        subSelect.disabled = true;
        return;
      }

      // одоо сонгогдсон дэдүүдийг хадгална
      const currentSelected = getSelectedValues(subSelect);

      // mains дээрх бүх sub-ийг нэгтгэнэ
      let merged = [];
      mains.forEach(code => {
        const subs = subMap[code] || [];
        merged = merged.concat(subs);
      });

      // unique
      const uniq = Array.from(new Set(merged));

      if (!uniq.length) {
        setPlaceholder(subSelect, "Дэд сонголт алга байна...");
        subSelect.disabled = true;
        return;
      }

      // өмнөх сонголтоос боломжтойг нь үлдээнэ
      const keepSelected = currentSelected.filter(v => uniq.includes(v));

      setOptions(subSelect, uniq, keepSelected);
      subSelect.disabled = false;
    };

    // эхний build
    rebuild();

    // main checkbox өөрчлөгдөх бүрт rebuild
    qsa('input[name="activity_directions"]').forEach(b => {
      b.addEventListener("change", rebuild);
    });
  }

  document.addEventListener("DOMContentLoaded", init);
})();
