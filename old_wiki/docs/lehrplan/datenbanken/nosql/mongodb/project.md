# Aufgabe: Kanban Board mit Flask und PyMongo 🌶🌶🌶
[1 - 2 Tage]

Erweitere das zuvor erstellte ToDo-Liste-Projekt, um ein Kanban Board als Webanwendung mit Flask zu entwickeln. Das Board soll es Benutzern ermöglichen, Aufgaben in verschiedenen Phasen zu organisieren, z.B., "To Do", "In Progress", "Done".

**Schritte:**

1. **Flask-App erstellen:**🌶
    - Erstelle eine Flask-Anwendung mit einer Startseite und den erforderlichen Routen für die Anzeige des Kanban Boards.

2. **Datenbankanbindung mit PyMongo:** 🌶
    - Verwende PyMongo, um eine Verbindung zur MongoDB-Datenbank herzustellen, in der die Aufgaben gespeichert werden.

3. **HTML-Vorlagen erstellen:** 🌶🌶
    - Erstelle HTML-Vorlagen für die verschiedenen Ansichten des Kanban Boards (z.B., "To Do", "In Progress", "Done").
    - Nutze Bootstrap oder andere CSS-Frameworks, um das Design zu verbessern.

4. **Flask-Routen implementieren:** 🌶🌶
    - Implementiere Flask-Routen für das Anzeigen von Aufgaben in verschiedenen Phasen des Kanban Boards.
    - Beispiel: `/board/todo`, `/board/in_progress`, `/board/done`.

5. **Flask-Formulare für CRUD-Aktionen:** 🌶🌶
    - Integriere Flask-Formulare, um Benutzern das Hinzufügen, Aktualisieren und Löschen von Aufgaben direkt über die Webanwendung zu ermöglichen.

6. **Drag-and-Drop-Funktionalität (optional):** 🌶🌶🌶🌶
    - Erweitere die Webanwendung um Drag-and-Drop-Funktionalität, um Aufgaben zwischen verschiedenen Phasen des Kanban Boards zu verschieben.

7. **Benutzerauthentifizierung (optional):** 🌶🌶🌶
    - Implementiere eine einfache Benutzerauthentifizierung, um sicherzustellen, dass nur authentifizierte Benutzer das Kanban Board nutzen können.

8. **Hosting (optional):** 🌶🌶🌶🌶
    - Hoste die Webanwendung in Azure.


# Lösung
- [Hier](kanban-board.zip) herunterladen.

## offline-Version

- `forms/`
    - [`tasks.py`](./kanban-board/forms/tasks.py)
    - [`update_task.py`](./kanban-board/forms/update_task.py)
- `static/`
    - [`create_task_style.css`](./kanban-board/static/css/create_task_style.css)
    - [`update_task.css`](./kanban-board/static/css/update_task.css)
- `templates/` (**_ggf. Inspect-Modus des Browsers verwenden!!_**)
    - [`create_task.html`](./kanban-board/templates/create_task.html)
    - [`done_board.html`](./kanban-board/templates/done_board.html)
    - [`in_progress_board.html`](./kanban-board/templates/in_progress_board.html)
    - [`kanban_board.html`](./kanban-board/templates/kanban_board.html)
    - [`todo_board.html`](./kanban-board/templates/todo_board.html)
    - [`update_task.html`](./kanban-board/templates/update_task.html)
- `utils/`
    - [`database.py`](kanban-board/utils/database.py)
- [`app.py`](./kanban-board/app.py)
- [`docker-compose.yaml`](./kanban-board/docker-compose.yaml)