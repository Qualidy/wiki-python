# In dieser LZK musst du die Funktionsrümpfe füllen.
# Diese Funktionsrümpfe werden dann automatisiert getestet.
# Bei jeder Funktion ist geschrieben, was sie tut
# und ein Beispiel einer Anwendung.
# Ihr dürft nicht den Methodennamen umbenennen. Alles andere
# könnt ihr anpassen
# Sendet mir eure Lösungen gezippet (!) an viktor.reichert@qualidy.de um 9:50 Uhr
# Viel Erfolg!


# 6 Punkte
# Schreibe eine Funktion, die ein dictionary als Parameter enthält
# und ein neues Dictionary zurückgibt, bei dem alle Keys, die vom
# Typ int oder float sind entfernt worden.
# Das Dictionary, das als Argument übergeben wurde,
# bleibt aber unverändert.
#
test_1 = {'h': 1, 4: 2, 2.0: "e"} #-> {'h': 1}
# {} -> {}
# {5: 1, 4: 2, 2.0: "e"}) -> {}

def remove_float_and_int_keys(dic: dict):
    copy = dic.copy()
    for key in dic:
        if type(key) == int or type(key) == float:
            del copy[key]
    return copy

print((remove_float_and_int_keys(test_1)))

# 7 Punkte
# Erstelle eine Funktion, die einen String erwartet. Dieser
# String besteht nur aus Groß- und Kleinbuchstaben und einzelnen
# Leerzeichen, die weder am Anfang noch am Ende des Strings sind.
# Schreibe eine Funktion, welche die Reihenfolge alle Buchstaben zwischen
# zwei Leerzeichen ändert.
#
test_2 = "Hallo wie geht es dir" #-> "ollaH eiw theg se rid"
# "" -> ""
# "abc" -> "cba"
# "t st s" -> "t ts s"


def resort_within_word(words: str):
    list_of_words = words.split()
    resorted = []
    for word in list_of_words:
        resorted.append(word[::-1])
    return " ".join(resorted)

print(resort_within_word(test_2))

# 7 Punkte
# Schreibe eine Funktion, die eine Liste als Parameter
# annimmt und eine neue Liste zurückgibt, bei der
# alle Elemente außer den größten und dem kleinsten
# entfernt wurden. Wenn die Liste leer ist, soll auch die
# leere Liste zurückgegeben werden.
#
test_3 = [1,4,3,4,1,2] #-> [1,4,4,1]
# [1] -> [1]
# [] -> []
def keep_smallest_biggest(my_list: list):
    if not my_list:
        return my_list
    else:
        my_list.sort()
        copy = my_list.copy()
        for number in my_list:
            if my_list[0] < number < my_list[-1]:
                copy.remove(number)
    return copy


print(keep_smallest_biggest(test_3))

# 7 Punkte
# Schreibe eine Funktion, die ein String als Parameter
# erhält und für jedes Zeichen, im String, außer Leerzeichen(!)
# ein Dictionary erstellt, das jedes auftauchende Zeichen
# als Key enthält und als Value speichert, wie oft
# das Zeichen im String auftaucht.
#
test_4 = "du da" #-> {"d": 2, "u":1, "a": 1}
# "" -> {}
# "  " -> {}
# "12321" -> {"1": 2, "2": 2, "3": 1}


def count_letters(my_str: str):
    dic = {}
    my_str = my_str.replace(" ","")
    for char in my_str:
        dic[char] = dic.get(char, 0) + 1
    return dic


print(count_letters(test_4))

# 8 Punkte
# Schreibe eine Funktion das eine Liste von ints erhält.
# Die Funktion soll alle Elemente der Liste aufsummieren,
# dabei alle folgende Regel beachten:
# Ist die Zahl gerade, so wird sie normal hinzuaddiert,
# ist die Zahl ungerade, so wird sie abgezogen.
#
test_5 =  [1,2,3,4,5] #-> -1+2-3+4-5 = -3
# [] -> 0
# [0,0,0] -> 0
# [-1, -3, -5] -> -(-1)-(-3)-(-5) = 9

def funny_sum(my_list: list):
    summe = 0
    for num in my_list:
        if num % 2 == 0:
            summe += num
        else:
            summe -= num
    return summe


print(funny_sum(test_5))



# 9 Punkte
# Schreibe eine Funktion, die eine Liste von Zahlen erhält.
# Es soll ein Tupel zurückgegeben werden, bei dem von je zwei
# benachbarten Elementen geprüft wird, ob das erste echt größer
# als das zweite ist. Wenn ja, so wird an der jeweiligen Stelle
# True eingesetzt, sonst False. Das resultierende Tupel
# ist also um ein kürzer als die Eingangsliste.
# Bei Listen, die höchstens die Länge 1 haben, soll immer
# das leere Tupel zurückgegeben werden.
#
test_6 = [4,2,6,3,1,1] #-> (True, False, True, True, False)
# [] -> ()
# [1] -> ()
# [1,2] -> (True,)

def is_left_bigger(my_list: list):
    if not my_list and len(my_list) == 1:
        return ()
    else:
        result = []
        for i in range(len(my_list)-1):
            if my_list[i] > my_list[i+1]:
                result.append(True)
            else:
                result.append(False)
    return tuple(result)


print(is_left_bigger(test_6))



