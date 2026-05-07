# Debugger

Programmieren ist ein komplexer Prozess, der Präzision und Aufmerksamkeit erfordert. Trotzdem sind Fehler beim 
Programmieren allgegenwärtig. Um diese Fehler zu finden, hilft es oft, den Code Schritt für Schritt ablaufen zu lassen,
sodass wir den Programmablauf als Menschen verstehen können. Ein **Debugger** erlaubt einem genau diese Art der 
Codedurchführung. Wir werden in diesem Kapitel sehen, wie man den Debugger nutzen kann.

{{ task(file="tasks/python_grundlagen/debugging/debugging/01_kaferalarm.yaml") }}
{{ task(file="tasks/python_grundlagen/debugging/debugging/02_von_diesen_sieben_tricks_sollt_ihr_nichts_wissen.yaml") }}
### Der Debugger

Ein Debugger ist ein wesentliches Werkzeug in der Softwareentwicklung, das Programmierern hilft, den Code Schritt für 
Schritt auszuführen, um Fehler (Bugs) zu finden und zu beheben. Debugger bieten die Möglichkeit, den Zustand eines 
Programms zu einem bestimmten Zeitpunkt zu überprüfen, Variablenwerte zu inspizieren und den Programmfluss zu 
kontrollieren. 

Debugger haben alle ähnliche Funktionen:

* **Haltepunkte setzen**: Erlaubt es dem Entwickler, die Ausführung des Programms an bestimmten Punkten anzuhalten.
* **Schrittweise Ausführung**: Führt das Programm Zeile für Zeile aus, um die Auswirkungen jeder Anweisung zu beobachten.
* **Variablen inspizieren**: Zeigt die aktuellen Werte von Variablen im Programm an.
* **Programmfluss steuern**: Erlaubt es, den Ablauf des Programms zu steuern, beispielsweise durch Fortsetzen der Ausführung oder Rückkehr zu einem früheren Punkt.

Im Folgenden werden wir 2 Varianten den Debugger zu benutzen ansehen:

* Eingebauter Debugger von **VSCode**
* Eingebauter Debugger von **PyCharm**

## Debugger in IDE Nutzen

Schau die eines der folgenden Videos an, um zu sehen, wie man den Debugger in VSCode bzw. Pycharm nutzt:
{{ youtube_video("https://www.youtube.com/embed/JCuTVvR49bs?si=kxM1Abs5o2r9Ikd-") }}

{{ youtube_video("https://www.youtube.com/embed/NwNF68bEl5g?si=LbQ_3UM0ja3qiSSQ") }}

Übersicht in VSCode:
![](vscode_debugger.jpg)

Übersicht in Pycharm
![](pycharm_debugger.jpg)

| Fachbegriff   | Bedeutung                                                                                                                                                                           |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Breakpoint    | Zeile im Code, bis zu der dieser vom Debugger ausgeführt wird. Diese Zeile wartet noch auf die Ausführung.                                                                          |
| Continue      | Führt den Code weiter aus bis zum nächsten Breakpoint oder zum Programmende.                                                                                                        |
| Step Over     | Führe die aktuelle Codezeile aus und gehe zur nächsten Codezeile, die ausgeführt werden soll.                                                                                       |
| Step Into     | Wenn in der akutellen Zeile eine Funktion ausgeführt werden soll, wird in diese hineingesprungen, sodass die Ausführung der Funktion schritt für Schritt nachvollzogen werden kann. |
| Step Out      | Wenn derzeit eine Funktion ausgeführt wird, wird die Ausführung so lange automatisch weitergeführt, bis die Funktionsausführung beendet ist und dann wieder unterbrochen.           |
| Restart       | Beendet die Ausführung der Applikation und startet den Debugmodus erneut.                                                                                                           |
| Stop          | Beendet die Ausführung der Applikation.                                                                                                                                             |
| Debug Console | Erlaubt die Ausführung von Befehlen, während das Programm im Debugmodus pausiert. Funktionen können hier ausgeführt und Variablen gelesen und manipuliert werden.                   |

{{ task(file="tasks/python_grundlagen/debugging/debugging/03_debugger_bei_verschachtelten_if_bedingunen.yaml") }}
