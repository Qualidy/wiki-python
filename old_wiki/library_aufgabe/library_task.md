# Aufgabenbeschreibung: Bibliotheksverwaltungssystem

## 1. Klassen definieren
Erstelle Klassen für `Buch`, `Mitglied` und `Bibliothek`. Jede Klasse sollte geeignete Attribute und Methoden haben, um das Bibliothekssystem zu verwalten.
### Buch-Klasse:
- `title` (String): Der Titel des Buches.
- `author` (String): Der Autor des Buches.
- `isbn` (String): Die ISBN (Internationale Standardbuchnummer) des Buches.
- `checked_out` (Boolean): Gibt an, ob das Buch ausgeliehen ist oder nicht. Wird auf "False" gesetzt, wenn das Buch verfügbar ist, und auf "True", wenn es ausgeliehen wurde.

### Mitglied-Klasse:
- `name` (String): Der Name des Mitglieds.
- `member_id` (String): Die Mitglieds-ID des Mitglieds.
- `checked_out_books` (Liste): Eine Liste von Büchern, die das Mitglied ausgeliehen hat.

### Bibliothek-Klasse:
- `books` (Liste): Eine Liste von Büchern in der Bibliothek.
- `member` (Liste): Eine Liste von Mitgliedern in der Bibliothek.

## 2. Buchklasse implementieren
- Definiere eine `__init__`-Methode, um das Buch mit Titel, Autor und ISBN zu initialisieren.
- Implementiere eine `display_info`-Methode, um die Informationen des Buches auszugeben.

## 3. Mitgliedsklasse implementieren
- Definiere eine `__init__`-Methode, um das Mitglied mit Namen und Mitglieds-ID zu initialisieren.
- Implementiere eine `display_info`-Methode, um die Informationen des Mitglieds auszugeben.
- Implementiere eine `check_out_book`-Methode, um Mitgliedern das Ausleihen von Büchern zu ermöglichen.
- Implementiere eine `return_book`-Methode, um Mitgliedern das Zurückgeben von Büchern zu ermöglichen.

## 4. Bibliotheksklasse implementieren
- Definiere eine `__init__`-Methode, um eine leere Liste von Büchern und Mitgliedern zu initialisieren.
- Implementiere Methoden, um Bücher und Mitglieder zur Bibliothek hinzuzufügen.
- Implementiere Methoden, um die Liste der Bücher und Mitglieder in der Bibliothek anzuzeigen.

## 5. Beispielhafte Verwendung
- Erstelle Instanzen von Büchern, Mitgliedern und der Bibliothek.
- Füge Bücher und Mitglieder der Bibliothek hinzu.
- Zeige die Bücher und Mitglieder der Bibliothek an.
- Führe Ausleih- und Rückgabevorgänge durch, um die Funktionalität zu testen.
- Zeige die Bücher und Mitglieder der Bibliothek erneut an, um die Änderungen zu sehen.

## 6. Testen
- Teste den Code mit verschiedenen Szenarien, um sicherzustellen, dass er korrekt funktioniert. Dazu gehört auch das Überprüfen von Fällen, in denen Bücher bereits ausgeliehen sind oder überhaupt nicht ausgeliehen wurden, das Zurückgeben von Büchern, die nicht ausgeliehen wurden, usw.