# 7 Punkte
# Schreibe eine Funktion die einen positiven Integer erhält.
# Sie gibt den Integer zurück, bei dem dann alle Ziffern
# Vertauscht sind. Führende Nullen werden dabei gestrichen.
#
# 13050 -> 5031
# 0 -> 0
# 1000 -> 1
# 1111 -> 1111

test_7 = 13050

def swap_digets(number: int):
    if number == 0:
        return 0
    else:
        while number % 10 == 0:
            number = int(number / 10)
        str_of_number = str(number)
    return int(str_of_number[::-1])

print(swap_digets(test_7))







# 6 Punkte
# Schreibe eine Funktion, die einen String erwartet und
# jeden Kleinbuchstaben groß und jeden Großbuchstaben klein schreibt.
#
# "Aloh" -> "aLOH"
# "" -> ""
# "aaaa" -> "AAAA"
test_8 = "Ich bin ein Text" #-> "iCH BIN EIN tEXT"


def swap_case(words: str):
    new_words = ""
    for char in words:
        if char.islower():
            new_words += char.upper()
        else:
            new_words += char.lower()
    return new_words


print(swap_case(test_8))


# 6 Punkte
# Schreibe eine Funktion, die zwei Parameter annimmt und zwei Rückgabewerte
# besitzt. Die erste Rückgabe ist die Summe der beiden und die zweite
# Rückgabe ist die Subtraktion des zweiten vom ersten.
#
# 6, 9 -> 15, -3
# 1, 1 -> 2, 0
# 0, 0 -> 0, 0
# -22, -3 -> -25, -19

test_9_1 = 6
test_9_2 = 9

def add_and_sub(a, b):
    return a+b, a-b

print(add_and_sub(test_9_1, test_9_2))



# 6 Punkte
# Schreibe eine Funktion, die eine Text aus Buchstaben und leerzeichen
# erhält. Gebe ein Tupel zurück, das zählt, wie viele Zeichen
# zwischen zwei Leerzeichen sind. Bei zwei aufeinanderfolgenden Leerzeichen
# wird der Eintrag im Tupel ausgelassen (es gibt also keine Nullen
# im Tupel).
#
test_10 = "Hallo wer bist  du denn" #-> (5, 3, 4, 2, 4)
# "" -> ()
# "   " -> ()
# "Hallo      du" -> (5, 2)

def all_len(words: str):
    list_of_words = words.split()
    print(list_of_words)
    counts = []
    for word in list_of_words:
        counts.append(len(word))
    return counts

# print(all_len((test_10)))



# 7 Punkte
# Baue eine Funktion, die Zahlen im Text findet
# und ein Set mit diesen zurückgibt.
# Im Text können positive ints auftauchen. Diese sind immer von
# Leerzeichen umschlossen oder stehen am Anfang oder Ende des
# Textes.
#
# "10 ist größer als 8 ist gleich 8" -> {8, 10}
# "10 10 100 1" -> {1, 10, 100}
# "10" -> {10}
# "random Text" -> {}

def get_unique_numbers(text):
    ...


# 10 Punkte
# Schreibe eine Funktion, ein Tupel in ein Set verwandelt,
# und eine Liste in einen Tupel. Bei einem Set wird eine Liste
# aus dem kleinsten und größten Element erstellt. Wenn es keine
# Elemente in der Liste gibt, wird die Leere Liste zurückgegeben.
#
# (1,2,3,2) -> {1,2,3}
# {1,2,3} -> [1,3]
# [1,3] -> (1,3)
# () -> {}
# {} -> []
# [] -> ()


def change_type(my_obj: object):
    if isinstance(my_obj, tuple):
        return set(my_obj)
    if isinstance(my_obj, list):
        return tuple(my_obj)

# hier war die Zeit vorbei 🥲




# 6 Punkte
# Definiere eine Funktion, die als ersten Parameter eine Liste
# von Tupeln der Länge 2 erwartet und als zweiten Parameter eine
# Funktion. Die Funktion gibt eine neue Liste zurück, in
# der die Operation auf die Elemente des Tupels angewandt wurde.
#
# apply_operation([(1, 3), (4.5, 5.5)], min) -> [1, 4.5]
# apply_operation([], min) -> []
# apply_operation([("a", "b")], max) -> ["b"]
def apply_operation(list_of_pairs, operation):
    ...


# 7 Punkte
# Definiere eine Funktion, die als Parameter eine Liste von Listen mit
# Zahlen erhält. Als Argument wird niemals eine leere Liste übergeben werden
# und in der Oberliste sind keine leeren Listen enthalten.
# Die Funktion liefert eine neue Liste von Listen zurück,
# bei der alle positiven Zahlen durch `True` und alle negativen
# Zahlen durch `False` ersetzt wurden. Wie die `0` zugeordnet wird,
# soll durch einen zweiten Parameter `zero_is_true` festgelegt werden.
# Dieser zweite Parameter soll Optional sein und per Default auf `True`
# gesetzt sein.
#
# [[1,2], [-2, 0, 3]] -> [[True, True], [False, True, True]]
# [[1,2], [-2, 0, 3]], zero_is_true=False -> [[True, True], [False, False, True]]
# [[1]] -> [[True]]
# [[1, -1, 0]] -> [[True, False, True]]
def deep_positive_check(list_of_lists, zero_is_true):
    ...
