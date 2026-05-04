# Benennungskonventionen in der Programmierung

Für detaillierte Benennungskonventionen, siehe [PEP 8](https://peps.python.org/pep-0008/).

## Variablen

Unklare Variablennamen wie im folgenden Beispiel:

```python
a = 50
b = 100
c = a + b
```

sollten vermieden werden. Stattdessen empfiehlt es sich, klare und aussagekräftige Bezeichner zu verwenden, die den [PEP 8-Richtlinien](https://peps.python.org/pep-0008/#prescriptive-naming-conventions) entsprechen:

```python
basispreis = 50
steuer = 100
gesamtpreis = basispreis + steuer
```

# Aussagekräftige Namen

Variablen- und Funktionsnamen sollten:

- Informativ und beschreibend sein, um die Lesbarkeit und Wartbarkeit des Codes zu verbessern.
- Einfach aussprechbar und nicht irreführend sein.
- Leicht durchsuchbar sein.
- Keine kryptischen Abkürzungen oder Codierungen enthalten. *(Anmerkung: Hier wird auf die Vermeidung von unklaren Abkürzungen oder spezifischen Codierungen hingewiesen, die außerhalb des Kontexts keinen Sinn ergeben.)*
- Einfach zu verstehen sein.
- Keine Umgangssprache, Mundart oder kulturelle Spezifika beinhalten.
- Eindeutig sein und keine doppelten Bezeichnungen oder vorangestellte Präfixe haben.
- Fachbegriffe aus dem relevanten Themengebiet verwenden, um eine fachspezifische Sprache zu schaffen, die auch mit Nicht-Programmierern kommuniziert werden kann. Dies führt uns in den Bereich des Domain-Driven Designs.

## Funktionen

Allgemeine Funktionsnamen wie im folgenden Beispiel:

```python
def calc(x):
    return x * 2 + 5
```

sollten vermieden werden, da sie wenig über die eigentliche Funktion aussagen. Besser ist es, Namen zu verwenden, die sich auf die spezifische Aufgabe beziehen:

```python
def calculate_adjusted_value(x):
    return x * 2 + 5
```

Dieser Name ist immer noch nicht vollständig aussagekräftig. Nehmen wir an, wir arbeiten in einer Applikation, die mit direkten Speicheradressen operiert:

```python
def get_next_memory_address(old_address):
    return old_address * 2 + 5
```

Durch einen solchen spezifischen Namen kann man oft auf zusätzliche Kommentare verzichten.