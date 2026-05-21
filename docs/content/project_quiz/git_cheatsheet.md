# Git Cheat Sheet – Schnelle Referenz

Ein kompakter Überblick über die wichtigsten Git-Befehle für dieses Projekt.

---

## 🔧 Initial Setup (einmalig)

### Repository klonen
```bash
git clone https://github.com/username/pcep-quiz.git
cd pcep-quiz
```

### Konfiguration (lokal für dieses Projekt)
```bash
git config user.name "Max Mustermann"
git config user.email "max@example.com"
```

### Globale Konfiguration (nur einmalig nötig)
```bash
git config --global user.name "Max Mustermann"
git config --global user.email "max@example.com"
```

---

## 📌 Wichtige Befehle im Workflow

### 1️⃣ Feature-Branch erstellen
```bash
git checkout -b feature/quiz-engine
# oder (modernere Syntax):
git switch -c feature/quiz-engine
```

**Naming-Konvention:**
- `feature/` – neue Funktion
- `fix/` – Bugfix
- `refactor/` – Code-Verbesserung
- `docs/` – Dokumentation

Beispiele:
```bash
git checkout -b feature/quiz-engine
git checkout -b feature/statistics
git checkout -b feature/main-menu
```

---

### 2️⃣ Status anschauen
```bash
git status
```

Zeigt:
- Geänderte Dateien
- Neue Dateien (untracked)
- Staged Changes

---

### 3️⃣ Änderungen hinzufügen (staging)
```bash
# Alle Änderungen staging
git add .

# Nur bestimmte Datei
git add quiz_engine.py

# Interaktiv (einzelne Teile wählen)
git add -p
```

---

### 4️⃣ Commit erstellen
```bash
# Mit Message
git commit -m "feat: add run_quiz function with basic loop"

# Interaktiv (öffnet Editor)
git commit
```

**Gutes Commit-Format:**
```
<type>: <kurze Beschreibung>

<längere Erklärung (optional)>
```

**Beispiele:**
```bash
git commit -m "feat: add question display function"
git commit -m "fix: validate user input in get_answer"
git commit -m "refactor: split main into smaller functions"
git commit -m "docs: add type hints to quiz_engine"
```

---

### 5️⃣ Changes anschauen (vor Commit)
```bash
# Unstaged changes anschauen
git diff

# Staged changes anschauen
git diff --staged

# Kompletter Diff zur main branch
git diff main
```

---

### 6️⃣ Commit-Historik anschauen
```bash
# Einfache Liste
git log

# Kompakte Darstellung (empfohlen!)
git log --oneline

# Mit Branches visualisieren
git log --graph --oneline --all

# Letzten 5 Commits
git log -5
```

Beispiel-Output:
```
* a1b2c3d feat: add statistics module
* d4e5f6g feat: add main menu
* h7i8j9k feat: complete quiz_engine
* l0m1n2o feat: add questions.py
```

---

### 7️⃣ Push zum Remote (GitHub)
```bash
# Beim ersten Push (upstream setzen)
git push -u origin feature/quiz-engine

# Danach einfach
git push

# Spezifischen Branch pushen
git push origin feature/quiz-engine
```

---

### 8️⃣ Pull Request erstellen (GitHub)

1. Auf GitHub gehen
2. "Compare & pull request" Button erscheint
3. Title & Description ausfüllen
4. "Create pull request" klicken

Oder via CLI:
```bash
gh pr create --title "Add quiz engine" --body "Implements core quiz loop"
```

---

### 9️⃣ Branches anschauen
```bash
# Lokale Branches
git branch

# Alle Branches (auch remote)
git branch -a

# Welcher Branch bin ich gerade?
git branch --show-current
```

---

### 🔟 Zu anderen Branch wechseln
```bash
git checkout main
# oder (modern):
git switch main
```

---

## 🔄 Häufige Workflows

### Workflow 1: Feature entwickeln & pushen

