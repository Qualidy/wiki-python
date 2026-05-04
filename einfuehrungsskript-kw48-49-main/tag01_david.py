# BMI Berechnen
# Mein Ziel: BMI = body mass index = gewicht(kg) / groesse^2
# Wie gelange ich dahin? ALGORITHMUS/Schritt-fuer-Schritt-Anleitung/Kochrezept aufsgellen 


# 1. gewicht abfragen
weight_str = input("Gewicht eingeben (kg): ")
weight = float(weight_str) #wandle meinen String in eine FLOAT/GLEITKOMMAZAHL/reelle Zahl um 
# 2. groesse abfragen
height_str = input("Groesse eingeben (m): ")
height = float(height_str)

# 3. formel auswerten
bmi = weight / height**2
# 4. Ergebnis ausgeben
print( "Dein BMI betraegt: ", round(bmi, 2) )



'''
1. Gib den Text `'Hallo, Wolfsburg"` aus.
2. Gib die drei Wörter "Tick", "Trick", und "Track" durch Kommas getrennt aus.
3. Wiederhole Aufabe 2, aber verwende 3 Variablen, um die 3 Wörter zu speichern. (Hinweis: Nutze f-Strings)
4. Frage den Nutzer nach seinem Namen und speichere diesen in der Variable `name`.
5. Erstelle die Variablen `x` und `y` und weise ihnen die Zahlen `10` und `50` zu.
6. Schreibt ein Programm, in dem hier der Variable mit dem Namen `name` euren Namen zuweist
7. Gebe die Variable `name` aus der zweiten Aufgabe zusammen mit einem Gruß aus, z.B. "Hallo Thomas"
8. Definiere eine Variable mit dem Namen `hallo-thomas = "Hallo Thomas"`. Was passiert? Wie kannst du das Problem beheben?
9. Lege eine Variable an, die eine List mit den Zahlen 1 bis 5 enthält.
10. Weise drei Variablen `x`, `y` und `z` den selben Wert zu.
11. Erhöhe den Wert von `x` aus der vorherigen Aufgabe, um `1` und gib wieder alle Variablen aus.
12. Welche Werte haben die Variablen `name` und `greeting` nach dem Ausführen des folgendes Codes:
   ```python
   name = "Tom"
   greeting = "Hallo, " + name
   name = "Emma"
   ```
12. Was denkst du passiert, wenn du`print(4 * "Hallo ")` ausführst? Probier es aus!
13. Was passiert, bei `print(4 + "Hallo")`? Probiere es aus!
14. Schreibe ein Programm, welches eine Zahl als Eingabe erwartet, diese verdoppelt und dann ausgibt.
'''

# %
x = 5
x = x + 2
print(x)

# %



