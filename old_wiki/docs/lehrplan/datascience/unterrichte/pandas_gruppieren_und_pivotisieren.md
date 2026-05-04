# Exkurs: Pandas: Gruppieren und Pivotisieren

<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/9CMfH4jKO5g?si=-GyPmqUIULiFnyEX" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


## Einführung [10 min]

## Gruppieren in Pandas

Das Gruppieren von Daten ist eine der wichtigsten Aufgaben in der Datenanalyse. Es ermöglicht die Organisation von Daten in kategorische Segmente, wodurch die Analyse komplexer Daten vereinfacht wird. Die Gruppierung in Pandas wird mit der groupby-Methode erreicht. Diese Methode teilt die Daten in Gruppen auf, die einen gemeinsamen Wert in einer bestimmten Spalte haben.

Zum Beispiel, wenn man eine Datenmenge mit Verkaufszahlen hat, könnte man diese Daten nach dem Verkaufsregion gruppieren. Dadurch könnte man analysieren, welche Region die höchsten Verkäufe erzielt, welche die geringsten und so weiter. Das Gruppieren ist besonders nützlich für aggregierte Berechnungen wie Summen, Durchschnitte, Maxima, Minima usw.

## Pivotisieren in Pandas

Pivotisieren ist eine weitere mächtige Technik in Pandas, die es ermöglicht, die Datenstruktur zu ändern und Tabellen neu zu organisieren. Es ist besonders hilfreich, um Daten aus einer langen Form in eine breite Form zu transformieren und umgekehrt. Beim Pivotisieren werden die Werte einer oder mehrerer Spalten als Spaltenkopf verwendet, was zu einer "gedrehten" Darstellung der Daten führt.

Ein gängiges Beispiel für Pivotisieren ist die Umwandlung von Zeitreihendaten. Wenn man zum Beispiel tägliche Verkaufszahlen über mehrere Jahre hat, kann man die Daten so pivotisieren, dass die Jahre die Spalten bilden und jede Zeile einem Tag entspricht. Dies erleichtert es, jahreszeitliche Trends oder Muster im Laufe der Zeit zu erkennen.

## Anwendungsbeispiele

Die Fähigkeit, Daten zu gruppieren und zu pivotisieren, ist in vielen realen Szenarien nützlich. Im Geschäftsbereich ermöglicht es Unternehmen, Verkaufstrends zu analysieren, Kundensegmente zu verstehen oder die Leistung verschiedener Abteilungen zu bewerten. In der Wissenschaft erlauben diese Techniken Forschern, große Datensätze zu kategorisieren und zu analysieren, was für die Entdeckung neuer Erkenntnisse unerlässlich ist.

Ein konkretes Beispiel könnte die Analyse von Patientendaten in einem Krankenhaus sein. Durch das Gruppieren der Daten nach Diagnosen und das Pivotisieren nach Behandlungsjahren können Muster in der Effektivität von Behandlungen oder die Verbreitung von Krankheiten im Laufe der Zeit aufgedeckt werden.

Gruppieren und Pivotisieren in Pandas sind wichtige Werkzeuge für die Datenanalyse. Sie bieten einen Ansatz, um Daten zu organisieren, Muster zu erkennen und letztendlich fundierte Entscheidungen zu treffen.

## Codebeispiele [45 min]

### Beispiel 1: Grundlegendes Gruppieren nach einer Spalte


```python
import pandas as pd

# Erstellen eines Beispiel-Datenrahmens
df = pd.DataFrame({
    'Produkt': ['Apfel', 'Banane', 'Apfel', 'Banane', 'Apfel', 'Banane'],
    'Verkaufsmenge': [10, 20, 15, 25, 5, 30]
})
print(df)

# Gruppieren nach der Spalte 'Produkt' und
# Berechnen der Gesamtverkaufsmenge für jedes Produkt
gruppen = df.groupby('Produkt').sum()
print(gruppen)
```

      Produkt  Verkaufsmenge
    0   Apfel             10
    1  Banane             20
    2   Apfel             15
    3  Banane             25
    4   Apfel              5
    5  Banane             30
             Verkaufsmenge
    Produkt               
    Apfel               30
    Banane              75


In diesem Beispiel wird ein DataFrame `df` erstellt, der Verkaufsdaten für Produkte enthält. Wir gruppieren die Daten nach der Spalte 'Produkt' und berechnen die Gesamtverkaufsmenge für jedes Produkt. Das Ergebnis ist ein neuer DataFrame, der die Gesamtverkaufsmenge für Äpfel und Bananen anzeigt.

### Beispiel 2: Gruppieren und Anwenden mehrerer Aggregatfunktionen


