#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Erzeugt die Unterseiten der Golf-Resort-Adendorf-Website."""

import os

OUT = os.path.dirname(os.path.abspath(__file__))

HEAD = """<!DOCTYPE html>
<html lang="de" class="no-js">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} – Golf Resort Adendorf</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,500&family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
</head>
<body>

<header class="site-header is-scrolled">
  <div class="header-inner">
    <a class="logo" href="index.html" aria-label="Golf Resort Adendorf – Startseite">
      <span class="logo-mark">A</span>
      <span class="logo-text"><strong>Golf Resort Adendorf</strong><span>Castanea Resort</span></span>
    </a>
    <nav class="main-nav" aria-label="Hauptnavigation">
      <a href="golfanlage.html">Golfanlage</a>
      <a href="greenfee.html">Greenfee</a>
      <a href="golf-lernen.html">Golf lernen</a>
      <a href="mitgliedschaft.html">Mitgliedschaft</a>
      <a href="gastronomie.html">Castello</a>
      <a href="kontakt.html">Kontakt</a>
      <a class="nav-ext" href="https://www.castanea-resort.de/de" target="_blank" rel="noopener">Hotel</a>
      <a class="btn btn--gold btn--sm" href="startzeiten.html"><span class="btn-label">Startzeit buchen</span></a>
    </nav>
    <button class="burger" aria-label="Menü öffnen" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>

<nav class="mobile-nav" aria-label="Mobile Navigation">
  <a href="index.html">Start</a>
  <a href="golfanlage.html">Golfanlage</a>
  <a href="greenfee.html">Greenfee</a>
  <a href="golf-lernen.html">Golf lernen</a>
  <a href="mitgliedschaft.html">Mitgliedschaft</a>
  <a href="gastronomie.html">Castello</a>
  <a href="kontakt.html">Kontakt</a>
  <a href="https://www.castanea-resort.de/de" target="_blank" rel="noopener">Hotel ↗</a>
  <a class="btn btn--gold" href="startzeiten.html"><span class="btn-label">Startzeit buchen</span></a>
</nav>

<main id="content">
"""

FOOT = """
</main>

<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a class="logo" href="index.html"><span class="logo-mark">A</span><span class="logo-text"><strong>Golf Resort Adendorf</strong><span>Castanea Resort</span></span></a>
        <p>Castanea Resort Golf Course<br>Moorchaussee 3<br>21365 Adendorf</p>
        <p class="mt-1"><a href="mailto:golf@castanea-resort.de">golf@castanea-resort.de</a><a href="tel:+49413122332660">04131 22 33 26 60</a></p>
      </div>
      <div>
        <h6>Golf spielen</h6>
        <a href="startzeiten.html">Startzeiten</a>
        <a href="greenfee.html">Greenfee</a>
        <a href="golfanlage.html">Golfanlage &amp; Platzdaten</a>
        <a href="golf-lernen.html">Golf lernen</a>
      </div>
      <div>
        <h6>Club &amp; Resort</h6>
        <a href="mitgliedschaft.html">Mitglied werden</a>
        <a href="gastronomie.html">Gastronomie „Castello“</a>
        <a href="https://www.castanea-resort.de/de" target="_blank" rel="noopener">Hotel „Castanea“ ↗</a>
        <a href="http://www.residenzhotel.de/" target="_blank" rel="noopener">Hotel „Residenz“ ↗</a>
        <a href="kontakt.html">Kontakt &amp; Anfahrt</a>
      </div>
      <div>
        <h6>Rechtliches</h6>
        <a href="https://www.golf-adendorf.de/impressum.html" target="_blank" rel="noopener">Impressum</a>
        <a href="https://www.golf-adendorf.de/datenschutz.html" target="_blank" rel="noopener">Datenschutz</a>
        <a href="https://www.golf-adendorf.de/barrierefreiheitserklaerung.html" target="_blank" rel="noopener">Barrierefreiheit</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 Golf Resort Adendorf KG</span>
      <span class="footer-claim">Golf für alle.</span>
    </div>
  </div>
</footer>

<div class="cta-dock">
  <a class="btn btn--gold" href="startzeiten.html"><span class="btn-label">⛳ Startzeit buchen</span></a>
</div>

<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/lenis@1.1.14/dist/lenis.min.js"></script>
<script src="js/data.js"></script>
<script src="js/main.js"></script>
{extra_js}
</body>
</html>
"""


def hero(kicker, h1, lead, crumbs, ctas=""):
    return f"""
  <section class="page-hero">
    <div class="blob blob--green" style="width:420px;height:420px;top:-100px;right:-140px;"></div>
    <div class="blob blob--gold" style="width:280px;height:280px;bottom:-110px;left:-90px;"></div>
    <div class="container">
      <nav class="breadcrumb" aria-label="Brotkrumen" data-reveal>
        <a href="index.html">Start</a><span class="sep">/</span><span class="current">{crumbs}</span>
      </nav>
      <span class="kicker" data-reveal>{kicker}</span>
      <h1 class="split-lines">{h1}</h1>
      <p class="lead" data-reveal data-delay="0.15">{lead}</p>
      {f'<div class="hero-cta" data-reveal data-delay="0.25">{ctas}</div>' if ctas else ''}
    </div>
  </section>
"""


CTA_BAND = """
  <section style="padding-top:0;">
    <div class="container">
      <div class="cta-band" data-reveal="scale">
        <h2>Bereit für den ersten Abschlag?</h2>
        <p>Buchen Sie Ihre Startzeit in unter einer Minute – oder sichern Sie sich Ihr Spielrecht für die ganze Saison.</p>
        <div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap;">
          <a class="btn btn--gold btn--lg" href="startzeiten.html"><span class="btn-label">Startzeit buchen</span> <span class="btn-arrow">→</span></a>
          <a class="btn btn--white btn--lg" href="mitgliedschaft.html"><span class="btn-label">Mitglied werden</span></a>
        </div>
      </div>
    </div>
  </section>
"""

PAGES = {}