```bash
# 1. Feature-Branch erstellen
git checkout -b feature/quiz-engine

# 2. Code schreiben
# ... editiere quiz_engine.py ...

# 3. Status anschauen
git status

# 4. Änderungen staging
git add quiz_engine.py

# 5. Commit
git commit -m "feat: add run_quiz function"

# 6. Mehr Code schreiben
# ... editiere quiz_engine.py weiter ...

# 7. Erneut Add & Commit
git add .
git commit -m "feat: add display_question function"

# 8. Push
git push -u origin feature/quiz-engine

# 9. Am nächsten Tag: neuer Code
# ... editiere quiz_engine.py ...
git add .
git commit -m "feat: add result display"
git push
```

---

### Workflow 2: Änderungen verwerfen

```bash
# Unstaged Änderungen verwerfen (VOR git add)
git restore quiz_engine.py
# oder:
git checkout quiz_engine.py

# Staged Änderungen unstagen (nach git add, vor git commit)
git restore --staged quiz_engine.py

# Letzte 1 Commit rückgängig machen (nur lokal!)
git reset --soft HEAD~1
```

⚠️ **Vorsicht:** Folgende Commands sind destruktiv:
```bash
git reset --hard HEAD~1    # Commits + Code löschen!
git revert HEAD            # Sicherer: neuer Commit der Änderungen rückgängig macht
```

---

### Workflow 3: Main mit neuesten Änderungen updaten

```bash
# 1. Auf main wechseln
git checkout main

# 2. Neueste Änderungen vom Remote holen
git pull origin main
# oder einfach:
git pull

# 3. Zurück zum Feature-Branch
git checkout feature/quiz-engine
```

---

### Workflow 4: Merge (nach Pull Request Approval)

```bash
# 1. Auf main wechseln
git checkout main

# 2. Branch pullen (falls nicht lokal)
git pull origin main

# 3. Feature-Branch mergen
git merge feature/quiz-engine

# 4. Push
git push origin main

# 5. Feature-Branch löschen (optional)
git branch -d feature/quiz-engine
```

---

## 🆘 Häufige Fehler & Lösungen

### Problem: "fatal: your current branch is ahead of 'origin/main'"

```bash
# Einfach pushen
git push
```

---

### Problem: "fatal: refusing to merge unrelated histories"

```bash
# Beim klonen passiert → nicht relevant bei diesem Projekt
```

---

### Problem: Falscher Name oder Email in Commit

```bash
# Letzten Commit korrigieren
git commit --amend --author="Neuer Name <neuer@email.com>"

# Global wechseln (zukünftige Commits)
git config --global user.name "Richtiger Name"
```

---

### Problem: Falsche Datei gecomiitet

```bash
# Vor dem Push rückgängig machen
git reset --soft HEAD~1
git restore --staged falsche_datei.py
git commit -m "feat: correct commit message"
git push
```

---

### Problem: Merge Conflicts

```bash
# Conflict anschauen
git status

# Datei öffnen und konflikt manuell lösen
# Dann:
git add .
git commit -m "fix: resolve merge conflict"
git push
```

---

## 📊 Nützliche Kombinationen

### Gesamte Repository-Historie visualisieren
```bash
git log --graph --oneline --all --decorate
```

### Änderungen seit letztem Commit anschauen
```bash
git diff HEAD
```

### Alle Commits eines Authors
```bash
git log --author="Max Mustermann"
```

### Commits mit Keyword suchen
```bash
git log --grep="quiz"
```

---

## 🎯 Best Practices

✅ **DO:**
- Oft committen (nach jeder Funktion)
- Aussagekräftige Commit-Messages schreiben
- Vor dem Push `git log` checken
- Regelmäßig `git pull` machen
- Feature-Branches für neue Features nutzen

❌ **DON'T:**
- Große Changesets in 1 Commit
- "fixed" oder "update" als Messages
- Auf main direkt committen
- Vergessen zu pushen
- Andere Branches löschen ohne Grund

---

## 📚 Weitere Infos

- Interaktives Tutorial: https://learngitbranching.js.org/
- Offizielle Git Docs: https://git-scm.com/doc
- GitHub Guides: https://guides.github.com/

---

**Happy Committing! 🎉**
