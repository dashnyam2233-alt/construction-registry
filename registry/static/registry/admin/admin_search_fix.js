(function () {
  function isChangeList() {
    return !!document.querySelector("#changelist");
  }

  function caretToEnd(el) {
    try {
      const len = (el.value || "").length;
      el.setSelectionRange(len, len);
    } catch (e) {}
  }

  function fixSearchBox() {
    if (!isChangeList()) return;

    const wrapper = document.querySelector("#changelist-search");
    if (!wrapper) return;

    const form = wrapper.querySelector("form");
    if (!form) return;

    const input0 = form.querySelector('input[name="q"]');
    if (!input0) return;

    // ✅ 1) input дээр наалдсан listener-үүдийг цэвэрлэх (clone)
    const input = input0.cloneNode(true);
    input.value = input0.value || "";
    input.autocomplete = "off";
    input.spellcheck = false;
    input0.parentNode.replaceChild(input, input0);

    // ✅ 2) Гол шийдэл: “auto reload” хийдэг delegated handler-үүдийг тасална.
    // - Search input дээр бичих үед гарах бүх input/keyup/keydown event-ийг capture дээр хаана
    // - Enter дарсан үед л нэвтрүүлнэ (form submit ажиллана)
    function isSearchTarget(e) {
      return e && e.target === input;
    }

    // input event: always block (auto-search ихэвчлэн эндээс эхэлдэг)
    document.addEventListener(
      "input",
      function (e) {
        if (!isSearchTarget(e)) return;
        e.stopImmediatePropagation();
      },
      true
    );

    // keydown: Enter биш бол блоклоно (delegated key handlers-ийг тасална)
    document.addEventListener(
      "keydown",
      function (e) {
        if (!isSearchTarget(e)) return;
        if (e.key === "Enter") return; // зөвхөн Enter-г нэвтрүүлнэ
        e.stopImmediatePropagation();
      },
      true
    );

    // keyup: Enter биш бол блоклоно (зарим auto-search keyup дээр байдаг)
    document.addEventListener(
      "keyup",
      function (e) {
        if (!isSearchTarget(e)) return;
        if (e.key === "Enter") return;
        e.stopImmediatePropagation();
      },
      true
    );

    // ✅ 3) submit бол зөвхөн Enter/товч дээр ажиллана
    // (ямар нэг скрипт form.submit() хийвэл submitter байхгүй байдаг — түүнийг болиулна)
    form.addEventListener(
      "submit",
      function (e) {
        if (!e.submitter) {
          e.preventDefault();
          e.stopImmediatePropagation();
          return false;
        }
      },
      true
    );

    // ✅ 4) Page load дээр курсороо зөв тавина
    try {
      input.focus({ preventScroll: true });
      caretToEnd(input);
    } catch (e) {}
  }

  document.addEventListener("DOMContentLoaded", fixSearchBox);
})();
