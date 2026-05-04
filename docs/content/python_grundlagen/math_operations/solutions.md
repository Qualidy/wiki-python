# Lösungen
### 1. **Addition**:
`print(5 + 3)  # 8`
### 2. **Subtraktion**: 
`print(10 - 2)  # 8`
### 3. **Multiplikation**:
`print(4 * 2)  # 8`
### 4. **Division**:
`print(16 / 2)  # 8.0`
### 5. **Ganzzahlige Division**:
`print(17 // 2)  # 8`
### 6. **Modulo**: 
`print(18 % 10)  # 8`
### 7. **Potenzierung**:
`print(2 ** 3)  # 8`
### 8. **Quadratwurzel**: 
`import math; print(math.sqrt(64))  # 8.0`
### 9. **Exponentialfunktion**: 
`import math; print(math.exp(3))  # etwa 20.085`
### 10. **Natürlicher Logarithmus**:
`import math; print(math.log(8, math.e))  # etwa 2.079`

### 11. **Komplexe Rechnung**:
`print((3 + 4) * 5)  # 35`
### 12. **Vergleich**: 
`print(2 * 3 == 6)  # True`
### 13. **Runden**: 
`print(round(2.7))  # 3`
### 14. **Negative Zahlen**: 
`print(-3 * 3)  # -9`
### 15. **Variable in Rechnung**: 
`x = 5; print(x * x)  # 25`
### 16. **Verschiedene Operationen**: 
`print(2 + 3 * 5)  # 17, da die Multiplikation zuerst ausgeführt wird`
### 17. **Einsatz von Klammern**: 
`print((2 + 3) * 5)  # 25, da die Klammer zuerst ausgewertet wird`
### 18. **Potenzierung und Division**: 
`print(4 ** 2 / 8)  # 2.0, da zuerst potenziert und dann dividiert wird`
### 19. **Mehrere Operationen**: 
`print(3 + 4 * 2 - 1)  # 10, da Multiplikation vor Addition und Subtraktion ausgeführt wird`
### 20. **Komplexer Ausdruck**: 
`print((3 + 4) * (5 - 2) ** 2)  # 49, da zuerst die Klammern, dann die Potenzierung und zuletzt die Multiplikation ausgeführt wird`

### **Zinsrechner**
```python
# Benutzereingaben
anfangskapital = float(input("Gib das Anfangskapital ein: "))
zinssatz = float(input("Gib den Zinssatz in Prozent ein: "))
jahre = float(input("Gib die Anlagedauer in Jahren ein: "))

# Berechnung der Endsumme
endsumme = anfangskapital * (1 + zinssatz/100 * jahre)

# Ausgabe
print(f"Die Endsumme nach {jahre} Jahren beträgt: {endsumme:.2f} Euro")

```

### **Umrechner für Temperaturen**

```python
# Benutzereingaben
temperatur = float(input("Gib die Temperatur ein: "))
einheit = input("Ist die Temperatur in Celsius (C) oder Fahrenheit (F)? ")

# Umrechnung
if einheit.lower() == 'c':
    umgerechnet = temperatur * 9/5 + 32
    zieleinheit = "Fahrenheit"
elif einheit.lower() == 'f':
    umgerechnet = (temperatur - 32) * 5/9
    zieleinheit = "Celsius"

# Ausgabe
print(f"Die Temperatur in {zieleinheit} beträgt: {umgerechnet:.2f}°")

```