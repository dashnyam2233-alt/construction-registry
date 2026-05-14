// registry/static/registry/public_home.js v3
(function () {
  function qs(sel, root) { return (root || document).querySelector(sel); }

  /* ── Compose toggle ── */
  function initCompose() {
    var wrap = qs('[data-chat-compose]');
    if (!wrap) return;
    var btn  = qs('[data-compose-toggle]', wrap);
    var body = qs('[data-compose-body]', wrap);
    if (!btn || !body) return;
    body.hidden = true;
    btn.setAttribute('aria-expanded', 'false');
    btn.textContent = 'Дэлгэх ▾';
    btn.addEventListener('click', function () {
      var isOpen = !body.hidden;
      body.hidden = isOpen;
      btn.setAttribute('aria-expanded', String(!isOpen));
      btn.textContent = isOpen ? 'Дэлгэх ▾' : 'Эвхэх ▴';
      if (!isOpen) { var ta = qs('textarea', body); if (ta) ta.focus(); }
    });
  }

  /* ── Ticker (урсдаг зар) ── */
  function initTicker() {
    var ticker = qs('#heroTicker');
    var track  = qs('#heroTickerTrack');
    if (!ticker || !track) return;

    /* Агуулгыг хоёр дахин хуулж тасралтгүй гүйлт хийнэ */
    var clone = track.cloneNode(true);
    ticker.appendChild(clone);

    var speed = 0.5;   /* px per frame — хурдыг энд тохируулна */
    var pos   = 0;
    var paused = false;
    var raf;

    function getTrackWidth() {
      return track.scrollWidth;
    }

    function step() {
      if (!paused) {
        pos -= speed;
        var w = getTrackWidth();
        if (Math.abs(pos) >= w) {
          pos = 0;
        }
        ticker.scrollLeft = 0;
        track.style.transform = 'translateX(' + pos + 'px)';
        clone.style.transform  = 'translateX(' + pos + 'px)';
      }
      raf = requestAnimationFrame(step);
    }

    ticker.addEventListener('mouseenter', function () { paused = true; });
    ticker.addEventListener('mouseleave', function () { paused = false; });

    raf = requestAnimationFrame(step);
  }

  document.addEventListener('DOMContentLoaded', function () {
    initCompose();
    initTicker();
  });
})();
