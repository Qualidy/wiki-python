# Generatoren und Iteratoren

In Python können wir viele Intanzen mit Hilfe der for-Schleife iterieren. 
Zu diesen gehören:

- lists
- tuples
- dictionaries
- strings
- files
- etc...

All diese Klassen haben eins gemeinsam, sie implementieren die Methode
`__iter__()`, welche einen Iterator liefert und
so erlaubt die intern gespeicherten Elemente zu durchlaufen.

## Iteratoren

Klassen, die die Methode `__iter__()` implementieren werden als "iterable"
bezeichnet. `__iter__()` liefert einen Iterator zurück.
Dies ist ein eigenes Objekt, welches nur dafür zuständig ist, die Elemente der
ursprünglichen Instanz zu durchlaufen. Übrigens können wir statt 
`my_list.__iter__()` auch `iter(my_list)` schreiben.

Sobald wir den Iterator haben, können wir die Elemente durch den Funktionsaufruf
`next()` erhalten. Wenn es keine Elemente mehr gibt, kommt es zu einem
`StopIterationError`. Das kann z.B. so aussehen:

```python
nums = [3, 2, 8]

nums_iterator = nums.__iter__()  # auch iter(nums)

print(next(nums_iterator))  # 3
print(next(nums_iterator))  # 2
print(next(nums_iterator))  # 8
print(next(nums_iterator))  # StopIteration
```

**Was macht die For Loop im background?**

Ein for loop ruft `__iter__()` auf und gibt einen Iterator aus.
Dann werden die Elemente mithilfe von `next()` druchlaufen, bis
`StopIteration` aufgefangen wird.

Der folgende Code ist also identisch zur darauf folgenden `for`-Schleife:

```python
nums = [3, 2, 8]

nums_iterator = iter(nums)
while True:
    try:
        item = next(nums_iterator)
        print(item)
    except StopIteration:
        break
```

Und kurz als Schleife:

```python
for item in [3, 2, 8]:
    print(item)
```

**Was macht etwas zu einem Iterator?**

Ein Objekt, dass die Methode `__next__()` implementiert.

Unsere Liste selbst ist also kein Iterator. Prüfe dazu alle Methoden einer
Liste mit `dir([])`.

## Beispiel eines Iterators

Im Folgenden wollen wir einen Iterator bauen, der eine gewisse Anzahl an 
Zufallszahlen liefert:

```python
from random import randint


class RandomNumberGenerator:
    def __init__(self, start=0, end=100, maximum_numbers=10):
        self.start = start
        self.end = end
        self.maximum_numbers = maximum_numbers
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count > self.maximum_numbers:
            raise StopIteration
        return randint(self.start, self.end)
```

Wir können diesen nun Code nun wie folgt ausführen:

```python
rng = RandomNumberGenerator()

for random_number in rng:
    print(random_number)
```

### Aufgabe: Ersten Iterator verstehen🌶🌶
Mache dich mit dem oberen Beispiel vertraut. 

Was passiert, wenn die Funktion `__iter__()` nicht definiert wird?

<details>
<summary>Lösung</summary>
Die Instanz kann erstellt werden, aber sie kann nicht mehr in die for-Schleife
eingesetzt werden. Es kann jedoch nocht händisch die <code>next</code> Funktion
aufgerufen werden.
</details>

Was passiert, wenn keine `StopIteration` geworfen wird?

<details>
<summary>Lösung</summary>
Es werden unendlich viele Zufallszaheln generiert.
</details>


## Generatoren mit `yield` erstellen

Um Iterator schneller zu schreiben, gibt es das Keyword `yield`.

Der folgende Code zeigt eine Funktion `infinite_numbers`. Diese
liefert einen Iterator zurück, welcher immer größere Zahlen liefert.
Und das unendlich lange. Dies geschieht, indem bei jedem Aufruf von `next(nums)`
der Methodenrumpf von `infinite_numbers` durchlaufen wird. Immer
wenn die Zeile `yield current` erreicht wird, wird das aktuelle Wert von
`current` zurückgegeben, wie bei einem `return current`. ABER: beim nächsten
Aufruf von `next(nums)` wird die Codeausführung VON DIESER STELLE aus weitergeführt,
die nächste Zeile ist also `current += 1`!

