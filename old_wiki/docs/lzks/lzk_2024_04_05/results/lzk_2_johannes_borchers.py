# In dieser LZK musst du die Funktionsrümpfe füllen.
# Diese Funktionsrümpfe werden dann automatisiert getestet.
# Ihr dürft nicht den Methodennamen umbenennen. Alles andere
# könnt ihr anpassen
# Sendet mir eure Lösungen gezippet (!) an viktor.reichert@qualidy.de vor 11 Uhr.
# Viel Erfolg!
from unittest import TestCase, main


# Aufgabe: Person sagt Hallo Welt ⭐️
# Konzepte: Klassen, Attributes, Methoden, Instanziierung
# Schreibe eine Klasse `Person` mit den Attributen `name` und `alter`.
# Füge eine Methode `vorstellung` hinzu, die einen Begrüßungstext mit dem Namen der Person zurückgibt.
#
# Beispiel:
# Person("Anna", 25)
# => Hallo Welt, ich bin Anna und ich bin 25 Jahre alt.
class Person:
    def __init__(self, name: str, alter: int) -> None:
        self.name = name
        self.alter = alter
        pass

    def vorstellung(self):
        return f"Hallo Welt, ich bin {self.name} und ich bin {self.alter} Jahre alt."
    pass


class Test_Person(TestCase):
    def test_person_initialization(self):
        person = Person("Max", 30)
        self.assertEqual(person.name, "Max")
        self.assertEqual(person.alter, 30)

    def test_person_vorstellung(self):
        person = Person("Anna", 25)
        expected_message = "Hallo Welt, ich bin Anna und ich bin 25 Jahre alt."
        self.assertEqual(person.vorstellung(), expected_message)

    def test_person_attribute_types(self):
        person = Person("Lukas", 20)
        self.assertIsInstance(person.name, str)
        self.assertIsInstance(person.alter, int)

    def test_person_change_attributes(self):
        person = Person("Julia", 35)
        person.name = "Julie"
        person.alter = 36
        self.assertEqual(person.name, "Julie")
        self.assertEqual(person.alter, 36)


# Aufgabe: Typen erfragen ⭐️
# Erstelle eine Funktion, die zwei Parameter annimmt.
# Diese zunächst soll geprüft werden, dass beide Parameter int oder float sind.
# Wenn ja, dann sollen sie addiert werden und die Summe zurückgegeben werden.
# Wenn nein, soll None zurückgegeben werden.
#
# Beispiel:
# 0.2, 0.1 => 0.3
# "2", 1 => None
def add_or_none(a: int | float, b: int | float):
    if isinstance(a, float | int) and isinstance(b, float | int):
        return a+b
    else:
        return None
    pass


class Test_add_or_none(TestCase):
    def test_add_or_none_0(self):
        self.assertAlmostEqual(add_or_none(0.2, 0.1), 0.3)

    def test_add_or_none_1(self):
        self.assertAlmostEqual(add_or_none(0.2, 1), 1.2)

    def test_add_or_none_2(self):
        self.assertAlmostEqual(add_or_none(0.2, 1), 1.2)

    def test_add_or_none_3(self):
        self.assertIsNone(add_or_none("2", 1))

    def test_add_or_none_4(self):
        self.assertIsNone(add_or_none(None, 1))


# Aufgabe: Set aus Vokalwörter ⭐️
# Konzepte: Listen, Sets, Strings
# Schreibe eine Funktion, die eine Liste von Strings erhält und ein neues Set zurückgibt,
# in dem alle Strings, die NICHT mit einem Vokal beginnen, entfernt wurden.
#
# Beispiel:
# ['apple', 'banana', 'pear', 'orange'] -> {'apple', 'orange'}
def remove_non_vowel_starting_strings(string_list):
    return {a for a in string_list if a[0].lower() in ["a", "e", "i", "o", "u"]}
    pass


