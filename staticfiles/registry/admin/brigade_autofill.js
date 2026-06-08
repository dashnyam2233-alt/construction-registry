(function () {
  function getAdminBase() {
    var p = window.location.pathname; // /admin/registry/brigade/add/ OR /admin/registry/brigade/5/change/
    p = p.replace(/\/add\/$/, "/");
    p = p.replace(/\/\d+\/change\/$/, "/");
    return p;
  }

  async function fetchWorker(pk) {
    if (!pk) return null;
    var base = getAdminBase();
    var url = base + "worker-info/" + pk + "/";
    var res = await fetch(url, { credentials: "same-origin" });
    return await res.json();
  }

  function byId(id) {
    return document.getElementById(id);
  }

  function setValueById(id, value) {
    var el = byId(id);
    if (!el) return;
    el.value = value || "";
  }

  function clearLeader() {
    setValueById("id_leader_register_no_display", "");
    setValueById("id_leader_full_name_display", "");
    setValueById("id_leader_gender_display", "");
    setValueById("id_leader_birth_date_display", "");
    setValueById("id_leader_birth_place_display", "");
    setValueById("id_leader_married_display", "");
    setValueById("id_leader_profession_display", "");
    setValueById("id_leader_company_display", "");
    setValueById("id_leader_role_display", "");
    setValueById("id_leader_specialty_display", "");
    setValueById("id_leader_phone_display", "");
    setValueById("id_leader_email_display", "");
    setValueById("id_leader_social_display", "");
    setValueById("id_leader_address_display", "");
  }

  function fillLeader(p) {
    if (!p || !p.ok) {
      clearLeader();
      return;
    }

    setValueById("id_leader_register_no_display", p.register_no);
    setValueById("id_leader_full_name_display", p.full_name);
    setValueById("id_leader_gender_display", p.gender);
    setValueById("id_leader_birth_date_display", p.birth_date);

    var birthPlace = [p.birth_place_city, p.birth_place_sub].filter(Boolean).join(" / ");
    setValueById("id_leader_birth_place_display", birthPlace);

    setValueById("id_leader_married_display", p.married);
    setValueById("id_leader_profession_display", p.profession);
    setValueById("id_leader_company_display", p.company);
    setValueById("id_leader_role_display", p.responsible_role);
    setValueById("id_leader_specialty_display", p.engineer_specialty);
    setValueById("id_leader_phone_display", p.phone);
    setValueById("id_leader_email_display", p.email);

    var social = [p.facebook_url, p.instagram_url, p.viber].filter(Boolean).join(" | ");
    setValueById("id_leader_social_display", social);

    var addr = [p.city, p.district, p.address].filter(Boolean).join(" / ");
    setValueById("id_leader_address_display", addr);
  }

  function fillMember(prefix, p) {
    function set(suffix, value) {
      setValueById("id_" + prefix + "-" + suffix, value);
    }

    if (!p || !p.ok) {
      set("worker_register_no_display", "");
      set("worker_full_name_display", "");
      set("worker_phone_display", "");
      set("worker_email_display", "");
      set("worker_company_display", "");
      return;
    }

    set("worker_register_no_display", p.register_no);
    set("worker_full_name_display", p.full_name);
    set("worker_phone_display", p.phone);
    set("worker_email_display", p.email);
    set("worker_company_display", p.company);
  }

  function prefixFromElement(el) {
    if (!el) return null;

    // prefer id
    if (el.id) {
      var m1 = String(el.id).match(/^id_(.+)-worker$/);
      if (m1) return m1[1];
    }

    // fallback: name
    if (el.name) {
      // members-0-worker OR brigademember_set-0-worker
      var m2 = String(el.name).match(/^(.+)-worker$/);
      if (m2) return m2[1];
    }

    return null;
  }

  async function updateLeader() {
    var sel = byId("id_leader_worker");
    if (!sel) return;

    var pk = sel.value;
    if (!pk) {
      fillLeader(null);
      return;
    }
    var p = await fetchWorker(pk);
    fillLeader(p);
  }

  async function updateMemberFromSelect(sel) {
    if (!sel) return;
    var prefix = prefixFromElement(sel);
    if (!prefix) return;

    var pk = sel.value;
    if (!pk) {
      fillMember(prefix, null);
      return;
    }
    var p = await fetchWorker(pk);
    fillMember(prefix, p);
  }

  // ✅ event баригдахгүй үед ч ажиллуулах "poll scan"
  async function scanAndFillMembers() {
    var selects = document.querySelectorAll("select[name$='-worker'], select[id$='-worker']");
    for (var i = 0; i < selects.length; i++) {
      var sel = selects[i];
      var prefix = prefixFromElement(sel);
      if (!prefix) continue;

      // display field exists?
      var display = byId("id_" + prefix + "-worker_full_name_display");
      if (!display) continue;

      // already filled -> skip
      if ((display.value || "").trim() !== "") continue;

      // has selected value -> fill
      if (sel.value) {
        await updateMemberFromSelect(sel);
      }
    }
  }

  function bind() {
    // leader
    var leader = byId("id_leader_worker");
    if (leader) {
      leader.addEventListener("change", updateLeader);
      updateLeader();
    }

    // members (delegation)
    document.addEventListener("change", function (e) {
      var t = e.target;
      if (!t) return;
      // allow both select and hidden select2 backing select
      if ((t.tagName || "").toUpperCase() !== "SELECT") return;
      if (!(t.name && t.name.endsWith("-worker")) && !(t.id && t.id.endsWith("-worker"))) return;
      updateMemberFromSelect(t);
    });

    // select2 events (if present)
    if (window.django && django.jQuery) {
      var $ = django.jQuery;

      $(document).on("select2:select select2:clear", "#id_leader_worker", function () {
        updateLeader();
      });

      $(document).on("select2:select select2:clear", "select[name$='-worker'], select[id$='-worker']", function (e) {
        updateMemberFromSelect(e.target);
      });
    }

    // ✅ periodic scan (event алдагдсан ч бөглөнө)
    setInterval(function () {
      scanAndFillMembers();
    }, 600);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", bind);
  } else {
    bind();
  }
})();
