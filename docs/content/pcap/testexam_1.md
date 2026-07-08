# Testfragen 1

Kreuze die passende Antwort an. Die Lösung und Erklärung wird erst nach dem Prüfen angezeigt.



!!! note "Hinweis"

    Einige Code-Snippets liegen als Bilder vor, weil sie im Ausgangsmaterial als Bild gespeichert sind.



## Question 1

Consider the following code snippet:

![](../../assets/pcap_exam/image_rsrcF6A.jpg)

Which of the variables will contain False?

<div class="pcap-options" data-answer="B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">w</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">x</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">z</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">y</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B.**

Explanation

![](../../assets/pcap_exam/image_rsrcF6B.jpg)

Topic:

Try it yourself:

![](../../assets/pcap_exam/image_rsrcF6C.jpg)

The list with the value False is not empty and therefore it becomes True

<!-- page_16 -->

The string with the space also contain one character and therefore it also becomes True

The values that become False in Python are the following:

![](../../assets/pcap_exam/image_rsrcF6D.jpg)

</details>

## Question 2

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcF6E.jpg)

<!-- page_17 -->

<div class="pcap-options" data-answer="A">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">4</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">2</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">6</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">The code is erroneous.</span></label>
<label class="pcap-option"><input type="checkbox" value="E"> <span class="pcap-option-letter">E.</span> <span class="pcap-option-text">8</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A.**

Explanation

![](../../assets/pcap_exam/image_rsrcF6F.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcF6G.jpg)

This function looks for the highest element in a two dimensional list (or another iterable).

In the beginning the first number data[0][0] gets taken as a possible result. In the inner for loop every number is compared to the possible result. If one number is higher it becomes the new possible result.

And in the end the result is the highest number.

</details>

## Question 3

<!-- page_18 -->

isalnum() checks if a string contains only letters and digits, and this is:

<div class="pcap-options" data-answer="A">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">A method</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">A module</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">A function</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">A dataset</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A.**

Explanation

![](../../assets/pcap_exam/image_rsrcF6H.jpg)

Topic:

![](../../assets/pcap_exam/image_rsrcF6J.jpg)

isalnum() is a String-Method.

https://www.w3schools.com/python/ref_string_isalnum.asp

'Hello world' is not alphanumeric, because of the space character.

</details>

## Question 4

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcF6K.jpg)

<div class="pcap-options" data-answer="B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">2</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">4</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">5</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">3</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B.**

Explanation

![](../../assets/pcap_exam/image_rsrcF6M.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcF6N.jpg)

list.insert(i, x)

insert() inserts an item at a given position. The first argument is the index of the element before which to insert.

insert(0, 1) inserts 1 before index 0 (at the front of the list). The del keyword deletes the given object. In this case x[1]

The sum() function adds the items of a list (or a different iterable) and returns the sum.

</details>

## Question 5

What will be the output of the following code snippet?

![](../../assets/pcap_exam/image_rsrcF6P.jpg)

<!-- page_20 -->

<div class="pcap-options" data-answer="D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">3</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">None</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">4</span></label>
<label class="pcap-option"><input type="checkbox" value="E"> <span class="pcap-option-letter">E.</span> <span class="pcap-option-text">2</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: D.**

Explanation

![](../../assets/pcap_exam/image_rsrcF6R.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcF6S.jpg)

The operator precedence of the addition operator is higher than the operator precedence of the multiply and assign operator

That means the addition takes place before the multiplication.

</details>

## Question 6

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcF6T.jpg)

<div class="pcap-options" data-answer="D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">["Peter", "Wellert"]</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">["Peter", 404, 3.03, "Wellert", 33.3]</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">None of the above</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">[ 404, 3.03 ]</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: D.**

Explanation

![](../../assets/pcap_exam/image_rsrcF6U.jpg)

Topic:

![](../../assets/pcap_exam/image_rsrcF6V.jpg)

You have a list of five elements of various data types. [1:3] slices inclusive the first index and exclusive the third index. Meaning it slices the first and second index.

</details>

## Question 7

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcF6W.jpg)

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1 | Hello<br>2 | Hello<br>3 | Hello</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1 | Hello<br>2 | Hello</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">An infinite loop.</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1 | Hello<br>2 | Hello<br>3 | Hello<br>4 | Hello</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcF6X.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcF6Y.jpg)

The incrementation of num needs to be inside of the while loop. Otherwise the condition num > 0 will never be False

It should look like this:

<!-- page_23 -->

![](../../assets/pcap_exam/image_rsrcF6Z.jpg)

</details>

## Question 8

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcF70.jpg)

<div class="pcap-options" data-answer="D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">class</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">A number</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">name</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">A string ending with a long hexadecimal number.</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: D.**

<!-- page_24 -->

Explanation

![](../../assets/pcap_exam/image_rsrcF71.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcF72.jpg)

When there is no __str__() method present and you print an object, Python shows the object id in that way.

</details>

## Question 9

What is the expected output of the following code?

<!-- page_25 -->

![](../../assets/pcap_exam/image_rsrcF73.jpg)

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1 | True True</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1 | True False</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1 | False True</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1 | False False</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcF74.jpg)

Topics:

<!-- page_26 -->

![](../../assets/pcap_exam/image_rsrcF75.jpg)

busn_a is an instance of Business and therefore also an instance of the superclass Economy

econ_a is an instance of Economy

and therefore not an instance of the subclass Business

busn_a is referenced to busn_b

and they will point to the same object in the memory.

econ_a and econ_b are different objects.

</details>

## Question 10

What is the expected output of the following code if the user enters 2 and 4?

![](../../assets/pcap_exam/image_rsrcF76.jpg)

<!-- page_27 -->

<div class="pcap-options" data-answer="D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">4</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">2</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">6</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">24</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: D.**

Explanation

![](../../assets/pcap_exam/image_rsrcF77.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcF78.jpg)

As always the input() function returns a string. Therefore string concatenation takes place and the result is the string 24

(There are similar questions Q509 and Q648.)

</details>

## Question 11

The digraph written as #! is used to:

<div class="pcap-options" data-answer="B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">make a particular module entity a private one.</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">tell a Unix or Unix-like OS how to execute the contents of a Python file.</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">tell an MS Windows OS how to execute the contents of a Python file.</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">create a docstring.</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B.**

Explanation

![](../../assets/pcap_exam/image_rsrcF79.jpg)

Topic:

<!-- page_28 -->

This is a general UNIX topic. Best read about it here:

https://en.wikipedia.org/wiki/Shebang_(Unix)

</details>

## Question 12

Which of the following statements are true? (Select two answers)

<div class="pcap-options" data-answer="B,C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">The first argument of the open() function is an integer value.</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">The input() function reads data from the stdin stream.</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">There are three pre-opened file streams.</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">The readlines() function returns a string.</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B, C.**

Explanation

![](../../assets/pcap_exam/image_rsrcF7A.jpg)

Topics:

stdin, stdout, stderr are names of pre-opened streams. stdin is associated with the keyboard.

stdout and stderr are associated with the console.

https://en.wikipedia.org/wiki/Standard_streams

![](../../assets/pcap_exam/image_rsrcF7B.jpg)

readlines() with an s at the end returns a list of strings. The first argument of the open() function must be a string value with the name of the file.