```python
import pandas as pd

# Erstellen eines Beispiel-Datenrahmens
df = pd.DataFrame({
    'Produkt': ['Apfel', 'Banane', 'Apfel', 'Banane', 'Apfel', 'Banane'],
    'Verkaufsmenge': [10, 20, 15, 25, 5, 30],
    'Preis': [1.0, 0.5, 1.2, 0.45, 0.9, 0.55]
})
print(df, "\n")

# Gruppieren nach 'Produkt' und Anwenden mehrerer Aggregatfunktionen
ergebnis = df.groupby('Produkt').agg({'Verkaufsmenge': 'sum', 'Preis': 'mean'})
print(ergebnis)
```

      Produkt  Verkaufsmenge  Preis
    0   Apfel             10   1.00
    1  Banane             20   0.50
    2   Apfel             15   1.20
    3  Banane             25   0.45
    4   Apfel              5   0.90
    5  Banane             30   0.55 
    
             Verkaufsmenge     Preis
    Produkt                         
    Apfel               30  1.033333
    Banane              75  0.500000


Hier gruppieren wir den DataFrame `df` nach der Spalte 'Produkt'. Für die 'Verkaufsmenge' berechnen wir die Summe, und für den 'Preis' das arithmetische Mittel. Das Ergebnis ist ein DataFrame, der die Gesamtverkaufsmenge und den durchschnittlichen Preis für jedes Produkt zeigt.

### Beispiel 3: Pivot-Tabelle erstellen


```python
import pandas as pd

# Erstellen eines Beispiel-Datenrahmens
df = pd.DataFrame({
    'Datum': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02'],
    'Produkt': ['Apfel', 'Banane', 'Apfel', 'Banane'],
    'Verkaufsmenge': [10, 15, 20, 25]
})
print(df, "\n")

# Erstellen einer Pivot-Tabelle
pivot = df.pivot_table(values='Verkaufsmenge',
                       index='Datum',
                       columns='Produkt',
                       aggfunc='sum')
print(pivot)
```

            Datum Produkt  Verkaufsmenge
    0  2023-01-01   Apfel             10
    1  2023-01-01  Banane             15
    2  2023-01-02   Apfel             20
    3  2023-01-02  Banane             25 
    
    Produkt     Apfel  Banane
    Datum                    
    2023-01-01     10      15
    2023-01-02     20      25


In diesem Beispiel erstellen wir eine Pivot-Tabelle aus dem DataFrame `df`. Wir setzen 'Datum' als Index, 'Produkt' als Spalten und summieren die 'Verkaufsmenge'. Das Ergebnis zeigt die Verkaufsmengen für Äpfel und Bananen getrennt nach Datum.

### Beispiel 4: Gruppieren mit mehreren Spalten


```python
import pandas as pd

# Erstellen eines Beispiel-Datenrahmens
df = pd.DataFrame({
    'Region': ['Nord', 'Süd', 'Nord', 'Süd'],
    'Produkt': ['Apfel', 'Apfel', 'Banane', 'Banane'],
    'Verkaufsmenge': [10, 20, 15, 25]
})
print(df, "\n")

# Gruppieren nach mehreren Spalten
gruppen = df.groupby(['Region', 'Produkt']).sum()
print(gruppen)
```

      Region Produkt  Verkaufsmenge
    0   Nord   Apfel             10
    1    Süd   Apfel             20
    2   Nord  Banane             15
    3    Süd  Banane             25 
    
                    Verkaufsmenge
    Region Produkt               
    Nord   Apfel               10
           Banane              15
    Süd    Apfel               20
           Banane              25


Hier gruppieren wir den DataFrame `df` nach den Spalten 'Region' und 'Produkt'. Das Ergebnis ist ein DataFrame, der die Gesamtverkaufsmengen für Äpfel und Bananen in den jeweiligen Regionen anzeigt.

### Beispiel 5: Pivotisieren mit Multi-Index


```python
import pandas as pd

# Erstellen eines Beispiel-Datenrahmens
df = pd.DataFrame({
    'Datum': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02'],
    'Region': ['Nord', 'Süd', 'Nord', 'Süd'],
    'Produkt': ['Apfel', 'Banane', 'Apfel', 'Banane'],
    'Verkaufsmenge': [10, 15, 20, 25]
})
print(df, "\n")

# Pivotisieren mit Multi-Index
pivot = df.pivot_table(values='Verkaufsmenge', index=['Datum', 'Region'], columns='Produkt')
print(pivot)
```

            Datum Region Produkt  Verkaufsmenge
    0  2023-01-01   Nord   Apfel             10
    1  2023-01-01    Süd  Banane             15
    2  2023-01-02   Nord   Apfel             20
    3  2023-01-02    Süd  Banane             25 
    
    Produkt            Apfel  Banane
    Datum      Region               
    2023-01-01 Nord     10.0     NaN
               Süd       NaN    15.0
    2023-01-02 Nord     20.0     NaN
               Süd       NaN    25.0


