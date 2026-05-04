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
my_dict = {'h': 1, 4: 2, 2.0: "e"}
my_dict2 = {5: 1, 4: 2, 2.0: "e"}


def remove_float_and_int_keys(dic):
    result_dict = dic.copy()
    for key in dic.keys():
        if isinstance(key, int) or isinstance(key, float):
            result_dict.pop(key)

    return  result_dict


print(remove_float_and_int_keys(my_dict))
print(remove_float_and_int_keys(my_dict2))


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
def resort_within_word(words: str):
    str_list = words.split(" ")
    new_str = ""
    for word in str_list:
        new_str += word[::-1] + " "
    return new_str[:-1]


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
    new_list = my_list
    if len(new_list) > 1:
        for i in range(len(new_list)):
            if new_list[i] < new_list[0]:
                new_list[0] = new_list[i]
            elif new_list[i] > new_list[1]:
                new_list[1] = new_list[i]
        return new_list[:2]
    else:
        return new_list


print(keep_smallest_biggest([1, 2]))


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
    letter_dict = {}
    my_str = my_str.replace(" ", "")
    for letter in my_str:
        letter_dict[letter] = letter_dict.get(letter, 0) + 1
    return letter_dict


print(count_letters("12321"))


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
    summe = 0
    for i in my_list:
        if i % 2 == 0:
            summe += i
        else:
            summe -= i
    return summe


print(funny_sum([1, 2, 3, 4, 5]))


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
    is_bigger_list = []
    if len(my_list) > 1:
        for i in range(len(my_list) - 1):
            is_bigger_list.append(my_list[i] > my_list[i + 1])
        return tuple(is_bigger_list)
    else:
        return ()


print(is_left_bigger([4, 2, 6, 3, 1, 1]))


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
    return int(str(number)[::-1])


print(swap_digets(13050))


# 6 Punkte
# Schreibe eine Funktion, die einen String erwartet und
# jeden Kleinbuchstaben groß und jeden Großbuchstaben klein schreibt.
#
# "Aloh" -> "aLOH"
# "" -> ""
# "aaaa" -> "AAAA"
# "Ich bin ein Text" -> "iCH BIN EIN tEXT"
def swap_case(words: str):
    new_words = ""
    for char in words:
        if char.isupper():
            new_words += char.lower()
        else:
            new_words += char.upper()
    return new_words


print(swap_case("Ich bin ein Text"))


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
    return a + b, a - b


print(add_and_sub(-22, -3))


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
    word_list = words.split(" ")
    count_list = []
    for word in word_list:
        count_list.append(len(word))
    for i in count_list:
        if i == 0:
            count_list.remove(i)
    return tuple(count_list)


print(all_len("Hallo wer bist du  denn"))


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
def get_unique_numbers(text: str):
    number_set = set()
    for word in text.split(" "):
        if word.isnumeric():
            number_set.add(word)
    return number_set


print(get_unique_numbers("10 10 100 1"))


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
    return list(map(operation, list_of_pairs))


print(apply_operation([("a", "b")], max))


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
def deep_positive_check(list_of_lists, zero_is_true=True):
    bool_list = list_of_lists
    for liste in bool_list:
        for i in range(len(liste)):
            if liste[i] > 0:
                liste[i] = True
            elif liste[i] < 0:
                liste[i] = False
            else:
                liste[i] = zero_is_true
    return bool_list


print(deep_positive_check([[1, 2], [-2, 0, 3]]))
print(deep_positive_check([[1, 2], [-2, 0, 3]], False))