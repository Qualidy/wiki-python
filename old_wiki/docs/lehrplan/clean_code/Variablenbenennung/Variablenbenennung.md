# Variablenbenennung
[15min]

Die Benennung von Variablen in Python sollte den Richtlinien des [PEP8 zu Funktions- und Variablennamen](https://peps.python.org/pep-0008/#function-and-variable-names) folgen. Allgemein werden Variablen in Python in Kleinbuchstaben geschrieben. Wörter werden durch Unterstriche getrennt (snake_case).

**Ausnahmen:**

* In Python gibt es keine Konstanten. Konstanten werden in Großbuchstaben geschrieben. Dies ist jedoch nur eine Konvention und wird von Python nicht überprüft.
* Klassen werden in CamelCase geschrieben. Dies ist jedoch nur eine Konvention und wird von Python nicht überprüft.

**Nice to know:**

In bestehenden Paketen finden wir gelegentlich auch andere Schreibweisen. So werden z.B. in Pandas Variablen in CamelCase geschrieben. Dies ist jedoch nicht empfohlen und sollten in eigenen Projekten vermieden werden.

## Beispiel
[10 min]

Gegeben ist der folgende Code:
```python
def func(a, b, c, d):
    x = a + b
    y = c * d
    z = x - y
    return z
```
Dieser Code subtrahiert die Multiplikation von `c` und `d` von der Addition von `a` und `b`. Die Variable `z` enthält also das Ergebnis dieser Rechnung. Die Namensgebung dieser Funktion ist unvorteilhaft, da sie in anderen Teilen des Codes nicht mehr verständlich ist. Eine bessere Namensgebung wäre:

```python
def calculate_difference_of(primary_summand, secondary_summand, primary_factor, secondary_factor):
    primary_sum = primary_summand + secondary_summand
    secondary_sum = primary_factor * secondary_factor
    difference = primary_sum - secondary_sum
    return difference
```

### Aufgabe 1: Variablenumbenennug 🌶️🌶️
[15 min]

Gegeben ist ein Code-Ausschnitt, welcher den Warenwert eines Einkaufskorbes bereichnet. Leider hat der Entwicker wenig Wert auf die Namenskonventionen gelegt. Benennen Sie die Variablen entsprechend der Konventionen um und führen sie sprechende Variablennamen ein.

```python
a = [3, 5, 2]  
p = [10.99, 5.99, 7.49]  


def s(e, p):
    c = 0
    for i in range(len(e)):
        c += e[i] * p[i]
    return c


# warenKorbWertBerechnen
c = s(a, p)

# ausgabeWarenwert
print("Warenwert: $" + str(c))
```

[Lösung](solution.md#lsung-aufgabe-1)

### Aufgabe 2: Verbesserung der Variablennamen 🌶️🌶️🌶️
[30 min]

In diesem Python-Code für Tic Tac Toe sind einige Variablennamen zu kurz oder nicht intuitiv. Deine Aufgabe ist es, die Variablennamen so zu ändern, dass sie lesbarer und verständlicher werden. Hier sind einige Vorschläge, worauf du dich konzentrieren kannst:

* Funktion prntBrd(b): Benenne die Funktion und ihre Parameter um, um klarzustellen, dass sie das Spielfeld ausdruckt.
* Funktion chckWin(b, m): Ändere den Namen der Funktion und ihrer Parameter, um ihre Funktion, das Überprüfen eines Gewinns, besser zu reflektieren.
* Variablen innerhalb der Funktionen: Überarbeite Variablennamen wie `b`, `r`, `c`, `m`, `brd` und `curP`, um ihre Bedeutung klarer zu machen.
* Allgemeine Lesbarkeit: Überprüfe den Code auf allgemeine Lesbarkeit und Verständlichkeit und nimm entsprechende Änderungen vor. Denke daran, dass gute Variablennamen leicht zu verstehen sind und den Zweck oder den Wert, den sie repräsentieren, klar kommunizieren.

```python
def prntBrd(b):
    for r in b:
        print(" | ".join(r))
        print("-" * 9)

def chckWin(b, m):
    for r in range(3):
        if b[r][0] == b[r][1] == b[r][2] == m: return True
    for c in range(3):
        if b[0][c] == b[1][c] == b[2][c] == m: return True
    if b[0][0] == b[1][1] == b[2][2] == m: return True
    if b[0][2] == b[1][1] == b[2][0] == m: return True
    return False

def game():
    brd = [[" " for _ in range(3)] for _ in range(3)]
    curP = "X"
    while True:
        prntBrd(brd)
        r, c = map(int, input(f"Player {curP}, enter row and column (0-2): ").split())
        if brd[r][c] == " ":
            brd[r][c] = curP
            if chckWin(brd, curP):
                print(f"Player {curP} wins!")
                break
            curP = "X" if curP == "O" else "O"
        else:
            print("Invalid move, try again.")
    prntBrd(brd)

game()
```

[Lösung](solution.md#lsung-aufgabe-2)

Private, protected und public Variablen
[20 min]

In Python gibt es keine Möglichkeit, Variablen als private oder protected zu deklarieren. Es gibt jedoch eine Konvention, wie private Variablen benannt werden sollten. Private Variablen beginnen mit einem Unterstrich. Protected Variablen beginnen mit zwei Unterstrichen. Public Variablen haben keinen Unterstrich am Anfang. Diese Benamungen kommen vor allem in Klassen zum Einsatz.

| Sichtbarkeit | Schlüsselwort in Python                | Beispiel in Python | Zugriff                                       |
|--------------|----------------------------------------|--------------------|-----------------------------------------------|
| Private      | `__` (vorangehender Doppelunterstrich) | `__variable_name`  | Nur innerhalb der Klasse sichtbar             |
| Geschützt    | `_` (vorangehender Unterstrich)        | `_variable_name`   | Innerhalb der Klasse und abgeleiteten Klassen |
| Öffentlich   | Kein spezielles Schlüsselwort          | `variable_name`    | Von Überall                                   |

Geschützte Variablen sind nur für die Verwendung in der Klasse gedachte. Sie können jedoch von abgeleiteten Klassen verwendet werden. Private Variablen sind nur für die Verwendung in der Klasse gedacht und können nicht von abgeleiteten Klassen verwendet werden. Öffentliche Variablen können überall verwendet werden. Zu beachten ist, dass private Variablen in Python nur durch Konvention private sind. Sie können trotzdem von außen verwendet werden. Geschützte (protected) Variablen hingegen sind nicht direkt von außen abrufbar.
