# Lösungen 
### 1. **Elemente zu Set hinzufügen**

```python
s = {1, 2, 3}
s.update([4, 5, 6])
```

### 2. **Schlüssel-Wert-Paare in Dictionary**

```python
dictionary = {"a": 1, "b": 2, "c": 3}
```

### 3. **Element aus Set entfernen**

```python
s.remove(4)  # Entfernt die Zahl 4 aus dem Set
```

### 4. **Werte aus Dictionary abrufen**

```python
wert = dictionary["b"]
```

### 5. **Dictionary Werte ändern**

```python
dictionary["c"] = 4
```

### 6. **Set Operationen**

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
vereinigung = set1 | set2
schnittmenge = set1 & set2
```

### 7. **Schlüssel aus Dictionary entfernen**

```python
del dictionary["a"]
```

### 8. **Duplikate aus Liste entfernen**

```python
liste_ohne_duplikate = list(set([1, 2, 2, 3, 3, 4, 4, 5]))
```