class Test_remove_non_vowel_starting_strings(TestCase):
    def test_remove_vowel_starting_strings_0(self):
        self.assertSetEqual(remove_non_vowel_starting_strings(['apple', 'banana', 'pear', 'orange']),
                            {'apple', 'orange'})

    def test_remove_vowel_starting_strings_1(self):
        self.assertSetEqual(remove_non_vowel_starting_strings(['apple', 'banana', 'pear', 'orange']),
                            {'apple', 'orange'})

    def test_remove_vowel_starting_strings_2(self):
        self.assertSetEqual(remove_non_vowel_starting_strings(
            ['banana', 'pear',]), set())

    def test_remove_vowel_starting_strings_3(self):
        self.assertSetEqual(remove_non_vowel_starting_strings([]), set())

    def test_remove_vowel_starting_strings_4(self):
        self.assertSetEqual(
            remove_non_vowel_starting_strings(['apple']), {'apple'})

    def test_remove_vowel_starting_strings_5(self):
        self.assertSetEqual(remove_non_vowel_starting_strings(['apple', 'apple', 'apple']),
                            {'apple'})


# Aufgabe: 2er Potenz von geraden Zahlen ⭐️
# Konzepte: List Comprehensions, Listen, Filterung, Square
# Implementiere eine Funktion, die eine Liste von Zahlen erhält
# und mittels List Comprehension eine neue Liste zurückgibt,
# die nur die Quadrate der geraden Zahlen enthält.
#
# Beispiel:
# [1, 2, 3, 4, 5] -> [4, 16]
def squares_of_evens(input_list):
    return [i**2 for i in input_list if i % 2 == 0]
    pass


class Test_squares_of_evens(TestCase):
    def test_empty_list(self):
        self.assertEqual(squares_of_evens([]), [])

    def test_all_evens(self):
        self.assertEqual(squares_of_evens([2, 4, 6]), [4, 16, 36])

    def test_mix_evens_odds(self):
        self.assertEqual(squares_of_evens([1, 2, 3, 4, 5]), [4, 16])

    def test_all_odds(self):
        self.assertEqual(squares_of_evens([1, 3, 5]), [])

    def test_includes_zero(self):
        self.assertEqual(squares_of_evens([0, 1, 2]), [0, 4])

    def test_negative_numbers(self):
        self.assertEqual(squares_of_evens([-2, -4, 5]), [4, 16])


# Aufgabe: String-Liste nach Länge der Elemente sortieren ⭐️
# Konzepte: Listen, Lambda-Funktionen, Sortierung
# Implementiere eine Funktion, die eine Liste von Strings nach der Länge ihrer Elemente sortiert.
#
# Beispiel:
# ["aaa", "a", "aa"] => ["a", "aa", "aaa"]
def find_longest(list):
    res = 0
    for word in list:
        if len(word) >= res:
            res = len(word)
    return res


def sort_by_length(strings):
    res = []
    for i in range(find_longest(strings)+1):
        for word in strings:
            if len(word) == i:
                res.append(word)
    return res
    pass


class TestSortByLength(TestCase):
    def test_sort_simple_strings(self):
        self.assertEqual(sort_by_length(
            ["aaa", "a", "aa"]), ["a", "aa", "aaa"])

    def test_sort_with_same_length(self):
        self.assertEqual(sort_by_length(
            ["bb", "cc", "aa"]), ["bb", "cc", "aa"])

    def test_sort_with_empty_string(self):
        self.assertEqual(sort_by_length(["", "a", ""]), ["", "", "a"])

    def test_sort_empty_list(self):
        self.assertEqual(sort_by_length([]), [])

    def test_sort_long_strings(self):
        self.assertEqual(sort_by_length(
            ["hello", "hi", "h"]), ["h", "hi", "hello"])

    def test_sort_mixed_case(self):
        self.assertEqual(sort_by_length(["apple", "Dog", "cat"]), [
                         "Dog", "cat", "apple"])

    def test_sort_numerical_strings(self):
        self.assertEqual(sort_by_length(
            ["1234", "1", "123"]), ["1", "123", "1234"])

    def test_sort_special_characters(self):
        self.assertEqual(sort_by_length(
            ["@", "%%", "!!", "?"]), ["@", "?", "%%", "!!"])


