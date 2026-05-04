# Lösungen

<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/hKgXvQlLJlg?si=uZcmj-HEavDQpWNT" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

### Tupel erstellen
```python
fruechte = ("Apfel", "Banane", "Kirsche", "Orange", "Mango")
```
### 2. Auf Tupelelemente zugreifen
```python 
print(fruechte[1]) # Gibt 'Banane' aus
```
### 3.Tupelelemente ändern
Dies ist nicht möglich, da Tupel unveränderlich sind.
### 4. Ist das Element im Tupel?
```python
print("Apfel" in fruechte) # Gibt True aus, falls Apfel enthalten ist
```
### 5. Zählen
```python
print(fruechte.count("Banane")) # Gibt die Anzahl der 'Banane' aus
```
### 6. Umgekehrte Reihenfolge
```python
umgekehrtes_tupel = fruechte[::-1]
```
### 7. Tupel vom Tupel
```python
erste_drei = fruechte[:3]
```
### 8. Tupel kombinieren
```python
gemuese = ("Karotte", "Brokkoli", "Zwiebel")
kombiniert = fruechte + gemuese
```
### 9. Multiplikation
```python 
dreifach = fruechte * 3
```
### 10. Tupel verschachteln
```python
verschachtelt = (fruechte, gemuese)
```
### 11. Index zum Element finden
```python
print(fruechte.index("Kirsche")) # Gibt den Index von 'Kirsche' aus
```
### 12. Summe der Tupelelemente
```python
zahlen = (1, 2, 3, 4, 5)
print(sum(zahlen)) # Gibt die Summe aus, also 15
```
### 13. Sortieren
```python
sortierte_zahlen = tuple(sorted(zahlen, reverse=True))
```
### 14. Subtupel
```python
print(fruechte in verschachtelt) # Gibt True aus, falls fruechte ein Subtupel ist
```
### 15. Reingelegt
Dies druckt jedes String-Element im Tupel in Großbuchstaben aus.

### 16. Entpacken
Was ist in den folgenden Fällen die Konsolenausgabe?

```python
a, *b, c = ('first', 'second', 'third', 'forth')
print(a) # first
print(b) # ['second', 'third']
print(c) # third
print(type(a)) # <class 'str'>
print(type(b)) # <class 'list'>
print(type(c)) # <class 'str'>
```

### 17. Entpacken bei Listen
Die Konsolenausgabe ist exakt gleich wie in Aufgabe 16.

### 18. Alles entpackbar?
```python
my_tuple = ('first', 'second', 'third', 'forth', 'fifth')
a, b, c, d, e = my_tuple

f, *g = my_tuple # ok

*h, i = my_tuple # ok

k, *l, m, *n = my_tuple # SyntaxError: multiple starred expressions in assignment

p, q, *r = my_tuple # ok

*s, *t = my_tuple # SyntaxError: multiple starred expressions in assignment

u, v = my_tuple[:2] # ok
```

