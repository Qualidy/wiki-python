function erstelleUmfrage() {
  var form = FormApp.create("PCEP/PCAP Selbsteinschätzung");
  form.setDescription(
    "Diese Umfrage hilft uns, den Unterricht gezielt auf eure Bedürfnisse auszurichten. " +
    "Bitte schätzt ehrlich ein, wie sicher ihr euch bei den einzelnen Themen fühlt.\n\n" +
    "Skala: 1 = sehr unsicher, 5 = sehr sicher"
  );
  form.setIsQuiz(false);
  form.setAllowResponseEdits(true);

  // ============================================================
  // Abschnitt 1: Zertifizierungsziel
  // ============================================================
  form.addMultipleChoiceItem()
    .setTitle("Welche Zertifizierung traust du dir aktuell zu?")
    .setChoiceValues(["PCEP", "PCAP", "Unsicher", "Keine von beiden"])
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle("Wie sicher fühlst du dich insgesamt in Python?")
    .setChoiceValues([
      "1 – Ich habe noch große Lücken",
      "2 – Grundlagen sitzen, aber vieles ist noch wackelig",
      "3 – Ich fühle mich okay, brauche aber noch Übung",
      "4 – Ich fühle mich recht sicher",
      "5 – Ich bin sehr sicher"
    ])
    .setRequired(true);

  // ============================================================
  // Abschnitt 2: PCEP-Grundlagen
  // ============================================================
  form.addPageBreakItem()
    .setTitle("PCEP-Grundlagen")
    .setHelpText("Grundlegende Python-Kenntnisse (PCEP-Niveau 🔵).\n1 = sehr unsicher, 5 = sehr sicher");

  var pcepThemen = [
    "Variablen & Datentypen (int, float, str, bool)",
    "Typumwandlung (type casting)",
    "Operatoren (arithmetisch, Vergleich, logisch, bitweise)",
    "if / elif / else – Bedingte Anweisungen",
    "for-Schleifen (inkl. range())",
    "while-Schleifen (inkl. break, continue)",
    "Listen (erstellen, indexieren, slicen, Methoden)",
    "Tupel (Unterschied zu Listen, Immutability)",
    "Dictionaries (Keys, Values, Methoden)",
    "Sets (Mengenoperationen, Unterschied zu Listen)",
    "Funktionen definieren & aufrufen",
    "Parameter & Rückgabewerte (return)",
    "Scope (lokale vs. globale Variablen, global-Keyword)"
  ];

  pcepThemen.forEach(function(thema) {
    form.addScaleItem()
      .setTitle(thema)
      .setBounds(1, 5)
      .setLabels("sehr unsicher", "sehr sicher")
      .setRequired(true);
  });

  // ============================================================
  // Abschnitt 3: OOP (45% der PCAP-Prüfung)
  // ============================================================
  form.addPageBreakItem()
    .setTitle("OOP – Objektorientierte Programmierung")
    .setHelpText("Größter Prüfungsblock: 45% der PCAP-Prüfung 🟠.\n1 = sehr unsicher, 5 = sehr sicher");

  var oopThemen = [
    "Klassen & Objekte erstellen",
    "Instanzattribute vs. Klassenattribute",
    "Methoden (Instanzmethoden, self)",
    "Konstruktor (__init__)",
    "Einfache Vererbung",
    "Mehrfachvererbung",
    "MRO (Method Resolution Order)",
    "super() verwenden",
    "Dunder-Methoden (__str__, __repr__, __len__, __add__, ...)",
    "Abstrakte Klassen (abc-Modul)",
    "Polymorphismus (Methoden überschreiben)",
    "isinstance() vs. type()",
    "Kapselung (public, _protected, __private / Name Mangling)",
    "Komposition vs. Vererbung"
  ];

  oopThemen.forEach(function(thema) {
    form.addScaleItem()
      .setTitle(thema)
      .setBounds(1, 5)
      .setLabels("sehr unsicher", "sehr sicher")
      .setRequired(true);
  });

  // ============================================================
  // Abschnitt 4: Strings & Exceptions (18%)
  // ============================================================
  form.addPageBreakItem()
    .setTitle("Strings & Exceptions")
    .setHelpText("18% der PCAP-Prüfung 🟠.\n1 = sehr unsicher, 5 = sehr sicher");

  var strExcThemen = [
    "String-Methoden (split, join, strip, replace, find, ...)",
    "String-Formatierung (f-Strings, .format())",
    "try / except – Grundlagen",
    "try / except / else / finally – vollständiger Block",
    "Mehrere except-Blöcke & Exception-Hierarchie",
    "Eigene Exceptions schreiben (class MyError(Exception))",
    "raise – Exceptions gezielt auslösen",
    "Eingebaute Exceptions kennen (ValueError, TypeError, KeyError, ...)"
  ];

  strExcThemen.forEach(function(thema) {
    form.addScaleItem()
      .setTitle(thema)
      .setBounds(1, 5)
      .setLabels("sehr unsicher", "sehr sicher")
      .setRequired(true);
  });

  // ============================================================
  // Abschnitt 5: Dateien, os, datetime (25%)
  // ============================================================
  form.addPageBreakItem()
    .setTitle("Dateien, os & datetime")
    .setHelpText("25% der PCAP-Prüfung 🟠.\n1 = sehr unsicher, 5 = sehr sicher");

  var dateiThemen = [
    "Dateien öffnen & lesen (open, read, readlines)",
    "Dateien schreiben (write, writelines)",
    "Dateimodi verstehen (r, w, a, r+, b)",
    "with-Statement (Context Manager)",
    "os-Modul (Pfade, Verzeichnisse, os.path)",
    "datetime-Modul (date, time, datetime, timedelta)"
  ];

  dateiThemen.forEach(function(thema) {
    form.addScaleItem()
      .setTitle(thema)
      .setBounds(1, 5)
      .setLabels("sehr unsicher", "sehr sicher")
      .setRequired(true);
  });

  // ============================================================
  // Abschnitt 6: Module & pip (12%)
  // ============================================================
  form.addPageBreakItem()
    .setTitle("Module & pip")
    .setHelpText("12% der PCAP-Prüfung 🟠.\n1 = sehr unsicher, 5 = sehr sicher");

  var modulThemen = [
    "import-Varianten (import x, from x import y, as-Alias)",
    "Eigene Module & Packages erstellen",
    "__name__ == '__main__' verstehen",
    "pip (Pakete installieren, requirements.txt)",
    "venv (virtuelle Umgebungen erstellen & nutzen)"
  ];

  modulThemen.forEach(function(thema) {
    form.addScaleItem()
      .setTitle(thema)
      .setBounds(1, 5)
      .setLabels("sehr unsicher", "sehr sicher")
      .setRequired(true);
  });

  // ============================================================
  // Abschnitt 7: Weitere Themen
  // ============================================================
  form.addPageBreakItem()
    .setTitle("Weitere Themen")
    .setHelpText("Ergänzende Themen, die im Kurs vorkommen.\n1 = sehr unsicher, 5 = sehr sicher");

  var weitereThemen = [
    "List Comprehensions",
    "Dict & Set Comprehensions",
    "Lambda-Funktionen",
    "Generatoren (yield, Generator Expressions)",
    "Dekoratoren (@decorator)",
    "*args und **kwargs",
    "Rekursion"
  ];

  weitereThemen.forEach(function(thema) {
    form.addScaleItem()
      .setTitle(thema)
      .setBounds(1, 5)
      .setLabels("sehr unsicher", "sehr sicher")
      .setRequired(true);
  });

  // ============================================================
  // Abschnitt 8: Offene Fragen
  // ============================================================
  form.addPageBreakItem()
    .setTitle("Feedback & Wünsche")
    .setHelpText("Hier kannst du uns frei Rückmeldung geben.");

  form.addParagraphTextItem()
    .setTitle("Bei welchem Thema wünschst du dir am meisten Unterstützung?")
    .setRequired(false);

  form.addParagraphTextItem()
    .setTitle("Gibt es etwas, das im Kurs bisher zu kurz kam?")
    .setRequired(false);

  form.addParagraphTextItem()
    .setTitle("Sonstige Anmerkungen oder Wünsche?")
    .setRequired(false);

  // ============================================================
  // Ergebnis ausgeben
  // ============================================================
  Logger.log("Formular erstellt!");
  Logger.log("URL zum Bearbeiten: " + form.getEditUrl());
  Logger.log("URL zum Ausfüllen:  " + form.getPublishedUrl());
}