# Aufgabe: Dictionary nach Values filtern ⭐️⭐️
# Konzepte: Dictionaries, Typüberprüfung, Sortierung, Strings
# Schreibe eine Funktion, die ein Dictionary als Parameter annimmt und eine Liste von Keys zurückgibt,
# deren zugehörige Werte Strings sind. Die Liste soll alphabetisch sortiert sein.
#
# Beispiel:
# {'a': 1, 'c': 'world', 'b': 'hello'} -> ['b', 'c']
def keys_with_string_values(my_dict:dict):

    return sorted([k for k, v in my_dict.items() if isinstance(v, str)])
    pass


class Test_keys_with_string_values(TestCase):
    def test_keys_with_string_values_3(self):
        self.assertListEqual(keys_with_string_values({'a': 1, 'c': 'world', 'b': 'hello'}),
                             ['b', 'c'])

    def test_keys_with_string_values_4(self):
        self.assertListEqual(keys_with_string_values({'a': 1, 'c': 2, 'b': 3}),
                             list())

    def test_keys_with_string_values_0(self):
        self.assertListEqual(keys_with_string_values({'sweet': "", 'home': 'in'}),
                             ['home', 'sweet'])

    def test_keys_with_string_values_1(self):
        self.assertListEqual(keys_with_string_values({'sweet': "", }),
                             ['sweet'])

    def test_keys_with_string_values_2(self):
        self.assertListEqual(keys_with_string_values(dict()),
                             list())


# Aufgabe: Anzahl der Buchstaben ⭐️⭐️
# Konzepte: Strings, Dictionaries
# Entwickle eine Funktion `count_characters`, die einen String als Parameter annimmt.
# Die Funktion soll ein Dictionary zurückgeben, in dem die Schlüssel die
# einzigartigen Buchstaben des Strings sind und die zugehörigen Werte angeben,
# wie oft jeder Buchstabe im String vorkommt.
# Die Funktion sollte Groß- und Kleinschreibung ignorieren und nur alphabetische Zeichen berücksichtigen.
#
# Beispiel:
# "Hallo Welt" -> {"H": 1, "a": 1, "l": 3, "o": 1, "W": 1, "e": 1, "t": 1}
def count_characters(s):
    return {c.lower(): s.lower().count(c.lower()) for c in s if c.isalpha()}
    pass


class TestCountCharacters(TestCase):
    def test_empty_string(self):
        self.assertEqual(count_characters(""), {})

    def test_single_character(self):
        self.assertEqual(count_characters("a"), {"a": 1})

    def test_case_insensitivity(self):
        self.assertEqual(count_characters("Aa"), {"a": 2})

    def test_ignore_non_alpha(self):
        self.assertEqual(count_characters("a1!a"), {"a": 2})

    def test_mixed_case_string(self):
        self.assertEqual(count_characters("Hallo Welt"), {
                         "h": 1, "a": 1, "l": 3, "o": 1, "w": 1, "e": 1, "t": 1})

    def test_numbers_and_punctuation(self):
        self.assertEqual(count_characters("1234!@#a"), {"a": 1})

    def test_all_same_letter(self):
        self.assertEqual(count_characters("BBBBB"), {"b": 5})

    def test_mixed_characters(self):
        self.assertEqual(count_characters("Python 3.8!"), {
                         "p": 1, "y": 1, "t": 1, "h": 1, "o": 1, "n": 1})