# ---------------------------------------------------------------- startzeiten
PAGES["startzeiten.html"] = {
    "title": "Startzeiten buchen",
    "desc": "Startzeit auf dem 18-Loch Mastercourse oder 9-Loch Publiccourse im Golf Resort Adendorf online buchen – schnell, einfach, verbindlich.",
    "body": hero(
        "Online-Buchung",
        "Startzeit buchen",
        "Wählen Sie Tag, Platz und Uhrzeit – Ihre Startzeit ist in unter einer Minute reserviert. Die Reservierung von Start- und Trainingszeiten ist auf beiden Plätzen erforderlich.",
        "Startzeiten",
    ) + """
  <section style="padding-top:24px;">
    <div class="container">
      <div class="booking-panel" data-reveal>
        <h3 class="mb-2" style="font-size:1.4rem;">1. Tag wählen</h3>
        <div class="day-scroller" id="day-scroller"></div>
        <h3 class="mb-2" style="font-size:1.4rem;">2. Platz wählen</h3>
        <div class="course-toggle">
          <button class="course-btn is-active" data-course="master" type="button">⛳ Mastercourse (18 Loch)</button>
          <button class="course-btn" data-course="public" type="button">🏌️ Publiccourse (9 Loch)</button>
        </div>
        <h3 class="mb-2" style="font-size:1.4rem;">3. Startzeit wählen</h3>
        <div class="slot-grid" id="slot-grid"></div>

        <div class="booking-summary" id="booking-summary" style="display:none;">
          <h3 style="font-size:1.2rem;margin-bottom:12px;">Ihre Auswahl</h3>
          <dl id="summary-dl"></dl>
          <div class="grid grid--2 mt-2" style="gap:0 16px;">
            <div class="field">
              <label for="b-name">Name *</label>
              <input id="b-name" type="text" autocomplete="name">
              <span class="err-msg">Bitte Namen eingeben.</span>
            </div>
            <div class="field">
              <label for="b-email">E-Mail *</label>
              <input id="b-email" type="email" autocomplete="email">
              <span class="err-msg">Bitte gültige E-Mail eingeben.</span>
            </div>
            <div class="field">
              <label for="b-hcp">Handicap (HCPI)</label>
              <input id="b-hcp" type="text" inputmode="decimal" placeholder="z. B. 24,5">
            </div>
            <div class="field">
              <label for="b-players">Spieleranzahl</label>
              <select id="b-players">
                <option>1 Person</option><option selected>2 Personen</option><option>3 Personen</option><option>4 Personen</option>
              </select>
            </div>
          </div>
          <button class="btn btn--gold btn--lg" id="book-btn" type="button" style="width:100%;"><span class="btn-label">Startzeit verbindlich buchen</span> <span class="btn-arrow">→</span></button>
        </div>

        <div id="booking-success" style="display:none;text-align:center;padding:30px 0 10px;">
          <svg class="success-check" viewBox="0 0 120 120" aria-hidden="true">
            <circle cx="60" cy="60" r="50"></circle>
            <path d="M38 62 L54 78 L84 46"></path>
          </svg>
          <h3 style="color:var(--green);">Startzeit reserviert!</h3>
          <p class="mt-1" style="max-width:480px;margin-left:auto;margin-right:auto;">Sie erhalten umgehend eine Bestätigung per E-Mail. Bitte melden Sie sich 15 Minuten vor dem Abschlag im Sekretariat.</p>
          <div class="mt-3" style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap;">
            <a class="btn btn--gold" href="mitgliedschaft.html"><span class="btn-label">Öfter spielen? Mitglied werden</span></a>
            <a class="btn btn--outline" href="index.html"><span class="btn-label">Zur Startseite</span></a>
          </div>
        </div>
      </div>
      <p class="mt-2" style="font-size:.85rem;" data-reveal>Hinweis: Beispiel-Buchungsstrecke. Auf der Live-Website läuft die Startzeiten-Buchung über <strong>PC CADDIE://online</strong> (pccaddie.net, Club-Nr. 0493383).</p>
    </div>
  </section>

  <section style="background:var(--sand);padding:clamp(48px,6vw,72px) 0;">
    <div class="container">
      <div class="grid grid--3">
        <div class="text-center" data-reveal>
          <div class="icon-bubble" style="margin:0 auto 12px;">⚡</div>
          <h3 style="font-size:1.2rem;">In 60 Sekunden gebucht</h3>
          <p style="font-size:.95rem;">Tag, Platz, Zeit – fertig. Bestätigung sofort per E-Mail.</p>
        </div>
        <div class="text-center" data-reveal data-delay="0.1">
          <div class="icon-bubble" style="margin:0 auto 12px;">🌅</div>
          <h3 style="font-size:1.2rem;">Early Morning &amp; Sunset</h3>
          <p style="font-size:.95rem;">Früh oder spät starten und bis zu 53 % beim Greenfee sparen.</p>
        </div>
        <div class="text-center" data-reveal data-delay="0.2">
          <div class="icon-bubble" style="margin:0 auto 12px;">♾️</div>
          <h3 style="font-size:1.2rem;">Lieber unbegrenzt?</h3>
          <p style="font-size:.95rem;">Mit dem Premium-Spielrecht entfällt das Greenfee komplett. <a href="mitgliedschaft.html">Mehr erfahren →</a></p>
        </div>
      </div>
    </div>
  </section>
""" + CTA_BAND,
    "extra_js": """<script>
(function () {
  "use strict";
  var days = gaNextDays(7);
  var state = { day: 0, course: "master", slot: null };

  var scroller = document.getElementById("day-scroller");
  scroller.innerHTML = days.map(function (d, i) {
    return '<button class="day-chip' + (i === 0 ? " is-active" : "") + '" data-i="' + i + '" type="button"><span class="dow">' + d.dow + '</span><span class="dnum">' + d.dnum + "</span></button>";
  }).join("");

  function renderSlots() {
    var grid = document.getElementById("slot-grid");
    var slots = gaSlots(state.day, state.course);
    grid.innerHTML = slots.map(function (s) {
      var full = s.free === 0;
      return '<button class="slot' + (full ? " is-full" : "") + (state.slot === s.time ? " is-selected" : "") + '" data-t="' + s.time + '" type="button"' + (full ? " disabled" : "") + '><span class="t">' + s.time + '</span><span class="free">' + (full ? "belegt" : s.free + " frei") + "</span></button>";
    }).join("");
    grid.querySelectorAll(".slot:not(.is-full)").forEach(function (b) {
      b.addEventListener("click", function () { selectSlot(b.getAttribute("data-t")); });
    });
    if (typeof gsap !== "undefined" && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      gsap.fromTo(grid.children, { opacity: 0, y: 14 }, { opacity: 1, y: 0, duration: .4, stagger: .012, ease: "power2.out" });
    }
  }

  function updateSummary() {
    var box = document.getElementById("booking-summary");
    if (!state.slot) { box.style.display = "none"; return; }
    var d = days[state.day];
    var c = GA_COURSES[state.course];
    var preis = d.isWeekend ? c.preis.we : c.preis.wt;
    document.getElementById("summary-dl").innerHTML =
      "<dt>Platz</dt><dd>" + c.name + "</dd>" +
      "<dt>Datum</dt><dd>" + d.label + "</dd>" +
      "<dt>Startzeit</dt><dd>" + state.slot + " Uhr</dd>" +
      "<dt>Greenfee p. P.</dt><dd>" + preis.toFixed(2).replace(".", ",") + " € (Mitglieder: frei)</dd>";
    box.style.display = "block";
    box.scrollIntoView({ behavior: "smooth", block: "nearest" });
  }

  function selectSlot(t) {
    state.slot = t;
    document.querySelectorAll(".slot").forEach(function (s) {
      s.classList.toggle("is-selected", s.getAttribute("data-t") === t);
    });
    updateSummary();
  }

  scroller.querySelectorAll(".day-chip").forEach(function (chip) {
    chip.addEventListener("click", function () {
      state.day = parseInt(chip.getAttribute("data-i"), 10);
      state.slot = null;
      scroller.querySelectorAll(".day-chip").forEach(function (c) { c.classList.remove("is-active"); });
      chip.classList.add("is-active");
      renderSlots(); updateSummary();
    });
  });
  document.querySelectorAll(".course-btn").forEach(function (b) {
    b.addEventListener("click", function () {
      state.course = b.getAttribute("data-course");
      state.slot = null;
      document.querySelectorAll(".course-btn").forEach(function (c) { c.classList.remove("is-active"); });
      b.classList.add("is-active");
      renderSlots(); updateSummary();
    });
  });

  document.getElementById("book-btn").addEventListener("click", function () {
    var ok = true;
    ["b-name", "b-email"].forEach(function (id) {
      var el = document.getElementById(id);
      var bad = id === "b-email" ? !/^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$/.test(el.value.trim()) : !el.value.trim();
      el.classList.toggle("is-error", bad);
      el.closest(".field").classList.toggle("show-error", bad);
      if (bad) ok = false;
    });
    if (!ok) return;
    document.getElementById("booking-summary").style.display = "none";
    document.getElementById("slot-grid").style.display = "none";
    document.getElementById("day-scroller").style.display = "none";
    document.querySelector(".course-toggle").style.display = "none";
    document.querySelectorAll(".booking-panel h3").forEach(function (h) { h.style.display = "none"; });
    document.getElementById("booking-success").style.display = "block";
    window.scrollTo({ top: 0, behavior: "smooth" });
  });

  renderSlots();

  /* Vorauswahl per URL (?zeit=HH:MM) */
  var pre = new URLSearchParams(location.search).get("zeit");
  if (pre) selectSlot(pre);
})();
</script>"""
}

