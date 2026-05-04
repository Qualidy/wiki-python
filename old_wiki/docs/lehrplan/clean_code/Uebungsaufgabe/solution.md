# Lösung

```python
import json
from typing import List, Dict

class Buecherei:
    """
    Eine Klasse zur Verwaltung von Büchereidaten.

    Methods
    -------
    lese_buecher_datei(dateipfad: str) -> List[Dict]:
        Liest die Bücherdaten aus einer JSON-Datei.
    berechne_lesezeit(buecher: List[Dict]) -> List[Dict]:
        Berechnet und fügt die Lesezeit zu jedem Buch hinzu.
    schreibe_buecher_datei(buecher: List[Dict], dateipfad: str) -> None:
        Schreibt die manipulierten Bücherdaten in eine JSON-Datei.
    """

    def lese_buecher_datei(self, dateipfad: str) -> List[Dict]:
        """
        Liest die Bücherdaten aus einer JSON-Datei.

        Parameters
        ----------
        dateipfad : str
            Der Pfad zur JSON-Datei mit Bücherdaten.

        Returns
        -------
        List[Dict]
            Eine Liste von Büchern, wobei jedes Buch als Dictionary dargestellt wird.
        """
        with open(dateipfad, 'r', encoding='utf-8') as datei:
            buecher = json.load(datei)
        return buecher

    def berechne_lesezeit(self, buecher: List[Dict]) -> List[Dict]:
        """
        Berechnet und fügt die Lesezeit zu jedem Buch hinzu.

        Parameters
        ----------
        buecher : List[Dict]
            Eine Liste von Büchern, wobei jedes Buch als Dictionary dargestellt wird.

        Returns
        -------
        List[Dict]
            Die Liste von Büchern mit hinzugefügter Lesezeit.
        """
        for buch in buecher:
            buch['lesezeit'] = buch['seitenzahl'] * 2  # 2 Minuten pro Seite
        return buecher

    def schreibe_buecher_datei(self, buecher: List[Dict], dateipfad: str) -> None:
        """
        Schreibt die manipulierten Bücherdaten in eine JSON-Datei.

        Parameters
        ----------
        buecher : List[Dict]
            Eine Liste von Büchern, wobei jedes Buch als Dictionary dargestellt wird.
        dateipfad : str
            Der Pfad, an dem die neue JSON-Datei gespeichert werden soll.
        """
        with open(dateipfad, 'w', encoding='utf-8') as datei:
            json.dump(buecher, datei, indent=4)

# Verwendung der Buecherei-Klasse
buecherei = Buecherei()
buecher = buecherei.lese_buecher_datei('buecher.json')
buecher_mit_lesezeit = buecherei.berechne_lesezeit(buecher)
buecherei.schreibe_buecher_datei(buecher_mit_lesezeit, 'buecher_mit_lesezeit.json')
```
