# Class- & Static Methods

In Python gibt es zwei besondere Arten von Methoden, die direkt einer Klasse zugeordnet sind:
**statische Methoden** und **Klassenmethoden**. Diese Methoden haben spezielle Verwendungszwecke 
und werden mit den Dekoratoren `@staticmethod` und `@classmethod` definiert.

## Statische Methoden

[//]: # (<details>)

[//]: # (<summary>)

[//]: # (🎦 Video)

[//]: # (</summary>)

[//]: # ({{ youtube_video("https://www.youtube.com/embed/BQBcMf1cFB4?si=1BtB8qMroDTATEdE") }})

[//]: # (</details>)

Eine **statische Methode** ist eine Methode, die zu einer Klasse gehört, 
aber nicht auf eine Instanz zugreift. Sie wird mit dem Dekorator `@staticmethod` definiert 
und hat keinen Zugriff auf Instanzattribute. Statische Methoden sind in erster Linie nützlich,
wenn eine Methode nur auf Klassenebene operieren muss und keine Instanzinformationen benötigt.

Besonders gerne nutzt man statische Methoden für UtilityKlassen, wie zum Beispiel die folgende, die 
Fahrenheit in Celsius umrechnet und umgekehrt:

[Link zum Online Compiler💻](https://pythontutor.com/render.html#code=class%20TemperatureConverter%3A%0A%20%20%20%20%40staticmethod%0A%20%20%20%20def%20celsius_to_fahrenheit%28celsius%29%3A%0A%20%20%20%20%20%20%20%20return%20celsius%20*%209/5%20%2B%2032%0A%0A%20%20%20%20%40staticmethod%0A%20%20%20%20def%20fahrenheit_to_celsius%28fahrenheit%29%3A%0A%20%20%20%20%20%20%20%20return%20%28fahrenheit%20-%2032%29%20*%205/9%0A%0A%23%20Die%20statischen%20Methoden%20k%C3%B6nnen%20direkt%20von%20der%20Klasse%20aufgerufen%20werden%0Acelsius_temp%20%3D%2025%0Afahrenheit_equivalent%20%3D%20TemperatureConverter.celsius_to_fahrenheit%28celsius_temp%29%0Aprint%28f%22%7Bcelsius_temp%7D%20Grad%20Celsius%20entsprechen%20%7Bfahrenheit_equivalent%3A.2f%7D%20Grad%20Fahrenheit.%22%29%0A%0Afahrenheit_temp%20%3D%2077%0Acelsius_equivalent%20%3D%20TemperatureConverter.fahrenheit_to_celsius%28fahrenheit_temp%29%0Aprint%28f%22%7Bfahrenheit_temp%7D%20Grad%20Fahrenheit%20entsprechen%20%7Bcelsius_equivalent%3A.2f%7D%20Grad%20Celsius.%22%29&cumulative=true&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```python
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return celsius * 9/5 + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

# Die statischen Methoden können direkt von der Klasse aufgerufen werden
celsius_temp = 25
fahrenheit_equivalent = TemperatureConverter.celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp} Grad Celsius entsprechen {fahrenheit_equivalent:.2f} Grad Fahrenheit.")

fahrenheit_temp = 77
celsius_equivalent = TemperatureConverter.fahrenheit_to_celsius(fahrenheit_temp)
print(f"{fahrenheit_temp} Grad Fahrenheit entsprechen {celsius_equivalent:.2f} Grad Celsius.")
```

{{ task(file="tasks/python_grundlagen/oop/class_static_methods/class_static_methods/01_jaja_das_ist_nutzlich_ohne_ende.yaml") }}
{{ task(file="tasks/python_grundlagen/oop/class_static_methods/class_static_methods/02_verschiedene_ursprunge.yaml") }}