# ---------------------------------------------------------------- mitgliedschaft
PAGES["mitgliedschaft.html"] = {
    "title": "Mitglied werden",
    "desc": "Mitgliedschaft im Golf Resort Adendorf: Premium-Spielrechte ab 80 €/Jahr, AfterWork, Studenten- und Jugendtarife – jetzt online beantragen.",
    "body": hero(
        "Mitgliedschaft",
        "Ihr Spielrecht. Ihr Tempo.",
        "Unbegrenzt golfen ohne Greenfee: Wählen Sie Ihr Spielrecht und stellen Sie den Antrag direkt online – in drei Minuten erledigt, ohne Aufnahmegebühr.",
        "Mitglied werden",
        '<a class="btn btn--gold" href="#antrag"><span class="btn-label">Direkt zum Online-Antrag</span> <span class="btn-arrow">↓</span></a>'
        '<a class="btn btn--outline" href="kontakt.html"><span class="btn-label">Beratung gewünscht?</span></a>'
    ) + """
  <section style="padding-top:24px;">
    <div class="container">
      <div class="section-head">
        <span class="kicker" data-reveal>Alle Modelle</span>
        <h2 class="split-lines">Spielrechte im Überblick</h2>
        <p data-reveal>Klicken Sie auf ein Modell, um es im Antrag vorzubelegen.</p>
      </div>
      <div class="grid grid--3" id="price-grid"></div>
    </div>
  </section>

  <section id="antrag" style="background:var(--sand);">
    <div class="container container--narrow">
      <div class="section-head section-head--center">
        <span class="kicker" data-reveal>Online-Antrag</span>
        <h2 class="split-lines">In 3 Schritten zum Spielrecht</h2>
      </div>

      <div class="booking-panel" id="wizard">
        <div class="wizard-progress" data-reveal>
          <div class="wp-step is-active" data-step="1"><div class="wp-dot">1<span class="wp-label">Spielrecht</span></div><div class="wp-bar"></div></div>
          <div class="wp-step" data-step="2"><div class="wp-dot">2<span class="wp-label">Ihre Daten</span></div><div class="wp-bar"></div></div>
          <div class="wp-step" data-step="3"><div class="wp-dot">3<span class="wp-label">Bestätigen</span></div></div>
        </div>

        <div class="wizard-pane is-active" data-pane="1">
          <div class="field">
            <label for="m-modell">Ihr Wunsch-Spielrecht *</label>
            <select id="m-modell"></select>
          </div>
          <div class="booking-summary" id="modell-info"></div>
          <div class="wizard-nav">
            <span></span>
            <button class="btn btn--gold" id="m-to-2" type="button"><span class="btn-label">Weiter</span> <span class="btn-arrow">→</span></button>
          </div>
        </div>

        <div class="wizard-pane" data-pane="2">
          <div class="grid grid--2" style="gap:0 18px;">
            <div class="field"><label for="m-vorname">Vorname *</label><input id="m-vorname" type="text" autocomplete="given-name"><span class="err-msg">Bitte Vornamen eingeben.</span></div>
            <div class="field"><label for="m-nachname">Nachname *</label><input id="m-nachname" type="text" autocomplete="family-name"><span class="err-msg">Bitte Nachnamen eingeben.</span></div>
            <div class="field"><label for="m-email">E-Mail *</label><input id="m-email" type="email" autocomplete="email"><span class="err-msg">Bitte gültige E-Mail eingeben.</span></div>
            <div class="field"><label for="m-geb">Geburtsdatum *</label><input id="m-geb" type="date"><span class="err-msg">Bitte Geburtsdatum angeben.</span></div>
            <div class="field"><label for="m-hcp">Handicap (falls vorhanden)</label><input id="m-hcp" type="text" placeholder="z. B. 36 oder PE"></div>
            <div class="field"><label for="m-telefon">Telefon</label><input id="m-telefon" type="tel" autocomplete="tel"></div>
          </div>
          <div class="field">
            <div class="check-row">
              <input id="m-dsgvo" type="checkbox">
              <label for="m-dsgvo" style="font-weight:400;margin:0;">Ich stimme der Verarbeitung meiner Daten zur Bearbeitung des Antrags zu und habe die <a href="https://www.golf-adendorf.de/datenschutz.html" target="_blank" rel="noopener">Datenschutzerklärung</a> gelesen. *</label>
            </div>
            <span class="err-msg">Bitte stimmen Sie der Datenverarbeitung zu.</span>
          </div>
          <div class="wizard-nav">
            <button class="btn btn--outline" data-back="1" type="button"><span class="btn-label">← Zurück</span></button>
            <button class="btn btn--gold" id="m-to-3" type="button"><span class="btn-label">Zur Übersicht</span> <span class="btn-arrow">→</span></button>
          </div>
        </div>

        <div class="wizard-pane" data-pane="3">
          <div class="booking-summary"><h3 style="font-size:1.15rem;margin-bottom:12px;">Ihr Antrag</h3><dl id="m-summary"></dl></div>
          <p class="mt-2" style="font-size:.88rem;">Mit dem Absenden stellen Sie einen Antrag auf Abschluss eines Spielrechtsvertrags. Wir melden uns innerhalb von 24 Stunden mit der Bestätigung – erst mit beidseitiger Unterschrift wird der Vertrag wirksam.</p>
          <div class="wizard-nav">
            <button class="btn btn--outline" data-back="2" type="button"><span class="btn-label">← Zurück</span></button>
            <button class="btn btn--gold btn--lg" id="m-submit" type="button"><span class="btn-label">Antrag verbindlich senden ✓</span></button>
          </div>
        </div>

        <div class="wizard-pane" data-pane="4">
          <div style="text-align:center;padding:24px 0 8px;">
            <svg class="success-check" viewBox="0 0 120 120" aria-hidden="true">
              <circle cx="60" cy="60" r="50"></circle>
              <path d="M38 62 L54 78 L84 46"></path>
            </svg>
            <h3 style="color:var(--green);">Herzlich willkommen im Club!</h3>
            <p class="mt-1" style="max-width:520px;margin:8px auto 0;">Ihr Antrag<span id="m-success-name"></span> ist eingegangen. Sie erhalten umgehend alle Unterlagen per E-Mail – wir freuen uns auf Ihre erste Runde!</p>
            <div class="mt-3" style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap;">
              <a class="btn btn--gold" href="startzeiten.html"><span class="btn-label">Gleich Startzeit buchen</span></a>
              <a class="btn btn--outline" href="golf-lernen.html"><span class="btn-label">Kurse entdecken</span></a>
            </div>
          </div>
        </div>
      </div>

      <p class="mt-2 text-center" style="font-size:.85rem;" data-reveal>Beispiel-Antragsstrecke. Auf der Live-Website: PDF-Spielrechtsvertrag zum Ausfüllen sowie Angebots-Funnels über <strong>mitfit</strong> (angebote.mitfit.de).</p>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="grid grid--3">
        <div class="card" data-reveal>
          <div class="icon-bubble">🤝</div>
          <h3 style="font-size:1.25rem;">Partneranlagen</h3>
          <p>Als Mitglied profitieren Sie von Greenfee-Rabatten bei Green Eagle, GC Brunstorf, GC Bad Bevensen, GCC am Hockenberg und GC Escheburg.</p>
        </div>
        <div class="card" data-reveal data-delay="0.1">
          <div class="icon-bubble">🃏</div>
          <h3 style="font-size:1.25rem;">Heide Golf Card</h3>
          <p>Mit dem „Ass im Bag“ spielen Sie uneingeschränkt von Montag bis Sonntag auf unserer Anlage.</p>
        </div>
        <div class="card" data-reveal data-delay="0.2">
          <div class="icon-bubble">🏆</div>
          <h3 style="font-size:1.25rem;">Turniere &amp; Mannschaften</h3>
          <p>Vom offenen Herrentag bis zur Clubmeisterschaft – sechs Mannschaften von Liga bis AK 70 freuen sich auf Verstärkung.</p>
        </div>
      </div>
    </div>
  </section>
""" + CTA_BAND,
    "extra_js": """<script>
(function () {
  "use strict";
  /* Preiskarten */
  var grid = document.getElementById("price-grid");
  grid.innerHTML = GA_MITGLIEDSCHAFTEN.map(function (m, i) {
    return '<div class="price-card' + (m.featured ? " is-featured" : "") + '" data-reveal data-delay="' + ((i % 3) * 0.08) + '" data-id="' + m.id + '">' +
      (m.badge ? '<span class="badge">' + m.badge + "</span>" : "") +
      "<h3>" + m.name + '</h3><div class="price">' + m.preis.toLocaleString("de-DE") + " €<small> / Jahr</small></div><ul>" +
      m.leistungen.map(function (l) { return "<li>" + l + "</li>"; }).join("") +
      '</ul><span class="btn btn--sm btn--outline"><span class="btn-label">Dieses Modell wählen</span></span></div>';
  }).join("");
  if (window.gaInitReveals) window.gaInitReveals();

  /* Wizard */
  var sel = document.getElementById("m-modell");
  sel.innerHTML = GA_MITGLIEDSCHAFTEN.map(function (m) {
    return '<option value="' + m.id + '">' + m.name + " – " + m.preis.toLocaleString("de-DE") + " €/Jahr</option>";
  }).join("");

  function modell() {
    return GA_MITGLIEDSCHAFTEN.find(function (m) { return m.id === sel.value; });
  }
  function renderInfo() {
    var m = modell();
    document.getElementById("modell-info").innerHTML =
      '<h3 style="font-size:1.15rem;margin-bottom:10px;">' + m.name + "</h3><dl>" +
      "<dt>Jahresbeitrag</dt><dd>" + m.preis.toLocaleString("de-DE") + " €</dd>" +
      "<dt>Leistungen</dt><dd>" + m.leistungen.join(" · ") + "</dd></dl>";
  }
  sel.addEventListener("change", renderInfo);
  renderInfo();

  grid.addEventListener("click", function (e) {
    var card = e.target.closest(".price-card");
    if (!card) return;
    sel.value = card.getAttribute("data-id");
    renderInfo();
    document.getElementById("antrag").scrollIntoView({ behavior: "smooth" });
  });

  /* Vorauswahl per URL (?modell=id) */
  var pre = new URLSearchParams(location.search).get("modell");
  if (pre && GA_MITGLIEDSCHAFTEN.some(function (m) { return m.id === pre; })) {
    sel.value = pre; renderInfo();
    setTimeout(function () { document.getElementById("antrag").scrollIntoView({ behavior: "smooth" }); }, 400);
  }

  function goto(step) {
    document.querySelectorAll(".wizard-pane").forEach(function (p) {
      p.classList.toggle("is-active", p.getAttribute("data-pane") == step);
    });
    document.querySelectorAll(".wp-step").forEach(function (s) {
      var n = parseInt(s.getAttribute("data-step"), 10);
      s.classList.toggle("is-active", n === step);
      s.classList.toggle("is-done", n < step);
    });
    var y = document.getElementById("wizard").getBoundingClientRect().top + window.scrollY - 110;
    window.scrollTo({ top: y, behavior: "smooth" });
  }
  document.querySelectorAll("[data-back]").forEach(function (b) {
    b.addEventListener("click", function () { goto(parseInt(b.getAttribute("data-back"), 10)); });
  });
  function val(id) { return document.getElementById(id).value.trim(); }
  function bad(id, isBad) {
    var el = document.getElementById(id);
    el.classList.toggle("is-error", isBad);
    el.closest(".field").classList.toggle("show-error", isBad);
    return isBad;
  }

  document.getElementById("m-to-2").addEventListener("click", function () { goto(2); });
  document.getElementById("m-to-3").addEventListener("click", function () {
    var b = false;
    b = bad("m-vorname", !val("m-vorname")) || b;
    b = bad("m-nachname", !val("m-nachname")) || b;
    b = bad("m-email", !/^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$/.test(val("m-email"))) || b;
    b = bad("m-geb", !val("m-geb")) || b;
    var ds = document.getElementById("m-dsgvo");
    ds.closest(".field").classList.toggle("show-error", !ds.checked);
    if (!ds.checked) b = true;
    if (b) return;
    var m = modell();
    document.getElementById("m-summary").innerHTML =
      "<dt>Spielrecht</dt><dd>" + m.name + "</dd>" +
      "<dt>Jahresbeitrag</dt><dd>" + m.preis.toLocaleString("de-DE") + " € (zzgl. ggf. Verbandsbeiträge)</dd>" +
      "<dt>Name</dt><dd>" + val("m-vorname") + " " + val("m-nachname") + "</dd>" +
      "<dt>E-Mail</dt><dd>" + val("m-email") + "</dd>" +
      "<dt>Geburtsdatum</dt><dd>" + val("m-geb").split("-").reverse().join(".") + "</dd>" +
      (val("m-hcp") ? "<dt>Handicap</dt><dd>" + val("m-hcp") + "</dd>" : "");
    goto(3);
  });
  document.getElementById("m-submit").addEventListener("click", function () {
    document.getElementById("m-success-name").textContent = ", " + val("m-vorname");
    goto(4);
    document.querySelectorAll(".wp-step").forEach(function (s) { s.classList.add("is-done"); s.classList.remove("is-active"); });
  });
})();
</script>"""
}

