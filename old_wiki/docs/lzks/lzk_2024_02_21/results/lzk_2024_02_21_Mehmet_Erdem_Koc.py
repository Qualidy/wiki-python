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
# {'h': 1, 4: 2, 2.0: "e"} -> {'h': 1}
# {} -> {}
# {5: 1, 4: 2, 2.0: "e"}) -> {}
def remove_float_and_int_keys(dic: dict):
    new_dic = dic.copy()
    for key in new_dic.keys():
        if key == int or key == float:
            new_dic.pop(key)

    return new_dic

print(remove_float_and_int_keys({'h': 1 , 4: 2 , 2.0: "e"}))

# 7 Punkte
# Erstelle eine Funktion, die einen String erwartet. Dieser
# String besteht nur aus Groß- und Kleinbuchstaben und einzelnen
# Leerzeichen, die weder am Anfang noch am Ende des Strings sind.
# Schreibe eine Funktion, welche die Reihenfolge alle Buchstaben zwischen
# zwei Leerzeichen ändert.
#
# "Hallo wie geht es dir" -> "ollaH eiw theg se rid"
# "" -> ""
# "abc" -> "cba"
# "t st s" -> "t ts s"
def resort_within_word(words):
    word_string = words.split(" ")
    word_list = []
    for wrd in word_string:
        word_list.append(wrd)
    new_string = ""
    i = 0
    for word in word_list:
        new_string += word[::-1]
        if i < len(word_list) - 1:
            new_string += " "
            i += 1
    return new_string


print(resort_within_word("Hallo wie geht es dir"))


# 7 Punkte
# Schreibe eine Funktion, die eine Liste als Parameter
# annimmt und eine neue Liste zurückgibt, bei der
# alle Elemente außer den größten und dem kleinsten
# entfernt wurden. Wenn die Liste leer ist, soll auch die
# leere Liste zurückgegeben werden.
#
# [1,4,3,4,1,2] -> [1,4,4,1]
# [1] -> [1]
# [] -> []
def keep_smallest_biggest(my_list):
    i = 0
    for big_number in my_list:
        if big_number > i:
            i = big_number
        else:
            my_list.remove(big_number)
            continue
    return my_list

print(keep_smallest_biggest([1]))

# 7 Punkte
# Schreibe eine Funktion, die ein String als Parameter
# erhält und für jedes Zeichen, im String, außer Leerzeichen(!)
# ein Dictionary erstellt, das jedes auftauchende Zeichen
# als Key enthält und als Value speichert, wie oft
# das Zeichen im String auftaucht.
#
# "du da" -> {"d": 2, "u":1, "a": 1}
# "" -> {}
# "  " -> {}
# "12321" -> {"1": 2, "2": 2, "3": 1}
def count_letters(my_str):
    my_dic = {}
    new_string = my_str.replace(" ", "")
    for char in new_string:
        if char in my_dic:
            my_dic[char] += 1
        else:
            my_dic[char] = 1
    return my_dic

print(count_letters("12123123123"))

# 8 Punkte
# Schreibe eine Funktion das eine Liste von ints erhält.
# Die Funktion soll alle Elemente der Liste aufsummieren,
# dabei alle folgende Regel beachten:
# Ist die Zahl gerade, so wird sie normal hinzuaddiert,
# ist die Zahl ungerade, so wird sie abgezogen.
#
# [1,2,3,4,5] -> -1+2-3+4-5 = -3
# [] -> 0
# [0,0,0] -> 0
# [-1, -3, -5] -> -(-1)-(-3)-(-5) = 9
def funny_sum(my_list):
    rechnung = 0
    for number in my_list:
        if number % 2 == 0:
            rechnung += number
        else:
            rechnung -= number
    return rechnung

print(funny_sum([1,2,3,4,5]))
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
# [4,2,6,3,1,1] -> (True, False, True, True, False)
# [] -> ()
# [1] -> ()
# [1,2] -> (True,)
def is_left_bigger(my_list):
    boolean_tuple = ()
    for number in range(0,len(my_list),2):
        if my_list[number] < my_list[number+1]:
            boolean_tuple = boolean_tuple + (boolean_tuple,False)
        else:
            boolean_tuple = boolean_tuple + (boolean_tuple,True)
    return boolean_tuple

print(is_left_bigger([4,2,6,3,1,1]))


# 7 Punkte
# Schreibe eine Funktion die einen positiven Integer erhält.
# Sie gibt den Integer zurück, bei dem dann alle Ziffern
# Vertauscht sind. Führende Nullen werden dabei gestrichen.
#
# 13050 -> 5031
# 0 -> 0
# 1000 -> 1
# 1111 -> 1111
def swap_digets(number):
    ...


# 6 Punkte
# Schreibe eine Funktion, die einen String erwartet und
# jeden Kleinbuchstaben groß und jeden Großbuchstaben klein schreibt.
#
# "Aloh" -> "aLOH"
# "" -> ""
# "aaaa" -> "AAAA"
# "Ich bin ein Text" -> "iCH BIN EIN tEXT"
def swap_case(words):
    ...


# 6 Punkte
# Schreibe eine Funktion, die zwei Parameter annimmt und zwei Rückgabewerte
# besitzt. Die erste Rückgabe ist die Summe der beiden und die zweite
# Rückgabe ist die Subtraktion des zweiten vom ersten.
#
# 6, 9 -> 15, -3
# 1, 1 -> 2, 0
# 0, 0 -> 0, 0
# -22, -3 -> -25, -19
def add_and_sub(a, b):
    ...


# 6 Punkte
# Schreibe eine Funktion, die eine Text aus Buchstaben und leerzeichen
# erhält. Gebe ein Tupel zurück, das zählt, wie viele Zeichen
# zwischen zwei Leerzeichen sind. Bei zwei aufeinanderfolgenden Leerzeichen
# wird der Eintrag im Tupel ausgelassen (es gibt also keine Nullen
# im Tupel).
#
# "Hallo wer bist  du denn" -> (5, 3, 4, 2, 4)
# "" -> ()
# "   " -> ()
# "Hallo      du" -> (5, 2)
def all_len(words):
    ...


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
def change_type(my_obj):
    ...


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
