# Generatoren und Iteratoren

| Begriff         | Kurzerklärung                                                                                                                                                                                                      | Link zur Referenz                                                                  |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| Iterator        | Eine Instanz, die die `__next__()` Methode implementiert. Ein Iterator liefert beim Aufruf von `next` Elemente.                                                                                                    | [Referenz](https://docs.python.org/3/glossary.html#term-iterator)                  |
| Iterable        | Eine Instanz, die die `__iter__()` Methode implementiert. Diese liefert einen Iterator zurück.                                                                                                                     | [Referenz](https://docs.python.org/3/glossary.html#term-iterable)                  |
| Generator       | Eine Funktion, die `yield` benutzt. Sie liefert damit Automatisch einen Iterator.                                                                                                                                  | [Referenz](https://docs.python.org/3/glossary.html#term-generator)                 |
| `yield`         | Ein Schlüsselwort, das anzeigt, dass die Funktion einen Iterator liefert. Beim Ausführen des Iterarators wird bei dieser Zeile eine Rückgabe durchgeführt und die Codedurchführung hier später wieder aufgenommen. | [Referenz](https://docs.python.org/3/reference/expressions.html#yield-expressions) |
| `StopIteration` | Fehler der von `next()` geworfen wird, wenn es keine weiteren Elemente mehr gibt.                                                                                                                                  | [Referenz](https://docs.python.org/3/library/exceptions.html#StopIteration)        |

# Anonyme Funktionen

| Begriff                              | Kurzerklärung                                                                                | Link zur Referenz                                                             |
|--------------------------------------|----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| lambda expression / anonyme Funktion | Eine Funktion, die in der Form `lambda parameter: returnd_operation(parameter)` gegeben ist. | [Referenz](https://docs.python.org/3/glossary.html#term-lambda)               |
| map                                  | Wende eine Funktion auf jedes Element eines Iterable an.                                     | [Referenz](https://docs.python.org/3/library/functions.html#map)              |
| filter                               | Behalte nur die Elemente eines Iterable, das True bei einer übergebenen Funktion zurückgibt. | [Referenz](https://docs.python.org/3/library/functions.html#filter)           |
| reduce                               | Fasse die Elemente eines Iterables in einer Accumulator zusammen.                            | [Referenz](https://docs.python.org/3/library/functools.html#functools.reduce) |

# Dekoratoren

| Begriff   | Kurzerklärung                                                                                                               | Link zur Referenz                                                              |
|-----------|-----------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| decorator | Eine Funktion, die eine ander Funktion erweitert. Diese wird gemeinhin mit `@` über der zu erweiternden Funktion notiert    | [Referenz](https://docs.python.org/3/glossary.html#term-decorator)             |
| `@wraps`  | Wird beim erstellen des Dekorators verwendet, um die neue Funktion den selben Namen, Dokumentation usw. der alten zu geben. | [Referenz](https://docs.python.org/3/library/functools.html#functools.wraps)   |