# ---------------------------------------------------------------- greenfee
PAGES["greenfee.html"] = {
    "title": "Greenfee & Preise",
    "desc": "Greenfee im Golf Resort Adendorf: Mastercourse ab 35 €, Publiccourse ab 25 €, Early Morning & Sunset-Tarife. Jugendliche zahlen die Hälfte.",
    "body": hero(
        "Gäste",
        "Greenfee &amp; Preise",
        "Faire Preise für jede Tageszeit: Mit Early-Morning- und Sunset-Tarifen spielen Sie den Mastercourse schon ab 35 €. Jugendliche und Studierende zahlen überall die Hälfte.",
        "Greenfee",
        '<a class="btn btn--gold" href="startzeiten.html"><span class="btn-label">Startzeit buchen</span> <span class="btn-arrow">→</span></a>'
    ) + """
  <section style="padding-top:24px;">
    <div class="container">
      <div class="grid grid--2" style="align-items:start;">
        <div data-reveal>
          <h3 class="mb-2">Mastercourse (18 Loch)</h3>
          <table class="price-table">
            <tr><th>Tarif</th><th>Erwachsene</th><th>Bis 25 J.</th></tr>
            <tr><td>Greenfee Mo – Fr</td><td class="pr">75,00 €</td><td class="pr">35,00 €</td></tr>
            <tr><td>Greenfee Sa, So &amp; Feiertage</td><td class="pr">85,00 €</td><td class="pr">40,00 €</td></tr>
            <tr><td>Early Morning (bis 9 Uhr, Mo – Do)</td><td class="pr">40,00 €</td><td class="pr">20,00 €</td></tr>
            <tr><td>Sunset (ab 3 Std. vor Sonnenuntergang, Mo – Fr)</td><td class="pr">35,00 €</td><td class="pr">17,50 €</td></tr>
            <tr><td>Sunset (Sa – So)</td><td class="pr">40,00 €</td><td class="pr">20,00 €</td></tr>
          </table>
        </div>
        <div data-reveal data-delay="0.12">
          <h3 class="mb-2">Publiccourse (9 Loch)</h3>
          <table class="price-table">
            <tr><th>Tarif</th><th>Erwachsene</th><th>Bis 25 J.</th></tr>
            <tr><td>9-Loch Greenfee Mo – Fr</td><td class="pr">25,00 €</td><td class="pr">12,50 €</td></tr>
            <tr><td>9-Loch Greenfee Sa, So &amp; Feiertage</td><td class="pr">35,00 €</td><td class="pr">17,50 €</td></tr>
          </table>
          <h3 class="mb-2 mt-3">Training Area &amp; Sonstiges</h3>
          <table class="price-table">
            <tr><th>Leistung</th><th colspan="2">Preis</th></tr>
            <tr><td>Rangefee (bis 25 J.: 5,00 €)</td><td class="pr" colspan="2">10,00 €</td></tr>
            <tr><td>10er-Karte Range (bis 25 J.: 40,00 €)</td><td class="pr" colspan="2">80,00 €</td></tr>
            <tr><td>Rangebälle (26 Stück)</td><td class="pr" colspan="2">2,00 €</td></tr>
            <tr><td>Trolley / Tag</td><td class="pr" colspan="2">5,00 €</td></tr>
            <tr><td>E-Cart 18 Loch / 9 Loch</td><td class="pr" colspan="2">35,00 € / 25,00 €</td></tr>
            <tr><td>Trackman</td><td class="pr" colspan="2">45,00 € / Std.</td></tr>
          </table>
        </div>
      </div>
      <p class="mt-2" data-reveal style="font-size:.92rem;">Gruppenermäßigung ab 10 Personen auf Anfrage. Mitglieder spielen je nach Spielrecht ohne Greenfee – <a href="mitgliedschaft.html">zur Mitgliedschaft →</a></p>
    </div>
  </section>

  <section style="background:var(--sand);">
    <div class="container">
      <div class="cta-band" data-reveal="scale" style="background:linear-gradient(120deg,var(--gold) 0%,#B08F35 100%);">
        <h2 style="color:var(--green-deep);">Ab 30 Runden lohnt sich das Spielrecht</h2>
        <p style="color:rgba(20,56,31,.75);">Wer regelmäßig spielt, fährt mit einer Mitgliedschaft günstiger – inklusive unbegrenztem Range-Zugang und Partnerclub-Rabatten.</p>
        <a class="btn btn--lg" href="mitgliedschaft.html"><span class="btn-label">Spielrechte vergleichen</span> <span class="btn-arrow">→</span></a>
      </div>
    </div>
  </section>
""",
    "extra_js": ""
}

