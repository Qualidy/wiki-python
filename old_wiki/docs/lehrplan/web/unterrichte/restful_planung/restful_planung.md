# Planung einer RESTful API in Flask

[60 min]

## Schritt 1: Zieldefinition und Funktionsumfang

**Ermittlung der Kernfunktionen**: Definiere die Hauptaufgaben, die Ihre API erfüllen soll. Ein Beispiel könnte das Verwalten von Benutzerkonten, das Posten von Nachrichten in einem sozialen Netzwerk oder das Abwickeln von Transaktionen in einem E-Commerce-System sein.

**Anwendungsfälle identifizieren**: Überlege, welche Aktionen die Benutzer durchführen sollen. Dazu gehören das Erstellen, Lesen, Aktualisieren und Löschen von Daten (CRUD-Operationen).

**Sicherheitsmaßnahmen planen**: Überlege, ob und wie die API gesichert wird. Das könnte z.B. über Authentifizierungstoken, OAuth oder andere Mechanismen funktionieren. Hierfür gibt es Flask-Erweiterungen wie Flask-JWT oder Flask-OAuthlib.

## Schritt 2: Datenmodellierung

**Datenstruktur festlegen**: Definiere, wie die Daten strukturiert sein sollen. Welche Attribute hat beispielsweise ein Benutzer? Name, E-Mail, Passwort usw. sind gängige Felder.

**Beziehung zwischen Datenmodellen**: Bestimme die Beziehungen zwischen den Modellen. Zum Beispiel könnte ein Benutzer mehrere Bestellungen haben, und jede Bestellung könnte mehrere Produkte enthalten.

**Datenbankintegration mit SQLAlchemy**:
Flask arbeitet nicht direkt mit einer Datenbank, aber z.B. kann SQLAlchemy verwendet werden, um Modelle zu definieren, die Ihre Datenstrukturen repräsentieren.

### Tabelle: Users

| Feld | Datentyp | Einschränkungen |
|------|----------|-----------------|
| id   | INTEGER  | PRIMARY KEY, AUTOINCREMENT |
| name | VARCHAR(100) | NOT NULL |

### Tabelle: Products

| Feld | Datentyp | Einschränkungen |
|------|----------|-----------------|
| id   | INTEGER  | PRIMARY KEY, AUTOINCREMENT |
| name | VARCHAR(150) | NOT NULL |

### Tabelle: Reviews

| Feld | Datentyp | Einschränkungen |
|------|----------|-----------------|
| id   | INTEGER  | PRIMARY KEY, AUTOINCREMENT |
| product_id | INTEGER | FOREIGN KEY (products.id), NOT NULL |
| review_text | TEXT | NOT NULL |
| user_id | INTEGER | FOREIGN KEY (users.id), NOT NULL |

## Schritt 3: Endpoint-Strukturierung

**Ressourcenbasiertes Design**: RESTful APIs sind in der Regel ressourcenorientiert. Dies bedeutet, dass die Endpoints um die Ressourcen (wie Benutzer, Produkte, Nachrichten) herum strukturiert werden sollten. Zum Beispiel also wie folgend.

### Benutzer-Endpoints

1. **Auflisten aller Benutzer**
   - **Endpoint:** `GET /users`
   - **Beschreibung:** Gibt eine Liste aller Benutzer zurück.
   - **Parameter:** Keine
   - **Rückgabe:** Liste von Benutzerobjekten.

2. **Erstellen eines neuen Benutzers**
   - **Endpoint:** `POST /users`
   - **Beschreibung:** Erstellt einen neuen Benutzer.
   - **Parameter:** Benutzerdaten im Request Body (z.B. Name, E-Mail, Passwort).
   - **Rückgabe:** Details des erstellten Benutzers.

3. **Abrufen eines spezifischen Benutzers**
   - **Endpoint:** `GET /users/{id}`
   - **Beschreibung:** Gibt Details eines spezifischen Benutzers zurück.
   - **Parameter:** Benutzer-ID
   - **Rückgabe:** Benutzerobjekt.

4. **Aktualisieren eines spezifischen Benutzers**
   - **Endpoint:** `PUT /users/{id}`
   - **Beschreibung:** Aktualisiert die Daten eines spezifischen Benutzers.
   - **Parameter:** Benutzer-ID und aktualisierte Daten im Request Body.
   - **Rückgabe:** Aktualisierte Benutzerdaten.

5. **Löschen eines spezifischen Benutzers**
   - **Endpoint:** `DELETE /users/{id}`
   - **Beschreibung:** Löscht einen spezifischen Benutzer.
   - **Parameter:** Benutzer-ID
   - **Rückgabe:** Bestätigung des Löschvorgangs.

### Produkt-Endpoints

1. **Produktdetails abrufen**
   - **Endpoint:** `GET /products/{id}`
   - **Beschreibung:** Gibt Details eines spezifischen Produkts zurück.
   - **Parameter:** Produkt-ID
   - **Rückgabe:** Produktdetails.

2. **Bewertungen für ein Produkt auflisten**
   - **Endpoint:** `GET /products/{id}/reviews`
   - **Beschreibung:** Listet alle Bewertungen für ein spezifisches Produkt auf.
   - **Parameter:** Produkt-ID
   - **Rückgabe:** Liste von Bewertungen.

3. **Eine Bewertung zu einem Produkt hinzufügen**
   - **Endpoint:** `POST /products/{id}/reviews`
   - **Beschreibung:** Fügt eine neue Bewertung zu einem Produkt hinzu.
   - **Parameter:** Produkt-ID und Bewertungsdetails im Request Body.
   - **Rückgabe:** Details der hinzugefügten Bewertung.
