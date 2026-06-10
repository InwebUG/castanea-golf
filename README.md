# Golf Resort Adendorf – Website-Redesign

Statischer Website-Prototyp für das [Golf Resort Adendorf](https://www.golf-adendorf.de/) (Castanea Golf Resort) mit Fokus auf flüssige Animationen und Conversion: Nutzer:innen sollen schnell eine **Startzeit buchen** oder eine **Mitgliedschaft abschließen**.

## Highlights

- **POV-Hero mit echtem Drohnen-Video:** Lizenzfreies Footage (Pexels) wird per Scroll frame-genau gescrubbt – man "fliegt" den Golfschuss übers Fairway selbst. Während des Flugs erscheinen nacheinander drei Paare von Glas-Containern mit Inhalten (Startzeiten, Mitgliedschaft, Anlage, Greenfee, Kurse, Gastronomie/Hotel), ohne je die zentralen Texte zu überdecken. Lädt das Video nicht, greift automatisch eine in CSS/SVG gezeichnete Fallback-Szene.
- **Beispiel-Buchungsstrecke** für Startzeiten (Tag → Platz → Slot → Daten → Bestätigung) im Stil des echten Systems
- **Mitgliedschafts-Antrag** als 3-Schritte-Wizard mit allen 9 Spielrechts-Modellen; Vorauswahl per `?modell=<id>`
- Lenis Smooth-Scrolling, GSAP ScrollTrigger-Reveals, Seitenübergänge, Magnetic Buttons, `prefers-reduced-motion`-Fallbacks

## Lokal starten

Wegen des Video-Ladens per `fetch` wird ein lokaler Server benötigt:

```bash
python3 -m http.server 8741
# → http://127.0.0.1:8741/
```

Jeder Webserver funktioniert (das Video wird als Blob geladen und ist daher auch ohne HTTP-Range-Support seekbar).

## Struktur

```
index.html              Startseite mit POV-Video-Hero
startzeiten.html        Beispiel-Buchungsstrecke (Tee-Times)
mitgliedschaft.html     Spielrechte + Online-Antrag (Wizard)
greenfee.html           Preise (echte Daten der Live-Seite)
golfanlage.html         Plätze, Platzdaten, Partneranlagen
golf-lernen.html        Kurse (Beispielangebote)
gastronomie.html        Clubhaus „Castello"
kontakt.html            Kontaktformular + Anfahrt
css/style.css           Design-System (Tiefgrün/Sand/Gold, Playfair Display + Inter)
js/main.js              Gemeinsame Interaktion & Animationen
js/data.js              Beispieldaten (Startzeiten, Mitgliedschaften, News)
assets/fairway-flug.mp4 Hero-Video (Pexels, lizenzfrei)
build.py                Generator für die Unterseiten (gemeinsamer Header/Footer)
```

Unterseiten ändern: `build.py` bearbeiten und `python3 build.py` ausführen. `index.html` wird direkt gepflegt.

## Hinweise zu Inhalten & Buchungssystemen

- Termine/Slots sind **Beispieldaten**. Die Live-Website bucht Startzeiten und Turniere über **PC CADDIE://online** (`pccaddie.net`, Club-Nr. 0493383) und vermittelt Kursangebote über **mitfit**-Funnels.
- Texte und Preise stammen von golf-adendorf.de (Stand der Recherche); der Hotel-Link führt weiterhin extern auf castanea-resort.de. Der Login-Bereich folgt später.

## Lizenzen

- **Hero-Video:** [Pexels](https://www.pexels.com/) – kostenlose Nutzung gemäß [Pexels-Lizenz](https://www.pexels.com/license/), keine Attribution erforderlich.
- **Schriften:** Playfair Display & Inter via Google Fonts (OFL).
- **Bibliotheken:** GSAP (Standard-Lizenz, via CDN), Lenis (MIT, via CDN).
- Marken, Logos und Originaltexte gehören der Golf Resort Adendorf KG bzw. dem Castanea Resort.