<!-- page_29 -->

</details>

## Question 13

The function body is missing. What snippet would you insert in the line indicated below:

![](../../assets/pcap_exam/image_rsrcF7C.jpg)

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">return "number"</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">print(number)</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">return number</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">print("number")</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcF7D.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcF7E.jpg)

The parameter name is number therefore it can not be in quotes. If you only print something in the function, the function will return None and that is not wanted here, because the return values gets already printed outside of the function.

<!-- page_30 -->

</details>

## Question 14

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcF7F.jpg)

<div class="pcap-options" data-answer="A">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">3</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">4</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">2</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A.**

Explanation

![](../../assets/pcap_exam/image_rsrcF7G.jpg)

Topics:

<!-- page_31 -->

![](../../assets/pcap_exam/image_rsrcF7H.jpg)

There are three operators at work here. Of them the not operator has the highest precedence, followed by the and operator. The or operator has the lowest precedence.

</details>

## Question 15

An operator able to check whether two values are not equal is coded as:

<!-- page_32 -->

<div class="pcap-options" data-answer="D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">&lt;&gt;</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">not ==</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">=/=</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">! =</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: D.**

Explanation

![](../../assets/pcap_exam/image_rsrcF7J.jpg)

Topic:

![](../../assets/pcap_exam/image_rsrcF7K.jpg)

Other languages have <> or =/= as not equal to operators

In Python the not equal to operator is !=

not == does not work like this, because you can not have two operators next to each other.

It would work like that:

print(not(1 == 2)) # True

</details>

## Question 16

What will be the output of the following code snippet?

<!-- page_33 -->

![](../../assets/pcap_exam/image_rsrcF7M.jpg)

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">2</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">3</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">4</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcF7N.jpg)

Topics:

<!-- page_34 -->

![](../../assets/pcap_exam/image_rsrcF7P.jpg)

The knowledge you need here is that a dictionary can have indexes of different data types.

Therefore d[1] is a different index than d['1'] and they can both exist in the same dictionary.

To iterate through a dictionary is the same as iterating through dict.keys()

In k will be the keys of the dictionary. In this case 1 and '1'

The value of the first key will be 2 and the value of the other key will also be 2 and therefore (the) sum is 4

<!-- page_35 -->

</details>

## Question 17

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcF7R.jpg)

<div class="pcap-options" data-answer="B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">The code is erroneous.</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">23</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">100</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">None of the above.</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B.**

Explanation

![](../../assets/pcap_exam/image_rsrcF7S.jpg)

Topics:

<!-- page_36 -->

![](../../assets/pcap_exam/image_rsrcF7T.jpg)

The object variable id does not get changed by the initialisation of the local variable id in the __init__() method. They are two different entities.

</details>

## Question 18

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcF7U.jpg)

<!-- page_37 -->

<div class="pcap-options" data-answer="D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1 | True True</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1 | False True</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1 | False False</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1 | True False</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: D.**

Explanation

![](../../assets/pcap_exam/image_rsrcF7V.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcF7W.jpg)

The object creature is a Tiger and therefore a Cat and does have the attribute Species

The class Cat doesn't have the method set_species()

That method is defined in its subclass Tiger

<!-- page_38 -->

</details>

## Question 19

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcF7X.jpg)

<div class="pcap-options" data-answer="A">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">****</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">*</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">The code is erroneous.</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">**</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A.**

Explanation

![](../../assets/pcap_exam/image_rsrcF7Y.jpg)

Topics:

<!-- page_39 -->

![](../../assets/pcap_exam/image_rsrcF7Z.jpg)

The for loop inside of the function will iterate twice. Before the loop res has one star. In the first iteration a second star is added.

res then has two stars.

In the second iteration two more stars are added to those two star and res will end up with four stars.

The for loop outside of the function will just iterate through the string and print every single star.

You could get that easier by just printing the whole return value.

</details>

## Question 20

What is the expected output of the following code?

<!-- page_40 -->

![](../../assets/pcap_exam/image_rsrcF80.jpg)

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">2 1 2</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1 2 2</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1 1 2</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1 2 1</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcF81.jpg)

Topic:

![](../../assets/pcap_exam/image_rsrcF82.jpg)

We have multiple assignments in Python. You can assign multiple values to multiple variables.

<!-- page_41 -->

a, b = 3, 7

It is just shorter than

![](../../assets/pcap_exam/image_rsrcF83.jpg)

It does not have practical use, but what also works is

![](../../assets/pcap_exam/image_rsrcF84.jpg)

First c becomes 23 and then c becomes 42

You better write

c = 42

The same happens in this question in

z, y, z = 1, 1, 2

First z becomes 1 and then z becomes 2

You can also assign the same value to multiple variables:

![](../../assets/pcap_exam/image_rsrcF85.jpg)

</details>

## Question 21

Which module in Python supports regular expressions?

<div class="pcap-options" data-answer="B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">regex</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">re</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">None of the above</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">pyregex</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B.**

Explanation

![](../../assets/pcap_exam/image_rsrcF86.jpg)

Topic:

<!-- page_42 -->

![](../../assets/pcap_exam/image_rsrcF87.jpg)

Nothing to explain here. You just have to remember the name of the module re

</details>

## Question 22

The Exception class contains a property named args and it is a:

<div class="pcap-options" data-answer="A">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">tuple</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">list</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">string</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">dictionary</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A.**

Explanation

![](../../assets/pcap_exam/image_rsrcF88.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcF89.jpg)

<!-- page_43 -->

Makes sense. Integers as indexes is enough, therefore no dictionary

You might need more than one elements, therefore no string

You do not want it to be writable later on, therefore no list

That leaves the tuple

</details>

## Question 23

A PWG-lead repository, collecting open-source Python code, is called:

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">PWGR</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">PyCR</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">PyPI</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">PyRep</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcF8A.jpg)

Topic:

These websites describe it best:

https://pypi.org/help/#maintainers

https://en.wikipedia.org/wiki/Python_Package_Index

</details>

## Question 24

You want to check, whether the variable obj contains an object of the class A

Which of the following statements can you use?

<div class="pcap-options" data-answer="D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">A.isinstance(obj)</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">obj.isinstance(A)</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">isinstance(A, obj)</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">isinstance(obj, A)</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: D.**

Explanation

![](../../assets/pcap_exam/image_rsrcF8B.jpg)

<!-- page_44 -->

Topic:

![](../../assets/pcap_exam/image_rsrcF8C.jpg)

isinstance() is one of Python's built-in functions. There is no method isinstance()

The second argument can be a class or a tuple of classes.

</details>

## Question 25

How many elements does the L list contain?

![](../../assets/pcap_exam/image_rsrcF8D.jpg)

<!-- page_45 -->

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">three</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">two</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">zero</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">one</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcF8E.jpg)

Topic:

![](../../assets/pcap_exam/image_rsrcF8F.jpg)

range(-1, -2) has no element and therefore the list L will be empty.

</details>

## Question 26

Which of the following lines contain valid Python code? (Select two answers.)

<div class="pcap-options" data-answer="B,D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1 | lambda(a,b): return a if a &lt; b else b</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1 | lambda a,b: a if a &lt; b else b</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1 | lambda a,b = a if a &lt; b else b</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1 | lambda a,b: True</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B, D.**

