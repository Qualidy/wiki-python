# Wiederholung: `platform` und Standardmodule

Diese Einheit wiederholt kurz, was Module sind, legt den Fokus aber klar auf
das Built-in-Standardmodul `platform`. Danach folgt ein kompakter Überblick zu
weiteren Standardmodulen, die fuer PCAP-Aufgaben interessant sind.

## Lernziele

Am Ende kann ich ...

- erklaeren, was ein Python-Modul ist.
- den Unterschied zwischen `import module` und `from module import name` erklaeren.
- das Modul `platform` importieren und wichtige Funktionen nutzen.
- typische Rueckgaben von `platform.system()`, `platform.machine()` und
  `platform.python_version()` einordnen.
- `platform`, `os` und `sys` grob voneinander unterscheiden.
- weitere PCAP-relevante Standardmodule benennen.

## Kurze Wiederholung: Was ist ein Modul?

Ein Modul ist eine Datei oder Bibliothek mit Python-Code, die importiert werden
kann. Module enthalten Funktionen, Klassen, Konstanten oder andere Werte.

```python
import math

print(math.sqrt(16))
```

Hier wird das Standardmodul `math` importiert. Der Zugriff erfolgt danach ueber
den Modulnamen:

```python
math.sqrt(16)
```

## Importvarianten

```python
import platform
print(platform.system())
```

```python
from platform import system
print(system())
```

```python
import platform as pf
print(pf.system())
```

Faustregel:

- `import platform` ist am klarsten, weil man sieht, woher `system()` kommt.
- `from platform import system` ist praktisch, wenn nur wenige Namen gebraucht
  werden.
- `from platform import *` vermeiden, weil unklar wird, welche Namen im Programm
  existieren.

## Fokus: Das Modul `platform`

Das Modul `platform` liefert Informationen ueber die Umgebung, in der Python
gerade laeuft:

- Betriebssystem
- Rechnerarchitektur
- Python-Version
- Python-Implementierung
- Prozessor- und Plattforminformationen

Import:

```python
import platform
```

Ein einfaches Diagnose-Skript:

```python
import platform

print("System:", platform.system())
print("Machine:", platform.machine())
print("Python-Version:", platform.python_version())
print("Python-Implementierung:", platform.python_implementation())
```

Moegliche Ausgabe auf macOS:

```text
System: Darwin
Machine: arm64
Python-Version: 3.12.11
Python-Implementierung: CPython
```

Moegliche Ausgabe auf Windows:

```text
System: Windows
Machine: AMD64
Python-Version: 3.12.3
Python-Implementierung: CPython
```

!!! warning "Wichtig"
    Die exakten Ausgaben von `platform` sind systemabhaengig. In Aufgaben muss
    man deshalb oft verstehen, welche Art von Information geliefert wird, nicht
    eine konkrete Ausgabe auswendig lernen.

## Wichtige `platform`-Funktionen

| Funktion | Bedeutung | Beispielhafte Rueckgabe |
|----------|-----------|-------------------------|
| `platform.system()` | Betriebssystemname | `"Windows"`, `"Linux"`, `"Darwin"` |
| `platform.machine()` | Maschinen-/CPU-Architektur | `"AMD64"`, `"x86_64"`, `"arm64"` |
| `platform.processor()` | Prozessorbeschreibung | systemabhaengig, manchmal leer |
| `platform.python_version()` | Python-Version als String | `"3.12.11"` |
| `platform.python_implementation()` | Python-Implementierung | `"CPython"` |
| `platform.platform()` | zusammengefasste Plattformbeschreibung | systemabhaengiger String |

## `platform.system()`

`platform.system()` liefert den Namen des Betriebssystems.

```python
import platform

system_name = platform.system()

if system_name == "Windows":
    print("Windows-System")
elif system_name == "Linux":
    print("Linux-System")
elif system_name == "Darwin":
    print("macOS-System")
else:
    print("Anderes System")
```

Wichtig fuer macOS: `platform.system()` gibt meistens `"Darwin"` zurueck, nicht
`"macOS"`.

## `platform.machine()`

`platform.machine()` liefert die Maschinenarchitektur.

```python
import platform

machine = platform.machine()

if machine in ("x86_64", "AMD64"):
    print("64-bit Intel/AMD")
elif machine in ("arm64", "aarch64"):
    print("ARM 64-bit")
else:
    print("Andere Architektur:", machine)
```

Typische Werte:

- `"AMD64"` auf vielen Windows-Systemen
- `"x86_64"` auf vielen Linux/macOS-Systemen mit Intel/AMD
- `"arm64"` auf Apple Silicon
- `"aarch64"` auf manchen Linux-ARM-Systemen

## `platform.python_version()`

`platform.python_version()` liefert die Python-Version als String.

```python
import platform

version = platform.python_version()
print(version)
print(type(version))
```

Beispiel:

```text
3.12.11
<class 'str'>
```

Wenn man Versionsnummern vergleichen will, darf man Strings nicht blind wie
Zahlen behandeln.

