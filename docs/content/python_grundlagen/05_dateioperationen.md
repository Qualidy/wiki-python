# Dateioperationen in Python
[90min]

In Python gibt es verschiedene Möglichkeiten, Dateien zu öffnen, zu lesen und zu schreiben.
Hier werden die Verwendung von `with open` und das Lesen von CSV-Dateien als Beispiele behandelt.

## 1. Dateien ohne `with open`

Datei öffnen, lesen und schließen:

```python
datei = open("beispiel.txt", "r")
inhalt = datei.read()
datei.close()
```

Beim Arbeiten mit Dateien ohne `with open` musst du darauf achten, 
die Datei manuell zu öffnen und zu schließen. Das kann zu Problemen führen, wenn ein Fehler auftritt, 
bevor die Datei geschlossen wird.

## 2. Dateien mit `with open`

Datei mit `with open` öffnen und lesen:

```python
with open("beispiel.txt", "r") as datei:
    inhalt = datei.read()
```

Die `with open`-Anweisung ist eine sicherere Methode, um mit Dateien umzugehen. Sie stellt sicher, dass die Datei ordnungsgemäß geschlossen wird, selbst wenn ein Fehler auftritt. 

## 3. Dateipfade

Bei der Verwendung der `open`-Funktion in Python spielt die Angabe von Dateipfaden eine zentrale Rolle. 
Ein Pfad kann entweder absolut oder relativ sein. Ein absoluter Pfad gibt den vollständigen Speicherort 
einer Datei oder eines Verzeichnisses im Dateisystem an, beginnend vom Wurzelverzeichnis. 
Andererseits ist ein relativer Pfad in Bezug auf das aktuelle Arbeitsverzeichnis angegeben.
Dies bedeutet, dass er den Pfad relativ zu dem Ort angibt, an dem das Python-Skript ausgeführt wird.

Das Präfix "r" vor einem Pfad in Python steht für "raw" (roh) und wird häufig verwendet, um Escape-Zeichen zu deaktivieren. Escape-Zeichen, wie etwa \, können in normalen Zeichenketten eine spezielle Bedeutung haben (z. B. \n für einen Zeilenumbruch). Durch das Hinzufügen des "r"-Präfixes wird der Pfad als "rohe" Zeichenkette behandelt, was besonders nützlich ist, wenn man Windows-Pfade verwendet, da Backslashes in regulären Zeichenketten zu Escape-Zwecken verwendet werden und so zu Problemen führen könnten. Der "r"-Präfix sorgt dafür, dass der Pfad genau so interpretiert wird, wie er eingegeben wird, ohne Escape-Zeichen zu berücksichtigen.


## 3. CSV-Dateien lesen

CSV-Datei öffnen und lesen:

```
import csv

with open("beispiel.csv", "r") as csv_datei:
    csv_reader = csv.reader(csv_datei)
    for zeile in csv_reader:
        print(zeile)
```

Das `csv`-Modul ermöglicht das Lesen von CSV-Dateien.
Mit der `csv.reader`-Funktion kannst du die Zeilen der CSV-Datei durchgehen.

### Beispiel für CSV-Schreiben:

Wenn du Daten in eine CSV-Datei schreiben möchtest, kannst du die `csv`-Bibliothek ebenfalls verwenden. Hier ist ein Beispiel:

```python
import csv

# Daten, die in die CSV-Datei geschrieben werden sollen
daten = [
    ["Name", "Alter", "Stadt"],
    ["Max", 25, "Berlin"],
    ["Anna", 30, "München"],
    ["Tom", 22, "Hamburg"]
]

# Öffne die CSV-Datei im Schreib-Modus
with open("ausgabe.csv", "w", newline="") as csv_datei:
    # Erstelle einen CSV-Writer
    csv_writer = csv.writer(csv_datei)

    # Schreibe die Daten in die CSV-Datei
    for zeile in daten:
        csv_writer.writerow(zeile)

# Die CSV-Datei wurde erstellt und die Daten wurden erfolgreich geschrieben.
```

In diesem Beispiel werden Daten in eine CSV-Datei mit dem Namen "ausgabe.csv" geschrieben. Der `csv_writer` wird verwendet, um Zeilen in die Datei zu schreiben. Beachte, dass die Datei im Schreib-Modus ("w") geöffnet wird, und `newline=""` wird verwendet, um sicherzustellen, dass Zeilenenden korrekt behandelt werden.


