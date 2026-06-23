# Scope, Closure & lokale vs. globale Variablen – Zusammenfassung

🔄 *Wiederholung / Zusammenfassung – Details siehe [Scopes](../funktionen_vertiefung/scopes/scopes.md)*

## Scope (Gültigkeitsbereich)

Python verwendet die **LEGB-Regel** zur Namensauflösung:

| Scope | Beschreibung |
|-------|-------------|
| **L**ocal | Variablen innerhalb der aktuellen Funktion |
| **E**nclosing | Variablen in umschließenden (äußeren) Funktionen |
| **G**lobal | Variablen auf Modulebene |
| **B**uilt-in | Eingebaute Namen (`print`, `len`, …) |

### Lokale vs. globale Variablen

```python
x = "global"  # globale Variable

def beispiel():
    x = "lokal"  # lokale Variable – überschattet die globale
    print(x)     # "lokal"

beispiel()
print(x)  # "global" – die globale Variable ist unverändert
```

Mit `global` kann eine globale Variable innerhalb einer Funktion **verändert** werden:

```python
zaehler = 0

def erhoehe():
    global zaehler
    zaehler += 1

erhoehe()
print(zaehler)  # 1
```

## Closure

Eine **Closure** entsteht, wenn eine innere Funktion auf Variablen der äußeren Funktion zugreift – und die äußere Funktion bereits beendet ist. Die innere Funktion "merkt" sich die Werte aus dem Enclosing Scope.

```python
def multiplizierer(faktor):
    def multipliziere(zahl):
        return zahl * faktor  # faktor kommt aus dem Enclosing Scope
    return multipliziere

verdopple = multiplizierer(2)
verdreifache = multiplizierer(3)

print(verdopple(5))     # 10
print(verdreifache(5))  # 15
```

## Übungsaufgaben

{{ task(file="tasks/python_grundlagen/functions/functions/19_scope_lesezugriff.yaml") }}
{{ task(file="tasks/python_grundlagen/functions/functions/20_scope_global_keyword.yaml") }}
{{ task(file="tasks/python_grundlagen/functions/functions/21_closure_logger.yaml") }}
{{ task(file="tasks/python_grundlagen/functions/functions/22_closure_zaehler.yaml") }}
{{ task(file="tasks/python_grundlagen/functions/functions/23_scope_und_closure_kombination.yaml") }}
