/* registry/static/registry/admin/admin_menu.js v3 */
(function () {
  'use strict';

  var GROUPS = [
    {
      icon: '🏢',
      label: 'БАЙГУУЛЛАГА',
      items: [
        { url: '/admin/registry/company/',                   label: 'Компаниуд' },
        { url: '/admin/registry/governmentorganization/',    label: 'Төрийн байгууллагууд' },
        { url: '/admin/registry/nongovernmentorganization/', label: 'ТББ байгууллагууд' },
      ]
    },
    {
      icon: '👷',
      label: 'АЖИЛЛАГСАД',
      items: [
        { url: '/admin/registry/worker/',        label: 'Ажиллагсад' },
        { url: '/admin/registry/familymember/',  label: 'Ажилтны хамаарал' },
        { url: '/admin/registry/brigade/',       label: 'Бригадууд' },
        { url: '/admin/registry/brigademember/', label: 'Бригадын гишүүд' },
      ]
    },
    {
      icon: '📢',
      label: 'МАРКЕТИНГ',
      items: [
        { url: '/admin/registry/messagelog/',  label: '📨 Мессеж илгээх', highlight: true },
        { url: '/admin/registry/herobanner/',  label: 'Hero баннер' },
        { url: '/admin/registry/subbanner/',   label: 'Дэд баннер' },
        { url: '/admin/registry/sliderad/',    label: 'Урсдаг зарууд' },
        { url: '/admin/registry/banner/',      label: 'Баннерууд' },
        { url: '/admin/registry/publicpost/',  label: 'Нээлттэй постууд' },
      ]
    },
    {
      icon: '👤',
      label: 'ХЭРЭГЛЭГЧ',
      items: [
        { url: '/admin/registry/usercompanyprofile/', label: 'Хэрэглэгчийн компани' },
        { url: '/admin/auth/user/',                   label: 'Хэрэглэгчид' },
        { url: '/admin/auth/group/',                  label: 'Бүлгүүд' },
      ]
    },
    {
      icon: '⚙️',
      label: 'ТОХИРГОО',
      items: [
        { url: '/admin/registry/siteconfig/', label: 'Системийн тохиргоо' },
      ]
    },
  ];

  function buildSidebar() {
    var sidebar = document.getElementById('nav-sidebar');
    if (!sidebar) return;

    var modules = sidebar.querySelectorAll('.module');
    modules.forEach(function (m) { m.remove(); });

    var curPath = window.location.pathname;

    GROUPS.forEach(function (group) {
      var titleEl = document.createElement('div');
      titleEl.className = 'nav-group-title';
      titleEl.innerHTML = '<span class="ng-icon">' + group.icon + '</span>' + group.label;
      sidebar.appendChild(titleEl);

      group.items.forEach(function (item) {
        var isActive = curPath === item.url || curPath.startsWith(item.url.replace(/\/$/, '/'));

        var link = document.createElement('a');
        link.href = item.url;
        link.textContent = item.label;

        if (item.highlight) {
          link.style.cssText = 'display:block;background:#f0a500;color:#0d1117;font-weight:700;border-radius:6px;margin:4px 10px;padding:7px 12px;text-align:center;text-decoration:none;font-size:13px;';
          link.addEventListener('mouseenter', function () { this.style.background = '#d99400'; });
          link.addEventListener('mouseleave', function () { this.style.background = '#f0a500'; });
        } else {
          link.style.cssText = 'display:block;padding:6px 14px 6px 22px;font-size:13px;text-decoration:none;color:var(--link-fg,#417690);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;' + (isActive ? 'background:var(--selected-row,#e4f0f8);font-weight:700;' : '');
          link.addEventListener('mouseenter', function () { this.style.background = 'var(--selected-row,#e4f0f8)'; this.style.color = 'var(--link-hover-color,#265d87)'; });
          link.addEventListener('mouseleave', function () { this.style.background = isActive ? 'var(--selected-row,#e4f0f8)' : ''; this.style.color = 'var(--link-fg,#417690)'; });
        }

        sidebar.appendChild(link);
      });
    });

    var divider = document.createElement('div');
    divider.style.cssText = 'height:1px;background:var(--hairline-color,#e5e5e5);margin:8px 0;';
    sidebar.appendChild(divider);

    var gs = document.createElement('a');
    gs.href = '/admin/global-search/';
    gs.textContent = '🔍 Нэгдсэн хайлт';
    gs.style.cssText = 'display:block;padding:7px 14px 7px 22px;font-size:13px;color:var(--link-fg,#417690);text-decoration:none;';
    sidebar.appendChild(gs);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', buildSidebar);
  } else {
    buildSidebar();
  }
})();
