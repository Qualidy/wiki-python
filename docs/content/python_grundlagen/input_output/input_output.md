# Input und Output

## Die `print`-Funktion

{{ youtube_video("https://www.youtube.com/embed/dEzipXx0x-g?si=MNYz2ZMIjAl_5RDI") }}
[//]: # ([45min])

Die `print`-Funktion ist eines der grundlegendsten Werkzeuge in Python. Sie wird verwendet, um Werte auf der Konsole 
auszugeben, sei es Text, Zahlen oder den Inhalt von Variablen. Ein einfacher Aufruf von `print` sieht wie folgt aus:
`print("Hallo, Welt!")`. 

Die Verwendung von Formatierungs-Strings, auch bekannt als f-Strings, macht die Arbeit mit der `print`-Funktion sehr
angenehm. Mit f-Strings können wir Werte von Variablen direkt in einen String einfügen, indem wir die Variable in 
geschweifte Klammern `{}` setzen und dem String ein `f` voranstellen.

**Beispiel**: 

```python
name = "Anna"
alter = 30
print(f"Mein Name ist {name} und ich bin {alter} Jahre alt.")
```

Diese Methode der String-Formatierung ist nicht nur effizient, sondern verbessert auch die Lesbarkeit des Codes 
erheblich. Sie ermöglicht es, dynamisch Werte in Strings einzubetten, was besonders nützlich ist, wenn es darum geht, 
komplexe Ausgaben zu generieren oder Benutzerinteraktionen zu gestalten.

## Die `input`-Funktion

{{ youtube_video("https://www.youtube.com/embed/2sgoMPkyBog?si=36-kkhLA7MA39SAN") }}

[//]: # ([45min])
Die `input`-Funktion in Python ist ein wesentliches Werkzeug, um Benutzereingaben zu erhalten. Sie ermöglicht es einem
Programm, während der Ausführung Daten vom Benutzer zu erfragen. Wenn `input()` aufgerufen wird, hält das Programm an
und wartet auf eine Eingabe von der Tastatur. Nachdem der Benutzer seine Eingabe bestätigt hat (üblicherweise 
durch Drücken der Enter-Taste), gibt `input()` diese Eingabe als String zurück. Optional kann `input()` einen 
String als Argument erhalten, der als Eingabeaufforderung (Prompt) dient. Hier ein einfaches Beispiel:

```python
name = input("Bitte gib deinen Namen ein: ")
print(f"Hallo, {name}!")
```

In diesem Beispiel wird der Benutzer aufgefordert, seinen Namen einzugeben. Nach der Eingabe wird der eingegebene 
Name mit einer Begrüßung ausgegeben. Es ist wichtig zu beachten, dass `input()` immer einen String zurückgibt. Wenn wir 
Zahlen oder andere Datentypen erwarten, müssen wir die Eingabe entsprechend konvertieren:

```python
alter_string = input("Gib dein Alter an: ")
alter = int(alter_string)
```

Damit haben wir bereits eine Menge Grundlagen gelernt, mit denen wir kleine Programme schreiben können. Damit wir das 
nicht nur theoretisch besprechen folgen jetzt erstmal eine Reihe an Übungsaufgaben.

# Aufgaben
[40min]

{{ task(file="tasks/python_grundlagen/input_output/input_output/01_einfache_ausgabe.yaml") }}
{{ task(file="tasks/python_grundlagen/input_output/input_output/02_variable_ausgeben.yaml") }}
{{ task(file="tasks/python_grundlagen/input_output/input_output/03_zahlen_ausgeben.yaml") }}
{{ task(file="tasks/python_grundlagen/input_output/input_output/04_mehrere_argumente.yaml") }}
{{ task(file="tasks/python_grundlagen/input_output/input_output/05_zeilenende_andern.yaml") }}
{{ task(file="tasks/python_grundlagen/input_output/input_output/06_begruung.yaml") }}
{{ task(file="tasks/python_grundlagen/input_output/input_output/07_kombinierte_eingabe_und_ausgabe.yaml") }}
{{ task(file="tasks/python_grundlagen/input_output/input_output/08_formatierte_ausgabe.yaml") }}
{{ task(file="tasks/python_grundlagen/input_output/input_output/09_mehrere_eingaben.yaml") }}
{{ task(file="tasks/python_grundlagen/input_output/input_output/10_rechnung_mit_eingabe.yaml") }}
{{ task(file="tasks/python_grundlagen/input_output/input_output/11_eingabe_in_liste_speichern.yaml") }}
{{ task(file="tasks/python_grundlagen/input_output/input_output/12_benutzereingaben_vergleichen.yaml") }}
## Anspruchsvolle Aufgaben

{{ task(file="tasks/python_grundlagen/input_output/input_output/13_personliche_statistik.yaml") }}
