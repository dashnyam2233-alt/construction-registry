(function () {
  function byId(id) {
    return document.getElementById(id);
  }

  function getRow(el) {
    // Django admin typically wraps field in .form-row
    if (!el) return null;
    return el.closest(".form-row") || el.closest(".fieldBox") || el.parentElement;
  }

  function showRow(row, show) {
    if (!row) return;
    row.style.display = show ? "" : "none";
  }

  function setRequired(input, required) {
    if (!input) return;
    input.required = !!required;
    if (!required && input.value) {
      // keep value as-is; do not wipe automatically (safer for user)
    }
  }

  function initOtherToggle() {
    // Worker modeladmin uses default ids: id_profession, id_profession_other, id_responsible_role, id_responsible_role_other
    var professionSel = byId("id_profession");
    var professionOther = byId("id_profession_other");

    var roleSel = byId("id_responsible_role");
    var roleOther = byId("id_responsible_role_other");

    var profRow = getRow(professionOther);
    var roleRow = getRow(roleOther);

    function refresh() {
      var profIsOther = professionSel && professionSel.value === "other";
      showRow(profRow, !!profIsOther);
      setRequired(professionOther, !!profIsOther);

      // role "OTHER" is used in RESPONSIBLE_ROLE_CHOICES
      var roleIsOther = roleSel && roleSel.value === "OTHER";
      showRow(roleRow, !!roleIsOther);
      setRequired(roleOther, !!roleIsOther);
    }

    if (professionSel) professionSel.addEventListener("change", refresh);
    if (roleSel) roleSel.addEventListener("change", refresh);

    refresh();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initOtherToggle);
  } else {
    initOtherToggle();
  }
})();