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
dic = {'h': 1, 4: 2, 2.0: "e"} #-> {'h': 1}
newdic = {}
{} #-> {}
{5: 1, 4: 2, 2.0: "e"}#) #-> {}

def remove_float_and_int_keys(dic):
    ...
#     for key in dic.key():
#         if not type(key) == int or type(key) == float:
#             newdic[key] = dic[key]
#     return newdic

# remove_float_and_int_keys(dic)

# print(newdic)


# 7 Punkte
# Erstelle eine Funktion, die einen String erwartet. Dieser
# String besteht nur aus Groß- und Kleinbuchstaben und einzelnen
# Leerzeichen, die weder am Anfang noch am Ende des Strings sind.
# Schreibe eine Funktion, welche die Reihenfolge alle Buchstaben zwischen
# zwei Leerzeichen ändert.
#
#words = "Hallo wie geht es dir" #-> "ollaH eiw theg se rid"
changed_new_word_list = []
words = "" #-> ""
#words= "abc" #-> "cba"
#words= "t st s" #-> "t ts s"

def resort_within_word(words):
    new_word_list = words.split(" ")
    for element in new_word_list:
        changed_new_word_list.append(element[::-1])
    print(changed_new_word_list)
    return changed_new_word_list # Von Viktor Korrigiert

#resort_within_word(words)    


# 7 Punkte
# Schreibe eine Funktion, die eine Liste als Parameter
# annimmt und eine neue Liste zurückgibt, bei der
# alle Elemente außer den größten und dem kleinsten
# entfernt wurden. Wenn die Liste leer ist, soll auch die
# leere Liste zurückgegeben werden.
#
new_my_list = []
mylist = [1,4,3,4,1,2] #-> [1,4,4,1]

# [1] -> [1]
# [] -> []
def keep_smallest_biggest(my_list):
    for i in range(len(my_list)):
        max_value = max(mylist)
        min_value = min(my_list)
    for i in mylist:
        if i == max_value or i==min_value:
            new_my_list.append(i)

    print(new_my_list)
    return new_my_list # Von Viktor Korrigiert
      
#keep_smallest_biggest(mylist)

   #...


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
    ...


# 8 Punkte
# Schreibe eine Funktion das eine Liste von ints erhält.
# Die Funktion soll alle Elemente der Liste aufsummieren,
# dabei alle folgende Regel beachten:
# Ist die Zahl gerade, so wird sie normal hinzuaddiert,
# ist die Zahl ungerade, so wird sie abgezogen.
#
numberlist = [1,2,3,4,5] #-> -1+2-3+4-5 = -3
# [] -> 0
# [0,0,0] -> 0
#[-1, -3, -5] #-> -(-1)-(-3)-(-5) = 9

def funny_sum(my_list):
    z = 0
    for i in my_list:
        if i % 2 == 0:
            z= z +i
        else:
            z= z - i
    print(z)
    return z # von Viktor korrigiert
#funny_sum(numberlist)

    #...


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
    ...


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
a, b = 6, 9 #-> 15, -3
# 1, 1 -> 2, 0
# 0, 0 -> 0, 0
# -22, -3 -> -25, -19
def add_and_sub(a, b):
    c = a + b
    d = a - b
    return c,d
c,d = add_and_sub(a, b)

#print(c,d)

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
text = "10 ist größer als 8 ist gleich 8" #-> {8, 10}
# "10 10 100 1" -> {1, 10, 100}
# "10" -> {10}
# "random Text" -> {}
helplist = []
def get_unique_numbers(text):
    wordlist = text.split(" ")
    print(wordlist)
    for element in wordlist:
         if type(element) == type(1):
             print("stimmt")
    #         helplist = helplist.append(element)
    # print(helplist)
    #print(resultset)
get_unique_numbers(text)
    


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