# ---------------------------------------------------------------- golfanlage
PAGES["golfanlage.html"] = {
    "title": "Golfanlage & Platzdaten",
    "desc": "18-Loch Mastercourse von Kurt Rossknecht, 9-Loch Publiccourse und Übungsanlagen mit Flutlicht – die Golfanlage des Castanea Resorts in Adendorf.",
    "body": hero(
        "Die Anlage",
        "Golfanlage &amp; Platzdaten",
        "27 Spielbahnen zwischen Steinmauern, Seen und Inselgrün – plus Übungsanlagen, die keine Wünsche offenlassen.",
        "Golfanlage",
        '<a class="btn btn--gold" href="startzeiten.html"><span class="btn-label">Startzeit buchen</span> <span class="btn-arrow">→</span></a>'
    ) + """
  <section style="padding-top:24px;">
    <div class="container">
      <div class="grid grid--3">
        <article class="card" data-reveal>
          <div class="icon-bubble">⛳</div>
          <h3>Mastercourse „Castanea“</h3>
          <p>Der 6.175 m lange Mastercourse (Par 72) wurde von Golfplatzarchitekt Kurt Rossknecht geplant. Markante Steinmauern und zahlreiche Seen erinnern an spanische Anlagen – dominiert von naturbelassenem Aufbau, modellierten Bunkerlandschaften und einem spannenden Inselgrün. Es gilt nicht nur lang, sondern auch präzise zu spielen.</p>
        </article>
        <article class="card" data-reveal data-delay="0.1">
          <div class="icon-bubble">🏌️</div>
          <h3>Publiccourse „Castello“</h3>
          <p>Attraktiver 9-Loch-Platz (Par 27, 1.390 m) mit Course Rating: ideales Training für das kurze Spiel und ein angenehmer Einstieg für Neueinsteigende. Bunker und Bachläufe fordern auch erfahrene Spieler – regelmäßig Austragungsort von Turnieren.</p>
        </article>
        <article class="card" data-reveal data-delay="0.2">
          <div class="icon-bubble">💡</div>
          <h3>Übungsanlagen</h3>
          <p>Driving Range mit 24 überdachten und 20 Rasen-Abschlagplätzen, Chipping- und Puttinggreen sowie Übungsbunker. In der Dämmerung erhellt Flutlicht die Range. Die Pros der Akademie unterstützen mit modernen Lehrmethoden inkl. Videoanalyse.</p>
        </article>
      </div>
    </div>
  </section>

  <section style="background:var(--sand);">
    <div class="container">
      <div class="section-head">
        <span class="kicker" data-reveal>Diese Woche</span>
        <h2 class="split-lines">Platzdaten</h2>
        <p data-reveal>Beispieldaten – tagesaktuelle Platzinformationen live im Sekretariat oder telefonisch unter 04131 22 33 26 60.</p>
      </div>
      <div data-reveal style="overflow-x:auto;">
        <table class="price-table" id="platzdaten-table"></table>
      </div>
      <div class="status-row mt-3" data-reveal>
        <span class="status-chip"><span class="dot"></span>Driving Range geöffnet</span>
        <span class="status-chip"><span class="dot"></span>Putting Green geöffnet</span>
        <span class="status-chip"><span class="dot"></span>Chipping Area geöffnet</span>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="section-head">
        <span class="kicker" data-reveal>Mitglieder-Vorteil</span>
        <h2 class="split-lines">Partneranlagen</h2>
      </div>
      <div data-reveal style="overflow-x:auto;">
        <table class="price-table">
          <tr><th>Anlage</th><th>Vorteil</th><th>Gültigkeit</th></tr>
          <tr><td>Green Eagle Golf Courses</td><td class="pr">20 € Greenfee-Rabatt</td><td>Mo – So</td></tr>
          <tr><td>Golf &amp; Country Club Brunstorf</td><td class="pr">15 € Greenfee-Rabatt</td><td>Mo – So</td></tr>
          <tr><td>Golf Club Bad Bevensen</td><td class="pr">50 % Greenfee-Rabatt</td><td>Mo – So</td></tr>
          <tr><td>GCC am Hockenberg</td><td class="pr">„Two for One“</td><td>Mo – Fr</td></tr>
          <tr><td>Golf Club Escheburg</td><td class="pr">30 € Greenfee (Jugend: 15 €)</td><td>Mo – So</td></tr>
        </table>
      </div>
      <p class="mt-2" data-reveal style="font-size:.9rem;">Gilt jeweils mit DGV-Ausweis (Adendorf). Startzeiten vorab bei den Partnerclubs reservieren.</p>
    </div>
  </section>
""" + CTA_BAND,
    "extra_js": """<script>
(function () {
  "use strict";
  var days = gaNextDays(7);
  var rows = days.map(function (d, i) {
    var turnier = i === 1 ? "Offener Herrentag (Zählspiel)" : (i === 4 ? "Family & Friends" : "");
    return "<tr><td>" + d.label + "</td><td class=\\"pr\\">geöffnet" + (turnier ? " · " + turnier : "") + "</td><td>zugelassen</td><td>ja</td></tr>";
  }).join("");
  document.getElementById("platzdaten-table").innerHTML =
    "<tr><th>Datum</th><th>Platz</th><th>E-Carts / Trolleys</th><th>Vorgabewirksam</th></tr>" + rows;
})();
</script>"""
}

