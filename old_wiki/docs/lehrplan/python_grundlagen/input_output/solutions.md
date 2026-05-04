
# Lösungen

### 1. **Einfache Ausgabe**: 
```python
print("Hallo Welt")
```
### 2. **Variable ausgeben**: 
```python
text = "Python"; print(text)
```
### 3. **Zahlen ausgeben**: 
```python
print(100)
```
### 4. **Mehrere Argumente**: 
```python
print("Hallo", "Welt")
```
### 5. **Zeilenende ändern**: 
```python
print("Hallo!", end="")
```
### 6. **Eingabeaufforderung**: 
```python
name = input("Wie heißt du? ")
```
### 7. **Begrüßung**:
```python
name = input("Wie heißt du? ")
print(f"Hallo, {name}!")
```
### 8. **Numerische Eingabe**: 
```python
alter = int(input("Wie alt bist du? "))
print(alter)
```
### 9. **Kombinierte Eingabe und Ausgabe**:
```python
essen = input("Was ist dein Lieblingsessen? ")
print(f"Ich mag auch {essen}!")
```
### 10. **Formatierte Ausgabe**:
```python
name = input("Wie heißt du? ")
alter = input("Wie alt bist du? ")
print(f"Name: {name}, Alter: {alter}")
```
### 11. **Mehrere Eingaben**:
```python
vorname = input("Vorname: ")
nachname = input("Nachname: ")
print(f"Vollständiger Name: {vorname} {nachname}")
```
### 12. **Rechnung mit Eingabe**:
```python
zahl1 = int(input("Erste Zahl: "))
zahl2 = int(input("Zweite Zahl: "))
print(f"Ergebnis: {zahl1 + zahl2}")
```
### 13. **Fehlerkorrektur**:
```python
try: 
    zahl = int(input("Gib eine Zahl ein: "))
    print(zahl) 
except ValueError: 
    print("Das war keine gültige Zahl!")
```
### 14. **Eingabe in Liste speichern**:
```python
farben = [input("Erste Farbe: "), input("Zweite Farbe: "), input("Dritte Farbe: ")]
print(farben)
```
### 15. **Benutzereingaben vergleichen**: 
```python 
passwort1 = input("Passwort: ")
passwort2 = input("Passwort wiederholen: ")
if passwort1 == passwort2:
    print("Erfolg")
else:
    print("Die Passwörter stimmen nicht überein!")
```

# Komplex-Aufgabe

### **Persönliche Statistik**

```python
# Eingabe der persönlichen Informationen
name = input("Gib deinen Namen ein: ")
alter = int(input("Gib dein Alter ein: "))
groesse = float(input("Gib deine Größe in Metern ein (z.B. 1.75): "))
lieblingsfarben = input("Gib deine Lieblingsfarben ein, getrennt durch Kommas: ").split(',')

# Berechnung der Anzahl der Lieblingsfarben
anzahl_farben = len(lieblingsfarben)

# Ausgabe der Informationen
print("\n--- Persönliche Statistiken ---")
print(f"Name: {name}")
print(f"Alter: {alter} Jahre")
print(f"Größe: {groesse} Meter")
print(f"Anzahl der Lieblingsfarben: {anzahl_farben}")
print(f"Lieblingsfarben: {', '.join(lieblingsfarben)}")
```