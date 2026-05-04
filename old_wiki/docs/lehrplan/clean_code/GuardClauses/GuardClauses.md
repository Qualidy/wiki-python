# Clean Code Konzept: Guard Clauses

Ein Guard Clause ist eine bedingte Anweisung am Anfang einer Funktion, die die Ausführung der Funktion schnell beendet, wenn eine bestimmte Bedingung erfüllt ist. Statt mehrere Ebenen von `if`-Anweisungen zu verschachteln, verwenden Sie Guard Clauses, um "Wächter" am Eingang Ihrer Funktionen zu platzieren, die unerwünschte Bedingungen abweisen.

<details>
<summary>Video 🎥</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/ZzwWWut_ibU?si=MJlXx4HWaqNcfsYr" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</details>

## Anwendung des Konzepts

### Beispiel: Vorher
Ohne Guard Clauses kann der Code tief verschachtelt und schwer zu folgen sein.
```python
def process_user(user):
    if user.is_active:
        if user.balance > 0:
            # Logik zur Bearbeitung des Benutzers
            print("Benutzer verarbeitet.")
        else:
            print("Der Benutzer hat kein Guthaben.")
    else:
        print("Benutzer ist nicht aktiv.")
```

### Beispiel: Nachher
Mit Guard Clauses wird der Code flacher und klarer.
```python
def process_user(user):
    if not user.is_active:
        print("Benutzer ist nicht aktiv.")
        return
    if user.balance <= 0:
        print("Der Benutzer hat kein Guthaben.")
        return
    
    # Logik zur Bearbeitung des Benutzers
    print("Benutzer verarbeitet.")
```

## Vorteile der Anwendung
- **Verbesserte Lesbarkeit:** Guard Clauses reduzieren die Verschachtelung und machen den Code leichter verständlich.
- **Frühe Fehlererkennung:** Durch das frühzeitige Abfangen von Fehlern oder unerwünschten Zuständen können Sie sicherstellen, dass der nachfolgende Code unter bekannten Bedingungen ausgeführt wird.
- **Wartbarkeit:** Guard Clauses erleichtern die Wartung des Codes, da die Bedingungen, unter denen bestimmte Codepfade ausgeführt werden, klar definiert sind.

## Häufige Fallstricke
- **Übermäßige Verwendung:** Zu viele Guard Clauses können dazu führen, dass der Code schwer zu folgen ist, besonders wenn sie komplexe Bedingungen enthalten.
- **Verborgene Logik:** Wichtig ist, dass Guard Clauses die Hauptlogik einer Funktion nicht verbergen sollten. Sie sollten nur für klare, einfache Bedingungen verwendet werden.

## Übungsaufgaben

### Aufgabe 1 🌶️
Refaktorisieren Sie den folgenden Code, indem Sie Guard Clauses verwenden.
```python
def login(user):
    if user.account_exists:
        if not user.account_locked:
            print("Login erfolgreich.")
        else:
            print("Account gesperrt.")
    else:
        print("Account existiert nicht.")
```
**Ziel:** Vereinfachen Sie den Code durch die Verwendung von Guard Clauses.

### Aufgabe 2 🌶️🌶️
Optimieren Sie diesen Code mit Guard Clauses für eine klarere Struktur.
```python
def discount_eligibility(order):
    if order.customer.is_member:
        if order.total >= 100:
            print("Rabatt gewährt.")
        else:
            print("Mindestbestellwert nicht erreicht.")
    else:
        print("Nur für Mitglieder.")
```
**Ziel:** Verbessern Sie die Lesbarkeit und verringern Sie die Verschachtelung des Codes.

## Weiterführende Ressourcen
- [Refactoring.Guru: Replacing Nested Conditional with Guard Clauses](https://refactoring.guru/replace-nested-conditional-with-guard-clauses)
- [Martin Fowler: Replace Nested Conditional with Guard Clauses](https://martinfowler.com/bliki/GuardClause.html)

## Fazit
Guard Clauses bieten eine einfache, aber effektive Möglichkeit, die Klarheit und Qualität von Code zu verbessern. Durch ihre Anwendung wird der Code nicht nur sauberer und wartbarer, sondern fördert auch ein tieferes Verständnis für die Bedingungen, unter denen bestimmte Codepfade ausgeführt werden.