# ---------------------------------------------------------------- golf-lernen
PAGES["golf-lernen.html"] = {
    "title": "Golf lernen",
    "desc": "Golf lernen im Golf Resort Adendorf: Schnupperkurs, Platzreife und Handicap-Training mit erfahrenen Pros – jetzt Kurs sichern.",
    "body": hero(
        "Akademie",
        "Golf lernen – von Anfang an gut",
        "Vom ersten Schnupperschlag bis zur Platzreife: Unsere Pros begleiten Sie mit modernen Lehrmethoden, Videoanalyse und viel Geduld. Treffpunkt ist das Clubhaus Castello.",
        "Golf lernen",
        '<a class="btn btn--gold" href="#kurse"><span class="btn-label">Kurse ansehen</span> <span class="btn-arrow">↓</span></a>'
    ) + """
  <section id="kurse" style="padding-top:24px;">
    <div class="container">
      <div class="grid grid--3">
        <article class="price-card" data-reveal>
          <h3>Golf ausprobieren</h3>
          <div class="price">29 €<small> / Schnupperkurs</small></div>
          <ul>
            <li>2 Stunden mit Pro auf der Driving Range</li>
            <li>Leihschläger &amp; Rangebälle inklusive</li>
            <li>Kein Vorwissen nötig</li>
            <li>Wird bei Kursbuchung angerechnet</li>
          </ul>
          <a class="btn btn--sm btn--gold" href="kontakt.html"><span class="btn-label">Termin sichern</span></a>
        </article>
        <article class="price-card is-featured" data-reveal data-delay="0.1">
          <span class="badge">Der Klassiker</span>
          <h3>Platzreife-Kurs</h3>
          <div class="price">299 €<small> / inkl. Prüfung</small></div>
          <ul>
            <li>4 × 2 Stunden Training in Kleingruppen</li>
            <li>Regelkunde &amp; Etikette</li>
            <li>Freies Üben inkl. Rangebälle</li>
            <li>DGV-Platzreife-Prüfung inklusive</li>
          </ul>
          <a class="btn btn--sm btn--gold" href="kontakt.html"><span class="btn-label">Kurs buchen</span></a>
        </article>
        <article class="price-card" data-reveal data-delay="0.2">
          <h3>Handicap-Training</h3>
          <div class="price">199 €<small> / Modul</small></div>
          <ul>
            <li>Wöchentliches Gruppentraining</li>
            <li>Tägliche vorgabewirksame 9-Loch-Turniere</li>
            <li>Trackman-Analyse buchbar</li>
            <li>Spielbegleitung auf dem Platz</li>
          </ul>
          <a class="btn btn--sm btn--gold" href="kontakt.html"><span class="btn-label">Kurs buchen</span></a>
        </article>
      </div>
      <p class="mt-2" style="font-size:.85rem;" data-reveal>Beispielangebote – die Live-Website vermittelt Kurse über <strong>mitfit</strong>-Funnels („Golf ausprobieren“, „Golf lernen“, „Golf spielen“, „Online-Bedarfscheck“).</p>
    </div>
  </section>

  <section style="background:var(--sand);">
    <div class="container">
      <div class="section-head">
        <span class="kicker" data-reveal>Trainingsplan (Beispielwoche)</span>
        <h2 class="split-lines">So sieht Ihre Kurswoche aus</h2>
      </div>
      <div data-reveal style="overflow-x:auto;">
        <table class="price-table">
          <tr><th>Kurs</th><th>Trainer</th><th>Mo</th><th>Di</th><th>Mi</th><th>Do</th></tr>
          <tr><td>Platzreife Gruppe 1</td><td>Heiko</td><td>09–11 Uhr</td><td>09–11 Uhr</td><td>09–11 Uhr</td><td>09–11 Uhr</td></tr>
          <tr><td>Handicap Gruppe 1</td><td>Bruce</td><td>10–12 Uhr</td><td>10–12 Uhr</td><td>10–12 Uhr</td><td>09–11 Uhr</td></tr>
          <tr><td>Platzreife Gruppe 2</td><td>Matthias</td><td>14–16 Uhr</td><td>14–16 Uhr</td><td>14–16 Uhr</td><td>14–16 Uhr</td></tr>
        </table>
      </div>
      <div class="grid grid--3 mt-3">
        <div class="card" data-reveal><div class="icon-bubble">🗺️</div><h3 style="font-size:1.15rem;">Gute Orientierung</h3><p style="font-size:.92rem;">Zu Kursbeginn erhalten Sie Platzübersicht, Kursplan und die PIN für den Ballautomaten.</p></div>
        <div class="card" data-reveal data-delay="0.1"><div class="icon-bubble">🏅</div><h3 style="font-size:1.15rem;">Täglich Turniere</h3><p style="font-size:.92rem;">Vorgabewirksame 9-Loch-Turniere auf Master- und Publiccourse – ideal zum HCP-Verbessern.</p></div>
        <div class="card" data-reveal data-delay="0.2"><div class="icon-bubble">🛅</div><h3 style="font-size:1.15rem;">Bag-Unterstand</h3><p style="font-size:.92rem;">Bags am Range-Raum unterstellen (1 €/Tag), Trolley-Miete 5 €/Tag.</p></div>
      </div>
    </div>
  </section>
""" + CTA_BAND,
    "extra_js": ""
}

