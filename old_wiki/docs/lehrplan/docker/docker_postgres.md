# Postgresql Datenbank mit Docker


Wir können Docker verwenden, um eine Postgres-Datenbank zu starten. Dies ist besonders nützlich, wenn wir eine Datenbank für unsere Anwendung benötigen, aber nicht möchten, dass sie auf unserem lokalen System installiert wird. Außerdem könen wir somit die Datenbank leichter in unsere CI/CD-Pipeline integrieren.

## Postgres Docker Image

Postgres bietet ein offizielles Docker-Image, das wir verwenden können. Dieses Image enthält alles, was wir benötigen, um eine Postgres-Datenbank zu starten. Wir können das Image von Docker Hub herunterladen und starten, indem wir den folgenden Befehl ausführen:

```bash
docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d -p <DEIN_PORT>:5432 postgres
```

In diesem Befehl verwenden wir die folgenden Optionen:

- `--name some-postgres`: Gibt dem Container den Namen `some-postgres`.
- `-e POSTGRES_PASSWORD=mysecretpassword`: Setzt das Passwort für den Postgres-Benutzer `postgres
- `-d`: Startet den Container im Hintergrund.
- `-p <DEIN_PORT>:5432`: Veröffentlicht den Port 5432 des Containers auf den angegebenen Port auf dem Host-System.
- `postgres`: Der Name des Docker-Images, das wir verwenden möchten.


## Verbindung zur Postgres-Datenbank

Nachdem der Container gestartet wurde, können wir auf die Postgres-Datenbank über den angegebenen Port zugreifen. Dies können wir beispielsweise über einen SQL Editor oder das Plugin SQLTools in VSCode tun.

![sql_editor](sql_editor.png)

Ebenso können wir uns beispielsweise mit SQLAlchemy in Python verbinden. Dafür passen wir einfach den connection string an:

```python
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:mysecretpassword@localhost:<DEIN_PORT>/postgres')
```