(function () {
  const UB_DISTRICTS = [
    ["", "---------"],
    ["BGD", "Баянгол"],
    ["BZD", "Баянзүрх"],
    ["CHD", "Чингэлтэй"],
    ["SHD", "Сонгинохайрхан"],
    ["SBD", "Сүхбаатар"],
    ["HUD", "Хан-Уул"],
    ["ND", "Налайх"],
    ["BD", "Багануур"],
    ["BHD", "Багахангай"],
  ];

  // ЖИШЭЭ: Увс (чи хэлсэн жишээгээр)
  const AIMAG_SOUMS = {
    UVS: [
      ["", "---------"],
      ["Өндөрхангай", "Өндөрхангай"],
      ["Улаангом", "Улаангом"],
      ["Баруунтуруун", "Баруунтуруун"],
      ["Малчин", "Малчин"],
      ["Тэс", "Тэс"],
      ["Түргэн", "Түргэн"],
      ["Хяргас", "Хяргас"],
      ["Сагил", "Сагил"],
      ["Наранбулаг", "Наранбулаг"],
      ["Давст", "Давст"],
      ["Зүүнхангай", "Зүүнхангай"],
      ["Завхан", "Завхан"],
      ["Ховд", "Ховд"],
      ["Цагаанхайрхан", "Цагаанхайрхан"],
      ["Бөхмөрөн", "Бөхмөрөн"],
    ],
  };

  function setOptions(selectEl, options) {
    if (!selectEl) return;
    selectEl.innerHTML = "";
    for (const [val, label] of options) {
      const opt = document.createElement("option");
      opt.value = val;
      opt.textContent = label;
      selectEl.appendChild(opt);
    }
  }

  function autoSelectFirstNonEmpty(selectEl) {
    if (!selectEl) return;
    for (let i = 0; i < selectEl.options.length; i++) {
      const v = (selectEl.options[i].value || "").trim();
      if (v !== "") {
        selectEl.selectedIndex = i;
        return;
      }
    }
    selectEl.selectedIndex = 0;
  }

  function hookBirthPlace(cityId, subId) {
    const cityEl = document.getElementById(cityId);
    const subEl = document.getElementById(subId);
    if (!cityEl || !subEl) return;

    function apply(autoPick) {
      const city = cityEl.value;

      if (!city) {
        setOptions(subEl, [["", "---------"]]);
        subEl.value = "";
        subEl.disabled = true;
        return;
      }

      subEl.disabled = false;

      if (city === "UB") {
        setOptions(subEl, UB_DISTRICTS);
        if (autoPick) autoSelectFirstNonEmpty(subEl);
        return;
      }

      const soums = AIMAG_SOUMS[city] || [["", "---------"]];
      setOptions(subEl, soums);
      if (autoPick) autoSelectFirstNonEmpty(subEl);
    }

    cityEl.addEventListener("change", function () {
      apply(true);
    });

    apply(true);
  }

  document.addEventListener("DOMContentLoaded", function () {
    hookBirthPlace("id_birth_place_city", "id_birth_place_sub");
  });
})();
