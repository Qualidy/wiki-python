# Lernziele Data Science

# Data Science: Einführung

- wissen was Data Science ist
- den Ablauf eines Data Science Projektes verstehen (Data Science Prozess)
- ein konkretes Beispiel für ein Data Science Projekt kennen
- wissen, wozu man die Bibliotheken Pandas, Matplotib, Seaborn braucht

# Pandas: Einführung

- die grundlegenden Datenstruktur von Pandas kennen: DataFrame, Series, Index
- Zugriff auf Spalten und Zeilen beherrschen
  Spalten oder Zeilen abändern können

# Pandas: Import/Export von Daten

- einen Überblick erhalten, welche Datenformate Pandas für die read() und to() Funktionen kennt
- verstehen, dass alle read() und to() Funktionen parametrisierbar (einstellbar) sind für spezifischere Wünsche / Situationen
- erfahren, dass Pandas auch direkt mit Datenbanken arbeiten kann

# Pandas: Umgang mit fehlenden Werten

- verstehen, wieso Datenlücken in realen Daten üblich sind
- wissen, dass es zwei generelle Lösungsmöglichkeiten gibt: Entfernung oder Imputation
- Pandas Funktionen zum Umgang mit Lücken kennen und beherrschen

# NumPy: Arrays

- wissen wozu wir NumPy brauchen
- das Erzeugen und Reshapen von Arrays beherrschen
- Bestimmen von Spalten-/Zeilensummern
- Bestimmen und Auffinden von Maxima, Minima
- Berechnen von Mittelwert und Median eines NumPy Arrays


# NumPy: Slicing

- wissen wieso man manchmal nur ein Stück von einer Datenstruktur braucht
- das Slicing mit dem Slicing-Operator : beherrschen
- verstehen, dass es auch eine Schrittweitenangabe (Step) beim Slicing gibt
- aus einem mehrdimensionalen NumPy-Array n-dimensionale Blöcke ausschneiden können


# Matplotlib: Linienplots

- Anwendungsbereiche für Linienplots kennen
- Aus Python-Listen von Werten oder NumPy Arrays Linienplots erzeugen können
- Linienplots paramterisieren können (Farben, Linientypen)
- Anmerkungen in Linienplots einfügen können
- Legenden und Gitterlinien einblenden

# Matplotlib: Subplots

- wissen was Subplots sind
- verstehen, dass es mehrere Möglichkeiten gibt in Matplotlib Subplots zu erzeugen
- Subplots-Gitter beliebiger Anordnung erstellen und mit Plots befüllen können
- Subplots parametrisieren können (Breite und Höhe über mehrere Gitterzellen festlegen)

# Seaborn: Einführung

- wissen, wie sich Seaborn von Matplotlib unterscheidet
- violinplots, boxplots, jointplots, kdeplots, countplots, facetgrids kennen lernen
- Scatterplots mit Regressionsgeraden erzeugen können

# Pandas: Gruppieren und Pivotisieren

- Anwendungsfälle für das Gruppieren bzw. Pivotisieren von Daten kennen
- Gruppieren von Daten und das Berechnen von Summen, Minima, Maxima, Durchschnittswerten, etc. pro Gruppe beherrschen
- Pivotosieren von Tabellen nach einem oder mehreren Merkmalen können

# Matplotlib: Ticks

- wissen, was Ticks sind
- wissen, wie man Ticks an ganz bestimmten Stellen auf der x- und y-Achse erscheinen lassen kann
- Ticks konfigurieren können (Labels, Farbe)

# Pandas: Multiindex

- verstehen, dass es bei Pandas Tabellen auch hierarschiche Indizies gibt (Multiindex)
- verstehen, wieso es das gibt und was es bringt
- Tabellen mit Multiindex erzeugen können
- Daten aus Tabellen mit Multiindex auslesen können

# Pandas & Matplotlib: Zeitreihen

- Zeitreihen glätten können
- Zeitreihen auf eine beliebige neue Periode (z.B. wochenweise, monatsweise) resampeln
- Zeitreihen auf Trends und Saisonalität untersuchen können
- Zeitreihen alternativ als Heatmaps visualisieren können
- wissen, was Zeitreihenprädiktion ist
- Zeitreihen unterteilen und deskriptive Statistiken für die Teilzeitreihen berechnen können

# Pandas: Outlier (Ausreißer)

- wissen, wie Outlier entstehen (Messfehler vs. Extremwerte)
- verstehen, wieso Outlier gefährlich sind (Verfälschung von Statistiken)
- Z-Score und IQR-Methode kennen, um Ausreißer zu identifizieren
- Z-Score Methode anwenden können auf Pandas DataFrames, um Ausreißer zu identifizieren
- IQR Methode anwenden können auf Pandas DataFrames, um Ausreißer zu identifizieren
- Boxplots zur Visualisierung von Ausreißern interpretieren können
- Ausreißer mit Hilfe der Standardabweichung direkt identifizieren und rausfiltern können
- Ausreißer mit Winsorizing entfernen

# Pandas/Matplotlib/Seaborn: DateTime (Zeitstempel)

- wissen, wie man aus String DateTime Objekte macht
- Bestimmte zeitliche Ausschnitte aus einer Zeitreihe "rausschneiden" können
- Zeitreihen mit Matplotlib oder Seaborn visualisieren können
- Hinzufügen von zusätzlichen Spalten auf Basis eines Zeitstempels wie Wochentag, Arbeitswoche, etc.
- Frühestes/Spätestes Datum in einer Zeitreihe ermitteln können
- Fehlende zeitliche Daten ergänzen können