# Aufgabe:  Simple Zip-Funktion selber bauen ⭐️⭐
# Konzepte: Listen, Zip, Index, Loops
# Entwickle eine Funktion, die zwei Listen annimmt und eine Liste von Tupeln zurückgibt,
# wobei jedes Tupel Paare von Elementen aus beiden Listen an den entsprechenden Indizes enthält.
# Listen die ungleich lang sind, sollen nur bis zur gleichen länge gezippt werden
#
# Beispiel:
# ['a', 'b'], [1, 2] -> [('a', 1), ('b', 2)]
# ['a', 'b'], [1, 2, 3, 4] -> [('a', 1), ('b', 2)]
def zip_lists(list1, list2):
    res = []
    while list1 and list2:
        res.append((list1[0], list2[0]))
        list1.pop(0)
        list2.pop(0)
    return res
    pass


print(f"{zip_lists(['a', 'b'], [1, 2, 3, 4])}")


class Test_zip_lists(TestCase):
    def test_zip_lists_0(self):
        self.assertListEqual(zip_lists(['a', 'b'], [1, 2]), [
                             ('a', 1), ('b', 2)])

    def test_zip_lists_1(self):
        self.assertListEqual(zip_lists(['a', 'b'], [1, 2, 3, 4]), [
                             ('a', 1), ('b', 2)])

    def test_zip_lists_2(self):
        self.assertListEqual(zip_lists(['a', 'b'], []), [])

    def test_zip_lists_3(self):
        self.assertListEqual(zip_lists(['a'], [1]), [('a', 1)])

    def test_zip_lists_longer_first_list(self):
        self.assertListEqual(zip_lists([1, 2, 3, 4], ['a', 'b']), [
                             (1, 'a'), (2, 'b')])

    def test_zip_lists_with_none_elements(self):
        self.assertListEqual(zip_lists([None, 2, 3], ['a', None, 'c']), [
                             (None, 'a'), (2, None), (3, 'c')])

    def test_zip_lists_with_different_types(self):
        self.assertListEqual(zip_lists(["one", 2, 3.0], [True, False, "three"]), [
                             ("one", True), (2, False), (3.0, "three")])


# Aufgabe: Zahlen in String erhöhen ⭐️⭐️
# Konzepte: Strings, Numbers, List Comprehension
# Erstelle eine Funktion, die einen String erhält, welcher aus Zahlen und Leerzeichen besteht.
# Die Funktion soll einen neuen String zurückgeben, in dem jede Zahl um 1 erhöht wurde.
#
# Beispiel:
# "1 23 456" -> "2 34 567"
# "9 5 0" -> "10 6 1"
def increment_numbers_in_string(input_string: str):
    res = ""
    for x in input_string:
        if x.isnumeric():
            res += str(int(x)+1)
        else:
            res += x
    return res  # str([int(x)+1 if x.isnumeric() else x for x in input_string])
    pass


class Test_increment_numbers_in_string(TestCase):
    def test_increment_numbers_in_string_0(self):
        self.assertEqual(increment_numbers_in_string("1 23 456"), "2 34 567")

    def test_increment_numbers_in_string_1(self):
        self.assertEqual(increment_numbers_in_string("9 5 0"), "10 6 1")

    def test_increment_numbers_in_string_2(self):
        self.assertEqual(increment_numbers_in_string("Hallo"), "Hallo")

    def test_increment_numbers_in_string_3(self):
        self.assertEqual(increment_numbers_in_string("Ha110"), "Ha221")

    def test_increment_numbers_in_string_4(self):
        self.assertEqual(increment_numbers_in_string(""), "")


# Aufgabe: VW und der komische Rest ⭐️⭐️
# Konzepte: Klassen, Vererbung
# Definiere eine Basisklasse `Fahrzeug` mit einem Attribut `geschwindigkeit`.
# Leite eine Klasse `Auto` ab, die ein zusätzliches Attribut `marke` hat.
class Fahrzeug:
    def __init__(self, geschwindigkeit) -> None:
        self.geschwindigkeit = geschwindigkeit
        pass
    pass


class Auto(Fahrzeug):
    def __init__(self, geschwindigkeit, marke) -> None:
        super().__init__(geschwindigkeit)
        self.marke = marke
    pass


