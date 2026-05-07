# Lösungen

### Aufgabe: Benutzernamen🌶🌶
{{ youtube_video("https://www.youtube.com/embed/eDZBJG3_Jec?si=zVdbTua2zIKLV5La") }}

```python
# Eingabe eines Benutzernamens
benutzername = input("Bitte geben Sie Ihren Benutzernamen ein: ")

# Überprüfung der Länge des Benutzernamens
if len(benutzername) > 10:
    print("Der Benutzername ist zu lang.")
elif len(benutzername) < 3:
    print("Der Benutzername ist zu kurz.")
else:
    print(f"Willkommen, {benutzername}!")

# Überprüfung auf Großschreibung
if benutzername.isupper():
    print("Ihr Benutzername ist vollständig in Großbuchstaben geschrieben.")
elif benutzername.islower():
    print("Ihr Benutzername ist vollständig in Kleinbuchstaben geschrieben.")
else:
    print("Ihr Benutzername enthält sowohl Groß- als auch Kleinbuchstaben.")

# Überprüfung auf das Vorhandensein eines bestimmten Zeichens
if "!" in benutzername:
    print("Ihr Benutzername enthält ein Ausrufezeichen!")

# Konvertierung des Benutzernamens in Kleinbuchstaben
kleinbuchstaben_benutzername = benutzername.lower()
print(f"Ihr Benutzername in Kleinbuchstaben: {kleinbuchstaben_benutzername}")
```

1. Die Länge des Benutzernamens wird überprüft, und je nach Länge werden verschiedene Meldungen ausgegeben.

2. Es wird überprüft, ob der Benutzername ausschließlich aus Groß- oder Kleinbuchstaben besteht, und entsprechende
   Meldungen werden ausgegeben.

3. Es wird überprüft, ob ein Ausrufezeichen im Benutzernamen vorhanden ist, und eine Meldung wird ausgegeben, wenn dies
   der Fall ist.

4. Schließlich wird der Benutzername in Kleinbuchstaben konvertiert und angezeigt.

{{ youtube_video("https://www.youtube.com/embed/XTU_6zn-K4g?si=PoDSHzST5JCvfKum") }}

### 1. Länge eines Strings ermitteln:

```python
text = "Dies ist ein Beispiel"
print(f"Länge des Strings: {len(text)}")
```

### 2. String rückwärts ausgeben:

```python
text = "Python"
print(text[::-1])
```

### 3. String in Großbuchstaben konvertieren:

```python
text = "python"
print(text.upper())
```

### 4. Anzahl der Vokale zählen: 
Erstelle einen String und zähle die Anzahl der Vokale in ihm.

```python
text = "Ich bin ein Star, holt mich hier raus!"
text = text.lower()
vocals = text.count("a") + text.count("e") + text.count("i") + text.count("o") + text.count("u")
print(f"Vokale in {text}: {vocals}")
```

### 5. Erster und letzter Buchstabe eines Strings:

```python
text = "Python"
print(f"Erster Buchstabe: {text[0]}, Letzter Buchstabe: {text[-1]}")
```

### 6. Zeichen ersetzen:

```python
text = "Python ist großartig."
neuer_text = text.replace("groß", "super")
print(neuer_text)
```

### 7. Leerzeichen entfernen:

```python
text = " Text mit Leerzeichen "
ohne_leerzeichen = text.strip()
print(ohne_leerzeichen)
```

### 8. String in Wörter aufteilen:

```python
text = "Dies ist ein Satz."
woerter = text.split()
print(woerter)
```

### 9. Überprüfung, ob ein String nur aus Zahlen besteht:

```python
text = "12345"
if text.isdigit():
   print("Der String besteht nur aus Zahlen.")
else:
   print("Der String enthält andere Zeichen als Zahlen.")
```

### 10. Funktion zur Überprüfung von Anagrammen:

```python
s1, s2 = "listen", "silent" 
if sorted(s1.lower()) == sorted(s2.lower()):
    print(f"{s1} ist Anagramm von {s2}")
else:
    print("Kein Anagramm")
```

### 11. Anzahl der Wörter in einem String zählen:
```python
text = "Dies ist ein Beispiel Satz."
woerter = text.split()
anzahl_woerter = len(woerter)
print(f"Anzahl der Wörter: {anzahl_woerter}")
```

### 12. String in Titel-Case umwandeln:

```python
text = "python ist großartig"
titel_case = text.title()
print(titel_case)
```

### 13. Funktion für Palindrom-Überprüfung:

```python
text = 'Anna'
text = text.lower()  # Um Groß-/Kleinschreibung zu ignorieren
if text == text[::-1]:
   print(f"{text} ist ein Palindrom")
else:
   print(f"{text} ist KEIN Palindrom")
```

### 14. Vokale verboten:

```python
text = "Bastian weiß Bescheid😲"
replace_symbol = "*"
text = text.lower().replace("a", replace_symbol).replace("e", replace_symbol).replace("i", replace_symbol).replace("o", replace_symbol).replace("u", replace_symbol)
print(f"Text ohne Vokale: {text}")
```
