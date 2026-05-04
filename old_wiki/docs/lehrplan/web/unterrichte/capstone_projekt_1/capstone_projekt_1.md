# Capstone Projekt: Wetter API CLI Anwendung

[150 min]

Erstelle ein Kommandozeilen-Programm bei dem der Nutzer um die Eingabe einer Stadt gebeten wird und dann das aktuelle Wetter für den gegebenen Standort bekommt.
Füge zusätzlich die Option hinzu, eine Vorhersage für die kommenden 7 Tage anzuzeigen.

![Wetter CLI Projekt](../../images/1_wetter_cli.png)

## Anforderungen

- Interaktive CLI Anwendung mit 3 Optionen
  - Wetter Aktuell (fragt den Nutzer nach der Stadt)
  - Wetter Vorhersage (fragt den Nutzer nach der Stadt)
  - Beenden
- Die CLI Anwendung soll mehrere Anfragen nacheinander annehmen können.
- Falls das Rate-Limit (Status-Code `429`) überschritten wird, soll das Programm den Fehler abfangen.
- Nutze die WMO Codes für den aktuellen Wetterstatus

### Bonus

- Die CLI Anwendung soll visuell mit Emojis aufgebessert werden (Warm/Kalt, Wolkig/Gewitter)
- Es können mehrere Städte angebeben werden für die man im Vergleich die Wetterdaten sieht
- Nutze `bullet` um die CLI noch visueller und interaktiver zu machen.

## Ressourcen

- [API Wetter für Lat/Long](https://open-meteo.com/) 

- [API für City to Lat/Long](https://geocode.maps.co/)

- [Beautiful Python Prompts Made Simple](https://github.com/bchao1/bullet)

<details>
<summary>WMO Wetter Code Mapping</summary>

<pre><code>
wmo_codes = {
        0: 'Klarer Himmel',
        1: 'Hauptsächlich klar',
        2: 'Teilweise bewölkt',
        3: 'Bewölkt',
        45: 'Nebel',
        48: 'Nebel mit Reifbildung',
        51: 'Leichter Nieselregen',
        53: 'Mäßiger Nieselregen',
        55: 'Dichter Nieselregen',
        56: 'Leichter gefrierender Nieselregen',
        57: 'Dichter gefrierender Nieselregen',
        61: 'Leichter Regen',
        63: 'Mäßiger Regen',
        65: 'Starker Regen',
        66: 'Leichter gefrierender Regen',
        67: 'Starker gefrierender Regen',
        71: 'Leichter Schneefall',
        73: 'Mäßiger Schneefall',
        75: 'Starker Schneefall',
        77: 'Schneegriesel',
        80: 'Leichte Regenschauer',
        81: 'Mäßige Regenschauer',
        82: 'Starke Regenschauer',
        85: 'Leichte Schneeschauer',
        86: 'Starke Schneeschauer',
        95: 'Gewitter',
        96: 'Gewitter mit leichtem Hagel',
        99: 'Gewitter mit starkem Hagel'
}
</code></pre>
</details>

<br/>



[Lösung](./solutions.md)

