#Aufgabe 1 

from unittest import TestCase, main


class Person:
    def __init__(self, name, alter) -> None:
        self.name = name
        self.alter = alter 
        
    def vorstellung(self):
        return f"Hallo Welt, ich bin {self.name} und ich bin {self.alter} Jahre alt."

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
        
        
        

#Aufgabe 2

from unittest import TestCase, main

def add_or_none(a, b):
    if type(a) == float and type(b) == float or type(a) == int and type(b) == int or type(a) == float and type(b) == int or type(a) == int and type(b) == float:
        return a + b
    else: 
        return None

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
        
        
        

#Aufgabe 3
from unittest import TestCase, main


def remove_non_vowel_starting_strings(string_list):
    fruechte_set = set()
    for wort in string_list:
        if wort[0] in Vokabeln:
            fruechte_set.add(wort)
    return fruechte_set
        

class Test_remove_non_vowel_starting_strings(TestCase):
    def test_remove_vowel_starting_strings_0(self):
        self.assertSetEqual(remove_non_vowel_starting_strings(['apple', 'banana', 'pear', 'orange']),
                             {'apple', 'orange'})

    def test_remove_vowel_starting_strings_1(self):
        self.assertSetEqual(remove_non_vowel_starting_strings(['apple', 'banana', 'pear', 'orange']),
                             {'apple', 'orange'})

    def test_remove_vowel_starting_strings_2(self):
        self.assertSetEqual(remove_non_vowel_starting_strings(['banana', 'pear',]), set())
        
    def test_remove_vowel_starting_strings_3(self):
        self.assertSetEqual(remove_non_vowel_starting_strings([]), set())
        
    def test_remove_vowel_starting_strings_4(self):
        self.assertSetEqual(remove_non_vowel_starting_strings(['apple']), {'apple'})     

    def test_remove_vowel_starting_strings_5(self):
        self.assertSetEqual(remove_non_vowel_starting_strings(['apple', 'apple', 'apple']),
                             {'apple'})

        
Woerterliste = ['apple', 'banana', 'pear', 'orange']
Vokabeln = "aeiouAEIOU"     
        

    
#Aufgabe 4
from unittest import TestCase, main



def squares_of_evens(input_list):
    neue_liste = []
    for zahl in input_list:
        if zahl % 2 == 0:
            neue_liste.append(zahl**2)
    return neue_liste
    


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
        
        
Zahlenliste = [1, 2, 3, 4, 5]


#Aufgabe 5

from unittest import TestCase, main

def sort_by_length(strings):
    return sorted(strings, key = lambda buchstabe: len(buchstabe))

class TestSortByLength(TestCase):
    def test_sort_simple_strings(self):
        self.assertEqual(sort_by_length(["aaa", "a", "aa"]), ["a", "aa", "aaa"])

    def test_sort_with_same_length(self):
        self.assertEqual(sort_by_length(["bb", "cc", "aa"]), ["bb", "cc", "aa"])

    def test_sort_with_empty_string(self):
        self.assertEqual(sort_by_length(["", "a", ""]), ["", "", "a"])

    def test_sort_empty_list(self):
        self.assertEqual(sort_by_length([]), [])

    def test_sort_long_strings(self):
        self.assertEqual(sort_by_length(["hello", "hi", "h"]), ["h", "hi", "hello"])
        
    def test_sort_mixed_case(self):
        self.assertEqual(sort_by_length(["apple", "Dog", "cat"]), ["Dog", "cat", "apple"])

    def test_sort_numerical_strings(self):
        self.assertEqual(sort_by_length(["1234", "1", "123"]), ["1", "123", "1234"])

    def test_sort_special_characters(self):
        self.assertEqual(sort_by_length(["@", "%%", "!!", "?"]), ["@", "?", "%%", "!!"])

#Aufgabe 7

from unittest import TestCase, main


def count_characters(s):
    zaehler = {}
    for buchstabe in s:
        if buchstabe.isalpha():
            buchstabe = buchstabe.lower()
            if buchstabe not in zaehler:
                zaehler[buchstabe] = 1
            else:
                zaehler[buchstabe] += 1
    return zaehler
            

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
        self.assertEqual(count_characters("Hallo Welt"), {"h": 1, "a": 1, "l": 3, "o": 1, "w": 1, "e": 1, "t": 1})
        
    def test_numbers_and_punctuation(self):
        self.assertEqual(count_characters("1234!@#a"), {"a": 1})

    def test_all_same_letter(self):
        self.assertEqual(count_characters("BBBBB"), {"b": 5})

    def test_mixed_characters(self):
        self.assertEqual(count_characters("Python 3.8!"), {"p": 1, "y": 1, "t": 1, "h": 1, "o": 1, "n": 1})


#Aufgabe 9 

from unittest import TestCase, main


# Aufgabe: Zahlen in String erhöhen ⭐️⭐️
# Konzepte: Strings, Numbers, List Comprehension
# Erstelle eine Funktion, die einen String erhält, welcher aus Zahlen und Leerzeichen besteht.
# Die Funktion soll einen neuen String zurückgeben, in dem jede Zahl um 1 erhöht wurde.
#
# Beispiel:
# "1 23 456" -> "2 34 567"
# "9 5 0" -> "10 6 1"

def increment_numbers_in_string(input_string):
    return ' '.join(str(int(nummer) + 1) if nummer.isdigit() else nummer for nummer in input_string.split())

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
        
        


#Aufgabe 10 
from unittest import TestCase, main

class Fahrzeug:
    def __init__(self, geschwindigkeit):
        self.geschwindigkeit = geschwindigkeit

class Auto(Fahrzeug):
    def __init__(self,geschwindigkeit, marke):
        super().__init__(geschwindigkeit)
        self.marke = marke

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
        
