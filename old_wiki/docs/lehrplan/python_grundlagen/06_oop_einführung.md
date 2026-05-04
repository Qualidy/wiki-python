# Einführung in die Objektorientierte Programmierung (OOP)
[120min]

Die objektorientierte Programmierung (OOP) ist ein mächtiges Programmierparadigma, 
das auf dem Konzept von "Objekten" basiert. Im Gegensatz zu prozeduralen Programmieransätzen,
bei denen der Code als eine Abfolge von Aufgaben organisiert ist, 
legt die OOP den Fokus auf die Modellierung von reellen Entitäten und ihren Interaktionen.

## Warum OOP?

Die OOP wurde entwickelt, um die Komplexität von Softwareentwicklung zu reduzieren, 
indem sie den Code in gut organisierte, wiederverwendbare und erweiterbare Strukturen gliedert.
Hier sind einige Gründe, warum OOP verwendet wird:

**Modellierung der Realität:** OOP ermöglicht es, reale Objekte und ihre Beziehungen in der Software abzubilden.
Dies erleichtert das Verständnis und die Wartung des Codes.

**Wiederverwendbarkeit:** Durch die Verwendung von Klassen und Objekten können bestimmte Funktionen oder Strukturen
leicht in verschiedenen Teilen der Software wiederverwendet werden.

**Modularität:** OOP fördert die Aufteilung des Codes in Module (Klassen), was die Entwicklung, Wartung und Erweiterung erleichtert.

**Erweiterbarkeit:** Neue Funktionen können durch Hinzufügen neuer Klassen oder Erben von bestehenden Klassen einfach hinzugefügt werden.

## Grundlegende Konzepte der OOP:

### 1. Klassen und Objekte

- **Klassen:** Eine Klasse ist eine abstrakte Vorlage, die die Eigenschaften und Verhaltensweisen von Objekten definiert. Klassen repräsentieren Konzepte und enthalten Attribute (Daten) sowie Methoden (Funktionen).

- **Objekte:** Ein Objekt ist eine Instanz einer Klasse. Es repräsentiert eine konkrete Entität und enthält Daten (Attribute) und Methoden.

### 2. Vererbung

Vererbung ermöglicht es einer Klasse, die Eigenschaften und Methoden einer anderen Klasse zu erben. 
Dies fördert die Wiederverwendung von Code und die Strukturierung von Klassen.

### 3. Polymorphismus

Polymorphismus erlaubt es, dass Objekte unterschiedlicher Klassen auf die gleiche Weise behandelt werden können.
Das bedeutet, dass verschiedene Klassen denselben Methodennamen haben können, der je nach Kontext unterschiedlich
implementiert ist.

### 4. Kapselung

Kapselung beschreibt die Beschränkung des Zugriffs auf die internen Details einer Klasse und erlaubt den Zugriff
nur über eine definierte Schnittstelle. Dies fördert die Sicherheit und erleichtert die Änderung der internen
Implementierung.

Insgesamt ermöglicht die OOP eine organisierte und strukturierte Entwicklung von Software, wodurch Code besser lesbar,
wartbar und erweiterbar wird.


# Analogie

Stell dir vor, du möchtest eine Kaffeemaschine bauen. Die Kaffeemaschine repräsentiert dabei die Klasse, 
die den Bauplan für alle Kaffeemaschinen darstellt. Diese Klasse definiert, welche Funktionen und Eigenschaften 
alle Kaffeemaschinen haben sollten, wie beispielsweise die Fähigkeit, Kaffee zu brühen, eine Warmhalteplatte und eine Tropfschale.

Jetzt entscheidest du dich, konkrete Kaffeemaschinen zu bauen, basierend auf diesem Bauplan. Jede einzelne Kaffeemaschine, die du herstellst, ist dann ein Objekt dieser Klasse. Du könntest eine Kaffeemaschine namens "EspressoExpress" mit schnellem Brühvorgang und einer speziellen Dampfdüse für Milchschaum erstellen. Ein anderes Exemplar könnte "FilterFreude" heißen und auf eine besonders einfache Bedienung und große Kaffeemengen ausgelegt sein.

So wie die Klasse den Bauplan für die Kaffeemaschine liefert, gibt sie vor, welche Funktionen und Eigenschaften die Kaffeemaschinen haben sollten. Die einzelnen Maschinen, also die Objekte, sind dann die konkreten Umsetzungen dieses Bauplans mit individuellen Variationen.

**In diesem Sinne sind Klassen wie Baupläne, und Objekte sind die konkreten Instanzen, die basierend auf diesen Bauplänen erstellt werden.**
