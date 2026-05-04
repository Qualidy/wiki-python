# Verwendung von Funktionsparametern statt globaler Variablen

Es liegen folgende Dateien vor:

```python
# config.py
# Global configuration variable
settings = {
    "debug_mode": False
}
```

```python
# main.py
import config

def enable_debug():
    config.settings["debug_mode"] = True

def perform_operation():
    if config.settings["debug_mode"]:
        print("Debug mode is enabled. Performing operation in debug mode.")
    else:
        print("Performing operation in standard mode.")

print("Initial debug mode:", config.settings["debug_mode"])
enable_debug()
perform_operation()
print("Final debug mode:", config.settings["debug_mode"])
```

Der Code stellt zwei Module bereit, config.py und main.py. config.py dient hierbei dazu,
Konfigurationen für alle Module bereitzustellen. Das Problem hierbei ist, dass die globale 
Variable von main.py geändert wird. Wird nun ein weiteres Modul eingebunden,
so kann dieses die Variable ebenfalls nutzen und änder.
Dies führt zu unerwartetem Verhalten und macht die Software schwer wartbar.
Ein besser Weg ist es, die Konfigurationen als Funktionsparameter zu übergeben.
Hierbei wird die Konfiguration gekapselt und kann nicht mehr von anderen Modulen geändert werden.

**Unerwünschte Effekte mit Globalen Variablen:**

* **Beeinträchtigung von Lesbarkeit und Wartbarkeit:** Globale Variablen können von überall im Code geändert werden, was zu unerwartetem Verhalten und schwer zu findenden Fehlern führen kann.
* **Erschwerte Nachvollziehbarkeit des Datenflusses:** Da ihre Werte an vielen Stellen verändert werden können, ohne dass dies offensichtlich ist, wird der Datenfluss im Programm unklar.
* **Probleme in größeren Projekten:** In umfangreichen Projekten wird die Nachverfolgung der Verwendung und Änderung globaler Variablen fast unmöglich, was die Komplexität unnötig erhöht.
* **Erschwerte Testbarkeit:** Globale Variablen erschweren das isolierte Testen von Codeabschnitten, da Änderungen an ihnen unerwartete Seiteneffekte in anderen Teilen des Programms haben können.
* **Risiko von Seiteneffekten:** Änderungen an globalen Variablen können unerwartete Auswirkungen auf andere Teile des Programms haben, was die Fehlersuche und -behebung erschwert.