class Test_Auto(TestCase):
    def test_correct_classes(self):
        self.assertTupleEqual(Auto.__mro__, (Auto, Fahrzeug, object))

    def test_auto_instance(self):
        auto = Auto(120, "VW")
        self.assertIsInstance(auto, Auto)
        self.assertIsInstance(auto, Fahrzeug)

    def test_correct_attributes_0(self):
        auto = Auto(150, "VW")
        self.assertEqual(auto.geschwindigkeit, 150)
        self.assertEqual(auto.marke, "VW")

    def test_inheritance_from_fahrzeug(self):
        auto = Auto(100, "Toyota")
        self.assertTrue(hasattr(auto, "geschwindigkeit"))

    def test_check_Fahrzeug_has_no_marke(self):
        f = Fahrzeug(100)
        self.assertFalse(hasattr(f, "marke"))


# Aufgabe: Magic Numbers ⭐️⭐️⭐️
# Konzepte: Klassen, Magic Methods / Dunder Methods
#
# Implementiere eine Klasse `Zahl`, die die Magic Method `__add__` und `__eq__` verwendet.
# Die Klasse Zahl speichert einfach nur eine Zahl in einem Attribut `zahl`.
#
# Um zwei Instanzen der Klasse zu addieren bildet man die Summe der beiden gespeicherten Zahlen.
# Falls das addierte Element nicht vom Typ Zahl sein sollte, soll eine NotImplemented Exception geworfen werden.
#
# Zwei Instanzen der Klasse Zahl sind gleich, wenn, die intern gespeicherte Zahl gleich ist.
#
# Es sind nur erlaubt int oder float in Zahl zu speichern. Andernfalls solle ein TypeError geworfen werden.
#
# Beispiel:
# Zahl(2) + Zahl(1) => Zahl(3)
# Zahl(2) == Zahl(1) => False

class Zahl:
    def __init__(self, zahl) -> None:
        if isinstance(zahl, (float | int)):
            self.zahl = zahl
        else:
            raise TypeError
        pass

    def __add__(self, zahl1):
        if isinstance(zahl1,Zahl):
            return Zahl(self.zahl + zahl1.zahl)
        else:
            raise NotImplementedError
            

    def __eq__(self, zahl2):
        if isinstance(zahl2,Zahl):
            return self.zahl == zahl2.zahl
        else:
            return False
    pass


class Test_Zahl(TestCase):
    def test_init_zahl_0(self):
        self.assertIsInstance(Zahl(2), Zahl)

    def test_init_zahl_1(self):
        with self.assertRaises(TypeError):
            Zahl("2")

    def test_zahl_has_attribute_0(self):
        self.assertIn("zahl", Zahl(0).__dict__)

    def test_zahl_has_attribute_1(self):
        self.assertIn("__add__", Zahl.__dict__)

    def test_zahl_has_attribute_2(self):
        self.assertIn("__eq__", Zahl.__dict__)

    def test_zahl_eq_0(self):
        self.assertEqual(Zahl(2), Zahl(1+1))

    def test_zahl_eq_1(self):
        self.assertNotEqual(Zahl(2), Zahl(1))

    def test_zahl_eq_2(self):
        self.assertNotEqual(Zahl(2), 2)

    def test_add_zahl_0(self):
        a = Zahl(8)
        b = Zahl(9)
        self.assertEqual(a + b, Zahl(17))

    def test_add_zahl_1(self):
        a = Zahl(8)
        b = Zahl(-8)
        self.assertEqual(a + b, Zahl(0))

    def test_add_zahl_2(self):
        with self.assertRaises(NotImplementedError):
            Zahl(8) + 4


# Aufgabe: Löffelsprache Compiler ⭐️⭐️⭐️⭐️
# Löffelsprache sprechen ist ein Kindespiel aus der Jugend des Authors dieser Prüfung.
# Das Spiel besteht daraus die Vokale innerhalb eines Satzes folgendermaßen zu ersetzen:
# a -> alawa
# e -> elewe
# i -> iliwi
# o -> olowo
# u -> uluwu
# ä -> äläwä
# ü -> ülüwü
# ö -> ölöwö
# ei -> eileiwei