# ---------------------------------------------------------------- gastronomie
PAGES["gastronomie.html"] = {
    "title": "Gastronomie „Castello“",
    "desc": "Clubhaus-Restaurant „Castello“ im Golf Resort Adendorf: frische Küche, große Sonnenterrasse mit Fairway-Blick – auch für Nicht-Golfer geöffnet.",
    "body": hero(
        "Clubhaus",
        "Gastronomie „Castello“",
        "Klassische Clubhausküche mit frischen, unkomplizierten Speisen – und einer großen Außenterrasse mit Blick über Fairways, Greens und den immer wiederkehrenden Sunset. Nicht nur für Golfer!",
        "Castello"
    ) + """
  <section style="padding-top:24px;">
    <div class="container">
      <div class="grid grid--2" style="align-items:start;">
        <div class="card" data-reveal style="padding:36px;">
          <div class="icon-bubble">🕐</div>
          <h3>Öffnungszeiten</h3>
          <table class="price-table mt-2" style="box-shadow:none;">
            <tr><td>Montag</td><td class="pr">Ruhetag</td></tr>
            <tr><td>Dienstag – Donnerstag</td><td class="pr">12:00 – 20:00 Uhr</td></tr>
            <tr><td>Freitag – Sonntag</td><td class="pr">12:00 – 21:00 Uhr</td></tr>
          </table>
          <p class="mt-2">Reservierung: <a href="tel:+49413122332620">04131 22 33 26 20</a></p>
        </div>
        <div>
          <div class="card" data-reveal="right" style="padding:36px;margin-bottom:24px;">
            <div class="icon-bubble">📜</div>
            <h3>Speisekarte</h3>
            <p>Saisonal, regional, unkompliziert: von der Currywurst nach der Runde bis zum Sunset-Dinner auf der Terrasse.</p>
            <a class="btn btn--sm btn--outline mt-2" href="https://www.golf-adendorf.de/fileadmin/content/Dokumente/Castello_Speisekarte_2026_neu4.pdf" target="_blank" rel="noopener"><span class="btn-label">Speisekarte (PDF) ↗</span></a>
          </div>
          <div class="card" data-reveal="right" data-delay="0.1" style="padding:36px;background:var(--green-deep);border-color:var(--green-deep);">
            <div class="icon-bubble" style="background:rgba(201,165,70,.2);">🏨</div>
            <h3 style="color:var(--sand);">Mehr Genuss im Hotel</h3>
            <p style="color:var(--green-pale);">Der Gastronomie-Boulevard des Castanea Resorts: Restaurants, Bar und 1.700 m² Spa – direkt nebenan.</p>
            <a class="link-more mt-2" style="color:var(--gold);" href="https://www.castanea-resort.de/de" target="_blank" rel="noopener">Zum Hotel ↗</a>
          </div>
        </div>
      </div>
    </div>
  </section>
""" + CTA_BAND,
    "extra_js": ""
}