```python
print("3.10" > "3.9")  # False, weil Stringvergleich
```

Fuer den Unterricht reicht hier: `platform.python_version()` ist gut zum
Anzeigen, aber nicht ideal fuer robuste Versionslogik.

## `platform.python_implementation()`

Diese Funktion gibt an, welche Python-Implementierung verwendet wird.

```python
import platform

print(platform.python_implementation())
```

Meistens ist die Ausgabe:

```text
CPython
```

Andere moegliche Implementierungen sind z.B. `PyPy`, `Jython` oder
`IronPython`. Fuer PCAP ist wichtig: Python ist die Sprache, CPython ist die
haeufigste Implementierung dieser Sprache.

## `platform.platform()`

`platform.platform()` liefert eine zusammengefasste Beschreibung des Systems.

```python
import platform

print(platform.platform())
```

Beispielausgaben:

```text
macOS-15.6.1-arm64-arm-64bit
Windows-11-10.0.26100-SP0
Linux-6.8.0-...-x86_64-with-glibc2.39
```

Diese Ausgabe ist praktisch fuer Diagnose-Logs, aber schlecht fuer harte
Fallunterscheidungen, weil sie sehr systemabhaengig ist.

## `platform`, `os` und `sys` unterscheiden

| Modul | Fokus | Typische Nutzung |
|-------|-------|------------------|
| `platform` | Informationen ueber Betriebssystem, Architektur, Python-Version | Diagnose, Systeminformationen anzeigen |
| `os` | Betriebssystem-nahe Funktionen | Pfade, Umgebungsvariablen, Verzeichnisse |
| `sys` | Python-Laufzeit und Interpreter | `sys.path`, `sys.argv`, `sys.version` |

Beispiele:

```python
import os
import platform
import sys

print(platform.system())  # Betriebssystemname
print(os.getcwd())        # aktuelles Arbeitsverzeichnis
print(sys.version)        # detaillierte Python-Version
```

## Weitere PCAP-relevante Standardmodule

Diese Module muessen nicht alle tief behandelt werden, sind aber als Namen und
Grundidee wichtig:

| Modul | Wofuer? | Mini-Beispiel |
|-------|--------|---------------|
| `math` | Mathematikfunktionen | `math.sqrt(16)` |
| `random` | Zufallszahlen | `random.randint(1, 6)` |
| `datetime` | Datum und Uhrzeit | `datetime.date.today()` |
| `time` | Zeitfunktionen, Pausen | `time.sleep(1)` |
| `os` | Betriebssystemfunktionen | `os.getcwd()` |
| `sys` | Interpreter/Laufzeit | `sys.path` |
| `platform` | Plattforminformationen | `platform.system()` |

Kurze Beispiele:

```python
import math
import random
import datetime

print(math.pi)
print(random.randint(1, 6))
print(datetime.date.today())
```

## Typische Importfehler

| Fehler | Ursache | Loesung |
|--------|---------|---------|
| `ModuleNotFoundError` | Modulname falsch oder externes Paket nicht installiert | Schreibweise pruefen, bei externen Paketen Installation pruefen |
| `AttributeError` | Modul wurde importiert, aber Name existiert darin nicht | Funktion/Attribut im Modul pruefen |
| Schatten von Standardmodulen | eigene Datei heisst z.B. `platform.py`, `random.py` oder `sys.py` | Datei umbenennen |
| zirkulaerer Import | Zwei eigene Module importieren sich gegenseitig | gemeinsame Logik in ein drittes Modul verschieben |

!!! danger "Haeufiger Fehler"
    Eine eigene Datei `platform.py` zu nennen, ist eine schlechte Idee, wenn man
    das Standardmodul `platform` importieren will. Python findet dann oft zuerst
    die eigene Datei.

## Aufgaben

{{ task(file="tasks/python_grundlagen/wiederholung/args_module_oop/05_module_preisrechner.yaml") }}
{{ task(file="tasks/python_grundlagen/wiederholung/args_module_oop/06_importfehler_erklaeren.yaml") }}
{{ task(file="tasks/python_grundlagen/wiederholung/args_module_oop/07_kleines_paket_bauen.yaml") }}
{{ task(file="tasks/python_grundlagen/wiederholung/args_module_oop/16_platform_diagnose.yaml") }}
{{ task(file="tasks/python_grundlagen/wiederholung/args_module_oop/17_platform_output_einordnen.yaml") }}
{{ task(file="tasks/python_grundlagen/wiederholung/args_module_oop/18_standardmodule_zuordnen.yaml") }}
{{ task(file="tasks/python_grundlagen/wiederholung/args_module_oop/19_system_report_abstrakt.yaml") }}
{{ task(file="tasks/python_grundlagen/wiederholung/args_module_oop/20_training_timer_abstrakt.yaml") }}
{{ task(file="tasks/python_grundlagen/wiederholung/args_module_oop/21_diagnose_quiz_abstrakt.yaml") }}