Explanation

![](../../assets/pcap_exam/image_rsrcF8G.jpg)

Topics:

<!-- page_46 -->

![](../../assets/pcap_exam/image_rsrcF8H.jpg)

Both wrong answers have invalid syntax.

</details>

## Question 27

Knowing that a function named randint() resides in the module named random choose the proper way to import it:

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">from randint import random</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">import randint</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">from random import randint</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">import randint from random</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcF8J.jpg)

Topic:

<!-- page_47 -->

![](../../assets/pcap_exam/image_rsrcF8K.jpg)

The module name is random

You have to write the module first. And you import from a module.

from the module random you want to import the method randint

</details>

## Question 28

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcF8M.jpg)

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">It outputs None</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">The code is erroneous and will raise an exception.</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">It outputs False</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">It outputs True</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

<!-- page_48 -->

Explanation

![](../../assets/pcap_exam/image_rsrcF8N.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcF8P.jpg)

text_1 and text_2 are two different objects.

</details>

## Question 29

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcF8R.jpg)

<div class="pcap-options" data-answer="D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">0</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">0.0</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">0.4</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">0.2</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: D.**

Explanation

<!-- page_49 -->

![](../../assets/pcap_exam/image_rsrcF8S.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcF8T.jpg)

The operators here come from two different groups: The group "Multiplication, Division, Floor division, Modulus" has a higher precedence than the group "Addition, Subtraction".

Therefore the order of operations here is: // -> / -> +

</details>

## Question 30

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcF8U.jpg)

<div class="pcap-options" data-answer="B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">[ 1, 4 ]</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">[ 4, 3 ]</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">[ 1, 3, 4 ]</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">[ 1, 3 ]</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B.**

Explanation

![](../../assets/pcap_exam/image_rsrcF8V.jpg)

<!-- page_50 -->

Topics:

![](../../assets/pcap_exam/image_rsrcF8W.jpg)

A list is mutable. When you assign it to a different variable, you create a reference of the same object. If afterwards you change one of them, the other one is changed too.

</details>

## Question 31

Which of the following commands can be used to read n characters from a file?

<div class="pcap-options" data-answer="A">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">file.read(n)</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">n = file.read()</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">n = file.readline()</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">file.readline(n)</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A.**

Explanation

![](../../assets/pcap_exam/image_rsrcF8X.jpg)

Topics:

<!-- page_51 -->

![](../../assets/pcap_exam/image_rsrcF8Y.jpg)

![](../../assets/pcap_exam/image_rsrcF8Z.jpg)

The read() method has one optional parameter. If it is given, that number of characters are read.

If it is not given, the whole file is read.

file.readline([size])

The readline() method has also one optional parameter to specify the number of characters to be read. But it would only read that number of characters from the first line. If you want to read more characters, only the read() method will work.

</details>

## Question 32

What is the expected output of the following code?

<!-- page_52 -->

![](../../assets/pcap_exam/image_rsrcF90.jpg)

<div class="pcap-options" data-answer="A">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">bcac</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">bca</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">bcbc</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">acac</span></label>
<label class="pcap-option"><input type="checkbox" value="E"> <span class="pcap-option-letter">E.</span> <span class="pcap-option-text">bac</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A.**

Explanation

![](../../assets/pcap_exam/image_rsrcF91.jpg)

Topics:

<!-- page_53 -->

![](../../assets/pcap_exam/image_rsrcF92.jpg)

func(1) will try to execute 1 / 1

That will work fine and therefore not the except block, but the else block will be executed -> b

The finally block always gets executed -> c

func(0) will try to execute 1 / 0

That can not work.

In Python (like in any programming language) you can not divide by zero. In Python a ZeroDivisionError is raised and the except block is executed -> a

<!-- page_54 -->

Therefore the else block is not executed. And again the finally block always gets executed -> c

</details>

## Question 33

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcF93.jpg)

<div class="pcap-options" data-answer="B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">0</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">True</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">False</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B.**

Explanation

![](../../assets/pcap_exam/image_rsrcF94.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcF95.jpg)

The mathematical constant e is 2.718281828459045

It is true, that is not 16.0 like math.pow(2, 4)

The integer value of True is 1

<!-- page_55 -->

By the way, there is also a Python built-in function pow()

</details>

## Question 34

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcF96.jpg)

<div class="pcap-options" data-answer="D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">0</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">The code is erroneous and cannot be run.</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">2</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">4</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: D.**

Explanation

![](../../assets/pcap_exam/image_rsrcF97.jpg)

Topics:

<!-- page_56 -->

![](../../assets/pcap_exam/image_rsrcF98.jpg)

plane * 2 evaluates to CessnaCessna

There are two e and two a and therefore the counter will be 4

</details>

## Question 35

Which of the following variable names is illegal?

<div class="pcap-options" data-answer="A">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">in</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">In_</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">In</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">IN</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A.**

Explanation

![](../../assets/pcap_exam/image_rsrcF99.jpg)

Topic:

<!-- page_57 -->

![](../../assets/pcap_exam/image_rsrcF9A.jpg)

You can not name a variable like a Python keyword. Here is a list of all the Python keywords:

![](../../assets/pcap_exam/image_rsrcF9B.jpg)

Here are the other rules for naming variables in Python:

● A variable name must start with a letter or the underscore character.

● A variable name can not start with a number.

● A variable name can only contain alpha-numeric characters and underscores (a-z, 0-9, and _)

<!-- page_58 -->

Variable names are case-sensitive (age, Age and AGE are three different variables)

</details>

## Question 36

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcF9C.jpg)

<div class="pcap-options" data-answer="B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">7777777</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">The code is erroneous.</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">49</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">77</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B.**

Explanation

![](../../assets/pcap_exam/image_rsrcF9D.jpg)

Topic:

![](../../assets/pcap_exam/image_rsrcF9E.jpg)

As the error message above states, you can only multiply a string by an integer.

</details>

## Question 37

What will be the output of the following code snippet?

![](../../assets/pcap_exam/image_rsrcF9F.jpg)

<!-- page_59 -->

<div class="pcap-options" data-answer="A">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">2 1</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1 2</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1 1</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">2 2</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A.**

Explanation

![](../../assets/pcap_exam/image_rsrcF9G.jpg)

Topic:

![](../../assets/pcap_exam/image_rsrcF9H.jpg)

Integer is an immutable data type. The values get copied from one variable to another.

In the end x and y changed their values.

</details>

## Question 38

Which of the following statements are true about the __pycache__ directory/folder? (Select two answers.)

<div class="pcap-options" data-answer="A,C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">It is created automatically.</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">It has to be created manually by the module's creator.</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">It contains semi-compiled module code.</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">It has to be created manually by the module's user.</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A, C.**

<!-- page_60 -->

Explanation

![](../../assets/pcap_exam/image_rsrcF9J.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcF9K.jpg)

Run the code and check your file system.

(Your IDE (e.g. PyCharm) may not show the __pycache__ folder.)

When the module my_module is imported Python automatically creates the folder __pycache__

And in the folder is a file with semi-compiled code

![](../../assets/pcap_exam/image_rsrcF9M.jpg)

</details>

## Question 39

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcF9N.jpg)

<div class="pcap-options" data-answer="B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">The code will raise an AttributeError exception.</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">0</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">2</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B.**

