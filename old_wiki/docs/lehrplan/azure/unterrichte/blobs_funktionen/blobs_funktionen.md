# Exkurs: Blobs und Funktionen

[60 min]

Azure Blob Storage ist ein Objektspeicherdienst von Microsoft Azure, der zum Speichern großer Mengen unstrukturierter Daten, wie Text- oder Binärdaten, dient. Blobs werden in "Containern" (auch als **"Buckets"** bezeichnet) organisiert.

Um eine Blob-Datei in einen Bucket hochzuladen wird die Azure Python Library verwendet.

**Container Erstellung**:

```python
from azure.storage.blob import BlobServiceClient
service_client = BlobServiceClient.from_connection_string("your_connection_string")
container_client = service_client.create_container("your_container_name")
```

**Blob Upload**:

```python
blob_client = container_client.get_blob_client("your_blob_name")

# blobs sind binäre daten, deshalb nutzen wir hier rb - read binary
with open("your_file_path", "rb") as data:
    blob_client.upload_blob(data)
```

## Microtasks mit Azure Functions

Azure Functions ist ein serverloser Berechnungsdienst, der es ermöglicht, Code in Reaktion auf Ereignisse zu schreiben und auszuführen, ohne sich um die Infrastruktur kümmern zu müssen.

Hierfür gibt es verschiedene Event-Trigger für unterschiedliche Anwendungsfälle. 

- **Blob-Trigger**: Reagiert, wenn ein Blob in Azure Storage erstellt oder aktualisiert wird.
- **HTTP-Trigger**: Reagiert auf HTTP-Anfragen.

Auch hier nutzen wir die Azure Python Library um die Funktion lokal entwickeln zu können und dann über ein deployment in der Cloud verfügbar zu machen.

```python
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    name = req.params.get('name')
    if not name:
        return func.HttpResponse(f"Bitte einen Namen im Query-String oder im Request-Body angeben.")
    return func.HttpResponse(f"Hallo, {name}!")
```

## Aufgaben

[60 min]

### Simpler Blob Store Upload 🌶️️🌶️️

Erstelle ein Azure Speicherkonto und einen Container. Schreibe dann ein Skript, um eine Datei in den Blob Container hochzuladen.

### Hallo Welt! der Azure Funktionen 🌶️️🌶️️

Erstelle eine einfache HTTP-Trigger-Funktion, die einen Namen als Parameter akzeptiert und eine Begrüßung zurückgibt.

### Blob-Triggered Azure Funktion 🌶️️🌶️️🌶️️

Erweitere die Funktion, um auf einen Blob-Trigger zu reagieren, der eine Textdatei liest und deren Inhalt zurückgibt.

## Komplex-Aufgabe: Simples Excel Zeittracking (2er Teams) 🌶️️🌶️️🌶️️🌶️️🌶️️

[240 min]

Erstelle einen simplen Dokumentupload für eine Zeiterfassungs-Excel Dokument. Sobald das Dokument im Blob Store liegt, wird eine Azure Funktion getriggert, die die Stunden pro Woche summiert und die Über- oder Fehlstunden für den angegebenen Monat anzeigt.

Das hochgeladene Excel Dokument soll dem folgendem Format folgen.
|Woche|M|D|M|D|F|
|-|-|-|-|-|-|
|1|8|7|9|9|5|
|2|8|7|9|9|5|
|3|8|7|9|9|5|
|4|8|7|9|9|5|
