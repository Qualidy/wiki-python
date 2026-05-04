### Aufgabe: Compiler und Interpreter
Siehe Video in Aufgabenstellung.

### Aufgabe: Fehlerstelle

```python
import dis
i=i+4

Traceback (most recent call last):
  File "C:\Program Files\JetBrains\PyCharm Community Edition 2022.1\plugins\python-ce\helpers\pydev\pydevconsole.py", line 364, in runcode
    coro = func()
           ^^^^^^
  File "<input>", line 1, in <module>
NameError: name 'i' is not defined. Did you mean: 'id'?

dis.dis()

  0           0 RESUME                   0
  1 -->       2 LOAD_NAME                0 (i)
              4 LOAD_CONST               0 (4)
              6 BINARY_OP                0 (+)
             10 STORE_NAME               0 (i)
             12 RETURN_CONST             1 (None)
```

Der Fehler tritt beim ersten `LOAD_NAME` Befehl aus. Wir sehen hier auch noch mit `-->` markiert
die Stelle der letzten Ausführung

### Aufgabe: Verschiedene Interpreter 
Siehe Video in Aufgabenstellung.

### Aufgabe: Verschiedene Interpreter

````python
import platform

print(platform.python_implementation())
````