Explanation

![](../../assets/pcap_exam/image_rsrcF9P.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcF9R.jpg)

![](../../assets/pcap_exam/image_rsrcF9S.jpg)

<!-- page_62 -->

The topics here are private variables and name mangling:

https://docs.python.org/3/tutorial/classes.html#private-variables

If you have instance variables with two leading underscores, you can not just access them from outside of the class. You would need getter and setter like in class B

</details>

## Question 40

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcF9T.jpg)

<div class="pcap-options" data-answer="A">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">3 42</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">The code is erroneous.</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">3 1</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1 1</span></label>
<label class="pcap-option"><input type="checkbox" value="E"> <span class="pcap-option-letter">E.</span> <span class="pcap-option-text">1 42</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A.**

Explanation

![](../../assets/pcap_exam/image_rsrcF9U.jpg)

Topics:

<!-- page_63 -->

![](../../assets/pcap_exam/image_rsrcF9V.jpg)

This question is about argument passing. It is a big difference, whether you pass a mutable or an immutable data type. The immutable integer in x gets copied to p1 and the change of p1 does not affect x

The mutable list in y gets referenced to p2 and the change of p2 effect y

</details>

## Question 41

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcF9W.jpg)

<div class="pcap-options" data-answer="A">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">[ 3, 5, 20, 5, 25, 1, 3 ]</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">[ 1, 3, 4, 5, 20, 5, 25 ]</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">[ 1, 3, 3, 4, 5, 5, 20, 25 ]</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">[ 3, 4, 5, 20, 5, 25, 1, 3 ]</span></label>
<label class="pcap-option"><input type="checkbox" value="E"> <span class="pcap-option-letter">E.</span> <span class="pcap-option-text">[ 3, 1, 25, 5, 20, 5, 4 ]</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A.**

Explanation

![](../../assets/pcap_exam/image_rsrcF9X.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcF9Y.jpg)

list.pop([i])

The index is optional. If the index is given, pop() removes and returns the element at the given index. The default index is -1

Meaning that the last index is removed and returned. Here the index 1 gets removed: the number 4

</details>

## Question 42

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcF9Z.jpg)

<!-- page_65 -->

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">4 4</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1 1</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">The code is erroneous.</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1 4</span></label>
<label class="pcap-option"><input type="checkbox" value="E"> <span class="pcap-option-letter">E.</span> <span class="pcap-option-text">4 1</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcFA0.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFA1.jpg)

<!-- page_66 -->

![](../../assets/pcap_exam/image_rsrcFA2.jpg)

A variable name shadows into a function. You can use it in an expression like in func2() or you can assign a new value to it like in func3()

BUT you can not do both at the same time like in func()

There is going to be the new variable num and you can not use it in an expression before its first assignment.

</details>

## Question 43

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcFA3.jpg)

<div class="pcap-options" data-answer="B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1 | 261</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1 | ('list index out of range',)</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1 | ('success',)</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1 | 321</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B.**

Explanation

![](../../assets/pcap_exam/image_rsrcFA4.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFA5.jpg)

There is no third last index and an IndexError is raised. The except branch is executed and the args of the exception are printed.

</details>

## Question 44

What will be the output of the following code snippet?

![](../../assets/pcap_exam/image_rsrcFA6.jpg)

<div class="pcap-options" data-answer="D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">0</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">6/10</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">None of the above.</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">0.6</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: D.**

Explanation

![](../../assets/pcap_exam/image_rsrcFA7.jpg)

Topic:

<!-- page_68 -->

![](../../assets/pcap_exam/image_rsrcFA8.jpg)

The division operator does its normal job. And remember the division operator ALWAYS returns a float.

</details>

## Question 45

What is true about updating already installed Python packages?

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">It's an automatic process which doesn't require any user attention.</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">It can be done only by uninstalling the package once again.</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">It's performed by the install command accompanied by the -U option.</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">It can be done by reinstalling the package using the reinstall command.</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcFA9.jpg)

Topic:

First use pip list --outdated to list your outdated packages. Then use pip install -U package_name to update one of the packages. If you do pip list --outdated again, you will see, that the chosen package is no longer in the list of outdated packages.

pip install --upgrade package_name would work, too.

You can also use pip show package_name to see the version (and other information) of a package.

</details>

## Question 46

<!-- page_69 -->

Select the true statements about the map() function. Choose two.

<div class="pcap-options" data-answer="A,D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">The map() function can accept more than two arguments.</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">The map() function can accept only two arguments.</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">The first map() function argument can be a list.</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">The second map() function argument can be a list.</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A, D.**

Explanation

![](../../assets/pcap_exam/image_rsrcFAA.jpg)

Topic:

![](../../assets/pcap_exam/image_rsrcFAB.jpg)

Yes, the map() function can accept more than two arguments. The elements of the second parameter of the map() function (here list1) will be assigned to the first parameter of the lambda function (here x).

The elements of the third parameter of the map() function (here list2) will be assigned to the second parameter of the lambda function (here y).

There could even be more parameters. And yes, the second map() function argument (here list1) can be a list. But the first map() function argument must be a function.

</details>

## Question 47

<!-- page_70 -->

What is the expected behavior of the following program?

![](../../assets/pcap_exam/image_rsrcFAC.jpg)

<div class="pcap-options" data-answer="F">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">The program will raise an exception handled by the first except block.</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">The program will cause a ZeroDivisionError exception and output the following message: Too bad...</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">The program will cause a ValueError exception and output a default error message.</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">The program will cause a ZeroDivisionError exception and output a default error message.</span></label>
<label class="pcap-option"><input type="checkbox" value="E"> <span class="pcap-option-letter">E.</span> <span class="pcap-option-text">The program will cause a ValueError exception and output the following message: Too bad...</span></label>
<label class="pcap-option"><input type="checkbox" value="F"> <span class="pcap-option-letter">F.</span> <span class="pcap-option-text">The program will cause a SyntaxError exception.</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: F.**

Explanation

![](../../assets/pcap_exam/image_rsrcFAD.jpg)

Topics:

<!-- page_71 -->

![](../../assets/pcap_exam/image_rsrcFAE.jpg)

There are two syntax errors:

break can not be used outside of a loop, and the default except must be last.

</details>

## Question 48

What is the expected output of the following code?

<!-- page_72 -->

![](../../assets/pcap_exam/image_rsrcFAF.jpg)

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">I from B is 30</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">I from A is 0</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">I from A is 30</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">I from A is 20</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcFAG.jpg)

Topics:

<!-- page_73 -->

![](../../assets/pcap_exam/image_rsrcFAH.jpg)

When b is instantiated as an object of class B its constructor calls the constructor of its parent class A

The classes A and B both have a method named calc() therefore the method in A gets overridden by the method in B

Now the constructor in A (which is called from out of B) will instantiate the object variable i

Then it will call the calc() method and pass 10 as a value. Because we are in B, the calc() method of B is called.

The passed value will be multiplied by 3 and stored in b.i

10 * 3 -> 30

And in the end the print() function will print: i from A is 30

</details>

## Question 49

What is the expected output of the following code?

<!-- page_74 -->

![](../../assets/pcap_exam/image_rsrcFAJ.jpg)