In diesem Beispiel verwenden wir eine Pivot-Tabelle, um den DataFrame `df` zu pivotisieren. Wir setzen 'Datum' und 'Region' als Multi-Index für die Zeilen und 'Produkt' als Spalten. Die Werte in der Tabelle repräsentieren die 'Verkaufsmenge'. Dies erzeugt eine mehrdimensionale Ansicht der Daten, die es ermöglicht, die Verkaufsmengen von Äpfeln und Bananen nach Datum und Region zu analysieren. Das Ergebnis ist eine übersichtliche Darstellung der Verkaufsmengen, die auf einen Blick zeigt, wie sich die Verkäufe über verschiedene Produkte und Regionen verteilen.

## Aufgaben [120 min]

### A1: Grundlegende Gruppierung 🌶️

Erstellen Sie einen Pandas DataFrame mit drei Spalten: 'Name', 'Kategorie' und 'Punkte'. Gruppieren Sie diesen DataFrame nach 'Kategorie' und berechnen Sie die durchschnittlichen Punkte je Kategorie.

### A2: Aggregation mit mehreren Funktionen 🌶️🌶️🌶️

Verwenden Sie den gleichen DataFrame wie in Aufgabe 1. Gruppieren Sie die Daten nach 'Kategorie' und wenden Sie mehrere Aggregatfunktionen an: Berechnen Sie für jede Kategorie die Gesamtanzahl, den Durchschnitt und die maximale Punktzahl.

### A3: Erstellen einer Pivot-Tabelle 🌶️🌶️

Erstellen Sie einen DataFrame mit Spalten 'Datum', 'Produkt' und 'Verkaufsmenge'. Erzeugen Sie eine Pivot-Tabelle, die die Gesamtverkaufsmenge für jedes Produkt nach Datum gruppiert.

### A4: Gruppierung nach mehreren Spalten 🌶️🌶️

Erstellen Sie einen DataFrame mit den Spalten 'Region', 'Produkt' und 'Verkaufsmenge'. Gruppieren Sie die Daten nach 'Region' und 'Produkt' und berechnen Sie die Gesamtverkaufsmenge für jede Kombination.

### A5: Pivotisieren mit Multi-Index 🌶️🌶️

Verwenden Sie einen DataFrame mit den Spalten 'Datum', 'Region', 'Produkt' und 'Verkaufsmenge'. Erstellen Sie eine Pivot-Tabelle mit einem Multi-Index aus 'Datum' und 'Region', wobei 'Produkt' als Spalten verwendet wird.

### A6: Filtern nach Gruppierungsaggregat 🌶️🌶️🌶️🌶️

Erstellen Sie einen DataFrame mit den Spalten 'Team', 'Spieler' und 'Punkte'. Gruppieren Sie die Daten nach 'Team' und filtern Sie die Gruppen, sodass nur Teams mit einer durchschnittlichen Punktzahl von über 15 Punkten angezeigt werden.

### A7: Erweiterte Pivot-Tabellen 🌶️🌶️

Erstellen Sie einen DataFrame mit den Spalten 'Datum', 'Produkt', 'Region' und 'Verkaufsmenge'. Erzeugen Sie eine Pivot-Tabelle, die die durchschnittliche Verkaufsmenge für jedes Produkt nach Region und Datum gruppiert.

### A8: Kombiniertes Gruppieren und Pivotisieren 🌶️🌶️🌶️

Erstellen Sie einen DataFrame mit den Spalten 'Monat', 'Verkäufer' und 'Verkaufsmenge'. Gruppieren Sie die Daten nach 'Verkäufer' und erstellen Sie eine Pivot-Tabelle, die die Gesamtverkaufsmenge pro Monat für jeden Verkäufer anzeigt.

### A9: Gruppieren und Berechnen von kumulativen Summen 🌶️🌶️🌶

Erstellen Sie einen DataFrame mit den Spalten 'Datum', 'Kategorie' und 'Wert'. Gruppieren Sie die Daten nach 'Kategorie' und berechnen Sie die kumulative Summe der Werte innerhalb jeder Kategorie.

### A10: Erweitertes Pivotisieren mit Füllen von fehlenden Werten 🌶️🌶️

Erstellen Sie einen DataFrame mit den Spalten 'Datum', 'Produkt' und 'Verkaufsmenge'. Erzeugen Sie eine Pivot-Tabelle, die die Gesamtverkaufsmenge für jedes Produkt nach Datum anzeigt, und füllen Sie fehlende Werte mit Nullen.

[Lösungen](pandas_gruppieren_und_pivotisieren_loesungen.md)
