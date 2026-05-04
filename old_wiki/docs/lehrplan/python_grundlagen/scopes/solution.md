## Scopes

### 1. **Globale Variable**
```python
global_var = "Ich bin global"

def test_global():
   print(global_var)

test_global()
```

### 2. **Lokale Variable**
```python
def test_lokal():
   lokal_var = "Ich bin lokal"
   print(lokal_var)

test_lokal()
```

### 3. **Globale und lokale Variable mit demselben Namen**
```python
var = "Ich bin global"

def test_gleichnamig():
   var = "Ich bin lokal"
   print(var)  # Lokale Variable
   print(globals()['var'])  # Globale Variable

test_gleichnamig()
```

### 4. **Änderung einer globalen Variable innerhalb einer Funktion**
```python
global_var = "Ursprünglich global"

def test_aendern():
   global_var = "Geändert lokal"
   print(global_var)

test_aendern()
print(global_var)  # Bleibt unverändert "Ursprünglich global"
```

### 5. **Verwenden des `global`-Keywords**
```python
global_var = "Ursprünglich global"

def test_global_keyword():
   global global_var
   global_var = "Geändert global"
   print(global_var)

test_global_keyword()
print(global_var)  # Wird zu "Geändert global"
```

### 6. **Nested Functions Scope**
```python
def außen():
   außen_var = "Variable von außen"

   def innen():
       print(außen_var)

   innen()

außen()
```

### 7. **Lokale Variable in einer Schleife**
```python
def test_schleife():
   for i in range(3):
       schleifen_var = i
   print(schleifen_var)

test_schleife()
```

### 8. **Funktionsargument Scope**
```python
def test_argument(arg):
   arg = "Geändert"
   print(arg)

var = "Original"
test_argument(var)
print(var)  # Bleibt "Original"
```

### 9. **Rückgabewerte und Scope**
```python
def gib_zurueck():
   return "Rückgabewert"

global_var = gib_zurueck()
print(global_var)
```
