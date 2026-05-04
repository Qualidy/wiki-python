# Lösung

## Lists, Tupels, Sets, Dictionaries


### 1. **Liste erstellen**

```python
liste = [1,2,3,4,5,6,7,8,9,10]
# or
liste = [i for i in range(1, 11)]
```

### 2. **Tupel zu Liste**

```python
tupel = (1, 2, 3)
liste = list(tupel)
```


### 3. **Liste invertieren**

```python
liste = liste[::-1]
```

### 4. **Tupel aus Listen**

```python
tupel = tuple(liste[:3])
```


### 5.. **Liste von Tupeln**

```python
liste_von_tupeln = [(i, i ** 2) for i in range(1, 6)]
```

### 6. **Listenelemente filtern**

```python
gerade_zahlen = [i for i in liste if i % 2 == 0]
```

### 7. **Element in Tupel überprüfen**

```python
3 in gerade_zahlen
```
