# Lösung

## Modellierung eines Domain-Modells für ein Autohaus
- **Entitäten und Wertobjekte:**
  - **Kunde** (Entität)
    - **Attribute:** `KundenID` (eindeutige Identität), `Name`, `Adresse` (Wertobjekt)
    - **Methoden:** 
      - `KaufeAuto()`: ermöglicht einem Kunden, ein Auto zu kaufen.
      - `FordereReparatur()`: ermöglicht einem Kunden, eine Reparatur zu beantragen.
  
  - **Auto** (Entität)
    - **Attribute:** `FahrzeugID` (eindeutige Identität), `Modell`, `Herstellungsjahr`
    - **Methoden:**
      - `WirdVerkauft()`: ändert den Status des Autos beim Verkauf.
      - `WirdRepariert()`: ändert den Status des Autos bei einer Reparatur.

  - **Reparaturauftrag** (Entität)
    - **Attribute:** `AuftragsID` (eindeutige Identität), `Beschreibung`, `Status`
    - **Methoden:**
      - `ErstelleAuftrag()`: erstellt einen neuen Reparaturauftrag.
      - `SchließeAuftrag()`: schließt einen bestehenden Reparaturauftrag ab.

  - **Adresse** (Wertobjekt)
    - **Attribute:** `Straße`, `Stadt`, `PLZ`
    - Keine eigenständige Identität, wird in Verbindung mit anderen Entitäten wie Kunden oder Lieferanten verwendet.

- **Aggregate:**
  - **Verkaufsauftrag**
    - Enthält Entitäten: `Kunde`, `Auto`
    - **Methoden:**
      - `FühreVerkaufDurch()`: führt den gesamten Verkaufsprozess aus.

- **Repositories:**
  - **KundenRepository**
    - Methoden: `FindeKundenNachID()`, `SpeichereKunden()`
  - **AutoRepository**
    - Methoden: `FindeAutoNachID()`, `AktualisiereAutoStatus()`

### Erklärung
- **Entitäten vs. Wertobjekte:** Entitäten wie `Kunde` und `Auto` haben eine eindeutige Identität (`KundenID`, `FahrzeugID`), die über ihre Lebensdauer hinweg konstant bleibt. Wertobjekte wie `Adresse` haben keine eigene Identität und sind durch ihre Attribute definiert.
- **Aggregate:** Der `Verkaufsauftrag` ist ein Beispiel für ein Aggregate Root, das verschiedene Entitäten zusammenfasst und eine Einheit bildet.
- **Repositories:** Sie bieten eine Abstraktionsschicht für den Zugriff auf Entitäten. `KundenRepository` und `AutoRepository` verwalten die Lebenszyklen ihrer jeweiligen Entitäten.

## Entwicklung eines Bounded Contexts für die Lagerverwaltung
- **Lagerverwaltung** (Bounded Context)
  - Verantwortlich für die Verwaltung von Lagerbeständen und die Nachverfolgung von Bauteilen.

- **Entitäten im Bounded Context:**
  - **Lagereinheit**
    - **Attribute:** `LagerID`, `Bezeichnung`, `Kapazität`
    - **Methoden:** `AktualisiereBestand()`
  - **Bauteil**
    - **Attribute:** `Teilenummer`, `Bezeichnung`, `Verfügbarkeit`
    - **Methoden:** `RegistriereNeuesBauteil()`, `AktualisiereBestand()`
  - **Lieferant**
    - **Attribute:** `LieferantenID`, `Name`, `Kontaktinformationen`
    - **Methoden:** `BestelleBauteile()`

- **Ubiquitous Language:**
  - Begriffe wie `Lagerplatz`, `Bestandsführung`, `Teilenummer`, `Nachbestellung` werden einheitlich verwendet, um Klarheit und Konsistenz im Team zu gewährleisten.

- **Repository:**
  - **BauteilRepository**
    - **Methoden:** `FindeBauteilNachTeilenummer()`, `AktualisiereBauteilBestand()`

### Erklärung
- **Bounded Context:** Der Bounded Context `Lagerverwaltung` definiert die Grenzen, innerhalb derer das spezifische Domain-Modell für die Lagerverwaltung gültig ist. Es isoliert die Geschäftslogik, die sich speziell auf Lagerverwaltung bezieht.
- **Ubiquitous Language:** Wichtig für die effektive Kommunikation im Team. Stellt sicher, dass alle Teammitglieder dieselbe Sprache sprechen und dass technische und geschäftliche Begriffe konsistent verwendet werden.
- **Entitäten und Repositories:** Entitäten wie `Lagereinheit` und `Bauteil` repräsentieren die Kernobjekte im Lagerverwaltungssystem. Die Repositories bieten eine Schnittstelle zum Zugriff auf diese Entitäten und ermöglichen es, komplexe Geschäftslogik von der Datenzugriffsschicht zu trennen.