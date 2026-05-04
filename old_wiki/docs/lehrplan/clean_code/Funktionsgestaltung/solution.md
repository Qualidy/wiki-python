# Lösung Aufgabe 1

```python
import sys

def lese_eingaben():
    if len(sys.argv) < 3:
        print("Bitte mindestens zwei Zahlen als Argumente eingeben.")
        return None, None
    return int(sys.argv[1]), int(sys.argv[2])

def berechne_operationen(zahl1, zahl2):
    summe = zahl1 + zahl2
    differenz = zahl1 - zahl2
    produkt = zahl1 * zahl2
    quotient = zahl1 / zahl2 if zahl2 != 0 else "Unendlich"
    return summe, differenz, produkt, quotient

def zeige_ergebnisse(summe, differenz, produkt, quotient):
    print(f"Summe: {summe}")
    print(f"Differenz: {differenz}")
    print(f"Produkt: {produkt}")
    print(f"Quotient: {quotient}")

def hauptfunktion():
    zahl1, zahl2 = lese_eingaben()
    if zahl1 is None or zahl2 is None:
        return
    summe, differenz, produkt, quotient = berechne_operationen(zahl1, zahl2)
    zeige_ergebnisse(summe, differenz, produkt, quotient)

if __name__ == "__main__":
    hauptfunktion()
```

In der gegebenen Übungsaufgabe wurde der ursprüngliche Code, der in einer einzelnen Funktion (komplexe_funktion) enthalten war, in mehrere spezialisierte Funktionen aufgeteilt. Hier sind die Änderungen im Detail:

1. Funktion `lese_eingaben`: Diese Funktion wurde neu hinzugeefügt. Sie liest die Eingaben aus `sys.argv` und prüft, ob mindestens zwei Zahlen als Argumente eingegeben wurden. Falls nicht, gibt sie `None, None` zurück. Diese Funktion trennt die Logik des Einlesens der Eingaben von den restlichen Berechnungen. 
2. Funktion `berechne_operationen`: Diese Funktion führt die Berechnungen (Summe, Differenz, Produkt, Quotient) durch, die zuvor in der `komplexe_funktion` enthalten waren. Sie nimmt zwei Zahlen als Parameter (`zahl1`, `zahl2`) und gibt die Ergebnisse der Berechnungen zurück. Diese Funktion konzentriert sich ausschließlich auf die Berechnungslogik. 
3. Funktion `zeige_ergebnisse`: Diese Funktion ist verantwortlich für die Ausgabe der Ergebnisse. Sie nimmt die berechneten Werte (Summe, Differenz, Produkt, Quotient) als Parameter und gibt sie auf dem Bildschirm aus. Diese Trennung der Ausgabefunktion von der Berechnungslogik verbessert die Lesbarkeit und Wartbarkeit des Codes. 
4. Funktion `hauptfunktion`: Dies ist die Hauptfunktion, die die oben genannten Funktionen in der richtigen Reihenfolge aufruft. Zuerst werden die Eingaben gelesen, dann die Operationen berechnet und schließlich die Ergebnisse angezeigt. Diese Funktion dient als Kontrollpunkt für den gesamten Prozess.

Durch diese Änderungen wird der Code modularer, lesbarer und wartbarer. Jede Funktion ist nun für eine spezifische Aufgabe zuständig, was den Code einfacher zu verstehen und zu pflegen macht.

# Lösung Aufgabe 2

```python
def count_words(text):
    # Zerlegt den Text in einzelne Wörter
    words = text.split()
    return len(words)

def calculate_word_frequency(text):
    # Erstellt ein Wörterbuch zur Zählung der Häufigkeit jedes Wortes
    words = text.split()
    word_frequency = {}
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    return word_frequency

def analyze_text(text):
    # Funktionen aufrufen, um Anzahl der Wörter und Wortfrequenz zu berechnen
    word_count = count_words(text)
    word_frequency = calculate_word_frequency(text)

    # Findet das am häufigsten vorkommende Wort
    most_frequent_word = max(word_frequency, key=word_frequency.get)

    # Berechnet die durchschnittliche Wortlänge
    total_characters = sum(len(word) for word in text.split())
    average_word_length = total_characters / word_count

    return word_count, most_frequent_word, average_word_length

if __name__ == "__main__":
    text = "Beispieltext mit einigen Wörtern. Einige Wörter wiederholen sich."
    word_count, most_frequent_word, average_word_length = analyze_text(text)
    print("Anzahl der Wörter:", word_count)
    print("Häufigstes Wort:", most_frequent_word)
    print("Durchschnittliche Wortlänge:", average_word_length)
```

Die Verbesserungen im überarbeiteten Code im Vergleich zum Original sind:

**Bessere Funktionsnamen und Aufteilung:**

* Im verbesserten Code werden spezifischere und beschreibende Funktionsnamen verwendet (`count_words`, `calculate_word_frequency`, `analyze_text`), was die Absicht jeder Funktion klarer macht.
* Der Code wurde in separate Funktionen aufgeteilt, wobei jede Funktion eine spezifische Aufgabe erfüllt. Dies folgt dem Prinzip "Do One Thing", was den Code wartbarer und verständlicher macht.

**Klarere Variable-Namen:**

* Die Variablennamen sind jetzt aussagekräftiger und beschreibender (`words`, `word_frequency`, `most_frequent_word`, `average_word_length`), was den Code lesbarer und einfacher zu verstehen macht.

**Effizientere Berechnung des häufigsten Wortes:**

* Im verbesserten Code wird `max` mit dem Schlüssel `word_frequency.get` verwendet, um das am häufigsten vorkommende Wort zu finden. Dies ist effizienter und klarer als die manuelle Iteration und Vergleichslogik im ursprünglichen Code.

**Verbesserte Berechnung der durchschnittlichen Wortlänge:**

* Die durchschnittliche Wortlänge wird jetzt durch eine List Comprehension berechnet, die die Längen aller Wörter summiert und dann durch die Gesamtzahl der Wörter teilt. Diese Methode ist eleganter und nutzt Python-Funktionen effizienter.

**Deutlichere Hauptfunktion:**

* Die `main`-Funktion ist nun klarer strukturiert und teilt den Prozess in verständliche Schritte: Textanalyse durchführen und Ergebnisse ausdrucken.

Insgesamt macht die verbesserte Version den Code modularer, klarer und einfacher zu warten, indem sie gut benannte Funktionen und Variablen verwendet und effizientere Python-Konstrukte nutzt.

# Lösung Aufgabe 3

```python
def reverse_and_combine_words(words):
    # Umkehren jedes Wortes in der Liste mit einer List Comprehension
    reversed_words = [word[::-1] for word in words]
    
    # Kombinieren der umgekehrten Wörter zu einem einzigen String
    combined_words = ', '.join(reversed_words)
    
    return combined_words

# Beispiel-Liste
words = ["Python", "Entwicklung", "spaßig", "Lernen"]

# Ausführen der Funktion und Ausgeben des Ergebnisses
reverse_and_combine_words(words)
```