<div class="pcap-options" data-answer="A">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1 | Name of the file: data.txt<br>2 | Peter Wellert<br>3 |<br>4 | Hello everybody</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1 | Peter Wellert<br>2 | Hello everybody</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1 | Peter Wellert Hello everybody</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">The code is erroneous.</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A.**

Explanation

![](../../assets/pcap_exam/image_rsrcFAK.jpg)

Topics:

<!-- page_75 -->

![](../../assets/pcap_exam/image_rsrcFAM.jpg)

![](../../assets/pcap_exam/image_rsrcFAN.jpg)

open() with the mode w+ opens a file for writing and reading. If the file doesn't exist, it will be created.

First something gets written into the file. Then the file pointer gets set back to the beginning. And then the file gets iterated line by line by the for loop.

</details>

## Question 50

<!-- page_76 -->

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcFAP.jpg)

<div class="pcap-options" data-answer="D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">The code is erroneous,<br>because the print method is called without an argument.</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">The code is erroneous,<br>because the constructor is called without an argument.</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">Nothing</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">Welcome</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: D.**

Explanation

![](../../assets/pcap_exam/image_rsrcFAR.jpg)

Topics:

<!-- page_77 -->

![](../../assets/pcap_exam/image_rsrcFAS.jpg)

Everything will work fine here. The __init__() method will initialize the object variable s with the value Welcome and the print() method will print just that.

</details>

## Question 51

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcFAT.jpg)

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">2019/Nov/27 11:27:22</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">2019/11/27 11:27:22</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">19/ November/27 11:27:22</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">19/11/27 11:27:22</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcFAU.jpg)

Topics:

<!-- page_78 -->

![](../../assets/pcap_exam/image_rsrcFAV.jpg)

You "just" have to learn these:

https://strftime.org

</details>

## Question 52

What would you insert instead ??? so that the program checks for even numbers?

![](../../assets/pcap_exam/image_rsrcFAW.jpg)

<div class="pcap-options" data-answer="D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">x % 1 == 2</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">x % "even" == True</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">x % x == 0</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">x % 2 == 0</span></label>
<label class="pcap-option"><input type="checkbox" value="E"> <span class="pcap-option-letter">E.</span> <span class="pcap-option-text">x % 2 == 1</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: D.**

Explanation

![](../../assets/pcap_exam/image_rsrcFAX.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFAY.jpg)

Every number that is divided by two does not leave a rest is even.

<!-- page_79 -->

</details>

## Question 53

What will be the output of the following code snippet?

![](../../assets/pcap_exam/image_rsrcFAZ.jpg)

<div class="pcap-options" data-answer="D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">[ 8, 9 ]</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">[ 1, 2]</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">[ 1, 2, 3 ]</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">[ 1, 3, 5, 7, 9 ]</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: D.**

Explanation

![](../../assets/pcap_exam/image_rsrcFB0.jpg)

Topic:

![](../../assets/pcap_exam/image_rsrcFB1.jpg)

List slicing: [start(inclusive):end(exclusive):step]

The start and end values are missing here.

If you leave them out, you will slice from the beginning to the end. If you leave the end out it will also be inclusive.

The third value (the step) is 2 therefore every second element gets taken.

</details>

## Question 54

You need to find out if a hardware platform utilizes the x86 or armCPU. Which method from the module platform can you use? (Select two answers.)

<div class="pcap-options" data-answer="B,C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1 | hardware()</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1 | platform()</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1 | processor()</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1 | node()</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B, C.**

Explanation

![](../../assets/pcap_exam/image_rsrcFB2.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFB3.jpg)

platform.platform()

Returns a single string identifying the underlying platform with as much useful information as possible.

https://docs.python.org/3/library/platform.html#platform.platform

platform.processor()

Returns the (real) processor name, e.g. 'amdk6'.

https://docs.python.org/3/library/platform.html#platform.processor

platform.node()

Returns the computer’s network name (may not be fully qualified!). An empty string is returned if the value cannot be determined.

https://docs.python.org/3/library/platform.html#platform.node

</details>

## Question 55

What is the expected output of the following code?

<!-- page_81 -->

![](../../assets/pcap_exam/image_rsrcFB4.jpg)

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">The code is erroneous.</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">0</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">2</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcFB5.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFB6.jpg)

The backslash is the character to escape another character. Here the backslash escapes the following single quote character. Together they are one character.

</details>

## Question 56

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcFB7.jpg)

<div class="pcap-options" data-answer="B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">[ 1, 3, 5, 7, 9 ]</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">[ 0, 2, 4, 6, 8 ]</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1 | 0<br>2 | 2<br>3 | 4<br>4 | 6<br>5 | 8</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">None of the above</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B.**

Explanation

![](../../assets/pcap_exam/image_rsrcFB8.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFB9.jpg)

This list comprehension will iterate through range(5) add each number to itself and assign the sum to the result list.

</details>

## Question 57

Which of the following snippets outputs 123 to the screen?

<div class="pcap-options" data-answer="A,B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1 | tmp = list("321")<br>2 | tmp.sort()<br>3 | print("".join(tmp))</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1 | print("".join(sorted("321")))</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1 | print(sorted("321"))</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1 | tmp = "321".sort()<br>2 | print(str(tmp))</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A, B.**

<!-- page_83 -->

Explanation

![](../../assets/pcap_exam/image_rsrcFBA.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFBB.jpg)

</details>

## Question 58

What is the default return value for a function that does not explicitly return any value?

<div class="pcap-options" data-answer="D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">void</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">int</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">public</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">None</span></label>
<label class="pcap-option"><input type="checkbox" value="E"> <span class="pcap-option-letter">E.</span> <span class="pcap-option-text">Null</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: D.**

Explanation

![](../../assets/pcap_exam/image_rsrcFBC.jpg)

<!-- page_84 -->

Topic:

![](../../assets/pcap_exam/image_rsrcFBD.jpg)

If a function does not have the keyword return the function will return the value None

The same happens if there is no value after the keyword return

</details>

## Question 59

A subclass is usually:

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">More general than its superclass.</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">A twin of its superclass.</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">More specialized than its superclass.</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">None of the above</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcFBE.jpg)

Topic:

<!-- page_85 -->

![](../../assets/pcap_exam/image_rsrcFBF.jpg)

The student is more "specialized" than the person. Not only does he have a firstname and a lastname but he has also a graduationyear

</details>

## Question 60

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcFBG.jpg)

<div class="pcap-options" data-answer="A">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1 | 23<br>2 | 42</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">23</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">42</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1 | 42<br>2 | 23</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A.**

Explanation

![](../../assets/pcap_exam/image_rsrcFBH.jpg)

Topic:

![](../../assets/pcap_exam/image_rsrcFBJ.jpg)

The function will try to execute print(23) and succeed. The finally block always gets executed.

</details>

## Question 61

Select the true statements. Choose two.

<!-- page_87 -->

<div class="pcap-options" data-answer="B,D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">The version function from the platform module returns a string with your Python version.</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">The version function from the platform module returns a string with your OS version.</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">The processor function from the platform module returns an integer with the number of processes currently running in your OS.</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">The system function from the platform module returns a string with your OS name.</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B, D.**

Explanation

![](../../assets/pcap_exam/image_rsrcFBK.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFBM.jpg)

