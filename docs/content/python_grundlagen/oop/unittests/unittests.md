# Unittest

{{ youtube_video("https://www.youtube.com/embed/hnd6Fs2L0do?si=MfhPW2wgUOiN8qel") }}

Wir haben im [Kapitel Docstring](../../docstring/docstring.md#unittests-in-der-dokumentation) gesehen,
wie man Unittests in den Docstring einbauen kann. Das ist nützlich, um sicherzustellen, dass der Nutzer
Codebeispiele besitzt und diese auch immer Funktionieren.

Eine weitere Möglichkeit Unittests zu schreiben ist mittels des Pakets `unittest`.
Der offensichtlichste Unterschied zum Modul `doctest` besteht darin, dass die
Testfälle bei dem Modul `unittest` außerhalb des eigentlichen Programmcodes definiert werden,
d.h. normalerweise in einer eigenen Datei. Der Vorteil besteht unter anderem
darin, dass die Programmdokumentation und die ausführliche Testung voneinander getrennt sind.
Der Preis dafür besteht jedoch in einem erhöhten Aufwand
für die Erstellung der Tests. Doch dieser lohnt sich.

Wir wollen nun für unser Modul `fibonacci.py` einen Test mit `unittest` erstellen.

[Link zum Onlinecompiler💻](https://pythontutor.com/render.html#code=def%20fib%28n%29%3A%0A%20%20%20%20%22%22%22%20%0A%20%20%20%20Die%20Fibonacci-Zahl%20f%C3%BCr%20die%20n-te%20%0A%20%20%20%20Generation%20wird%20iterativ%20berechnet%0A%20%20%20%20%22%22%22%0A%20%20%20%20a,%20b%20%3D%200,%201%0A%20%20%20%20for%20_%20in%20range%28n%29%3A%0A%20%20%20%20%20%20%20%20a,%20b%20%3D%20b,%20a%20%2B%20b%0A%20%20%20%20return%20a%0A%20%20%20%20%0Aprint%28fib%286%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```python
def fib(n):
    """ 
    Die Fibonacci-Zahl für die n-te 
    Generation wird iterativ berechnet
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
    
print(fib(6))
```

In einer Datei, z.B. `fibonacci_unittest.py`, müssen wir das Modul `unittest` und
das zu testende Modul, also in unserem Fall `fibonacci`, importieren.

__Hinweis:__ Es empfiehlt sich eine einheitliche Konvention innerhalb des Projekts
für die Dateinamen die Tests enthalten zu wählen.
Wird _Visual Studio Code_ verwendet so sollte für die Ausführungserkennung das Wort `test` im Dateinamen vorkommen.
Entweder `fibonacci_test.py` oder `test_fibonacci.py` abhängig davon, ob bevorzugt wird alle Testdateien im Dateibaum
nebeneinandern zu haben, oder alternativ die Testdatei neben der Codedatei, die sie testet, liegen zu haben.

Außerdem müssen wir eine Klasse mit beliebigem Namen - wir wählen in unserem Beispiel `FibonacciTest` - erstellen,
die von `unittest.TestCase` erbt. Wir werden das Konzept von Vererbung später genauer betrachtet; kurz gesagt
sorgen wir so dafür, dass unsere neue Klasse schon jede Menge Funktionen bereithält.

In dieser Klasse werden die nötigen Testfälle in Methoden definiert.
__Der Name dieser Methoden ist nicht beliebig, denn er muss mit **test** beginnen.__
In den Methoden benutzen wir die Methode `assertEqual` der Klasse
`TestCase`. `assertEqual(first, second, msg = None)` prüft, ob der Ausdruck `first` gleich dem Ausdruck `second` ist.
Falls die beiden Ausdrücke ungleich
sind, wird `msg` ausgegeben, wenn `msg` ungleich `None` ist.

```python
import unittest
from fibonacci import fib

class FibonacciTest(unittest.TestCase):

    def test_calculation_0(self):
        self.assertEqual(fib(0), 0)

    def test_calculation_1(self):
        self.assertEqual(fib(1), 1)

    def test_calculation_2(self):
        self.assertEqual(fib(5), 5)

    def test_calculation_3(self):
        self.assertEqual(fib(10), 55)

    def test_calculation_4(self):
        self.assertEqual(fib(20), 6765)

unittest.main()

# Für Jupyter/IPython Sessions:
# unittest.main(argv=[''], verbosity=2, exit=False) 
```

Rufen wir obigen Test auf, erhalten wir folgende Ausgabe:

```bash
Launching pytest with arguments python_programm.py::FibonacciTest --no-header --no-summary -q in C:\Users\Vikto\PycharmProjects\wiki-python

============================= test session starts =============================
collecting ... collected 5 items

python_programm.py::FibonacciTest::test_calculation_0 
python_programm.py::FibonacciTest::test_calculation_1 
python_programm.py::FibonacciTest::test_calculation_2 
python_programm.py::FibonacciTest::test_calculation_3 
python_programm.py::FibonacciTest::test_calculation_4 

============================== 5 passed in 0.03s ==============================
PASSED                   [ 20%]PASSED                   [ 40%]PASSED                   [ 60%]PASSED                   [ 80%]PASSED                   [100%]
Process finished with exit code 0
```

Bei der normalen Programmentwicklung ist dies das von uns gewünschte Ergebnis.

### Methoden der Klasse TestCase

Wir wollen nun näher auf die Klasse TestCase eingehen. Wir stellen dazu einige
wichtige Methoden dieser Klasse vor.

| Methode                                                                     | Bedeutung                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `setUp()`                                                                   | Bei der Methode `setUp` handelt es sich um eine sogenannte Hook-Methode. Sie wird vor jedem Aufruf der implementierten Testmethoden aufgerufen. Wird in der Methode setUp eine Ausnahme generiert, so wird diese auch als Error in der Testausgabe ausgegeben. Selbstverständlich wird auch bei einer Ausnahme im `setUp`-Code der Test abgebrochen.                                                                                                               |
| `tearDown()`                                                                | Die Methode `tearDown` wird nach dem Aufruf einer Testmethode gestartet. Ebenso wie bei setUp gilt, dass im Code von tearDown generierte Ausnahmen auch in der Testausgabe ausgegeben werden.                                                                                                                                                                                                                                                                      |
| `assertAlmostEqual(self, first, second, places=None, msg=None, delta=None)` | Diese Methode schlägt fehl, wenn die Differenz der beiden Parameter `first` und `second` gleich `0` ist, nachdem man sie vor dem Vergleich auf `places` Nachkommastellen gerundet hatte. Der Default-Wert für `places` ist `7`.                                                                                                                                                                                                                                    |
| `assertCountEqual(self, first, second, msg=None)`                           | Die Parameter `first` und `second` müssen hierbei sequentielle Datentypen sein. Es muss folgendes gelten:<br>Alle Elemente müssen genauso oft in `first` wie in `second` vorkommen.<br><br>Beispiel:<br><br>`[0, 1, 1]` und `[1, 0, 1]` gelten in obigem Sinne als gleich, weil die 0 und die 1 jeweils gleich oft vorkommen.<br><br>[0, 0, 1] und [0, 1] sind verschieden, weil die `0` in der ersten Liste zweimal vorkommt und in der zweiten Liste nur einmal. |
| `assertDictEqual(self, d1, d2, msg=None)`                                   | Betrachtet die beiden Argumente als Dictionaries und prüft auf Gleichheit.                                                                                                                                                                                                                                                                                                                                                                                         |
| `assertEqual(self, first, second, msg=None)`                                  | Der Test schlägt fehl, wenn die Parameter "first" und "second" nicht gleich sind. Dabei ist Gleichheit im Sinne von "==" gemeint, also Wertegleichheit und nicht nur reine Objektgleichheit.                                                                                                                                                                                                                                                                       |
| `assertTrue(self, expr, msg=None)`                                          | Prüft, ob der Ausdruck `expr` `True` ist.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `assertGreater(self, a, b, msg=None)`                                       | Prüft, ob a > b gilt.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `assertGreaterEqual(self, a, b, msg=None)`                                  | Prüft, ob a ≥ b gilt.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `assertFalse(self, expr, msg=None)`                                         | Prüft, ob der Ausdruck `expr` `False` ist.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `assertLess(self, a, b, msg=None)`                                          | Prüft, ob a < b gilt.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `assertLessEqual(self, a, b, msg=None)`                                     | Prüft, ob a ≤ b gilt.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `assertIn(self, member, container, msg=None)`                               | Prüft, ob a in b gilt.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `assertIs(self, expr1, expr2, msg=None)`                                    | Prüft, ob "a is b" gilt.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `assertIsInstance(self, obj, cls, msg=None)`                                | Prüft, ob isinstance(obj, cls) gilt.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `assertIsNone(self, obj, msg=None)`                                         | Prüft, ob "obj is None" gilt.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `assertIsNot(self, expr1, expr2, msg=None)`                                 | Prüft, ob "a is not b" gilt.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `assertIsNotNone(self, obj, msg=None)`                                      | Prüft, ob obj nicht None ist.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `assertListEqual(self, list1, list2, msg=None)`                             | Listen werden auf Gleichheit geprüft.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `assertMultiLineEqual(self, first, second, msg=None)`                       | Mehrzeilige Strings werden auf Gleichheit geprüft.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `assertNotRegexpMatches(self, text, unexpected_regexp, msg=None)`           | Schlägt fehl, wenn der Text "text" den regulären Ausdruck unexpected_regexp matched.                                                                                                                                                                                                                                                                                                                                                                               |
| `assertRaises(exception, callable, msg=None)`                               | Prüft, ob die angegebene Exception geworfen wird, wenn das `callable` aufgerufen wird. Wird gerne in einem `with`-Block verwendet.                                                                                                                                                                                                                                                                                                                                 |
| `assertTupleEqual(self, tuple1, tuple2, msg=None)`                          | Analog zu assertListEqual                                                                                                                                                                                                                                                                                                                                                                                                                                          |

Sie dazu [die Dokumentation](https://docs.python.org/3/library/unittest.html).

{{ task(file="tasks/python_grundlagen/oop/unittests/unittests/01_eigene_test_schreiben.yaml") }}
{{ task(file="tasks/python_grundlagen/oop/unittests/unittests/02_erst_die_tests.yaml") }}
{{ task(file="tasks/python_grundlagen/oop/unittests/unittests/03_wie_viele_tests.yaml") }}
{{ task(file="tasks/python_grundlagen/oop/unittests/unittests/04_den_wald_vor_lauter_baumen.yaml") }}
