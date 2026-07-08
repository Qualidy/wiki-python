# PCAP-Begriffsübersicht Python

Diese Seite sammelt englische Begriffe, die in PCAP-Fragen vorkommen koennen.
Die zweite Spalte ordnet den Begriff auf Deutsch ein. Die dritte Spalte fuehrt
zu passenden Stellen im Skript und in den Wiederholungen.

## Modules and Packages

| English term | Deutsch / Einordnung | Skriptstellen |
|--------------|----------------------|---------------|
| module | Modul; einzelne Python-Datei oder Bibliothek, die importiert werden kann | [Imports Einfuehrung](../python_grundlagen/module/module.md)<br>[Module und Imports Wiederholung](../wiederholung/module_imports_wiederholung.md) |
| package | Paket; Ordnerstruktur aus Modulen, meist mit `__init__.py` | [Pakete](../module_pakete_pip/pakete/pakete.md)<br>[Module und Imports Wiederholung](../wiederholung/module_imports_wiederholung.md) |
| import statement | Import-Anweisung, z.B. `import`, `from ... import ...`, `as` | [Imports Einfuehrung](../python_grundlagen/module/module.md)<br>[Module und Imports Wiederholung](../wiederholung/module_imports_wiederholung.md) |
| wildcard import | Import mit `*`; importiert oeffentliche Namen aus einem Modul | [Imports Einfuehrung](../python_grundlagen/module/module.md)<br>[Module und Imports Wiederholung](../wiederholung/module_imports_wiederholung.md) |
| qualified name | qualifizierter Name, z.B. `package.module.function` | [Imports Einfuehrung](../python_grundlagen/module/module.md)<br>[Pakete](../module_pakete_pip/pakete/pakete.md) |
| namespace | Namensraum; Zuordnung von Namen zu Objekten | [Imports Einfuehrung](../python_grundlagen/module/module.md)<br>[Scopes](../funktionen_vertiefung/scopes/scopes.md) |
| `dir()` | Funktion zur Anzeige verfuegbarer Namen und Attribute | [Imports Einfuehrung](../python_grundlagen/module/module.md)<br>[Polymorphismus & Introspection](../oop_vertiefung_teil2/polymorphismus_introspection.md) |
| `sys.path` | Suchpfad fuer Module | [Imports Einfuehrung](../python_grundlagen/module/module.md)<br>[Module und Imports Wiederholung](../wiederholung/module_imports_wiederholung.md) |
| `__name__` | Spezialvariable; ist bei direktem Start `"__main__"` | [Pakete](../module_pakete_pip/pakete/pakete.md)<br>[Module und Imports Wiederholung](../wiederholung/module_imports_wiederholung.md) |
| `__pycache__` | Cache-Ordner fuer kompilierten Python-Bytecode | [Pakete](../module_pakete_pip/pakete/pakete.md)<br>[Bytecode](../referenzmaterial/bytecode/bytecode.md) |
| `__init__.py` | Datei, die ein Verzeichnis als Python-Paket kennzeichnet | [Pakete](../module_pakete_pip/pakete/pakete.md) |
| `math` module | Standardmodul fuer mathematische Funktionen | [Mathematische Operationen](../python_grundlagen/math_operations/math_operations.md)<br>[Operatoren und Precedence](../wiederholung_woche8/operatoren_precedence.md) |
| `random` module | Standardmodul fuer Zufallsauswahl und Zufallszahlen | [Imports Einfuehrung](../python_grundlagen/module/module.md)<br>[Module und Imports Wiederholung](../wiederholung/module_imports_wiederholung.md) |
| `platform` module | Standardmodul fuer Informationen zur Laufzeitumgebung | [Module und Imports Wiederholung](../wiederholung/module_imports_wiederholung.md#weitere-pcap-relevante-standardmodule) |
| pip | Paketmanager fuer Python | [Pip und Venv](../module_pakete_pip/pip_venv/pip_venv.md) |
| virtual environment | virtuelle Umgebung zur Trennung von Abhaengigkeiten | [Pip und Venv](../module_pakete_pip/pip_venv/pip_venv.md) |

## Exceptions

| English term | Deutsch / Einordnung | Skriptstellen |
|--------------|----------------------|---------------|
| exception | Ausnahme/Fehlerobjekt waehrend der Programmausfuehrung | [Try-Except](../python_grundlagen/try_except/try_except.md)<br>[Exceptions Wiederholung](../wiederholung/exceptions.md) |
| exception handling | Fehlerbehandlung mit `try` und `except` | [Try-Except](../python_grundlagen/try_except/try_except.md)<br>[Exceptions Vertiefung](../exceptions/index.md) |
| exception hierarchy | Exception-Hierarchie; Vererbung der Fehlerklassen | [Exceptions Vertiefung](../exceptions/index.md)<br>[Exceptions Wiederholung](../wiederholung/exceptions.md) |
| `try` block | Codeblock, in dem ein Fehler auftreten kann | [Try-Except](../python_grundlagen/try_except/try_except.md)<br>[Exceptions Wiederholung](../wiederholung/exceptions.md) |
| `except` block | Fehlerbehandlungsblock | [Try-Except](../python_grundlagen/try_except/try_except.md)<br>[Exceptions Wiederholung](../wiederholung/exceptions.md) |
| multiple `except` clauses | mehrere `except`-Bloecke fuer unterschiedliche Fehlerarten | [Try-Except](../python_grundlagen/try_except/try_except.md)<br>[Exceptions Wiederholung](../wiederholung/exceptions.md) |
| tuple of exceptions | mehrere Exception-Typen in einem `except` als Tupel | [Try-Except](../python_grundlagen/try_except/try_except.md)<br>[Exceptions Wiederholung](../wiederholung/exceptions.md) |
| `else` clause | Block nach `try`/`except`, wenn kein Fehler auftrat | [Try-Except](../python_grundlagen/try_except/try_except.md)<br>[Exceptions Wiederholung](../wiederholung/exceptions.md) |
| `raise` statement | wirft eine Exception aus | [Exceptions Vertiefung](../exceptions/index.md)<br>[Eigene Exceptions](../wiederholung_woche8/eigene_exceptions.md) |
| re-raising | erneutes Werfen einer bereits gefangenen Exception | [Exceptions Vertiefung](../exceptions/index.md)<br>[Eigene Exceptions](../wiederholung_woche8/eigene_exceptions.md) |
| `assert` statement | prueft eine Annahme und wirft ggf. `AssertionError` | [Exceptions Vertiefung](../exceptions/index.md)<br>[Exceptions Wiederholung](../wiederholung/exceptions.md) |
| event class | Ereignisklasse; eigener Exception-Typ fuer einen Fehlerfall | [Exceptions Vertiefung](../exceptions/index.md)<br>[Eigene Exceptions](../wiederholung_woche8/eigene_exceptions.md) |
| exception object | Exception-Objekt, z.B. in `except E as e` | [Try-Except](../python_grundlagen/try_except/try_except.md)<br>[Exceptions Wiederholung](../wiederholung/exceptions.md) |
| custom exception | selbst definierte Exception-Klasse | [Exceptions Vertiefung](../exceptions/index.md)<br>[Eigene Exceptions](../wiederholung_woche8/eigene_exceptions.md) |
| `args` property | Tupel der Argumente einer Exception | [Exceptions Vertiefung](../exceptions/index.md)<br>[Exceptions Wiederholung](../wiederholung/exceptions.md) |

## Strings

| English term | Deutsch / Einordnung | Skriptstellen |
|--------------|----------------------|---------------|
| string | Zeichenkette; Datentyp `str` | [Strings](../python_grundlagen/strings/strings.md) |
| character | einzelnes Zeichen in einem String | [Strings](../python_grundlagen/strings/strings.md)<br>[chr und ord](../wiederholung_woche8/chr_ord.md) |
| ASCII | Zeichencodierung fuer einfache Zeichen | [Strings](../python_grundlagen/strings/strings.md)<br>[chr und ord](../wiederholung_woche8/chr_ord.md) |
| Unicode | Standard fuer Zeichen und Code Points | [Strings](../python_grundlagen/strings/strings.md)<br>[chr und ord](../wiederholung_woche8/chr_ord.md) |
| UTF-8 | haeufige Unicode-Codierung | [Strings](../python_grundlagen/strings/strings.md)<br>[chr und ord](../wiederholung_woche8/chr_ord.md) |
| code point | numerischer Wert eines Unicode-Zeichens | [Strings](../python_grundlagen/strings/strings.md)<br>[chr und ord](../wiederholung_woche8/chr_ord.md) |
| escape sequence | Escape-Sequenz wie `\n`, `\t` oder `\\` | [Strings](../python_grundlagen/strings/strings.md) |
| `ord()` | Funktion: Zeichen zu Code Point | [chr und ord](../wiederholung_woche8/chr_ord.md)<br>[Strings](../python_grundlagen/strings/strings.md) |
| `chr()` | Funktion: Code Point zu Zeichen | [chr und ord](../wiederholung_woche8/chr_ord.md)<br>[Strings](../python_grundlagen/strings/strings.md) |
| indexing | Zugriff auf ein Element per Index | [Strings](../python_grundlagen/strings/strings.md)<br>[Listen, Slices und Sortieren](../wiederholung_woche8/listen_slices_sortieren.md) |
| slicing | Ausschnitt mit `start:stop:step` | [Strings](../python_grundlagen/strings/strings.md)<br>[Listen, Slices und Sortieren](../wiederholung_woche8/listen_slices_sortieren.md) |
| immutability | Unveraenderlichkeit eines Objekts | [Strings](../python_grundlagen/strings/strings.md)<br>[Mutable, Immutable und Referenzen](../wiederholung_woche8/mutable_immutable_referenzen.md) |
| concatenation | Verkettung, z.B. mit `+` | [Strings](../python_grundlagen/strings/strings.md)<br>[Listen](../datenstrukturen/lists/lists.md) |
| repetition | Wiederholung, z.B. `"a" * 3` | [Strings](../python_grundlagen/strings/strings.md)<br>[Listen](../datenstrukturen/lists/lists.md) |
| membership operator | Zugehoerigkeitsoperator `in` oder `not in` | [Strings](../python_grundlagen/strings/strings.md)<br>[Listen](../datenstrukturen/lists/lists.md) |
| string comparison | Stringvergleich, lexikographische Ordnung | [Strings](../python_grundlagen/strings/strings.md)<br>[Operatoren und Precedence](../wiederholung_woche8/operatoren_precedence.md) |
| string method | Methode eines String-Objekts, z.B. `.split()` | [Strings](../python_grundlagen/strings/strings.md) |
| `join()` | verbindet Strings aus einem Iterable | [Strings](../python_grundlagen/strings/strings.md) |
| `split()` | zerlegt einen String in eine Liste | [Strings](../python_grundlagen/strings/strings.md) |
| `find()` / `index()` | Suche nach Teilstrings; Unterschied bei Nichtfinden beachten | [Strings](../python_grundlagen/strings/strings.md) |
| `sorted()` | eingebaute Funktion; erzeugt sortierte Liste | [Strings](../python_grundlagen/strings/strings.md)<br>[Listen, Slices und Sortieren](../wiederholung_woche8/listen_slices_sortieren.md) |
| `.sort()` | Listenmethode; sortiert in-place | [Listen](../datenstrukturen/lists/lists.md)<br>[Listen, Slices und Sortieren](../wiederholung_woche8/listen_slices_sortieren.md) |

## Object-Oriented Programming

| English term | Deutsch / Einordnung | Skriptstellen |
|--------------|----------------------|---------------|
| object-oriented programming | objektorientierte Programmierung | [Klassen definieren](../oop_grundlagen/define_classes/define_classes.md)<br>[OOP Wiederholung](../oop_vertiefung_teil2/oop_wiederholung.md) |
| class | Klasse; Bauplan fuer Objekte | [Klassen definieren](../oop_grundlagen/define_classes/define_classes.md)<br>[OOP Wiederholung](../oop_vertiefung_teil2/oop_wiederholung.md) |
| object | Objekt/Instanz einer Klasse | [Klassen definieren](../oop_grundlagen/define_classes/define_classes.md)<br>[OOP Wiederholung](../oop_vertiefung_teil2/oop_wiederholung.md) |
| instance | konkrete Instanz einer Klasse | [Klassen definieren](../oop_grundlagen/define_classes/define_classes.md)<br>[Attribute](../oop_grundlagen/attributes/attributes.md) |
| property | Eigenschaft eines Objekts; im Kurs auch `@property` | [Attribute](../oop_grundlagen/attributes/attributes.md)<br>[Getter & Setter](../oop_vertiefung/getter_setter/getter_setter.md) |
| attribute | Attribut; gespeicherte Eigenschaft eines Objekts | [Attribute](../oop_grundlagen/attributes/attributes.md)<br>[Klassen, super() und Dunder Methods](../wiederholung/klassen_oop_wiederholung.md) |
| method | Methode; Funktion in einer Klasse | [Methoden](../oop_grundlagen/methods/methods.md)<br>[Klassen, super() und Dunder Methods](../wiederholung/klassen_oop_wiederholung.md) |
| `self` | Referenz auf die aktuelle Instanz | [Methoden](../oop_grundlagen/methods/methods.md)<br>[Klassen, super() und Dunder Methods](../wiederholung/klassen_oop_wiederholung.md) |
| instance variable | Instanzvariable; Attribut eines einzelnen Objekts | [Attribute](../oop_grundlagen/attributes/attributes.md)<br>[Klassen, super() und Dunder Methods](../wiederholung/klassen_oop_wiederholung.md) |
| class variable | Klassenvariable; Attribut der Klasse | [Attribute](../oop_grundlagen/attributes/attributes.md)<br>[Class- & Staticmethod](../oop_vertiefung/class_static_methods/class_static_methods.md) |
| constructor | Konstruktor; in Python meist `__init__` | [Klassen definieren](../oop_grundlagen/define_classes/define_classes.md)<br>[Methoden](../oop_grundlagen/methods/methods.md) |
| initialization | Initialisierung eines Objekts | [Klassen definieren](../oop_grundlagen/define_classes/define_classes.md)<br>[super() in Klassen](../wiederholung_woche8/super_init_methoden.md) |
| encapsulation | Kapselung; Daten und Verhalten zusammenfassen | [Protected & Private](../oop_vertiefung/protected_private/protected_private.md)<br>[Getter & Setter](../oop_vertiefung/getter_setter/getter_setter.md) |
| inheritance | Vererbung | [Vererbung](../oop_vertiefung/vererbung_polymorphismus/vererbung/vererbung.md)<br>[Klassen, super() und Dunder Methods](../wiederholung/klassen_oop_wiederholung.md) |
| superclass | Oberklasse/Basisklasse | [Vererbung](../oop_vertiefung/vererbung_polymorphismus/vererbung/vererbung.md)<br>[super() in Klassen](../wiederholung_woche8/super_init_methoden.md) |
| subclass | Unterklasse/abgeleitete Klasse | [Vererbung](../oop_vertiefung/vererbung_polymorphismus/vererbung/vererbung.md)<br>[Komposition, Vererbung & Mixins](../oop_vertiefung_teil2/komposition_mixins.md) |
| single inheritance | einfache Vererbung | [Vererbung](../oop_vertiefung/vererbung_polymorphismus/vererbung/vererbung.md)<br>[Klassen, super() und Dunder Methods](../wiederholung/klassen_oop_wiederholung.md) |
| multiple inheritance | Mehrfachvererbung | [Mehrfachvererbung, MRO & Diamond](../oop_vertiefung_teil2/mro_diamond.md)<br>[Quiz Komposition, Mixins & MRO](../oop_vertiefung_teil2/quiz_komposition_mixins_mro.md) |
| diamond problem | Diamond-Problem bei Mehrfachvererbung | [Mehrfachvererbung, MRO & Diamond](../oop_vertiefung_teil2/mro_diamond.md)<br>[Quiz Komposition, Mixins & MRO](../oop_vertiefung_teil2/quiz_komposition_mixins_mro.md) |
| method resolution order | MRO; Reihenfolge der Methodensuche | [Mehrfachvererbung, MRO & Diamond](../oop_vertiefung_teil2/mro_diamond.md)<br>[super() in Klassen](../wiederholung_woche8/super_init_methoden.md) |
| polymorphism | Polymorphismus; gleicher Aufruf, unterschiedliches Verhalten | [Polymorphismus & Introspection](../oop_vertiefung_teil2/polymorphismus_introspection.md)<br>[OOP Wiederholung](../oop_vertiefung_teil2/oop_wiederholung.md) |
| overriding | Ueberschreiben einer geerbten Methode | [Vererbung](../oop_vertiefung/vererbung_polymorphismus/vererbung/vererbung.md)<br>[Magic Methods](../oop_vertiefung/magic_methods/magic_methods.md) |
| introspection | Introspection; Programm untersucht Objekte/Klassen | [Polymorphismus & Introspection](../oop_vertiefung_teil2/polymorphismus_introspection.md)<br>[Quiz Polymorphismus & Introspection](../oop_vertiefung_teil2/quiz_polymorphismus_introspection.md) |
| `hasattr()` | prueft, ob ein Objekt ein Attribut besitzt | [Polymorphismus & Introspection](../oop_vertiefung_teil2/polymorphismus_introspection.md)<br>[Quiz Polymorphismus & Introspection](../oop_vertiefung_teil2/quiz_polymorphismus_introspection.md) |
| `isinstance()` | prueft, ob ein Objekt Instanz einer Klasse ist | [Vererbung](../oop_vertiefung/vererbung_polymorphismus/vererbung/vererbung.md)<br>[Polymorphismus & Introspection](../oop_vertiefung_teil2/polymorphismus_introspection.md) |
| `__dict__` | Dictionary der Attribute eines Objekts oder einer Klasse | [Attribute](../oop_grundlagen/attributes/attributes.md)<br>[Polymorphismus & Introspection](../oop_vertiefung_teil2/polymorphismus_introspection.md) |
| `__name__` | Name einer Klasse oder eines Moduls | [Polymorphismus & Introspection](../oop_vertiefung_teil2/polymorphismus_introspection.md)<br>[Module und Imports Wiederholung](../wiederholung/module_imports_wiederholung.md) |
| `__module__` | Modul, in dem eine Klasse definiert wurde | [Polymorphismus & Introspection](../oop_vertiefung_teil2/polymorphismus_introspection.md)<br>[Module und Imports Wiederholung](../wiederholung/module_imports_wiederholung.md) |
| `__bases__` | Basisklassen einer Klasse | [Polymorphismus & Introspection](../oop_vertiefung_teil2/polymorphismus_introspection.md)<br>[Mehrfachvererbung, MRO & Diamond](../oop_vertiefung_teil2/mro_diamond.md) |
| public component | oeffentlicher Bestandteil einer Klasse oder Instanz | [Protected & Private](../oop_vertiefung/protected_private/protected_private.md)<br>[OOP Wiederholung](../oop_vertiefung_teil2/oop_wiederholung.md) |
| protected component | geschuetzter Bestandteil; Konvention mit einem fuehrenden Unterstrich | [Protected & Private](../oop_vertiefung/protected_private/protected_private.md)<br>[Klassen, super() und Dunder Methods](../wiederholung/klassen_oop_wiederholung.md) |
| private component | privater Bestandteil; doppelter Unterstrich loest Name Mangling aus | [Protected & Private](../oop_vertiefung/protected_private/protected_private.md)<br>[Getter & Setter](../oop_vertiefung/getter_setter/getter_setter.md) |
| name mangling | Namensumformung bei doppeltem Unterstrich | [Protected & Private](../oop_vertiefung/protected_private/protected_private.md)<br>[Klassen, super() und Dunder Methods](../wiederholung/klassen_oop_wiederholung.md) |
| magic method | Dunder Method wie `__str__`, `__init__`, `__add__` | [Magic Methods](../oop_vertiefung/magic_methods/magic_methods.md)<br>[Klassen, super() und Dunder Methods](../wiederholung/klassen_oop_wiederholung.md) |
| `__str__()` | String-Repräsentation eines Objekts fuer Nutzer:innen | [Magic Methods](../oop_vertiefung/magic_methods/magic_methods.md)<br>[Vererbung](../oop_vertiefung/vererbung_polymorphismus/vererbung/vererbung.md) |
| class method | Klassenmethode mit `@classmethod` | [Class- & Staticmethod](../oop_vertiefung/class_static_methods/class_static_methods.md)<br>[Klassen, super() und Dunder Methods](../wiederholung/klassen_oop_wiederholung.md) |
| static method | statische Methode mit `@staticmethod` | [Class- & Staticmethod](../oop_vertiefung/class_static_methods/class_static_methods.md)<br>[Klassen, super() und Dunder Methods](../wiederholung/klassen_oop_wiederholung.md) |

## Miscellaneous

| English term | Deutsch / Einordnung | Skriptstellen |
|--------------|----------------------|---------------|
| list comprehension | kompakte Schreibweise zum Erzeugen von Listen | [List Comprehensions](../comprehensions/list_comp/list_comp.md)<br>[Comprehensions Wiederholung](../wiederholung/comprehension_wiederholung.md) |
| conditional expression | bedingter Ausdruck, z.B. `a if cond else b` | [Booleans](../datenstrukturen/booleans/booleans.md)<br>[Operatoren und Precedence](../wiederholung_woche8/operatoren_precedence.md) |
| nested comprehension | verschachtelte Comprehension | [List Comprehensions](../comprehensions/list_comp/list_comp.md)<br>[Comprehensions Wiederholung](../wiederholung/comprehension_wiederholung.md) |
| lambda expression | anonyme Funktion mit `lambda` | [Lambda](../funktionen_fortgeschritten/lambda/lambda.md)<br>[map, filter und lambda](../wiederholung_woche8/map_filter_lambda.md) |
| first-class function | Funktion als Wert; kann uebergeben und gespeichert werden | [Funktionen](../python_grundlagen/functions/functions.md)<br>[Lambda](../funktionen_fortgeschritten/lambda/lambda.md) |
| `map()` | wendet eine Funktion auf jedes Element an | [Lambda](../funktionen_fortgeschritten/lambda/lambda.md)<br>[map, filter und lambda](../wiederholung_woche8/map_filter_lambda.md) |
| `filter()` | filtert Elemente anhand einer Funktion | [Lambda](../funktionen_fortgeschritten/lambda/lambda.md)<br>[map, filter und lambda](../wiederholung_woche8/map_filter_lambda.md) |
| closure | Funktion mit Zugriff auf Variablen aus aeusserem Scope | [Scopes](../funktionen_vertiefung/scopes/scopes.md)<br>[Scope und Closure](../wiederholung_woche8/scope_closure.md) |
| scope | Gueltigkeitsbereich eines Namens | [Scopes](../funktionen_vertiefung/scopes/scopes.md)<br>[Scope, Closure & Variablen](../wiederholung/function_scopes_and_closure.md) |
| local variable | lokale Variable | [Scopes](../funktionen_vertiefung/scopes/scopes.md)<br>[Scope, Closure & Variablen](../wiederholung/function_scopes_and_closure.md) |
| global variable | globale Variable | [Scopes](../funktionen_vertiefung/scopes/scopes.md)<br>[Scope, Closure & Variablen](../wiederholung/function_scopes_and_closure.md) |
| positional argument | Positionsargument | [Funktionen](../python_grundlagen/functions/functions.md)<br>[Args & Kwargs](../funktionen_vertiefung/args_kwargs/args_kwargs.md) |
| keyword argument | benanntes Argument | [Funktionen](../python_grundlagen/functions/functions.md)<br>[Args & Kwargs](../funktionen_vertiefung/args_kwargs/args_kwargs.md) |
| `*args` | sammelt zusaetzliche Positionsargumente | [Args & Kwargs](../funktionen_vertiefung/args_kwargs/args_kwargs.md)<br>[Args und Kwargs Wiederholung](../wiederholung/args_kwargs_wiederholung.md) |
| `**kwargs` | sammelt zusaetzliche benannte Argumente | [Args & Kwargs](../funktionen_vertiefung/args_kwargs/args_kwargs.md)<br>[Args und Kwargs Wiederholung](../wiederholung/args_kwargs_wiederholung.md) |
| operator precedence | Operatorrangfolge / Auswertungsreihenfolge | [Operatoren und Precedence](../wiederholung_woche8/operatoren_precedence.md)<br>[Mathematische Operationen](../python_grundlagen/math_operations/math_operations.md) |
| mutability | Veraenderlichkeit eines Objekts | [Listen](../datenstrukturen/lists/lists.md)<br>[Mutable, Immutable und Referenzen](../wiederholung_woche8/mutable_immutable_referenzen.md) |
| immutable object | unveraenderliches Objekt, z.B. String oder Tupel | [Tupel](../datenstrukturen/tupel/tupel.md)<br>[Mutable, Immutable und Referenzen](../wiederholung_woche8/mutable_immutable_referenzen.md) |
| mutable object | veraenderliches Objekt, z.B. Liste oder Dictionary | [Listen](../datenstrukturen/lists/lists.md)<br>[Dictionaries](../datenstrukturen/dictionaries/dictionaries.md) |
| iterator | Objekt, das mit `next()` Werte liefert | [Generatoren](../funktionen_fortgeschritten/generatoren/generatoren.md)<br>[Generatoren Wiederholung](../wiederholung_woche8/generatoren.md) |
| iterable | Objekt, ueber das iteriert werden kann | [Generatoren](../funktionen_fortgeschritten/generatoren/generatoren.md)<br>[Schleifen](../python_grundlagen/loops/loops.md) |
| generator | Iterator-Funktion mit `yield` | [Generatoren](../funktionen_fortgeschritten/generatoren/generatoren.md)<br>[Generatoren Wiederholung](../wiederholung_woche8/generatoren.md) |
| `yield` | gibt einen Wert aus einem Generator zurueck und pausiert | [Generatoren](../funktionen_fortgeschritten/generatoren/generatoren.md)<br>[Generatoren Wiederholung](../wiederholung_woche8/generatoren.md) |
| text mode | Textmodus beim Datei-I/O | [Dateioperationen](../dateien_dateisystem/dateioperationen/dateioperationen.md)<br>[Dateien lesen und schreiben](../wiederholung_woche8/dateien.md) |
| binary mode | Binaermodus beim Datei-I/O | [Dateioperationen](../dateien_dateisystem/dateioperationen/dateioperationen.md)<br>[Dateien lesen und schreiben](../wiederholung_woche8/dateien.md) |
| stream | Datenstrom, z.B. Datei oder Standardstream | [Ein- und Ausgabe](../python_grundlagen/input_output/input_output.md)<br>[Dateien lesen und schreiben](../wiederholung_woche8/dateien.md) |
| handle | Datei-Handle; Objekt, ueber das Datei-I/O laeuft | [Dateioperationen](../dateien_dateisystem/dateioperationen/dateioperationen.md)<br>[Dateien lesen und schreiben](../wiederholung_woche8/dateien.md) |
| predefined stream | vordefinierter Stream wie `stdin`, `stdout`, `stderr` | [Ein- und Ausgabe](../python_grundlagen/input_output/input_output.md)<br>[Dateien lesen und schreiben](../wiederholung_woche8/dateien.md) |
| `open()` | Funktion zum Oeffnen einer Datei | [Dateioperationen](../dateien_dateisystem/dateioperationen/dateioperationen.md)<br>[Dateien lesen und schreiben](../wiederholung_woche8/dateien.md) |
| `read()` / `readline()` / `readlines()` | Methoden zum Lesen aus Dateien | [Dateioperationen](../dateien_dateisystem/dateioperationen/dateioperationen.md)<br>[Dateien lesen und schreiben](../wiederholung_woche8/dateien.md) |
| `write()` | Methode zum Schreiben in Dateien | [Dateioperationen](../dateien_dateisystem/dateioperationen/dateioperationen.md)<br>[Dateien lesen und schreiben](../wiederholung_woche8/dateien.md) |
| `close()` | schliesst eine Datei | [Dateioperationen](../dateien_dateisystem/dateioperationen/dateioperationen.md)<br>[Dateien lesen und schreiben](../wiederholung_woche8/dateien.md) |
| `errno` | Fehlernummer bei I/O-Fehlern | [Dateioperationen](../dateien_dateisystem/dateioperationen/dateioperationen.md)<br>[Exceptions Wiederholung](../wiederholung/exceptions.md) |
| `bytearray` | veraenderbare Byte-Sequenz | [bytearray](../wiederholung_woche8/bytearray.md)<br>[Dateien lesen und schreiben](../wiederholung_woche8/dateien.md) |