Je nach Anforderungen kannst du verschiedene Modi (z.B. "w" für Schreiben, "a" für Anhängen) und Optionen verwenden. Es ist auch wichtig, die Datei nach dem Lesen oder Schreiben ordnungsgemäß zu schließen, besonders bei Verwendung von `with open`.

Hier eine Übersicht

| Modus | Beschreibung                    | Python-Dokumentation                                                                  |
|-------|---------------------------------|---------------------------------------------------------------------------------------|
| "r"   | Lesen                           | [Link](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files) |
| "w"   | Schreiben                       | [Link](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files) |
| "x"   | Exklusives Schreiben            | [Link](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files) |
| "a"   | Anhängen                        | [Link](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files) |
| "b"   | Binärmodus                      | [Link](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files) |
| "t"   | Textmodus                       | [Link](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files) |
| "+"   | Aktualisieren (Lesen/Schreiben) | [Link](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files) |

# Aufgaben:
[240min]

## 1. Verwendung von `with open` in Dateioperationen 🌶️️

Erläutere die Verwendung der `with open` Anweisung und warum sie bevorzugt wird, insbesondere im Zusammenhang mit Dateioperationen.

## 2. Lesen und Schreiben von CSV-Dateien 🌶️️🌶️️

Unterscheide zwischen dem Lesen und Schreiben von CSV-Dateien in Python. Verwende dazu die `csv`-Bibliothek und erkläre die grundlegenden Schritte.

## 3. Methoden im Kontext von Dateioperationen 🌶️️🌶️️🌶️️

Erkläre die Bedeutung der Methoden `read()`, `write()`, `seek()` und `close()` im Kontext von Dateioperationen. Warum ist es wichtig, die Datei nach dem Lesen oder Schreiben zu schließen?

## 4. Erstellung und Schreiben von Dateien 🌶️️

Erläutere, wie man eine Datei in Python erstellt und schreibt. Verwende dazu den `with open`-Ansatz und zeige, wie man Text in eine Datei schreibt.

## 5. Textmodus und Binärmodus in Dateioperationen 🌶️️🌶️️

Beschreibe den Unterschied zwischen dem Lesen einer Datei im Textmodus (`'r'`) und dem Binärmodus (`'rb'`) in Bezug auf die `open`-Funktion.

## 6. Umkehrung einer Datei 🌶️️🌶️️🌶️️

Schreibe eine Funktion, die den Inhalt einer Textdatei umkehrt. Das heißt, die erste Zeile wird zur letzten, die zweite zur vorletzten, usw.

## 7. CSV-Datei filtern 🌶️️🌶️️

Erstelle eine Funktion, die eine CSV-Datei liest, bestimmte Zeilen filtert und das Ergebnis in eine neue Datei schreibt. Die Filterkriterien sollten anpassbar sein.

## 8. Dateigröße berechnen 🌶️️🌶️️

Schreibe eine Funktion, die die Größe einer Datei in Kilobyte berechnet und ausgibt.

## 9. Zeichen zählen 🌶️️🌶️️

Erstelle eine Funktion, die die Anzahl der Zeichen in einer Textdatei zählt und zurückgibt. Berücksichtige dabei auch Leerzeichen und Sonderzeichen.

## 10. Datei verschlüsseln 🌶️️🌶️️🌶️️🌶️️

Implementiere eine einfache Verschlüsselungsfunktion, die den Inhalt einer Datei verschlüsselt und in eine neue Datei schreibt. Verwende dazu eine geeignete Verschlüsselungsmethode deiner Wahl.



### 3. Datei öffnen mit Fehlerbehandlung 🌶️️
   - Schreibe einen Code, der versucht, eine Datei mit dem Namen "beispiel.txt" zu öffnen. Verwende einen `try`-Block und behandle die `FileNotFoundError`-Ausnahme im `except`-Block, indem du eine Meldung ausgibst.

### 7. Komplexes Exception Handling 🌶️️🌶️️🌶️️
Erstelle einen Code, der eine Datei öffnet, ihren Inhalt liest und in eine andere Datei schreibt. Behandle dabei `FileNotFoundError`, `PermissionError` und `IOError` mit spezifischen Ausnahmen. Gib eine Meldung aus, wenn eine Ausnahme auftritt.

### 8. Fehlerbehandlung bei Dateioperationen 🌶️️🌶️️🌶️️
   - Schreibe einen Code, der versucht, den Inhalt einer Datei zu lesen und in eine andere Datei zu schreiben. Behandle mögliche `FileNotFoundError` und `PermissionError`-Ausnahmen im `except`-Block und gib entsprechende Meldungen aus.