# ---------------------------------------------------------------- kontakt
PAGES["kontakt.html"] = {
    "title": "Kontakt & Anfahrt",
    "desc": "Kontakt zum Golf Resort Adendorf: Moorchaussee 3, 21365 Adendorf · 04131 22 33 26 60 · golf@castanea-resort.de",
    "body": hero(
        "Wir freuen uns auf Sie",
        "Kontakt &amp; Anfahrt",
        "Fragen zu Startzeiten, Mitgliedschaft oder Kursen? Das Clubsekretariat ist täglich von 8 bis 17 Uhr für Sie da.",
        "Kontakt"
    ) + """
  <section style="padding-top:24px;">
    <div class="container">
      <div class="grid grid--2" style="gap:clamp(32px,5vw,64px);align-items:start;">
        <div class="card" data-reveal style="padding:36px;">
          <h3 class="mb-2">Schreiben Sie uns</h3>
          <form id="kontakt-form" novalidate>
            <div class="field">
              <label for="k-anrede">Anrede *</label>
              <select id="k-anrede"><option>Herr</option><option>Frau</option><option>Divers</option></select>
            </div>
            <div class="grid grid--2" style="gap:0 16px;">
              <div class="field"><label for="k-vorname">Vorname *</label><input id="k-vorname" type="text" autocomplete="given-name"><span class="err-msg">Bitte Vornamen eingeben.</span></div>
              <div class="field"><label for="k-name">Name *</label><input id="k-name" type="text" autocomplete="family-name"><span class="err-msg">Bitte Namen eingeben.</span></div>
            </div>
            <div class="field"><label for="k-email">E-Mail *</label><input id="k-email" type="email" autocomplete="email"><span class="err-msg">Bitte gültige E-Mail eingeben.</span></div>
            <div class="field"><label for="k-betreff">Betreff *</label><input id="k-betreff" type="text"><span class="err-msg">Bitte Betreff eingeben.</span></div>
            <div class="field"><label for="k-nachricht">Nachricht *</label><textarea id="k-nachricht"></textarea><span class="err-msg">Bitte Nachricht eingeben.</span></div>
            <div class="field">
              <div class="check-row">
                <input id="k-dsgvo" type="checkbox">
                <label for="k-dsgvo" style="font-weight:400;margin:0;">Ich bin mit der Verarbeitung meiner personenbezogenen Daten einverstanden und habe die <a href="https://www.golf-adendorf.de/datenschutz.html" target="_blank" rel="noopener">Datenschutzerklärung</a> zur Kenntnis genommen. *</label>
              </div>
              <span class="err-msg">Bitte stimmen Sie zu.</span>
            </div>
            <button class="btn btn--gold" type="submit"><span class="btn-label">Senden</span> <span class="btn-arrow">→</span></button>
            <p id="kontakt-success" style="display:none;color:var(--green);font-weight:700;margin-top:14px;">✓ Vielen Dank! Wir melden uns umgehend.</p>
          </form>
        </div>
        <div>
          <div class="card" data-reveal="right" style="margin-bottom:24px;">
            <div class="icon-bubble">📍</div>
            <h3 style="font-size:1.3rem;">Castanea Resort Golf Course</h3>
            <p>Moorchaussee 3<br>21365 Adendorf</p>
            <p class="mt-2">
              <a href="tel:+49413122332660">04131 22 33 26 60</a><br>
              <a href="mailto:golf@castanea-resort.de">golf@castanea-resort.de</a>
            </p>
            <p class="mt-2" style="font-size:.92rem;">Sekretariat täglich 8 – 17 Uhr</p>
          </div>
          <div class="card" data-reveal="right" data-delay="0.1" style="background:var(--green-pale);border-color:rgba(46,107,62,.3);">
            <div class="icon-bubble">🚗</div>
            <h3 style="font-size:1.3rem;">Anfahrt</h3>
            <p style="font-size:.95rem;">Nur 5 Minuten von Lüneburg: über die B209 Richtung Adendorf, dann der Beschilderung „Castanea Resort“ folgen. Kostenlose Parkplätze direkt an der Anlage.</p>
            <a class="link-more mt-2" href="https://maps.google.com/?q=Moorchaussee+3,+21365+Adendorf" target="_blank" rel="noopener">Route in Google Maps öffnen ↗</a>
          </div>
        </div>
      </div>
    </div>
  </section>
""" + CTA_BAND,
    "extra_js": """<script>
(function () {
  "use strict";
  var form = document.getElementById("kontakt-form");
  if (!form) return;
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var ok = true;
    ["k-vorname", "k-name", "k-betreff", "k-nachricht"].forEach(function (id) {
      var el = document.getElementById(id);
      var bad = !el.value.trim();
      el.classList.toggle("is-error", bad);
      el.closest(".field").classList.toggle("show-error", bad);
      if (bad) ok = false;
    });
    var mail = document.getElementById("k-email");
    var mailBad = !/^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$/.test(mail.value.trim());
    mail.classList.toggle("is-error", mailBad);
    mail.closest(".field").classList.toggle("show-error", mailBad);
    if (mailBad) ok = false;
    var ds = document.getElementById("k-dsgvo");
    ds.closest(".field").classList.toggle("show-error", !ds.checked);
    if (!ds.checked) ok = false;
    if (!ok) return;
    form.querySelectorAll("input, textarea, select, button").forEach(function (el) { el.disabled = true; });
    document.getElementById("kontakt-success").style.display = "block";
  });
})();
</script>"""
}

# ---------------------------------------------------------------- build
for fname, page in PAGES.items():
    html = HEAD.format(title=page["title"], desc=page["desc"]) + page["body"] + FOOT.format(extra_js=page["extra_js"])
    with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
        f.write(html)
    print("✓", fname, len(html), "Bytes")
