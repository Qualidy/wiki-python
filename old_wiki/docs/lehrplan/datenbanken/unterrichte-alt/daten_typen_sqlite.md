# Datentypen in SQLite
[20min]

SQLite verwendet ein dynamisches Typensystem, das sich von den meisten anderen SQL-Datenbanken unterscheidet. In SQLite
wird der Datentyp eines Wertes hauptsächlich durch den Wert selbst bestimmt, nicht durch die Spalte, in der der Wert
gespeichert ist. Trotzdem gibt es eine Reihe von Datentypen, die Sie in der Spaltendefinition verwenden können. Hier ist
eine vollständige Liste der Datentypen in SQLite:

1. **TEXT:** Für Textdaten. SQLite speichert Textdaten basierend auf der Kodierung der Datenbank (UTF-8, UTF-16BE oder
   UTF-16LE).

2. **INTEGER:** Für ganze Zahlen. Abhängig vom Wert kann SQLite ganze Zahlen in 1, 2, 3, 4, 6 oder 8 Bytes speichern.

3. **REAL:** Für Fließkommazahlen. SQLite speichert diese im 8-Byte-IEEE-Fließkommaformat.

4. **BLOB:** Für binäre Daten (Binary Large Object). Daten dieses Typs werden exakt so gespeichert, wie sie eingegeben
   wurden.

5. **NUMERIC:** Ein flexibler Typ für Zahlen. SQLite wählt den internen Typ (INTEGER, REAL, TEXT) basierend auf dem
   Wert.

6. **BOOLEAN:** SQLite hat keinen separaten Booleschen Datentyp. Stattdessen werden Boolesche Werte als INTEGER
   gespeichert, wobei 0 für 'false' und 1 für 'true' steht.

7. **DATE und TIME:** SQLite hat keine separaten Datentypen für Datum und Uhrzeit. Stattdessen werden diese als TEXT,
   REAL oder INTEGER gespeichert, abhängig vom gewählten Format.

SQLite verwendet ein flexibles Typensystem, das als "Manifest Typing" bekannt ist. Dies bedeutet, dass der Datentyp
einer Spalte nicht streng festgelegt ist; vielmehr kann jede Spalte Werte verschiedener Datentypen speichern. Die oben
genannten Typen sind Empfehlungen, die SQLite verwendet, um zu entscheiden, wie Daten intern gespeichert werden sollen,
basierend auf dem Typ der eingegebenen Daten.

## Große, binäre Daten-Objekte

SQLite behandelt BLOB-Daten (Binary Large Objects) ähnlich wie andere Datentypen und speichert sie direkt in der
Datenbankdatei. Im Gegensatz zu einigen anderen Datenbanksystemen, die große Objekte wie BLOBs in separaten
Dateisystemdateien auslagern können, speichert SQLite BLOB-Daten zusammen mit anderen Daten in derselben Datenbankdatei.

Einige wichtige Punkte zu BLOBs in SQLite:

1. **Direkte Speicherung:** BLOB-Daten werden innerhalb der SQLite-Datenbankdatei gespeichert. Dies bedeutet, dass die
   Datenbankdatei mit der Zeit anwachsen kann, insbesondere wenn große BLOBs gespeichert werden.

2. **Effizienz:** SQLite ist effizient im Umgang mit BLOB-Daten, solange die Größe der BLOBs angemessen ist. Für sehr
   große BLOBs (z.B. mehrere Megabyte oder Gigabyte) kann es jedoch effizienter sein, diese außerhalb der Datenbank zu
   speichern und in der Datenbank nur einen Verweis (z.B. einen Dateipfad) zu speichern.

3. **Transaktionsintegrität:** Da BLOBs direkt in der Datenbank gespeichert werden, profitieren sie von den
   Transaktions- und Integritätsfunktionen von SQLite. Das bedeutet, dass Änderungen an BLOB-Daten in einer Transaktion
   erfolgen können, was Konsistenz und Datenintegrität gewährleistet.

4. **Größenbeschränkungen:** SQLite hat eine maximale Größenbeschränkung für einzelne BLOBs, die standardmäßig auf 1
   Gigabyte festgelegt ist. Diese Grenze kann jedoch konfiguriert werden.

5. **Streaming:** SQLite unterstützt das Streaming von BLOB-Daten, was bedeutet, dass Sie Teile eines BLOBs lesen oder
   schreiben können, ohne den gesamten BLOB in den Speicher laden zu müssen. Dies ist nützlich für die Arbeit mit großen
   BLOBs.

In der Praxis bedeutet dies, dass SQLite für Anwendungen gut geeignet ist, die mit moderaten Mengen an BLOB-Daten
arbeiten, wie z.B. das Speichern von Bildern, Dokumenten oder anderen Medien, solange die Größe dieser Objekte nicht
extrem groß ist. Für sehr große BLOBs kann es jedoch besser sein, diese außerhalb der Datenbank zu speichern.
