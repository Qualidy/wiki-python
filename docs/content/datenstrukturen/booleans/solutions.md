### Aufgabe: Mathe, hier?!

```python
if not x > 5 and not y < 10:
    ...

# oder noch besser:

if x <= 5 and y >= 10:
    ...
```

### Aufgabe: Was ist eigentlich noch wahr heut zu Tage?

{{ youtube_video("https://www.youtube.com/embed/YCJ8sEm6JaU?si=eVkgPu459ywplJaP") }}

```python
a = [] # False
b = [1] # True
c = set() # False
d = {1,2,1} # True
e = 0 # False
f = 1 # True
g = -1 # True
h = 0.0 # False
i = 1.0 # True
j = -1.0 # True
k = "" # False
l = " " # True
m = "hallo" # True
n = None # False
```

### Aufgabe: Bedingungen kürzen

{{ youtube_video("https://www.youtube.com/embed/R1BGjaviHbc?si=iSW6y1BEFb1UIs_V") }}

Kürze den folgenden Code in den if-Bedingungen.

```python
zahl = ...

if not zahl % 2: 
    print("Die Zahl ist gerade.") 
else:   
    print("Die Zahl ist ungerade.")
```

```python
value = ...

if value: 
    print("Case 1") 
else:   
    print("Case 2")
```

```python
value = ...
my_list = ...

if not value and my_list: 
    print("Case 1") 
else:   
    print("Case 2")
```

```python
def func(var):
    return var > 5
```

### Aufgabe: Es steckt mehr dahinter

{{ youtube_video("https://www.youtube.com/embed/8DB1M9Q-vOk?si=LIsZbCJMVJnRdaQC") }}

```python
print(True + 3) # 4

print(True + True) # 2
print(True + True + True) # 3
print(True * True) # 1
print(True * False) # 0

print(True - True) # 0

print(True and False) # False
print(True or False) # True

print(0 and 1) # 0
print(1 and 2) # 2
print(2 and 1) # 1

print(0 or 1) # 
print([] or [1, 2, 3])
print(2 or 10)
print([1, 2, 3] or [4, 5, 6])
```
**Wie werden dei Booleans `True` und `False` bei `*`, `+`, `-` interpretiert?**

Booleans werden bei mathematische Operationen zu Integern übersetzt.
`True` zu `1` und `False` zu `0`.

**Wie funktioniert `and`?**

Wenn das erste Argument zu `True` auswertet, dann wird das zweite Argument
zurückgegeben, sonst das erste. `and` entspricht also folgendem Code:

```python
def my_and(a, b):
    if a:
        return b
    else:
        return a
```

**Wie funktioniert `and`?** Wenn das erste Argument zu `True` auswertet,
dann wird das zweite Argument zurückgegeben, sonst das erste.
`or` entspricht also folgendem Code:

```python
def my_or(a, b):
    if a:
        return a
    else:
        return b
```

### Aufgabe: kurz und knapp

```python
result = []
for i in ["Hallo", 3, " ", 0.0]:
    result.append(i if isinstance(i, str) else "no str")

print(result) # ["Hallo", "no str", " ", "no str"]
```

### Aufgabe: Versternt🌶🌶🌶
Schreibe eine Funktion `star_text(text, m, symbol)`, die einen Text enthält.
Es sollen alle Wörter mit einem symbol ersetzt werden,
die `m` oder weniger Zeichen sind.
Die Anzahl der Symbole soll der ursprünglichen Wortlänge entsprechen.
Wenn `m` und `symbol` nicht angegeben sind, soll `m=4` und `symbol='*'` gelten.
Es soll eine Liste einzelner Wörter zurückgegeben werden.

```python
my_text = "Python macht Spaß und wer das nicht glaubt der programmiert wohl Java oder C++"

def star_text(text, m=4, symbol='*'):
    result = []
    for word in text.split():
        result.append(len(word) * symbol if len(word) < m else word)
    return result

print(star_text(my_text))
# ['Python', 'macht', 'Spaß', '***', '***', '***', 'nicht', 'glaubt', '***', 'programmiert', 'wohl', 'Java', 'oder', '***']
```