Yes, the system function returns a string with your OS name and the version function returns a string with your OS version. The processor function returns a string with the name of your processor.

</details>

## Question 62

Entering the try: block implies that:

<div class="pcap-options" data-answer="B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">none of the instructions from this block will be executed.</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">some of the instructions from this block may not be executed.</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">all of the instructions from this block will be executed.</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">the block will be omitted.</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B.**

Explanation

![](../../assets/pcap_exam/image_rsrcFBN.jpg)

Topic:

<!-- page_88 -->

![](../../assets/pcap_exam/image_rsrcFBP.jpg)

In this case the multiplication and the printing will not be executed, because the type casting will already raise an exception.

</details>

## Question 63

You want to write a code snippet to read the total data from a text file and print it to the monitor. What snippet would you insert in the line indicated below:

![](../../assets/pcap_exam/image_rsrcFBR.jpg)

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">data = file.load()</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">data = file.readline()</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">data = file.read()</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">data = file.readlines()</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcFBS.jpg)

Topics:

<!-- page_89 -->

![](../../assets/pcap_exam/image_rsrcFBT.jpg)

The read() method is the right choice here. It reads the whole content of a file and returns it as a string.

The readline() method only reads one line. The readlines() method also reads the whole content, but returns it as a list of lines. That is definitely not wanted here. And load() is not a method of the file object.

</details>

## Question 64

Which of the following are valid Python string literals? (Select two answers.)