# Beispiel:
# Hast Du einen Stift für mich?
# -> Halawast Duluwu eileiweinelewen Stiliwift fülüwür miliwich?
# (Logischerweise muss bei der Ersetztung ein Großbuchstabe auch im Resultat auch groß sein)
# Erbse
# -> Elewerbselewe
def spoon(le: str):
    res = le.replace("a", "alawa").replace("O", "Olowo").replace("U", "Uluwu").replace("Ä", "Äläwä").replace("Ü", "Ülüwü").replace(
        "Ö", "Ölöwö").replace("o", "olowo").replace("u", "uluwu").replace("ä", "äläwä").replace("ü", "ülüwü").replace("ö", "ölöwö").replace("A", "Alawa")
    if "ei" in res or "Ei" in res:
        res = res.replace("ei", "eileiwei").replace("Ei", "Eileiwei")
    # for i in range(len(res)):
    #     if res[i]=="e" or res[i]=="E" and res[i+1]!="i":
    #         res = res.replace("e", "elewe")
    #         res = res.replace("E", "Elewe")
    le.replace("I", "Iliwi")
    le.replace("i", "iliwi")
    
    return res
    pass


class SpoonTest(TestCase):
    def test_spoon_empty(self):
        self.assertEqual(spoon(""), "")

    def test_spoon_umlaut(self):
        self.assertEqual(spoon("Hast Du einen Stift für mich? Hä?"),
                         "Halawast Duluwu eileiweinelewen Stiliwift fülüwür miliwich? Häläwä?")

    def test_spoon_capital(self):
        self.assertEqual(spoon("Erbse"), "Elewerbselewe")

    def test_spoon_ascii(self):
        self.assertEqual(spoon("Hast Du einen Stift?"),
                         "Halawast Duluwu eileiweinelewen Stiliwift?")

    def test_spoon_multiple_vowels(self):
        self.assertEqual(spoon("Au, das tut weh!"),
                         "Alawauluwu, dalawas tuluwut weleweh!")

    def test_spoon_no_vowels(self):
        self.assertEqual(spoon("Drk"), "Drk")


# Aufgabe: Klammernabgleich ⭐️⭐️⭐️⭐️
# Konzepte: String-Verarbeitung, Bedingungen
# Implementiere eine Funktion, die einen String als Parameter annimmt und überprüft,
# ob alle geschweiften Klammern korrekt geschlossen und vollständig sind.
# Die Funktion soll `True` zurückgeben, wenn die Klammern korrekt geschlossen sind
# und in der richtigen Reihenfolge stehen, ansonsten `False`.
#
# Beispiel:
# "{}{}" -> True
# "}{ -> False
# "{{}}" -> True
def valid_braces(la:str):
    open= la.count("{")
    close= la.count("}")
    if open==close:
        for x in la:
          if la =="{":
              la.replace("}","",1)
        
    else:
        False
    pass


class BracesTest(TestCase):
    def test_braces_empty(self):
        self.assertTrue(valid_braces(""))

    def test_braces_single(self):
        self.assertTrue(valid_braces("{}"))

    def test_braces_double(self):
        self.assertTrue(valid_braces("{}{}"))

    def test_braces_wrong_order(self):
        self.assertFalse(valid_braces("}{"))

    def test_braces_capsuled(self):
        self.assertTrue(valid_braces("{{}}"))

    def test_braces_nested_multiple_levels(self):
        self.assertTrue(valid_braces("{{{{}}}}"))

    def test_braces_long_mixed_sequence(self):
        self.assertFalse(valid_braces("{{}{}}{"))

    def test_braces_imbalanced_with_extra_closing(self):
        self.assertFalse(valid_braces("{{}}}}"))


# run unittests
if __name__ == "__main__":
    main()
