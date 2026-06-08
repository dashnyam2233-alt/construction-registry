const LanguageSwitcher = (() => {
  const TRANSLATE_URL = "/translate/content/";
  const SET_LANG_URL  = "/translate/set-lang/";
  const STORAGE_KEY   = "bnb_lang";
  const BATCH_SIZE    = 20;
  let currentLang      = localStorage.getItem(STORAGE_KEY) || "mn";
  let translationCache = {};

  function getElements() {
    return Array.from(document.querySelectorAll("[data-translate]"));
  }

  function getCsrf() {
    const c = document.cookie.split(";").find(s => s.trim().startsWith("csrftoken="));
    return c ? c.trim().split("=")[1] : "";
  }

  async function fetchTranslations(texts, targetLang) {
    const allResults = [];
    for (let i = 0; i < texts.length; i += BATCH_SIZE) {
      const batch = texts.slice(i, i + BATCH_SIZE);
      const res = await fetch(TRANSLATE_URL, {
        method: "POST",
        headers: {"Content-Type": "application/json", "X-CSRFToken": getCsrf()},
        body: JSON.stringify({ texts: batch, target: targetLang }),
      });
      const data = await res.json();
      if (data.error) throw new Error(data.error);
      allResults.push(...(data.translations || []));
    }
    return allResults;
  }

  function applyTranslations(elements, translations) {
    elements.forEach((el, i) => {
      if (translations[i] !== undefined) el.innerText = translations[i];
    });
  }

  async function translatePage(targetLang) {
    const elements = getElements();
    if (!elements.length) return;

    elements.forEach(el => {
      if (!el.dataset.originalText) {
        el.dataset.originalText = el.innerText.trim();
      }
    });

    if (targetLang === "mn") {
      elements.forEach(el => { el.innerText = el.dataset.originalText; });
      return;
    }

    const texts = elements.map(el => el.dataset.originalText).filter(t => t.length > 0);
    if (!texts.length) return;

    const cacheKey = targetLang + "|" + texts.join("|");
    if (translationCache[cacheKey]) {
      applyTranslations(elements, translationCache[cacheKey]);
      return;
    }

    const btn = document.getElementById("lang-toggle-btn");
    if (btn) { btn.disabled = true; btn.classList.add("translating"); }
    try {
      const translations = await fetchTranslations(texts, targetLang);
      translationCache[cacheKey] = translations;
      applyTranslations(elements, translations);
    } catch (err) {
      console.error("[BNB Lang] Failed:", err);
    } finally {
      if (btn) { btn.disabled = false; btn.classList.remove("translating"); }
    }
  }

  function updateButton() {
    const btn = document.getElementById("lang-toggle-btn");
    if (!btn) return;
    if (currentLang === "mn") {
      btn.innerHTML = `🇲🇳 <span>МН</span><span class="lang-sep">|</span><span class="lang-dim">EN</span>`;
    } else {
      btn.innerHTML = `🇬🇧 <span>EN</span><span class="lang-sep">|</span><span class="lang-dim">МН</span>`;
    }
  }

  async function toggle() {
    currentLang = currentLang === "mn" ? "en" : "mn";
    localStorage.setItem(STORAGE_KEY, currentLang);
    updateButton();
    await translatePage(currentLang);
    fetch(`${SET_LANG_URL}${currentLang}/?next=${encodeURIComponent(window.location.pathname)}`);
  }

  function init() {
    updateButton();
    const btn = document.getElementById("lang-toggle-btn");
    if (btn) btn.addEventListener("click", toggle);
    // Хуудас load болоход EN байвал автоматаар орчуулна
    if (currentLang === "en") {
      translatePage("en");
    }
  }

  return { init, toggle };
})();

document.addEventListener("DOMContentLoaded", LanguageSwitcher.init);