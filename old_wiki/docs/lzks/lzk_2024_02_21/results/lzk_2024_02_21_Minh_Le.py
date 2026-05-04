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
def remove_float_and_int_keys(dic):
    new_dic = dict()
    for key, value in dic.items():
        if type(key) not in [int, float]:
            new_dic[key] = value
    return new_dic

remove_float_and_int_keys({'h': 1, 4: 2, 2.0: "e"})
remove_float_and_int_keys({})
remove_float_and_int_keys({5: 1, 4: 2, 2.0: "e"})


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
    word_list = words.split()
    new_word_list = []
    for w in word_list:
        new_w = w[::-1]
        new_word_list.append(new_w)
    return ' '.join(new_word_list)

resort_within_word("Hallo wie geht es dir")
resort_within_word("")
resort_within_word("abc")

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
    if len(my_list):
        min_elem = min(my_list)
        max_elem = max(my_list)
        new_list = [elem for elem in my_list if elem in [min_elem, max_elem] ]
        return new_list
    else:
        return my_list
keep_smallest_biggest([1,4,3,4,1,2])
keep_smallest_biggest([1])
keep_smallest_biggest([])





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
    char_dict = dict()
    my_str_without_space = my_str.replace(' ', '')
    for char in my_str_without_space:
        char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict

count_letters("du da")
count_letters("")
count_letters("   ")
count_letters("12321")



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
    summation = 0
    for elem in my_list:
        if elem % 2: # even, False
            summation -= elem
        else:
            summation += elem
    return summation

funny_sum([1,2,3,4,5] )
funny_sum([])
funny_sum([0,0,0])
funny_sum([-1, -3, -5] )


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
# [1,2] -> (True,) <-- das ist komisch???
def is_left_bigger(my_list):
    bool_list = []
    if len(my_list): # not empty list
        for i in range(len(my_list)-1):
            bool_list.append( my_list[i] > my_list[i+1])
    return tuple(bool_list)

is_left_bigger([4,2,6,3,1,1])
is_left_bigger([])
is_left_bigger([1])
is_left_bigger([1,2]) # ??? KOMISCH?

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
    reversed_str_number = str(number)[::-1]
    reversed_str_number.strip('0')
    return int(reversed_str_number)

swap_digets(13050)
swap_digets(0)
swap_digets(1000)
swap_digets(1111)


# 6 Punkte
# Schreibe eine Funktion, die einen String erwartet und
# jeden Kleinbuchstaben groß und jeden Großbuchstaben klein schreibt.
#
# "Aloh" -> "aLOH"
# "" -> ""
# "aaaa" -> "AAAA"
# "Ich bin ein Text" -> "iCH BIN EIN tEXT"
def swap_case(words):
    new_words = ''
    for char in words:
        if char.islower():
            new_words += char.upper()
        else:
            new_words += char.lower()
    return new_words

swap_case("Aloh")
swap_case("")
swap_case("aaa")
swap_case("Ich bin ein Text")

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
    summation = a + b
    difference = a - b
    return summation, difference

add_and_sub(6,9)
add_and_sub(1,1)
add_and_sub(0,0)
add_and_sub(-22,-3)

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
    word_list = words.split()
    char_word_counter_list = [len(word) for word in word_list]
    return tuple(char_word_counter_list)

all_len("Hallo wer bist  du denn")
all_len("")
all_len("      ")
all_len("Hallo      du")


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
    numbers = [word for word in text.split() if word.isdigit() ]
    return set(numbers)

get_unique_numbers("10 ist größer als 8 ist gleich 8")
get_unique_numbers("10 10 100 1")

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
    if type(my_obj) == tuple:
        return set(my_obj)
    elif type(my_obj) == set:
        return list(my_obj)
    elif type(my_obj) == list:
        return tuple(my_obj)
    else:
        print("This is not valid")

change_type((1,2,3,2))
change_type({1,2,3})
change_type([1,3])
change_type(())


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
    new_list = []
    for elem in list_of_pairs:
        new_list.append(operation(elem))
    return new_list

apply_operation([(1, 3), (4.5, 5.5)], min)


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
def deep_positive_check(list_of_lists, zero_is_true = True):
    new_list_of_lists = []
    for list_elem in list_of_lists:
        if zero_is_true:
            new_sub_list = [elem >= 0 for elem in list_elem]
        else:
            new_sub_list = [elem > 0 for elem in list_elem]
        new_list_of_lists.append(new_sub_list)

    return new_list_of_lists

deep_positive_check([[1,2], [-2, 0, 3]])


