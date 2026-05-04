# Lösung
```python
class DatenAnalysator:
    """
    Eine Klasse zur Durchführung einfacher statistischer Analysen auf einer Liste von numerischen Daten.

    Attributes
    ----------
    daten : list of int/float
        Liste der numerischen Daten, mit denen die Analyse durchgeführt wird.

    Methods
    -------
    mittelwert()
        Berechnet den Mittelwert der Daten.
    maximum()
        Findet den maximalen Wert in den Daten.
    minimum()
        Findet den minimalen Wert in den Daten.
    """

    def __init__(self, daten):
        """
        Initialisiert den DatenAnalysator mit einer Liste von Daten.

        Parameter:
        ----------
        daten : list of int/float
            Die zu analysierenden numerischen Daten.
        
        Raises:
            ValueError: Wenn 'daten' leer ist.
        """
        if not daten:
            raise ValueError("Die Datenliste darf nicht leer sein.")
        self.daten = daten

    def mittelwert(self):
        """
        Berechnet den Mittelwert der Daten.

        Returns
        -------
        float
            Der Mittelwert der Daten.
        """
        return sum(self.daten) / len(self.daten)

    def maximum(self):
        """
        Findet den maximalen Wert in den Daten.

        Returns
        -------
        int/float
            Der maximale Wert in den Daten.
        """
        return max(self.daten)

    def minimum(self):
        """
        Findet den minimalen Wert in den Daten.

        Returns
        -------
        int/float
            Der minimale Wert in den Daten.
        """
        return min(self.daten)

    def daten_normalisieren(self):
        """
        Normalisiert die Daten, so dass alle Werte zwischen 0 und 1 liegen.
    
        Returns
        -------
        list of float
            Eine Liste der normalisierten Daten, wobei jeder Wert zwischen 0 und 1 liegt.
        """
        max_wert = self.maximum()
        min_wert = self.minimum()
        return [(x - min_wert) / (max_wert - min_wert) for x in self.daten]
```