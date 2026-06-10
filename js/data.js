/* ==========================================================================
   Golf Resort Adendorf – Beispieldaten
   (Die Live-Seite bucht Startzeiten & Turniere über PC CADDIE://online:
    https://www.pccaddie.net/clubs/0493383/app.php – hier Beispieldaten)
   ========================================================================== */

const GA_COURSES = {
  master: { name: "18-Loch Mastercourse „Castanea“", kurz: "Mastercourse", preis: { wt: 75, we: 85 } },
  public: { name: "9-Loch Publiccourse „Castello“", kurz: "Publiccourse", preis: { wt: 25, we: 35 } }
};

const GA_WOCHENTAGE = ["So", "Mo", "Di", "Mi", "Do", "Fr", "Sa"];
const GA_MONATE = ["Jan", "Feb", "Mär", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Dez"];

/* Nächste 7 Tage als Buchungstage */
function gaNextDays(n) {
  const out = [];
  const today = new Date();
  for (let i = 0; i < n; i++) {
    const d = new Date(today.getFullYear(), today.getMonth(), today.getDate() + i);
    out.push({
      iso: d.toISOString().slice(0, 10),
      dow: i === 0 ? "Heute" : GA_WOCHENTAGE[d.getDay()],
      dnum: d.getDate() + ". " + GA_MONATE[d.getMonth()],
      isWeekend: d.getDay() === 0 || d.getDay() === 6,
      dayIndex: i,
      label: GA_WOCHENTAGE[d.getDay()] + ", " + String(d.getDate()).padStart(2, "0") + ". " + GA_MONATE[d.getMonth()] + " " + d.getFullYear()
    });
  }
  return out;
}

/* Deterministische Beispiel-Verfügbarkeit (kein Zufall → stabil bei Reload) */
function gaSlots(dayIndex, course) {
  const slots = [];
  const start = 8 * 60, end = 17 * 60 + 30, step = 30;
  for (let m = start; m <= end; m += step) {
    const h = Math.floor(m / 60), min = m % 60;
    const seed = (m * 31 + dayIndex * 17 + (course === "master" ? 3 : 11)) % 9;
    let free = 4;
    if (seed === 0) free = 0;
    else if (seed < 3) free = 1;
    else if (seed < 5) free = 2;
    else if (seed < 7) free = 3;
    slots.push({
      time: String(h).padStart(2, "0") + ":" + String(min).padStart(2, "0"),
      free: free
    });
  }
  return slots;
}

/* Mitgliedschaften (Preise von golf-adendorf.de, Stand der Recherche) */
const GA_MITGLIEDSCHAFTEN = [
  {
    id: "premium",
    name: "Premium Spielrecht",
    preis: 1200,
    featured: true,
    badge: "Beliebteste Wahl",
    leistungen: ["Gesamte Anlage nutzbar", "Unbegrenztes Greenfee", "Unbegrenztes Rangefee", "Inkl. DGV-Ausweis (zzgl. Verbandsbeiträge ab 21 J.)"]
  },
  {
    id: "wochentags",
    name: "Premium wochentags",
    preis: 950,
    leistungen: ["Gesamte Anlage nutzbar", "Greenfee Mo. – Do.", "Rangefee Mo. – Do.", "Inkl. DGV-Ausweis (zzgl. Verbandsbeiträge ab 21 J.)"]
  },
  {
    id: "afterwork",
    name: "Premium AfterWork",
    preis: 765,
    leistungen: ["Mo. – Fr. ab 16 Uhr, Feiertage inklusive", "Wochenende ganztägig", "Gesamte Anlage nutzbar", "Greenfee & Rangefee inklusive"]
  },
  {
    id: "studenten",
    name: "Studenten (bis 28 J.)",
    preis: 400,
    leistungen: ["Gesamte Anlage nutzbar", "Unbegrenztes Greenfee", "Unbegrenztes Rangefee", "Inkl. DGV-Ausweis (zzgl. Verbandsbeiträge ab 21 J.)"]
  },
  {
    id: "jugend",
    name: "Jugendliche (bis 21 J.)",
    preis: 170,
    leistungen: ["Gesamte Anlage nutzbar", "Unbegrenztes Greenfee", "Unbegrenztes Rangefee"]
  },
  {
    id: "kinder",
    name: "Kinder (bis 12 J.)",
    preis: 80,
    leistungen: ["Gesamte Anlage nutzbar", "Unbegrenztes Greenfee", "Unbegrenztes Rangefee"]
  },
  {
    id: "akademie",
    name: "Akademie Public Course",
    preis: 550,
    leistungen: ["Publiccourse nutzbar", "Unbegrenztes Greenfee", "Unbegrenztes Rangefee", "Ideal für Einsteiger:innen"]
  },
  {
    id: "zweit",
    name: "Zweit-Spielrecht",
    preis: 750,
    leistungen: ["Gesamte Anlage nutzbar", "30 Runden p. a. inkl. Green- & Rangefee", "Nachweis Hauptmitgliedschaft erforderlich"]
  },
  {
    id: "fern",
    name: "Fern-Spielrecht",
    preis: 400,
    leistungen: ["Gesamte Anlage nutzbar", "20 Runden p. a. inkl. Green- & Rangefee", "Erstwohnsitz mind. 150 km entfernt"]
  }
];

/* News (Beispiele nach Vorbild der Live-Seite) */
const GA_NEWS = [
  {
    titel: "Bräunig gewinnt Saisonfinale und steigt auf",
    datum: "06.10.2025",
    text: "Christian Bräunig feiert ausgerechnet im Saisonfinale bei der Castanea Resort Championship seinen ersten Saisonsieg – bei schwierigen Bedingungen mit drei Schlägen Vorsprung."
  },
  {
    titel: "Die neuen Clubmeister:innen sind gekürt!",
    datum: "08.09.2025",
    text: "Die Clubmeisterschaft 2025 fand vom 05. bis 07. September statt – drei Tage spannender Golfsport auf dem Mastercourse mit würdigen Sieger:innen."
  },
  {
    titel: "Beeindruckende Spendensumme bei der 19. NCL-Golf-Trophy",
    datum: "18.08.2025",
    text: "Die Charity-Trophy zugunsten der NCL-Stiftung erzielte erneut eine beeindruckende Spendensumme – vielen Dank an alle Teilnehmenden und Sponsoren!"
  }
];