<div class="pcap-options" data-answer="A,D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1 | """The knights Who Say 'Ni!'"""</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1 | 'All the king's horses'</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1 | "\"</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1 | "king's Cross Station"</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A, D.**

Explanation

<!-- page_90 -->

![](../../assets/pcap_exam/image_rsrcFBU.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFBV.jpg)

A single quote can be used in a string delimited by double quotes (and vice versa).

And a single quote can be used in a multi-line string delimited by triple double quotes (and vice versa).

</details>

## Question 65

Which method is used to break the connection between the file handle and a physical file?

<div class="pcap-options" data-answer="D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">disconnect()</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">shutup()</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">lock()</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">close()</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: D.**

Explanation

![](../../assets/pcap_exam/image_rsrcFBW.jpg)

Topics:

<!-- page_91 -->

![](../../assets/pcap_exam/image_rsrcFBX.jpg)

The close() method closes an open file. You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.

https://www.w3schools.com/python/ref_file_close.asp

</details>

## Question 66

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcFBY.jpg)

<div class="pcap-options" data-answer="B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">[ 3 ]</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">[ 2 ]</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">[ 1 ]</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">[ ]</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B.**

Explanation

![](../../assets/pcap_exam/image_rsrcFBZ.jpg)

<!-- page_92 -->

Topics:

![](../../assets/pcap_exam/image_rsrcFC0.jpg)

The g() function expects three parameters. It will invoke the third parameter and pass the first two to it. When 1 and 1 are pass as arguments to the lambda function it will slice the list v by [1:2] and return a list like [2]

</details>

## Question 67

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcFC1.jpg)

<div class="pcap-options" data-answer="A">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1*1*1</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">The code is erroneous.</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">x y z</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1 1 1</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A.**

Explanation

<!-- page_93 -->

![](../../assets/pcap_exam/image_rsrcFC2.jpg)

Topic:

![](../../assets/pcap_exam/image_rsrcFC3.jpg)

The print() function has a sep parameter which stands for separator. The default value of the sep parameter is a space character. You can change it to anything you want.

</details>

## Question 68

What value will be assigned to the x variable?

![](../../assets/pcap_exam/image_rsrcFC4.jpg)

<div class="pcap-options" data-answer="A">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">True</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">False</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">0</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A.**

Explanation

![](../../assets/pcap_exam/image_rsrcFC5.jpg)

Topic:

<!-- page_94 -->

![](../../assets/pcap_exam/image_rsrcFC6.jpg)

The operators here are from three different groups.

"Comparisons, Identity, Membership operators", "Logical AND", "Logical OR".

The two comparison operators the greater than operator and the less than operator have the highest precedence. Then the logical and operator has a higher precedence than the logical or operator

</details>

## Question 69

Consider the following file module.py.

![](../../assets/pcap_exam/image_rsrcFC7.jpg)

What will be the output, if you run it?

<div class="pcap-options" data-answer="B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">__module__</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">__main__</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">main</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">module</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B.**

<!-- page_95 -->

Explanation

![](../../assets/pcap_exam/image_rsrcFC8.jpg)

Topic:

![](../../assets/pcap_exam/image_rsrcFC9.jpg)

The output will be: __main__

If you import that file, the output would be: module

But that is not asked here.

</details>

## Question 70

What happens if you run the following code, assuming that the d directory already exists?

![](../../assets/pcap_exam/image_rsrcFCA.jpg)

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">A DirectoryExistsError exception will be raised.</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">Python will overwrite the existing directory.</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">A FileExistsError exception will be raised.</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">All of the above.</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcFCB.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFCC.jpg)

The makedirs() method is to create all the directories. And than mkdir() raises the FileExistsError because the directory d already exists.

See also:

<!-- page_96 -->

https://docs.python.org/3/library/os.html#os.mkdir

</details>

## Question 71

The value thirty point eleven times ten raised to the power of nine should be written as:

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">30.11E9.0</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">30E11.9</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">30.11E9</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">30.11*10^9</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcFCD.jpg)

Topic:

![](../../assets/pcap_exam/image_rsrcFCE.jpg)

You could replace the E by * 10 **

</details>

## Question 72

What is the output of the following program if the user enters kangaroo at the first prompt and 0 at the second prompt?

<!-- page_97 -->

![](../../assets/pcap_exam/image_rsrcFCF.jpg)

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1 | Wrong value</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1 | Do not divide by zero!</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1 | 4.0</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1 | Error.Error.Error.</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcFCG.jpg)

Topics:

<!-- page_98 -->

![](../../assets/pcap_exam/image_rsrcFCH.jpg)

No exception will be thrown. The length of kangaroo is 8 and the length of 0 is 1

1 * 2 -> 2

8 / 2 -> 4.0

</details>

## Question 73

Which of the following for loops would output the below number pattern?

![](../../assets/pcap_exam/image_rsrcFCJ.jpg)

<div class="pcap-options" data-answer="B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1 | for i in range(1, 6)<br>2 | print(i, i, i, i, i)</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1 | for i in range(1, 6):<br>2 | print(str(i) * 5)</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1 | for i in range(0, 5):<br>2 | print(str(i) * 5)</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1 | for i in range(1, 5)<br>2 | print(str(i) * 5)</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B.**

Explanation

![](../../assets/pcap_exam/image_rsrcFCK.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFCM.jpg)

<!-- page_100 -->

![](../../assets/pcap_exam/image_rsrcFCN.jpg)

You need range(1, 6) because the start value 1 is inclusive and the end value 6 is exclusive.

To get the same numbers next to each other (without a space between them) you need to make a string and then use the multiply operator string concatenation

The standard separator of the print() function is one space.

![](../../assets/pcap_exam/image_rsrcFCP.jpg)

gives you one space between each number. It would work with print(i, i, i, i, i, sep='') but that answer is not offered here.

</details>

## Question 74

<!-- page_101 -->

Assuming that the open() invocation has gone successfully, the following snippet will:

![](../../assets/pcap_exam/image_rsrcFCR.jpg)

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">read the whole file at once.</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">cause an exception.</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">read the file line by line.</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">read the file character by character.</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcFCS.jpg)

Topic:

![](../../assets/pcap_exam/image_rsrcFCT.jpg)

The for loop will iterate through the file line by line. The mode 'rt' stands for read & text.

</details>

## Question 75

Given the code below, indicate a method which will correctly provide the value of the rack field?

<!-- page_102 -->

![](../../assets/pcap_exam/image_rsrcFCU.jpg)

<div class="pcap-options" data-answer="B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1 | def get():<br>2 | return rack</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1 | def get(self):<br>2 | return self.rack</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1 | def get(self):<br>2 | return rack</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1 | def get():<br>2 | return self.rack</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B.**

Explanation

![](../../assets/pcap_exam/image_rsrcFCV.jpg)

Topics:

<!-- page_103 -->

![](../../assets/pcap_exam/image_rsrcFCW.jpg)

The object method needs to have the object reference self as a parameter and the object variable needs to have self in front. Otherwise it would be a local variable.

</details>

## Question 76

A function named f() is included in a module named m and the module is part of a package named p. Which of the following code snippets allows you to properly invoke the function? (Select two answers.)

<div class="pcap-options" data-answer="A,B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1 | from p.m import f<br>2 |<br>3 | f()</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1 | import p.m<br>2 |<br>3 | p.m.f()</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1 | import p.m.f<br>2 |<br>3 | f()</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1 | import p<br>2 |<br>3 | m.f()</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A, B.**

Explanation

![](../../assets/pcap_exam/image_rsrcFCX.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFCY.jpg)

If you use the from keyword, you can just write the function name. Otherwise you have to write the qualified name in front of the function.

<!-- page_105 -->

</details>

## Question 77

You develop a Python application for your company. You have the following code.

![](../../assets/pcap_exam/image_rsrcFCZ.jpg)

Which of the following expressions is equivalent to the expression in the function?

<div class="pcap-options" data-answer="D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">(a + b ) * ( c - d )</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">A + ( ( b * c ) - d )</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">None of the above</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">(a + (b * c ) ) - d</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: D.**

Explanation

![](../../assets/pcap_exam/image_rsrcFD0.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFD1.jpg)

This question is about operator precedence

<!-- page_106 -->

The multiplication operator has the highest precedence and is therefore executed first.

That leaves the addition operator and the subtraction operator

They both are from the same group and therefore have the same precedence. That group has a left-to-right associativity. The addition operator is on the left and is therefore executed next.

And the last one to be executed is the subtraction operator

</details>

## Question 78

What is the expected behavior of the following snippet?

![](../../assets/pcap_exam/image_rsrcFD2.jpg)

It will:

<div class="pcap-options" data-answer="B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">print 6</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">print 8</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">cause a runtime exception on Line 8</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">cause a runtime exception on Line 9</span></label>
<label class="pcap-option"><input type="checkbox" value="E"> <span class="pcap-option-letter">E.</span> <span class="pcap-option-text">print 4</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B.**

Explanation

![](../../assets/pcap_exam/image_rsrcFD3.jpg)

Topics:

<!-- page_107 -->

![](../../assets/pcap_exam/image_rsrcFD4.jpg)

The first call of the function a() will pass 1 to the function.

2 * 1 -> 2

The function will return 2

2 + 2 -> 4

The second call of the function a() will pass 4 to the function.

2 * 4 -> 8

8 will be printed.

</details>

## Question 79

What is the output of the following code snippet?

![](../../assets/pcap_exam/image_rsrcFD5.jpg)

<!-- page_108 -->

<div class="pcap-options" data-answer="B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1 3</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">3 2</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">The code is erroneous.</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">3 3</span></label>
<label class="pcap-option"><input type="checkbox" value="E"> <span class="pcap-option-letter">E.</span> <span class="pcap-option-text">2 3</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B.**

Explanation

![](../../assets/pcap_exam/image_rsrcFD6.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFD7.jpg)

Okay, both parameters get the default value of the other one, but for the rest it's business as usual.

</details>

## Question 80

What is the expected output of the following code?

<!-- page_109 -->

![](../../assets/pcap_exam/image_rsrcFD8.jpg)

<div class="pcap-options" data-answer="E">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">The code is erroneous.</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">False</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">0</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1</span></label>
<label class="pcap-option"><input type="checkbox" value="E"> <span class="pcap-option-letter">E.</span> <span class="pcap-option-text">True</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: E.**

Explanation

![](../../assets/pcap_exam/image_rsrcFD9.jpg)

Topics:

<!-- page_110 -->

![](../../assets/pcap_exam/image_rsrcFDA.jpg)

C is a subclass of A

C is a grandchild of A so to speak.

B is a subclass of A

C is a subclass of B

And therefore C is a subclass of A

</details>

## Question 81

What is the expected output of the following code?

<!-- page_111 -->

![](../../assets/pcap_exam/image_rsrcFDB.jpg)

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">2 0</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">4 0</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">3 1</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">4 1</span></label>
<label class="pcap-option"><input type="checkbox" value="E"> <span class="pcap-option-letter">E.</span> <span class="pcap-option-text">3 0</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcFDC.jpg)

<!-- page_112 -->

Topics:

![](../../assets/pcap_exam/image_rsrcFDD.jpg)

The object b will inherit the object variable x from class A and get the attribute y from its own class B

The start value of x will be 3 and the start value from y will be 0

The method func() will be from the class B because the function from A with the same name will be overriden. When b.func() is called, y will be incremented and then the output is: 3 1

</details>

## Question 82

<!-- page_113 -->

Which of the following expressions evaluates to True and raises no exception?

<div class="pcap-options" data-answer="A">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1 | 10 != "1" + "0"</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1 | "Al" * 2 != 2 * "Al"</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1 | "9" * 3 &gt; "9" * 9</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1 | "9" * 1 &lt; 1 * 2</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A.**

Explanation

![](../../assets/pcap_exam/image_rsrcFDE.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFDF.jpg)

<!-- page_114 -->

</details>

## Question 83

What is the correct command to shuffle the following list?

![](../../assets/pcap_exam/image_rsrcFDG.jpg)

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">shuffle(people)</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">people.shuffle()</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">random.shuffle(people)</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">random.shuffleList(people)</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcFDH.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFDJ.jpg)

import random imports the whole module. If you want to use one of its methods, you have to add it by dot notation. The shuffle() method will change the original list in-place.

</details>

## Question 84

<!-- page_115 -->

What is the expected behavior of the following snippet?

![](../../assets/pcap_exam/image_rsrcFDK.jpg)

<div class="pcap-options" data-answer="D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">It outputs anonymous</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">It raises an exception.</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">It outputs an empty line.</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">It outputs Alpha</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: D.**

Explanation

![](../../assets/pcap_exam/image_rsrcFDM.jpg)

Topics:

<!-- page_116 -->

![](../../assets/pcap_exam/image_rsrcFDN.jpg)

Class A will override the get_ID() method of its superclass Team and therefore the output will be Alpha

</details>

## Question 85

Which of the following variables will Python consider to be private?

<div class="pcap-options" data-answer="B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1 | privatedata_</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1 | _privatedata</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1 | _privatedata_</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1 | private_data</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B.**

Explanation

![](../../assets/pcap_exam/image_rsrcFDP.jpg)

Topics:

<!-- page_117 -->

![](../../assets/pcap_exam/image_rsrcFDR.jpg)

If you want Python to treat your variable as private, you should start its name with two underscores.

</details>

## Question 86

The 0o prefix means that the number after it is denoted as:

<div class="pcap-options" data-answer="B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">binary</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">octal</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">decimal</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">hexadecimal</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B.**

Explanation

![](../../assets/pcap_exam/image_rsrcFDS.jpg)

Topic:

![](../../assets/pcap_exam/image_rsrcFDT.jpg)

The octal numeral system, or oct for short, is the base-8 number system, and uses the digits 0 to 7

<!-- page_118 -->

</details>

## Question 87

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcFDU.jpg)

<div class="pcap-options" data-answer="B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">The code is erroneous.</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">None</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">2</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B.**

Explanation

![](../../assets/pcap_exam/image_rsrcFDV.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFDW.jpg)

This is a conditional expression.

1 % 2 is 1 and therefore not equal to 0

The condition is True and the inner func() function call returns 1

<!-- page_119 -->

That 1 is passed to the outer function which will also return 1

</details>

## Question 88

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcFDX.jpg)

<div class="pcap-options" data-answer="A">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">['h' ,'e' ,'l' ,'l' ,'o']</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">[ h, e, l, l ,o ]</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">['h' 'e' 'l' 'l' 'o']</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">None of the above.</span></label>
<label class="pcap-option"><input type="checkbox" value="E"> <span class="pcap-option-letter">E.</span> <span class="pcap-option-text">hello</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A.**

Explanation

![](../../assets/pcap_exam/image_rsrcFDY.jpg)

Topic:

![](../../assets/pcap_exam/image_rsrcFDZ.jpg)

A string is a sequence of characters and works very fine with the list() function. The result is a list of strings, in which every character is a string of its own.

</details>

## Question 89

The system that allows you to diagnose input/output errors in Python is called:

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1 | error_number</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1 | error_string</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1 | errno</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1 | errcode</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcFE0.jpg)

Topics:

<!-- page_120 -->

https://docs.python.org/3/library/errno.html

http://www.ioplex.com/%7Emiallen/errcmpp.html

</details>

## Question 90

The ABC organics company needs a simple program that their call center will use to enter survey data for a new coffee variety. The program must accept input and return the average rating based on a five-star scale. The output must be rounded to two decimal places. You need to complete the code to meet the requirements.

![](../../assets/pcap_exam/image_rsrcFE1.jpg)

What should you insert instead of XXX, YYY and ZZZ?

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1 | XXX -> float(input("Enter next rating (1-5), -1 for done"))<br>2 | YYY -> printline(" The average star rating for the new coffee is: "<br>3 | ZZZ -> format(average, ".2f"))</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1 | XXX -> float(input("Enter next rating (1-5), -1 for done"))<br>2 | YYY -> print(" The average star rating for the new coffee is:<br>3 | ZZZ -> format(average, " .2d"))</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1 | XXX -> float(input("Enter next rating (1-5), -1 for done"))<br>2 | YYY -> print(" the average star rating for the new coffee is: "<br>3 | ZZZ -> format(average, ".2f"))</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1 | XXX -> input(input("Enter next rating (1-5), -1 for done"))<br>2 | YYY -> print(" The average star rating for the new coffee is: "<br>3 | ZZZ -> format(average, ".2d"))</span></label>
<label class="pcap-option"><input type="checkbox" value="E"> <span class="pcap-option-letter">E.</span> <span class="pcap-option-text">1 | XXX -> float(input("Enter next rating (1-5), -1 for done"))<br>2 | YYY -> output(" The average star rating for the new coffee is : "<br>3 | ZZZ -> format(average, ".2d"))</span></label>
<label class="pcap-option"><input type="checkbox" value="F"> <span class="pcap-option-letter">F.</span> <span class="pcap-option-text">1 | XXX -> print(input("Enter next rating (1-5), -1 for done"))<br>2 | YYY -> print(" The average star rating for the new coffee is: "<br>3 | ZZZ -> format(average, ".2f"))</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcFE2.jpg)

<!-- page_122 -->

Topics:

![](../../assets/pcap_exam/image_rsrcFE3.jpg)

The input() function always returns a string

You need to cast that string to a float with the float() function. The function to print something to the monitor is called print()

And if you want to round a float to two decimal places, you need the format string '.2f'

</details>

## Question 91

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcFE4.jpg)

<!-- page_123 -->

<div class="pcap-options" data-answer="D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">17</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">8</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">8.5</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">17.5</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: D.**

Explanation

![](../../assets/pcap_exam/image_rsrcFE5.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFE6.jpg)

The operators here come from three different groups:

"Exponent" has the highest precedence. Followed by "Multiplication, Division, Floor division, Modulus". "Addition, Subtraction" has the lowest precedence. Therefore the order of operations here is: ** -> / -> // -> + -> +

<!-- page_124 -->

</details>

## Question 92

The part of your code where you think an exception may occur should be placed inside:

<div class="pcap-options" data-answer="A">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">the try: branch</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">the except: branch</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">the exception: branch</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">None of the above</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A.**

Explanation

![](../../assets/pcap_exam/image_rsrcFE7.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFE8.jpg)

Therefore the name try

</details>

## Question 93

How many stars will the following code print to the monitor?

<!-- page_125 -->

![](../../assets/pcap_exam/image_rsrcFE9.jpg)

<div class="pcap-options" data-answer="D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">one</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">three</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">zero</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">two</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: D.**

Explanation

![](../../assets/pcap_exam/image_rsrcFEA.jpg)

Topic:

![](../../assets/pcap_exam/image_rsrcFEB.jpg)

In the first iteration of the while loop i is 0

i becomes 2 and the first star is printed. In the second iteration of the while loop i is 2

i becomes 4 and the second star is printed.

i is 4 and therefore 4 <= 3 is False what ends the while loop.

</details>

## Question 94

<!-- page_126 -->

When a module is imported, its contents:

<div class="pcap-options" data-answer="D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">are executed depending on the contents.</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">are executed as many times as they are imported.</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">are ignored.</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">are executed once.</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: D.**

Explanation

![](../../assets/pcap_exam/image_rsrcFEC.jpg)

Topic:

![](../../assets/pcap_exam/image_rsrcFED.jpg)

An imported module is executed only once.

</details>

## Question 95

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcFEE.jpg)

<!-- page_127 -->

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">2222222222</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">Syntax Error</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1024</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">4201</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcFEF.jpg)

Topic:

![](../../assets/pcap_exam/image_rsrcFEG.jpg)

This does work, but you should not do it. It violates the programming guideline E731: Do not assign a lambda expression, use a def

</details>

## Question 96

How many stars will the following snippet print to the monitor?

<!-- page_128 -->

![](../../assets/pcap_exam/image_rsrcFEH.jpg)

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">2</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">0</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">The snippet will enter an infinite loop.</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcFEJ.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFEK.jpg)

In the first iteration the break gets directly triggered. Therefore there will be only one star. The else would only apply, if the break does NOT get triggered.

</details>
