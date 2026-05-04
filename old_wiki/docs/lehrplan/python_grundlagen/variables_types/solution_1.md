# Lösung

## Floats, Integers, Booleans



### 1. **Integer Addition**

```python
print(3 + 5)
```

### 2. **Integer Subtraktion**

```python
print(10 - 4)
```

### 3. **Float Division**

```python
print(7.5 / 2.5)
```

### 4. **Multiplikation von Integers**

```python
print(6 * 8)
```

### 5. **Konvertierung von Float zu Integer**

```python
print(int(7.8))
```

### 6. **Vergleich von Integers**

```python
print(5 > 3)
```

### 7. **Booleansches AND**

```python
print(True and False)
```

### 8. **Booleansches OR**

```python
print(False or True)
```

### 9. **Umwandlung von Integer in Boolean**

```python
print(bool(0))  # False
print(bool(5))  # True
```

### 10. **Modulo-Operator mit Integers**

```python
print(10 % 3)
```

### 11. **Potenzierung von Floats**

```python
print(5.5 ** 3)
```

### 12. **Vergleich von Floats**

```python
print(5.5 == 5.5)
```

### 13. **Integer in Float konvertieren**

```python
print(float(7))
```

### 14. **Negation eines Booleans**

```python
print(not True)
```

### 15. **Kombination von Booleans und Integers**

```python
num = 5
print(num > 0)
```

### 16. **Diskussion**:

**Integer**: Wenn es nur ganze Zahlen Sinn ergeben, z.B. Alter, Geburtsjahr

**Floats**: Wenn auch Bruchteile relevant sind, z.B. Gewicht

### 17. **Diskussion**:
Nein, Fließkommazahlen haben keine unendlich hohe Genauigkeit. Für viele Anwendungen reicht dies aus, aber
inbesondere
wenn sehr viele Berechnungen durchgeführt werden, können diese Ungenauigkeiten zu signifikanten Abweichungen führen.
Deswegen verwendet man zum Beispiel für Geldbeträge auch immer Integer und nutzt die kleines WÄhrungseinheit. Erst
zur
Ausgabe wird umgerechnet.