```python
def infinite_numbers(start):
    current = start
    while True:
        yield current
        current += 1


nums = infinite_numbers(5)

for num in nums:
    print(num)
```

Schaue dir die Ausführung des Codes in diesem Onlincompiler genau an:

[💻 Link zum Onlinecompiler](https://pythontutor.com/render.html#code=def%20infinite_numbers%28start%29%3A%0A%20%20%20%20current%20%3D%20start%0A%20%20%20%20while%20True%3A%0A%20%20%20%20%20%20%20%20yield%20current%0A%20%20%20%20%20%20%20%20current%20%2B%3D%201%0A%0A%0Anums%20%3D%20infinite_numbers%285%29%0A%0Afor%20num%20in%20nums%3A%0A%20%20%20%20print%28num%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

**Definition**: Funktionen, die mithilfe von `yield` einen Iterator zurückgeben, werden **Generator** genannt.

### Aufgabe: ganz klein anfgaben🌶

Was passiert im folgenden Code?

```python
def get123():
    yield 1
    yield 2
    yield 3

for x in get123():
    print(x)
```

<details>
<summary>Lösung</summary>
Der Generator wird aufgerufen und gibt einen Iterator zurück der 3 mal aufgerufen wird.
Erst wird 1, dann 2 und dann 3 zurückgegeben. Dann kommt es zu einem StopIteration und
die Schleife beendet ihren Durchlauf.
</details>

### Aufgabe: range nachbauen 🌶:
Passe das obere Beispiel an, indem du einen Parameter `end` hinzufügst.
Dieser soll dafür sorgen, dass nur so lange Zahlen ausgegeben werden sollen,
bis `end` erreicht ist.

Füge dann einen weiteren optionalen Parameter `step_size` hinzu, der angibt, wie 
groß die Schritte zwischen zwei ausgegeben Zahlen sind.

<details>
<summary>Lösung</summary>
<pre><code>def infinite_numbers(start, end, step_size=1):
    current = start
    while current < end:
        yield current
        current += step_size</code></pre>
</details>

### Aufgabe: Was kommt zurück?🌶

Welchen Rückgabetyp hat der Aufruf einer Funktion, die `yield` verwendet?

<details>
<summary>Lösung</summary>
list_iterator
</details>


### Aufgabe: Mehrere Iteratoren🌶🌶
Führe den folgenden Code aus und erkläre was passiert:

```python
inf1 = infinite_nubmers(1)
inf2 = infinite_nubmers(1)

print(next(inf1))
print(next(inf1))
print(next(inf2))
print(next(inf1))
print(next(inf2))
```

<details>
<summary>Lösung</summary>
<pre><code>inf1 = infinite_nubmers(1)
inf2 = infinite_nubmers(1)

print(next(inf1)) # 1
print(next(inf1)) # 2
print(next(inf2)) # 1
print(next(inf1)) # 3
print(next(inf2)) # 2</code></pre>

Es werden bei jedem Aufruf von <code>infinite_numbers</code> ein neuer
Generator erstellt. Diese werden hier unabhängig voneinander durchlaufen.
</details>


### Aufgabe Quadratzahlengenerator 🌶

Erstelle einen Generator, der die Quadratzahlen von Zahlen bis zu einer Zahl N 
erstellt.

<details>
<summary>Lösung</summary>
<pre><code>
def square_numbers(n):
    for i in range(1, n + 1):
        yield i * i</code></pre>
</details>


### Aufgabe Primzahlengenerator🌶🌶

Erstelle einen Generator, der die Primzahlen von Zahlen bis zu einer Zahl N erstellt.

<details>
<summary>Lösung</summary>
<pre><code>def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers(n):
    for num in range(2, n + 1):
        if is_prime(num):
            yield num</code></pre>
</details>


### Aufgabe Zufallsreihenfolgengenerator🌶🌶

Erstelle eine Generator, um die Elemente einer Liste, Strings usw. in
zufälliger Reihenfolge durchzugehen. Jedes Element soll aber nur ein mal 
durchlaufen werden.

<details>
<summary>Lösung für Faule</summary>
<pre><code>from random import sample

def random_order(container):
    return iter(sample(container, len(container))</code></pre>
</details>

### Aufgabe: Noch mehr Zufälle... 🌶🌶

Erstelle eine Generator, um die `n` zufällige Elemente einer Liste, Strings usw.
zurückgibt. Sie soll ggf. auch Elemente mehrfach zurückgeben.

<details>
<summary>Lösung für Faule</summary>
<pre><code>from random import choice

def get_random_elements(container, n):
    for _ in range(n):
        yield choice(container)</code></pre>
</details>

### Aufgabe: Irgenwann ist auch gut mit dem Zufall 🌶🌶

Erstelle einen Generator, der Zufallszahlen von 1 bis 10 zurückgibt, bis die 10 ausgegeben wird..

<details>
<summary>Lösung für Faule</summary>
<pre><code>def get_randoms_till_10():
    current = 0
    while current != 10:
        current = randint(1, 10)
        yield current

for x in get_randoms_till_10():
    print(x)
</code></pre>
</details>



### Aufgabe: Generator Comprehension 🌶

Kannst du erklären, was `gencomp` im Code unten ist? 
(Hinweis: wir haben das nie in unseren Lektionen gelernt.

```python
meine_liste = [1,2,3,4,5]

gencomp = (item for item in meine_liste if item > 3)

for item in gencomp:
    print(item)
```

Hinweis: "generator comprehension" suchen...

<details>
<summary>Lösung</summary>
Eine "generator comprehension" ist ähnlich wie eine Listen- 
oder Set-Comprehension, aber anstelle einer Liste oder eines Sets erstellt 
sie einen Generator, der Elemente nacheinander liefert.

Eine generator comprehension wird in runden Klammern ( ) geschrieben, 
im Gegensatz zu eckigen Klammern [ ] für Listen-Comprehensions oder
geschweiften Klammern { } für Set- und Dictionary-Comprehensions.

<b>Vorteile:</b>

<b>Speicheroptimierung:</b> Ein Generator erzeugt seine Werte "on the fly" und 
speichert nicht alle Elemente im Speicher. Das macht sie besonders nützlich, 
wenn die Sequenz groß ist oder unendliche Folgen erzeugt werden.

<b>Lazy Evaluation:</b> Ein Generator berechnet und liefert seine Werte erst,
wenn sie angefordert werden, im Gegensatz zu Listen,
die sofort alle Elemente berechnen und speichern.
</details>


### Aufgabe: Sudoku

Gegeben sei der folgende BasisCode für eine Sudokuklasse:

```python
class Sudoku:
    def __init__(self, grid=None):
        if grid is None:
            self.grid = [[0 for _ in range(9)] for _ in range(9)]
        else:
            if len(grid) == 9 and all(len(row) == 9 for row in grid):
                self.grid = grid
            else:
                raise ValueError("Das Grid muss eine 9x9-Matrix sein.")

    def __str__(self):
        rows = []
        for i, row in enumerate(self.grid):
            if i % 3 == 0 and i != 0:
                rows.append("-" * 21)
            rows.append(" ".join(str(num) if num != 0 else '.' for num in row[0:3]) + " | " +
                        " ".join(str(num) if num != 0 else '.' for num in row[3:6]) + " | " +
                        " ".join(str(num) if num != 0 else '.' for num in row[6:9]))
        return "\n".join(rows)


test_grid = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

sudoku = Sudoku(test_grid)

print(sudoku)
```
Ziel dieser Aufgabe ist eine Methode `is_valid` zu entwickeln, 
die prüft, ob das Sudoku korrekt gefüllt ist. Es geht *nicht* darum einen Löser
zu entwickeln.

Was ein Sudoku ist und wie man es löst, kannst du [hier nachlesen](https://sudoku.com/de/wie-man-spielt/sudoku-regeln-fur-komplette-anfanger/).

Erstelle dafür zunächst die folgenden Generatoren:

`get_rows` liefert die Zeilen des Sudoku.

<details>
<summary>Lösung</summary>
<pre><code>
    def get_rows(self):
        for row in self.grid:
            yield row</code></pre>
</details>

`get_columns` liefert die Zeilen des Sudoku.

<details>
<summary>Lösung</summary>
<pre><code>
def get_columns(self):
        for col in range(9):
            yield [self.grid[row][col] for row in range(9)]</code></pre>
</details>

`get_squares` liefert die Quadrate des Sudoku.

<details>
<summary>🍀Tipp: Code zum Berechnen der Quadrate</summary>
<pre><code>
    for box_row in range(3):
        for box_col in range(3):
            square = []
            for row in range(box_row * 3, (box_row + 1) * 3):
                for col in range(box_col * 3, (box_col + 1) * 3):
                    square.append(self.grid[row][col])</code></pre>
</details>

<details>
<summary>Lösung</summary>
<pre><code>
    def get_squares(self):
        for box_row in range(3):
            for box_col in range(3):
                square = []
                for row in range(box_row * 3, (box_row + 1) * 3):
                    for col in range(box_col * 3, (box_col + 1) * 3):
                        square.append(self.grid[row][col])
                yield square</code></pre>
</details>

Erstelle nun `__iter__()` innerhalb von `Sudoku`, welches alle
drei Generatoren nacheinander durchführt. Recherchiere hierfür nach `yield from`.

<details>
<summary>Lösung</summary>
<pre><code>
    def __iter__(self):
        yield from self.get_rows()
        yield from self.get_columns()
        yield from self.get_squares()</code></pre>
</details>

Erstelle nun ein eine Methode `is_valid(self)` in `Sudoko`, die prüft,
ob das Sudoko valide ist. Iteriere dabei direkt über `self`.

<details>
<summary>Lösung</summary>
<pre><code>
    def is_valid(self):
        return all(set(sorted(group)) == set(range(1, 10)) for group in self)</code></pre>
</details>

<details>
<summary>🤯Gesamte Lösung</summary>
<pre><code>class Sudoku:
    def __init__(self, grid=None):
        if grid is None:
            self.grid = [[0 for _ in range(9)] for _ in range(9)]
        else:
            if len(grid) == 9 and all(len(row) == 9 for row in grid):
                self.grid = grid
            else:
                raise ValueError("Das Grid muss eine 9x9-Matrix sein.")

    def __str__(self):
        rows = []
        for i, row in enumerate(self.grid):
            if i % 3 == 0 and i != 0:
                rows.append("-" * 21)
            rows.append(" ".join(str(num) if num != 0 else '.' for num in row[0:3]) + " | " +
                        " ".join(str(num) if num != 0 else '.' for num in row[3:6]) + " | " +
                        " ".join(str(num) if num != 0 else '.' for num in row[6:9]))
        return "\n".join(rows)

    def get_rows(self):
        for row in self.grid:
            yield row

    def get_columns(self):
        for col in range(9):
            yield [self.grid[row][col] for row in range(9)]

    def get_squares(self):
        for box_row in range(3):
            for box_col in range(3):
                square = []
                for row in range(box_row * 3, (box_row + 1) * 3):
                    for col in range(box_col * 3, (box_col + 1) * 3):
                        square.append(self.grid[row][col])
                yield square

    def __iter__(self):
        yield from self.get_rows()
        yield from self.get_columns()
        yield from self.get_squares()

    def is_valid(self):
        return all(set(sorted(group)) == set(range(1, 10)) for group in self)

test_grid = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

sudoku = Sudoku(test_grid)

print(sudoku)

print("\nIst das Sudoku korrekt?")
print(sudoku.is_valid())
</code></pre>
</details>
