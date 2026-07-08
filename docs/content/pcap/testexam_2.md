# Testfragen 2

Kreuze die passende Antwort an. Die Lösung und Erklärung wird erst nach dem Prüfen angezeigt.



!!! note "Hinweis"

    Einige Code-Snippets liegen als Bilder vor, weil sie im Ausgangsmaterial als Bild gespeichert sind.



## Question 1

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcFEM.jpg)

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">0</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">2</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">The code is erroneous.</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcFEN.jpg)

Topics:

<!-- page_130 -->

![](../../assets/pcap_exam/image_rsrcFEP.jpg)

In a multiline string the line feed gets saved like any other character.

</details>

## Question 2

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcFER.jpg)

<div class="pcap-options" data-answer="D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">7.0</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">9.0</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">8</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">8.0</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: D.**

<!-- page_131 -->

Explanation

![](../../assets/pcap_exam/image_rsrcFES.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFET.jpg)

<!-- page_132 -->

The operators here are from three different groups: "Exponent" has the highest precedence. Followed by "Multiplication, Division, Floor division, Modulus". "Addition, Subtraction" has the lowest precedence.

Therefore the order of operations here is: ** -> // -> * -> / -> % -> +

</details>

## Question 3

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcFEU.jpg)

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1 | LR</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1 | RH</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1 | 1r</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1 | rh</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcFEV.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFEW.jpg)

The filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.

![](../../assets/pcap_exam/image_rsrcFEX.jpg)

<!-- page_133 -->

https://www.w3schools.com/python/ref_func_filter.asp

The lambda function will return True if the last character of its passed string is an "A" or an "O"

Otherwise it will return False. Therefore "alpha" and "bravo" end up in new_vect

At index 1 of "alpha" is "l" and at index 1 of "bravo" is "r". Therefore "lr" is printed.

</details>

## Question 4

You know that a function named func() resides in a module named mod

The module has been imported using the following line:

![](../../assets/pcap_exam/image_rsrcFEY.jpg)

How can you invoke the function?

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">mod::func()</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">func()</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">mod.func()</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">mod-.func()</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcFEZ.jpg)

Topic:

<!-- page_134 -->

![](../../assets/pcap_exam/image_rsrcFF0.jpg)

If you import the whole module you have to add the entity by dot notation.

</details>

## Question 5

Assuming that the following code has been executed successfully, indicate the expressions which evaluate to True and don't raise any exceptions.

![](../../assets/pcap_exam/image_rsrcFF1.jpg)

<!-- page_135 -->

(Select two answers.)

<div class="pcap-options" data-answer="B,C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1 | "stuff" in binder.__dict__</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1 | len(binder.__dict__) != len(Collection.__dict__)</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1 | "stamps" in Collection.__dict__</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1 | len(binder.__dict__) &gt; 0</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B, C.**

Explanation

![](../../assets/pcap_exam/image_rsrcFF2.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFF3.jpg)

<!-- page_136 -->

</details>

## Question 6

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcFF4.jpg)

<div class="pcap-options" data-answer="B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">The code is erroneous.</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">3 1</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1 3</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1 1</span></label>
<label class="pcap-option"><input type="checkbox" value="E"> <span class="pcap-option-letter">E.</span> <span class="pcap-option-text">3 3</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B.**

Explanation

![](../../assets/pcap_exam/image_rsrcFF5.jpg)

Topics: scope

<!-- page_137 -->

![](../../assets/pcap_exam/image_rsrcFF6.jpg)

The num variable inside the function scope will be a different variable. It will shadow the name of the num variable from the outer scope, but it will be a different entity.

</details>

## Question 7

The following statement ...

![](../../assets/pcap_exam/image_rsrcFF7.jpg)

<div class="pcap-options" data-answer="D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">is erroneous.</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">has no effect.</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">will stop the program if x is equal to O</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">will stop the program if xis not equal to O</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: D.**

Explanation

![](../../assets/pcap_exam/image_rsrcFF8.jpg)

Topic:

<!-- page_138 -->

![](../../assets/pcap_exam/image_rsrcFF9.jpg)

If the assertion (here x == 0) is True, the program will continue. Otherwise an AssertionError occurs.

</details>

## Question 8

Which of the following statements are true?

(Select two answers.)

<div class="pcap-options" data-answer="A,C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">The print() function writes its output to the stdout stream.</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">The open() function returns False when its operation fails.</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">Stdin, stdout, stderr are names of pre-opened streams.</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">The second argument of the open() function is an integer value.</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A, C.**

Explanation

![](../../assets/pcap_exam/image_rsrcFFA.jpg)

Topics:

● stdin, stdout, stderr are names of pre-opened streams.

● stdout and stderr are associated with the console.

● stdin is associated with the keyboard.

https://en.wikipedia.org/wiki/Standard_streams

</details>

## Question 9

What is the expected output of the following code?

<!-- page_139 -->

![](../../assets/pcap_exam/image_rsrcFFB.jpg)

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">The code is erroneous.</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">Peter</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">PeterWellert</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">Wellert</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcFFC.jpg)

Topic:

![](../../assets/pcap_exam/image_rsrcFFD.jpg)

String literals that are delimited by whitespace are automatically concatenated.

</details>

## Question 10

Which of the following functions immediately terminates a program?

<div class="pcap-options" data-answer="B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">sys.terminate()</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">sys.exit()</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">sys.halt()</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">None</span></label>
<label class="pcap-option"><input type="checkbox" value="E"> <span class="pcap-option-letter">E.</span> <span class="pcap-option-text">sys.stop()</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B.**

Explanation

![](../../assets/pcap_exam/image_rsrcFFE.jpg)

Topic:

<!-- page_140 -->

![](../../assets/pcap_exam/image_rsrcFFF.jpg)

The method in Python to immediately terminate a program is sys.exit()

The others methods do not exist.

</details>

## Question 11

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcFFG.jpg)

<!-- page_141 -->

<div class="pcap-options" data-answer="B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1 | False True</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1 | True False</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1 | False False</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1 | True True</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B.**

Explanation

![](../../assets/pcap_exam/image_rsrcFFH.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFFJ.jpg)

Yes, the holder object has the Token attribute because it is derived from its superclass.

No, The Ceil class doesn't have the set_token() method of its subclass.

</details>

## Question 12

What is the expected output of the following code:

<!-- page_142 -->

if there is no file named non_existing_file in the working directory/folder, and the open() function invocation is successful?

![](../../assets/pcap_exam/image_rsrcFFK.jpg)

<div class="pcap-options" data-answer="D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1 | 1 2 4</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1 | 1 2 3 4</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1 | 2 4</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1 | 1 3</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: D.**

Explanation

![](../../assets/pcap_exam/image_rsrcFFM.jpg)

Topics:

<!-- page_143 -->

![](../../assets/pcap_exam/image_rsrcFFN.jpg)

The file is only opened in write mode. Then 1 is printed. If you try to read from that file you get an IOError

![](../../assets/pcap_exam/image_rsrcFFP.jpg)

Therefore the except branch is executed and 3 is printed.

</details>

## Question 13

What is the expected output of the following code?

<!-- page_144 -->

![](../../assets/pcap_exam/image_rsrcFFR.jpg)

<div class="pcap-options" data-answer="A">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">3</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">0</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">2</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A.**

Explanation

![](../../assets/pcap_exam/image_rsrcFFS.jpg)

Topics:

<!-- page_145 -->

![](../../assets/pcap_exam/image_rsrcFFT.jpg)

The constructor will initialize a.v with the default value 2

An object is a mutable data type. Assigning it will create a reference to the same object.

b.set() will increment b.v to 3 and because it is a reference a.v is also changed to 3

</details>

## Question 14

A code point is:

<div class="pcap-options" data-answer="A">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">A number which makes up a character.</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">A code containing a point.</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">A point used to write a code.</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">None of the above.</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A.**

Explanation

![](../../assets/pcap_exam/image_rsrcFFU.jpg)

Topic:

<!-- page_146 -->

![](../../assets/pcap_exam/image_rsrcFFV.jpg)

For example in ASCII the number 65 makes up the character A

https://en.wikipedia.org/wiki/Code_point

</details>

## Question 15

The part of your code where the handling of an exception takes place should be placed inside:

<div class="pcap-options" data-answer="A">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">the except: branch</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">the exception: branch</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">the try: branch</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">None of the above</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A.**

Explanation

![](../../assets/pcap_exam/image_rsrcFFW.jpg)

Topic:

![](../../assets/pcap_exam/image_rsrcFFX.jpg)

It is about exceptions, but the branch is called except:

</details>

## Question 16

Consider the following code.

![](../../assets/pcap_exam/image_rsrcFFY.jpg)

<!-- page_147 -->

What would you insert instead of ???

so that the program prints the following pattern to the monitor?

![](../../assets/pcap_exam/image_rsrcFFZ.jpg)

<div class="pcap-options" data-answer="D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">2</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">n</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">str(n)</span></label>
<label class="pcap-option"><input type="checkbox" value="E"> <span class="pcap-option-letter">E.</span> <span class="pcap-option-text">-1</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: D.**

Explanation

![](../../assets/pcap_exam/image_rsrcFG0.jpg)

Topics:

<!-- page_148 -->

![](../../assets/pcap_exam/image_rsrcFG1.jpg)

![](../../assets/pcap_exam/image_rsrcFG2.jpg)

<!-- page_149 -->

![](../../assets/pcap_exam/image_rsrcFG3.jpg)

![](../../assets/pcap_exam/image_rsrcFG4.jpg)

<!-- page_150 -->

![](../../assets/pcap_exam/image_rsrcFG5.jpg)

range(1, 6, 1) delivers the right numbers 1, 2, 3, 4, 5. (It would also works without step 1, because that's the default value.)

You need the str() function here to get more numbers. Otherwise a calculation takes place and you end up with one number per row. By string concatenation you get the right result:

![](../../assets/pcap_exam/image_rsrcFG6.jpg)

</details>

## Question 17

Which of the following function calls can be used to invoke the below function definition?

![](../../assets/pcap_exam/image_rsrcFG7.jpg)

Choose three.

<!-- page_151 -->

<div class="pcap-options" data-answer="A,B,D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">test(1, 2, 3, 4)</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">test(1, 2, 3, d=4)</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">test(a=1, b=2, c=3, 4)</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">test(a=1, b=2, c=3, d=4)</span></label>
<label class="pcap-option"><input type="checkbox" value="E"> <span class="pcap-option-letter">E.</span> <span class="pcap-option-text">test(a=1, 2, 3, 4)</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A, B, D.**

Explanation

![](../../assets/pcap_exam/image_rsrcFG8.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFG9.jpg)

The keyword arguments always have to be at the end.

</details>

## Question 18

If the class’s constructor is declared as below, which one of the assignments is valid?

![](../../assets/pcap_exam/image_rsrcFGA.jpg)

<!-- page_152 -->

<div class="pcap-options" data-answer="B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">Object = Class(object)</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">object = Class()</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">object = Class(self)</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">object = Class</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B.**

Explanation

![](../../assets/pcap_exam/image_rsrcFGB.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFGC.jpg)

It needs to be Class()

Class without parentheses does not raise an exception, but you do not assign an object of Class

Instead you would create a reference.

</details>

## Question 19

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcFGD.jpg)

<!-- page_153 -->

<div class="pcap-options" data-answer="B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">0</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">The code is erroneous.</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">2</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B.**

Explanation

![](../../assets/pcap_exam/image_rsrcFGE.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFGF.jpg)

range(2) has two elements: 0 and 1

Therefore the outer list will have two elements. And data[2] does not exist.

</details>

## Question 20

Which of the following variable names is illegal?

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">true</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">TRUE</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">True</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">true</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcFGG.jpg)

Topic:

<!-- page_154 -->

![](../../assets/pcap_exam/image_rsrcFGH.jpg)

You can not name a variable like a Python keyword.

</details>

## Question 21

How many stars will the following code print to the monitor?

![](../../assets/pcap_exam/image_rsrcFGJ.jpg)

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">one</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">two</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">four</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">eight</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcFGK.jpg)

Topics:

<!-- page_155 -->

![](../../assets/pcap_exam/image_rsrcFGM.jpg)

Left shift by one, a classic way to double values. Every value goes to the bit on its left and thereby doubles in value. And 1, 2, 4, 8 are all smaller than 10 but not the 16 and therefore four stars will be printed.

</details>

## Question 22

The += operator, when applied to strings, performs:

<div class="pcap-options" data-answer="A">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">Concatenation</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">Multiplication</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">Subtraction</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">None of the above.</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A.**

Explanation

![](../../assets/pcap_exam/image_rsrcFGN.jpg)

Topic:

<!-- page_156 -->

![](../../assets/pcap_exam/image_rsrcFGP.jpg)

The add and assign operator when applied to strings, performs a string concatenation.

Just like the addition operator

</details>

## Question 23

Consider the following code.

![](../../assets/pcap_exam/image_rsrcFGR.jpg)

Which of the following statements best describes the behavior of the random.shuffle() method?

<div class="pcap-options" data-answer="A">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">It shuffles the elements of the list in-place.</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">It will not modify the list.<br>This function is just a placeholder and yet to be implemented.</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">It returns a list where the elements 10, 20, and 30 would be at random positions.</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">It shuffles the elements for the number of times equal to the size of the list.</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A.**

Explanation

![](../../assets/pcap_exam/image_rsrcFGS.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFGT.jpg)

The original list gets shuffled in-place. The return value is None

</details>

## Question 24

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcFGU.jpg)

<div class="pcap-options" data-answer="D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">4</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">4.0</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">3</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">3.5</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: D.**

Explanation

![](../../assets/pcap_exam/image_rsrcFGV.jpg)

Topics:

<!-- page_158 -->

![](../../assets/pcap_exam/image_rsrcFGW.jpg)

The operators here are from two different groups:

The group "Multiplication, Division, Floor division, Modulus" has a higher precedence than the group "Addition, Subtraction".

Therefore the order of operations here is: // -> / -> + -> + -> +

</details>

## Question 25

Is there a way to check if a class is a subclass of another class?

<div class="pcap-options" data-answer="A">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">Yes, there is a function that can do that.</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">No.</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">It may be possible, but only under special conditions.</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">None of the above.</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A.**

Explanation

![](../../assets/pcap_exam/image_rsrcFGX.jpg)

<!-- page_159 -->

Topic:

![](../../assets/pcap_exam/image_rsrcFGY.jpg)

And the name of the function is issubclass()

</details>

## Question 26

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcFGZ.jpg)

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">abcdef</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">An empty line.</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">ace</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">bdf</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

<!-- page_160 -->

Explanation

![](../../assets/pcap_exam/image_rsrcFH0.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFH1.jpg)

The generator function will return every second element of the passed data.

</details>

## Question 27

Which of the following is false?

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">A try statement can have one or more except clauses.</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">A try statement can have a finally clause and an except clause.</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">A try statement can have one or more final clauses.</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">A try statement can have a final clause without an except clause.</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcFH2.jpg)

Topics:

<!-- page_161 -->

![](../../assets/pcap_exam/image_rsrcFH3.jpg)

![](../../assets/pcap_exam/image_rsrcFH4.jpg)

<!-- page_162 -->

![](../../assets/pcap_exam/image_rsrcFH5.jpg)

● Yes, a try statement can have one or more except clauses.

● Yes, a try statement can have a finally clause and an except clause.

● Yes, a try statement can have a finally clause without an except clause.

● But NO, a try statement can NOT have more finally clauses.

</details>

## Question 28

What is the expected output of the following code?

<!-- page_163 -->

![](../../assets/pcap_exam/image_rsrcFH6.jpg)

<div class="pcap-options" data-answer="D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1 | spin default</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1 | spin spin</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1 | default default</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1 | default spin</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: D.**

Explanation

![](../../assets/pcap_exam/image_rsrcFH7.jpg)

Topics:

<!-- page_164 -->

![](../../assets/pcap_exam/image_rsrcFH8.jpg)

The FixedWing class doesn't have its own start() method and therefore the start() method of its superclass Aircraft is executed and default is returned and printed.

The RotorCraft class on the other hand does have its own start() method which overrides the start() method of its superclass Aircraft and therefore in the second iteration spin is returned and printed.

</details>

## Question 29

What is the expected output of the following code?

<!-- page_165 -->

![](../../assets/pcap_exam/image_rsrcFH9.jpg)

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">I'm gonna make him an offer he can't refuse.</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">The code is erroneous.</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">["I'm", 'gonna', 'make', 'him', 'an', 'offer', 'he', "can't", 'refuse.']</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">I</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcFHA.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFHB.jpg)

<!-- page_166 -->

The method readlines() always returns a list. In this case there is only one line in the file and readlines() returns a list with one element.

Therefore the for loop only has one iteration. The one element is a string.

The split() method with no argument passed will split the string at its whitespaces and return a list of the parts. At the end this list gets printed.

Actually the for loop is superfluous. The following would have sufficed:

![](../../assets/pcap_exam/image_rsrcFHC.jpg)

</details>

## Question 30

Select the true statements. Choose two.

<div class="pcap-options" data-answer="B,D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">The lambda function can evaluate multiple expressions.</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">The lambda function can evaluate only one expression.</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">The lambda function can accept a maximum of two arguments.</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">The lambda function can accept any number of arguments.</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B, D.**

Explanation

![](../../assets/pcap_exam/image_rsrcFHD.jpg)

Topic:

![](../../assets/pcap_exam/image_rsrcFHE.jpg)

"Lambda functions can have any number of arguments but only one expression. The expression is evaluated and returned. Lambda functions can be used wherever function objects are required."

<!-- page_167 -->

https://www.programiz.com/python-programming/anonymous-function#how

</details>

## Question 31

How many stars will the following code print to the monitor?

![](../../assets/pcap_exam/image_rsrcFHF.jpg)

<div class="pcap-options" data-answer="D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">one</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">zero</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">two</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">The snippet will enter an infinite loop.</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: D.**

Explanation

![](../../assets/pcap_exam/image_rsrcFHG.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFHH.jpg)

<!-- page_168 -->

i gets incremented inside the while loop, BUT i will always be smaller than i + 2

Therefore the whole condition will always be True and we build ourselves a nice infinite loop.

</details>

## Question 32

Consider the following code.

![](../../assets/pcap_exam/image_rsrcFHJ.jpg)

The value eventually assigned to x is equal to:

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">False</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">True</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">0</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcFHK.jpg)

Topic:

![](../../assets/pcap_exam/image_rsrcFHM.jpg)

x has the value 1

x gets compared with the equal to operator with itself.

It is true, that x is equal to x

True gets stored in the same variable, in x

<!-- page_169 -->

</details>

## Question 33

Which program will produce the following output:

![](../../assets/pcap_exam/image_rsrcFHN.jpg)

<div class="pcap-options" data-answer="D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1 | import calendar<br>2 | print(calendar.week)</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1 | import calendar<br>2 | print(calendar.weekheader(3))</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1 | import calendar<br>2 | print(calendar.weekheader())</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1 | import calendar<br>2 | print(calendar.weekheader(2))</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: D.**

Explanation

![](../../assets/pcap_exam/image_rsrcFHP.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFHR.jpg)

The argument has to be 2 because you want two letters per day of the week.

https://www.includehelp.com/python/calendar-weekheader-method-with-example.aspx

<!-- page_170 -->

</details>

## Question 34

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcFHS.jpg)

<div class="pcap-options" data-answer="B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1,3</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1.3</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">The code is erroneous.</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">13</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B.**

Explanation

![](../../assets/pcap_exam/image_rsrcFHT.jpg)

Topic:

![](../../assets/pcap_exam/image_rsrcFHU.jpg)

The function float() does its normal job here and converts the string to a float.

</details>

## Question 35

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcFHV.jpg)

<div class="pcap-options" data-answer="B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">abdef</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">The code is erroneous.</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">abcef</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">acdef</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B.**

Explanation

![](../../assets/pcap_exam/image_rsrcFHW.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFHX.jpg)

A string is immutable. You can not change it. You can read something by indexing, BUT you can not write something by indexing.

</details>

## Question 36

What is true about object-oriented programming (OOP)? (Select two answers.)

<!-- page_172 -->

<div class="pcap-options" data-answer="A,B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">A class is like a blueprint used to construct objects.</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">A class may exist without its objects, while objects cannot exist without their class.</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">A relation between superclass and its subclass is known as fraternity.</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">Polymorphism is a phenomenon which allows you to have many classes of the same name.</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A, B.**

Explanation

![](../../assets/pcap_exam/image_rsrcFHY.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFHZ.jpg)

Yes, a class is like a blueprint used to construct objects.

Yes, a class may exist without its objects, while objects cannot exist without their class.

A relation between a superclass and its subclass is known as inheritance. Polymorphism is the use of a single symbol to represent different types.

https://en.wikipedia.org/wiki/Polymorphism_(computer_science)

https://www.geeksforgeeks.org/polymorphism-in-python/

</details>

## Question 37

What value will be assigned to the x variable?

<!-- page_173 -->

![](../../assets/pcap_exam/image_rsrcFJ0.jpg)

<div class="pcap-options" data-answer="D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">0</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">true</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">False</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: D.**

Explanation

![](../../assets/pcap_exam/image_rsrcFJ1.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFJ2.jpg)

The operators here are from three different groups.

"Comparisons, Identity, Membership operators", "Logical AND", "Logical OR".

![](../../assets/pcap_exam/image_rsrcFJ3.jpg)

The three different comparison operators

![](../../assets/pcap_exam/image_rsrcFJ4.jpg)

have the highest precedence.

![](../../assets/pcap_exam/image_rsrcFJ5.jpg)

<!-- page_174 -->

![](../../assets/pcap_exam/image_rsrcFJ5.jpg)

Then the logical `and` operator has a higher precedence than the logical `or` operator.

</details>

## Question 38

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcFJ6.jpg)

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">Hello Python</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">AttributeError: 'Test' object has no attribute 's'</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">NameError: name 's' is not defined</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">TypeError: Test() takes no arguments</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcFJ7.jpg)

Topics:

<!-- page_175 -->

![](../../assets/pcap_exam/image_rsrcFJ8.jpg)

s is a local variable inside of the method Test.print()

What you want here is self.s

</details>

## Question 39

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcFJ9.jpg)

<div class="pcap-options" data-answer="A">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1 | 4</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1 | e</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1 | 2</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1 | ;</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A.**

Explanation

![](../../assets/pcap_exam/image_rsrcFJA.jpg)

Topics:

<!-- page_176 -->

![](../../assets/pcap_exam/image_rsrcFJB.jpg)

The split() method will return a list like: ['John', 'Doe', '42'] and the join() method will turn it to a string again but without the commas.

The second last element will be 4

</details>

## Question 40

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcFJC.jpg)

<div class="pcap-options" data-answer="D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1 | 2</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1 | 0</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1 | 4</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">The code is erroneous and cannot be run.</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: D.**

Explanation

![](../../assets/pcap_exam/image_rsrcFJD.jpg)

Topics:

<!-- page_177 -->

![](../../assets/pcap_exam/image_rsrcFJE.jpg)

plane + 2 will not work.

In Python you cannot add an integer to a string.

</details>

## Question 41

Which of the following expressions evaluates to True and raises no exception? (Select two answers.)

<div class="pcap-options" data-answer="A,D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">" " in " alphabet"</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">"xyz" not in "uvwxyz"</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">" " not in " "</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">"b" in "abc "</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A, D.**

Explanation

![](../../assets/pcap_exam/image_rsrcFJF.jpg)

Topics:

<!-- page_178 -->

![](../../assets/pcap_exam/image_rsrcFJG.jpg)

</details>

## Question 42

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcFJH.jpg)

<div class="pcap-options" data-answer="B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1 | 3</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1 | -3</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1 | -2</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1 | 2</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B.**

Explanation

![](../../assets/pcap_exam/image_rsrcFJJ.jpg)

Topics:

<!-- page_179 -->

![](../../assets/pcap_exam/image_rsrcFJK.jpg)

The math.floor() method rounds a number DOWN to the nearest integer.

https://www.w3schools.com/python/ref_math_floor.asp

The math.ceil() method rounds a number UP to the nearest integer

https://www.w3schools.com/python/ref_math_ceil.asp

The abs() function returns the absolute value of a given number.

https://www.w3schools.com/python/ref_func_abs.asp

</details>

## Question 43

What is the expected output of the following code?

<!-- page_180 -->

![](../../assets/pcap_exam/image_rsrcFJM.jpg)

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">2</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">The code is erroneous.</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">3</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcFJN.jpg)

Topics:

<!-- page_181 -->

![](../../assets/pcap_exam/image_rsrcFJP.jpg)

Peter is a different index than peter because P is a different character than p and therefore the dictionary will have three entries.

</details>

## Question 44

Which of the following is an example of a Python built-in concrete exception?

<div class="pcap-options" data-answer="B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">ArithmeticError</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">IndexError</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">ImportError</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">BaseException</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B.**

Explanation

![](../../assets/pcap_exam/image_rsrcFJR.jpg)

Topics:

<!-- page_182 -->

![](../../assets/pcap_exam/image_rsrcFJS.jpg)

IndexError is the only built-in concrete exception here. In the meaning that you can get an error message saying: IndexError ...

Since Python 3.6 the ImportError has the subclass ModuleNotFoundError and ImportError is not a Python built-in concrete exception anymore.

ArithmeticError is also not a built-in concrete exception. For example, you would get a ZeroDivisionError

BaseException is the base class for all built-in exceptions, which makes it the opposite of a built-in concrete exception.

https://docs.python.org/3/library/exceptions.html#exception-hierarchy

</details>

## Question 45

What can you do to indicate that a module entity should be treated as private? Choose two.

<!-- page_183 -->

<div class="pcap-options" data-answer="A,B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">You can mark the entity with the _ (single underscore) prefix.</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">You can mark the entity with the __ (double underscore) prefix.</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">You can mark the entity with the # (hashtag) prefix.</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">Nothing - all module entities are private by default.</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A, B.**

Explanation

![](../../assets/pcap_exam/image_rsrcFJT.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFJU.jpg)

<!-- page_184 -->

![](../../assets/pcap_exam/image_rsrcFJV.jpg)

If you use a private entity you need a getter and setter to deal with the entity. Using a single underscore you can still access the entity from outside the class, but a good IDE like PyCharm would already complain about it:

"Access to protected member _a of a class"

Using a double underscore you can not just access the entity from outside the class.

</details>

## Question 46

How many stars will the following snippet print to the monitor?

![](../../assets/pcap_exam/image_rsrcFJW.jpg)

<!-- page_185 -->

<div class="pcap-options" data-answer="B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">zero</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">one</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">two</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">three</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B.**

Explanation

![](../../assets/pcap_exam/image_rsrcFJX.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFJY.jpg)

i % 2 == 0 is known as test for even numbers.

In the first iteration i is an odd 1 and therefore the break does not get triggered and a star gets printed. In the second iteration i is an even 2 the break gets triggered and there is no more stars.

</details>

## Question 47

What is the expected output of the following code?

<!-- page_186 -->

![](../../assets/pcap_exam/image_rsrcFJZ.jpg)

<div class="pcap-options" data-answer="B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">['.', 'large', 'medium', 'small']</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">['large', 'medium', 'small']</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">['.', '..', 'large', 'small']</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">[]</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B.**

Explanation

![](../../assets/pcap_exam/image_rsrcFK0.jpg)

Topics:

<!-- page_187 -->

![](../../assets/pcap_exam/image_rsrcFK1.jpg)

This is pretty straight forward. You make the directory thumbnails you change into it, you make the three directories small medium large and then you list them.

But you need the knowledge, that listdir() never includes the special entries . and ..

https://www.tutorialspoint.com/python/os_listdir.htm

</details>

## Question 48

Complete the sentence. UTF‑8 is ...

<div class="pcap-options" data-answer="D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">a Python version name.</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">a synonym for "byte"</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">the 9th version of the UTF Standard.</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">an encoding form of the Unicode Standard.</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: D.**

Explanation

![](../../assets/pcap_exam/image_rsrcFK2.jpg)

<!-- page_188 -->

Topic:

UTF-8 is one of three encoding forms of the Unicode Standard. The others are UTF-16 and UTF-32. UTF-8 is the most popular one, because it is the most flexible. UTF-8 requires 8, 16, 24 or 32 bits (one to four bytes) to encode a Unicode character, UTF-16 requires either 16 or 32 bits to encode a character, and UTF-32 always requires 32 bits to encode a character.

</details>

## Question 49

Select the true statements about the filter() function. Choose two.

<div class="pcap-options" data-answer="A,B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">The filter function returns an iterator.</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">The filter() function has the following syntax: filter(function, iterable)</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">The filter() function does not return an iterator.</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">The filter() function has the following syntax: filter(iterable, function)</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A, B.**

Explanation

![](../../assets/pcap_exam/image_rsrcFK3.jpg)

Topic:

<!-- page_189 -->

![](../../assets/pcap_exam/image_rsrcFK4.jpg)

The filter() function returns a filter object, which is an iterator. The for loop can iterate through it, it has the attribute __iter__ and is an instance of collections.abc.Iterable

That is more than enough proof. And the order of the arguments has to be: first the function and second an iterable.

https://www.programiz.com/python-programming/methods/built-in/filter

</details>

## Question 50

Which of the following statements is false?

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">Multiplication precedes addition.</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">The ** operator has right-to-left associativity.</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">The result of the / operator is always an integer value.</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">The right argument of the % operator can not be zero.</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

<!-- page_190 -->

Explanation

![](../../assets/pcap_exam/image_rsrcFK5.jpg)

Topic:

![](../../assets/pcap_exam/image_rsrcFK6.jpg)

As written above, the result of the division operator is always a float value. Even if it operates with two integer values.

</details>

## Question 51

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcFK7.jpg)

<div class="pcap-options" data-answer="A">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">2</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">4</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">3</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">5</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A.**

Explanation

![](../../assets/pcap_exam/image_rsrcFK8.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFK9.jpg)

Remember to bring your best reading glasses to the exam. The second parameter will determine where the count() method will start its counting.

The first parameter (in this case ab) is what count() will look for.

count() will start at index 1 and therefore it will not find the ab right at the beginning of the string. That leaves two more ab to find.

</details>

## Question 52

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcFKA.jpg)

<div class="pcap-options" data-answer="D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">The code is erroneous.</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">4</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">2</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: D.**

Explanation

![](../../assets/pcap_exam/image_rsrcFKB.jpg)

Topics:

<!-- page_192 -->

![](../../assets/pcap_exam/image_rsrcFKC.jpg)

The backslash is the character to escape another character. If you write '\' the backslash escapes the ending single quote to a normal character.

It takes its syntactical meaning and the single quote becomes a normal character and it looses its ability to end the string. And therefore we get the syntax error.

If you write '\\' the one backslash escapes the other and you end up with a string with one normal backslash. If you write '\\\\' it is kind of the same and you end up with a string with two normal backslashes.

</details>

## Question 53

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcFKD.jpg)

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1 | False</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1 | None</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1 | True</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1 | 0</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

<!-- page_193 -->

![](../../assets/pcap_exam/image_rsrcFKE.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFKF.jpg)

The lambda function will return the Boolean conjunction of its argument and True

The f() function will invoke it and pass its second parameter as an argument. 1 > 0 is True will be the argument which is passed to the lambda function.

True and True is True and therefore True is returned by the lambda function and then by the f() function and finally printed.

</details>

## Question 54

Which of the following statements is false?

<div class="pcap-options" data-answer="A">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">The None value may not be used outside functions.</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">The None value can not be used as an argument of arithmetic operators.</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">The None value can be compared with variables.</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">The None value can be assigned to variables.</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A.**

Explanation

![](../../assets/pcap_exam/image_rsrcFKG.jpg)

Topic:

<!-- page_194 -->

![](../../assets/pcap_exam/image_rsrcFKH.jpg)

It is true that the None value can not be used as an argument of arithmetic operators.

But the None value can be assigned and compared to variables. And that can absolutely happen outside of a function.

</details>

## Question 55

Which of the following function headers is correct?

<div class="pcap-options" data-answer="D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">def func(a=1, b, c=2):</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">def func(a =1, b=1, c=2, d):</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">def func(a=1, b):</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">def func(a=1, b=1, c=2):</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: D.**

Explanation

![](../../assets/pcap_exam/image_rsrcFKJ.jpg)

Topics:

<!-- page_195 -->

![](../../assets/pcap_exam/image_rsrcFKK.jpg)

The default argument(s) have to be at the end.

</details>

## Question 56

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcFKM.jpg)

<div class="pcap-options" data-answer="A">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1 | Hello<br>2 | WelcomeWelcomeWelcome</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1 | Hello<br>2 | Welcome Welcome Welcome</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1 | Hello<br>2 | Viewers</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1 | Hello<br>2 | Welcome, Welcome, Welcome</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A.**

Explanation

![](../../assets/pcap_exam/image_rsrcFKN.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFKP.jpg)

In the function a string concatenation by multiplication takes place.

Once with the default value of num (1) and once with the one passed by argument (3)

</details>

## Question 57

What is the expected output of the following code?

<!-- page_197 -->

![](../../assets/pcap_exam/image_rsrcFKR.jpg)

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">counter is 101, number of times is 101</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">counter is 100, number of times is 100</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">counter is 100, number of times is 0</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">counter is 101, number of times is 0</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcFKS.jpg)

Topics:

<!-- page_198 -->

![](../../assets/pcap_exam/image_rsrcFKT.jpg)

This question is about argument passing. It is a big difference, whether you pass a mutable or an immutable data type. When you pass the immutable integer, it gets copied to the parameter num

The changes of num do not influence the variable number

On the other hand when you pass the mutable object, it gets referenced to to parameter c

c and counter point to the same object. You change one and the other is changed, too.

</details>

## Question 58

Which of the following sentences correctly describes the output of the below Python code?

<!-- page_199 -->

![](../../assets/pcap_exam/image_rsrcFKU.jpg)

<div class="pcap-options" data-answer="B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">res is the average of all the numbers in the list</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">res is the smallest number in the list.</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">res is the largest number in the list.</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">res is the sum of all the numbers in the list</span></label>
<label class="pcap-option"><input type="checkbox" value="E"> <span class="pcap-option-letter">E.</span> <span class="pcap-option-text">None of the above.</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B.**

Explanation

![](../../assets/pcap_exam/image_rsrcFKV.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFKW.jpg)

Classic way to find the smallest number. Take the first element as a possible result. Compare the next number with the possible result.

<!-- page_200 -->

If the next number is smaller, it becomes the new possible result and so forth. In the end the result is the smallest number.

</details>

## Question 59

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcFKX.jpg)

<div class="pcap-options" data-answer="A">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">4</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">0</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">10</span></label>
<label class="pcap-option"><input type="checkbox" value="E"> <span class="pcap-option-letter">E.</span> <span class="pcap-option-text">3</span></label>
<label class="pcap-option"><input type="checkbox" value="F"> <span class="pcap-option-letter">F.</span> <span class="pcap-option-text">2</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A.**

Explanation

![](../../assets/pcap_exam/image_rsrcFKY.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFKZ.jpg)

A set can not have duplicates.

</details>

## Question 60

If you want to import pi from math, which line will you use?

<!-- page_201 -->

<div class="pcap-options" data-answer="B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">from pi import math</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">from math import pi</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">import pi from math</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">import pi</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B.**

Explanation

![](../../assets/pcap_exam/image_rsrcFM0.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFM1.jpg)

The order is from big to small.

First the module than the variable: From the math module import the variable pi.

</details>

## Question 61

Consider the following code.

![](../../assets/pcap_exam/image_rsrcFM2.jpg)

Which of the assignments below is invalid?

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">obj = Test(1)</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">obj = Test("1")</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">obj = Test(1,2)</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">obj = Test()</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcFM3.jpg)

Topics:

<!-- page_202 -->

![](../../assets/pcap_exam/image_rsrcFM4.jpg)

In Python the first parameter of a method is the object reference. Technically it could have any name, but you should always call it self

That only leaves the parameter x to receive an argument.

x has a default value. Therefore you can pass one argument or none at all.

</details>

## Question 62

Given the code below, which of the expressions will evaluate to True?

<!-- page_203 -->

![](../../assets/pcap_exam/image_rsrcFM5.jpg)

(Select two answers.)

<div class="pcap-options" data-answer="B,D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1 | selection is element</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1 | selection.my_ID == 2</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1 | start.myID == -2</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1 | isinstance(start, Button)</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B, D.**

Explanation

![](../../assets/pcap_exam/image_rsrcFM6.jpg)

Topics:

<!-- page_204 -->

![](../../assets/pcap_exam/image_rsrcFM7.jpg)

![](../../assets/pcap_exam/image_rsrcFM8.jpg)

</details>

## Question 63

What is the expected output of the following code?

<!-- page_205 -->

![](../../assets/pcap_exam/image_rsrcFM9.jpg)

<div class="pcap-options" data-answer="D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">False True</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">True True</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">False False</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">True False</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: D.**

Explanation

![](../../assets/pcap_exam/image_rsrcFMA.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFMB.jpg)

Nothing changes here. The variables always get assigned the value they had before.

</details>

## Question 64

What is the expected output of the following code?

<!-- page_206 -->

![](../../assets/pcap_exam/image_rsrcFMC.jpg)

<div class="pcap-options" data-answer="B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1 5 9 13</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">4 8 12 16</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">13 14 15 16</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1 2 3 4</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B.**

Explanation

![](../../assets/pcap_exam/image_rsrcFMD.jpg)

Topics:

<!-- page_207 -->

![](../../assets/pcap_exam/image_rsrcFME.jpg)

data is a two dimensional list. In every iteration of the for loop,

pop() removes the last element of the corresponding inner list. That last element gets printed. The default value of the print() functions end parameter is the line feed. That gets overwritten here by a single space character.

</details>

## Question 65

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcFMF.jpg)

<!-- page_208 -->

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">False</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">0</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">True</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">The code is erroneous.</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcFMG.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFMH.jpg)

The function hasattr() checks whether an object has the given object variable. It also works with a class and a class variable

</details>

## Question 66

What is the expected output of the following code?

<!-- page_209 -->

![](../../assets/pcap_exam/image_rsrcFMJ.jpg)

<div class="pcap-options" data-answer="B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">2</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">True</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">False</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B.**

Explanation

![](../../assets/pcap_exam/image_rsrcFMK.jpg)

Topics:

<!-- page_210 -->

![](../../assets/pcap_exam/image_rsrcFMM.jpg)

This question is about operator overloading.

__eq__() overloads the equal to operator if used with objects of the class A

If you use the equal to operator with two object of the class A

the __eq__() method is called and the two objects are passed to it. The return value is going to be the result of the comparison. And because 1 * 2 == 2 * 1 the result is True

</details>

## Question 67

What is the expected result of the following code?

<!-- page_211 -->

![](../../assets/pcap_exam/image_rsrcFMN.jpg)

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">b</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">a</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">The code will cause a syntax error.</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcFMP.jpg)

Topics:

<!-- page_212 -->

![](../../assets/pcap_exam/image_rsrcFMR.jpg)

As the error message claims: default 'except:' must be last

</details>

## Question 68

What is the expected behavior of the following program?

![](../../assets/pcap_exam/image_rsrcFMS.jpg)

<!-- page_213 -->

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">The program will output 1 to the screen.</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">The program will cause a AttributeEror exception.</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">The program will cause a ValueError exception.</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">The program will cause a SyntaxError exception.</span></label>
<label class="pcap-option"><input type="checkbox" value="E"> <span class="pcap-option-letter">E.</span> <span class="pcap-option-text">The program will cause a TypeError exception.</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcFMT.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFMU.jpg)

The tuple.index() method expects a value and looks for that value in the tuple. It will return the index of the first value it finds. If it does not find the value, it raises a ValueError

https://www.w3schools.com/python/ref_tuple_index.asp

</details>

## Question 69

A list of package's dependencies can be obtained from pip using its command named:

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">list</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">dir</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">show</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">deps</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcFMV.jpg)

Topic:

With pip list you get a list with all your installed packages. Choose one of your packages and enter pip show package-name

Under Requires: you find a list of the package's dependencies.

<!-- page_214 -->

</details>

## Question 70

A programmer needs to use the following functions:

![](../../assets/pcap_exam/image_rsrcFMW.jpg)

Which modules have to be imported to make this possible? (Select two answers.)

<div class="pcap-options" data-answer="B,D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1 | math</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1 | random</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1 | tkinter</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1 | platform</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B, D.**

Explanation

![](../../assets/pcap_exam/image_rsrcFMX.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFMY.jpg)

Explanation:

https://www.w3schools.com/python/ref_random_choice.asp

https://docs.python.org/3/library/platform.html#platform.machine

https://docs.python.org/3/library/platform.html#platform.system

</details>

## Question 71

PyPI is often referred to as:

<!-- page_215 -->

<div class="pcap-options" data-answer="D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">Python Play</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">Py Software Store</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">pyTT</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">Cheese Shop</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: D.**

Explanation

![](../../assets/pcap_exam/image_rsrcFMZ.jpg)

Topic:

https://en.wikipedia.org/wiki/Python_Package_Index

</details>

## Question 72

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcFN0.jpg)

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">z</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">a</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">x</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">y</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcFN1.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFN2.jpg)

ord() returns an integer representing the Unicode character.

chr() turns that integer back to the Unicode character. You don't need to remember the number of every character, but like in the alphabet x is two before z

</details>

## Question 73

What is the expected output of the following code?

<!-- page_216 -->

![](../../assets/pcap_exam/image_rsrcFN3.jpg)

<div class="pcap-options" data-answer="D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1 | finally<br>2 | except</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1 | finally<br>2 | try</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1 | except<br>2 | finally</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1 | try<br>2 | finally</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: D.**

Explanation

![](../../assets/pcap_exam/image_rsrcFN4.jpg)

Topic:

![](../../assets/pcap_exam/image_rsrcFN5.jpg)

The snippet will try to execute print('try') and succeed. The finally block always gets executed.

<!-- page_217 -->

</details>

## Question 74

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcFN6.jpg)

<div class="pcap-options" data-answer="D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">0 0</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">0 1</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1 0</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">The code is erroneous.</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: D.**

Explanation

![](../../assets/pcap_exam/image_rsrcFN7.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFN8.jpg)

This question is a little tricky. Everything seems to be fine, BUT the right name of the dictionary method is values()

</details>

## Question 75

What is the expected output of the following code?

<!-- page_218 -->

![](../../assets/pcap_exam/image_rsrcFN9.jpg)

<div class="pcap-options" data-answer="A">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">None</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">The code is erroneous.</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">Value</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1</span></label>
<label class="pcap-option"><input type="checkbox" value="E"> <span class="pcap-option-letter">E.</span> <span class="pcap-option-text">Peter</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A.**

Explanation

![](../../assets/pcap_exam/image_rsrcFNA.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFNB.jpg)

func() has no return statement. Therefore None gets returned.

</details>

## Question 76

What is the expected output of the following code?

<!-- page_219 -->

![](../../assets/pcap_exam/image_rsrcFNC.jpg)

<div class="pcap-options" data-answer="A">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">2 3 4 5 6 6</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">2 3 4 5 6 1</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1 2 3 4 5 6</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1 1 2 3 4 5</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A.**

Explanation

![](../../assets/pcap_exam/image_rsrcFND.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFNE.jpg)

In the first for loop, the five last values of data get written to the first five indexes of data

The value of the last index stays the same.

range(1, 6) will produce the numbers 1, 2, 3, 4, 5

<!-- page_220 -->

And because the first of these number is 1 we need the data[i -1] to start at index 0

The old value at index 1 is 2. That gets written at index 0 and so forth ...

</details>

## Question 77

Given the code below, complete the print() method body in a way that will ensure that the get() method is properly invoked.

![](../../assets/pcap_exam/image_rsrcFNF.jpg)

(Select two answers.)

<div class="pcap-options" data-answer="C,D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1 | print(get())</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1 | print(Storage.get())</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1 | print(self.get())</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1 | print(Storage.get(self))</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C, D.**

Explanation

![](../../assets/pcap_exam/image_rsrcFNG.jpg)

Topics:

<!-- page_221 -->

![](../../assets/pcap_exam/image_rsrcFNH.jpg)

You can always invoke the method with the object reference self in front. If you invoke the same method at class level you have to pass the object reference self as an argument.

</details>

## Question 78

What is the expected output of the following code if the user enters 11 and 4 ?

![](../../assets/pcap_exam/image_rsrcFNJ.jpg)

<div class="pcap-options" data-answer="B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">3</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">2</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">4</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B.**

Explanation

![](../../assets/pcap_exam/image_rsrcFNK.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFNM.jpg)

input() returns strings, but the int() function casts them to integers. Then you have to concentrate with all the modulus operators.

</details>

## Question 79

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcFNN.jpg)

<div class="pcap-options" data-answer="B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">2</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">3</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">The code is erroneous.</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B.**

<!-- page_223 -->

Explanation

![](../../assets/pcap_exam/image_rsrcFNP.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFNR.jpg)

If you raise an Exception you can pass a list of arguments. They will be assigned as a tuple to the args attribute of the Exception object.

</details>

## Question 80

How many elements does the my_list list contain?

![](../../assets/pcap_exam/image_rsrcFNS.jpg)

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">three</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">one</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">two</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">None of the above.</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcFNT.jpg)

Topic:

<!-- page_224 -->

![](../../assets/pcap_exam/image_rsrcFNU.jpg)

range(1, 3) will be 1 & 2 and therefore the for loop will iterate twice. Both times 0 will be appended to the list.

</details>

## Question 81

You develop a Python application for your company. A list named employees contains 200 employee names, the last five being company management. You need to slice the list to display all employees excluding management. Which code segments can you use? Choose two.

<div class="pcap-options" data-answer="B,C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">Employees[ 1:-5 ]</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">Employees[ : -5 ]</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">Employees[0:-5]</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">Employees[0:-4 ]</span></label>
<label class="pcap-option"><input type="checkbox" value="E"> <span class="pcap-option-letter">E.</span> <span class="pcap-option-text">Employees[1:-4 ]</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B, C.**

Explanation

![](../../assets/pcap_exam/image_rsrcFNV.jpg)

Topic:

<!-- page_225 -->

![](../../assets/pcap_exam/image_rsrcFNW.jpg)

List slicing: [start(inclusive):end(exclusive)]

The default value for the start is 0. Meaning you can write it or leave it out. The negative index counts from the end. The end is exclusive.

-1 cuts out one element.

-5 cuts out five elements.

And that is what you need here for the five managers.

</details>

## Question 82

Which of the following statements are true? (Select two answers.)

<!-- page_226 -->

<div class="pcap-options" data-answer="A,D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">The open() function raises an exception when its operation fails.</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">Trying to write a file opened in read-only mode removes its contents.</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">Read, write, and delete are the names of file open modes.</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">The second argument of the open() function is a string.</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A, D.**

Explanation

![](../../assets/pcap_exam/image_rsrcFNX.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFNY.jpg)

Yes, the second argument of the open() function is a string, the open mode.

● Yes, the open() function raises a FileNotFoundError when its operation fails.

![](../../assets/pcap_exam/image_rsrcFNZ.jpg)

● No, trying to write a file opened in read-only mode will not remove its contents. It will produced an error:

<!-- page_227 -->

● No, read, write, and delete are not the names of file open modes. delete is not. read, write, append and create are open modes.

https://www.programiz.com/python-programming/methods/built-in/open

</details>

## Question 83

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcFP0.jpg)

<div class="pcap-options" data-answer="D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">0.0</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">0.16666666666666666</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">4.5</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">0</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: D.**

Explanation

![](../../assets/pcap_exam/image_rsrcFP1.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFP2.jpg)

There are only operators from the group "Multiplication, Division, Floor division, Modulus".

The group has a left-to-right associativity, meaning the left one gets evaluated first.

Therefore the order of operations here is: // -> *

</details>

## Question 84

<!-- page_228 -->

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcFP3.jpg)

<div class="pcap-options" data-answer="A">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1 | -1</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">An error message appears on the screen.</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1 | -2</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1 | -INF</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A.**

Explanation

![](../../assets/pcap_exam/image_rsrcFP4.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFP5.jpg)

Dividing by 0.0 raises the ZeroDivisionError which is a subclass of ArithmeticError

Therefore the except branch is executed.

</details>

## Question 85

<!-- page_229 -->

Which of the following are not valid Python string literals? (Select two answers.)

<div class="pcap-options" data-answer="C,D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1 | "this is a quote: \""</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1 | "\\"</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1 | 'whether 'tis nobler in the mind to suffer'</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1 | ''' To be, or not to be,<br>2 | that is the question"""</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C, D.**

Explanation

![](../../assets/pcap_exam/image_rsrcFP6.jpg)

Topics:

<!-- page_230 -->

![](../../assets/pcap_exam/image_rsrcFP7.jpg)

</details>

## Question 86

Consider the following code.

![](../../assets/pcap_exam/image_rsrcFP8.jpg)

The code causes the import of …

<div class="pcap-options" data-answer="B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">entity y from module x from package z</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">entity z from module y from package x</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">entity x from module y from package z</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">entity z from module x from package y</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B.**

Explanation

![](../../assets/pcap_exam/image_rsrcFP9.jpg)

<!-- page_231 -->

Topics:

![](../../assets/pcap_exam/image_rsrcFPA.jpg)

The order is from big to small:

from package.module import entity

</details>

## Question 87

How many stars will the following code send to the monitor?

![](../../assets/pcap_exam/image_rsrcFPB.jpg)

<!-- page_232 -->

<div class="pcap-options" data-answer="D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">zero</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">two</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">one</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">three</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: D.**

Explanation

![](../../assets/pcap_exam/image_rsrcFPC.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFPD.jpg)

When x is 2, 4 and 6 the if condition is True and the continue gets triggered. The iteration ends directly and the print() function doesn't get executed.

When x is 1, 3 and 5 the if condition is False, the continue does not get triggered and those three times the print() function gets executed. Therefore there will be three stars printed.

</details>

## Question 88

What is the expected result of the following code?

![](../../assets/pcap_exam/image_rsrcFPE.jpg)

<!-- page_233 -->

<div class="pcap-options" data-answer="C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">3</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">bytearray(0, 0, 0)</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">bytearray(b"\x00\x00\x00")</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">bytearray(b"3")</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: C.**

Explanation

![](../../assets/pcap_exam/image_rsrcFPF.jpg)

Topic:

![](../../assets/pcap_exam/image_rsrcFPG.jpg)

https://www.programiz.com/python-programming/methods/built-in/bytearray

</details>

## Question 89

Which of the following items are present in the function header?

<div class="pcap-options" data-answer="B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">return value</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">function name and parameter list</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">function name</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">parameter list</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B.**

Explanation

![](../../assets/pcap_exam/image_rsrcFPH.jpg)

Topics:

<!-- page_234 -->

![](../../assets/pcap_exam/image_rsrcFPJ.jpg)

In the function header is the keyword def the function name and the parameter list.

</details>

## Question 90

The errno.ENOENT symbol refers to an error described as:

<div class="pcap-options" data-answer="A">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">No such file or directory</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">Operation not permitted</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">Permission denied</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">No child processes</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A.**

Explanation

![](../../assets/pcap_exam/image_rsrcFPK.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFPM.jpg)

https://docs.python.org/3/library/errno.html#errno.ENOENT

</details>

## Question 91

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcFPN.jpg)

<!-- page_235 -->

<div class="pcap-options" data-answer="D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">This can not be evaluated.</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">This can not be predicted.</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1.0</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: D.**

Explanation

![](../../assets/pcap_exam/image_rsrcFPP.jpg)

Topic:

![](../../assets/pcap_exam/image_rsrcFPR.jpg)

All you have to know here is, that the division operator always returns a float.

Even if it is operating with two integers.

</details>

## Question 92

Which of the following statements are true? (Select two answers.)

<div class="pcap-options" data-answer="A,C">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">A source file named __init__.py is used to mark a directory/folder as containing a Python package, and to initiate the package.</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">A programmer is obliged to manually create a directory/folder named __pycache__ inside every package.</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">The variable named __name__ is a string containing the module name.</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">The .phy extension marks files that contain Python semi-compiled byte-code.</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A, C.**

Explanation

![](../../assets/pcap_exam/image_rsrcFPS.jpg)

Topics:

<!-- page_236 -->

![](../../assets/pcap_exam/image_rsrcFPT.jpg)

The __name__ variable can be used to determine whether the code has been run standalone (when the variable contains "__main__") or whether it has been imported as a module (when it contains the module name).

https://www.geeksforgeeks.org/__name__-special-variable-python/ https://docs.python.org/3/library/__main__.html

A source file named __init__.py is used to mark a directory/folder as containing a Python package, and to initialize the package.

https://docs.python.org/3/tutorial/modules.html#packages

</details>

## Question 93

<!-- page_237 -->

The ABC Video company needs a way to determine the cost that a customer will pay for renting a DVD. The cost is dependent on the time of day the DVD is returned. However, there are also special rates on Thursdays and Sundays. The fee structure is shown in the following list:

The cost is $1.59 per night. If the DVD is returned after 8 PM, the customer will be charged an extra day. If the video is rented on a Sunday, the customer gets 30% off for as long as they keep the video. If the video is rented on a Thursday, the customer gets 50% off for as long as they keep the video.

You need to write code to meet the requirements.

![](../../assets/pcap_exam/image_rsrcFPU.jpg)

What should you insert instead of XXX, YYY and ZZZ?

<div class="pcap-options" data-answer="A">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">1 | XXX -> == "n":<br>2 | YYY -> == "Sunday":<br>3 | ZZZ -> == "Thursday":</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">1 | XXX -> != "n":<br>2 | YYY -> is "Sunday":<br>3 | ZZZ -> is "Thursday":</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1 | XXX -> == "y":<br>2 | YYY -> &gt;= "Sunday":<br>3 | ZZZ -> &gt;= "Thursday":</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">1 | XXX -> == "y":<br>2 | YYY -> == "Sunday":<br>3 | ZZZ -> == "Thursday":</span></label>
<label class="pcap-option"><input type="checkbox" value="E"> <span class="pcap-option-letter">E.</span> <span class="pcap-option-text">1 | XXX -> == "n":<br>2 | YYY -> is "Sunday":<br>3 | ZZZ -> is "Thursday":</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A.**

Explanation

![](../../assets/pcap_exam/image_rsrcFPV.jpg)

Topics:

<!-- page_239 -->

![](../../assets/pcap_exam/image_rsrcFPW.jpg)

![](../../assets/pcap_exam/image_rsrcFPX.jpg)

<!-- page_240 -->

At this company, to return a video on time means to return it before 8 PM. Otherwise one day is added to the amount of rented days. If you return your video on a Sunday you get 30% off.

Meaning you only pay 70%. And if you return your video on a Thursday, you pay only half (50%).

</details>

## Question 94

What is the expected output of the following snippet?

![](../../assets/pcap_exam/image_rsrcFPY.jpg)

<div class="pcap-options" data-answer="A">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">python</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">P y t h o n</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">The code is erroneous.</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">P Y T H O N</span></label>
<label class="pcap-option"><input type="checkbox" value="E"> <span class="pcap-option-letter">E.</span> <span class="pcap-option-text">PYTHON</span></label>
<label class="pcap-option"><input type="checkbox" value="F"> <span class="pcap-option-letter">F.</span> <span class="pcap-option-text">Python</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: A.**

Explanation

![](../../assets/pcap_exam/image_rsrcFPZ.jpg)

Topics:

![](../../assets/pcap_exam/image_rsrcFR0.jpg)

<!-- page_241 -->

A string is immutable. You can not change it, even if you tried. Here it is not even tried otherwise the code would cause a TypeError

</details>

## Question 95

What is the expected output of the following code?

![](../../assets/pcap_exam/image_rsrcFR1.jpg)

<div class="pcap-options" data-answer="B">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">[ 4, 3, 2, 1 ]</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">[4, 3, 2 ]</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">The code is erroneous.</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">[ 4, 3 ]</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: B.**

Explanation

![](../../assets/pcap_exam/image_rsrcFR2.jpg)

Topic:

![](../../assets/pcap_exam/image_rsrcFR3.jpg)

![](../../assets/pcap_exam/image_rsrcFR4.jpg)

List slicing:

The step is negative here. That makes the slice be build from right to left (start interchanges with end). The start is the index 3 (inclusive) and the end is index 0 (exclusive).

Therefore we will get index 3 index 2 and index 1 which are the numbers 4, 3, 2

</details>

## Question 96

What is the expected output of the following code?

<!-- page_242 -->

![](../../assets/pcap_exam/image_rsrcFR5.jpg)

<div class="pcap-options" data-answer="D">
<label class="pcap-option"><input type="checkbox" value="A"> <span class="pcap-option-letter">A.</span> <span class="pcap-option-text">['red\n', 'yellow\n', 'blue\n']</span></label>
<label class="pcap-option"><input type="checkbox" value="B"> <span class="pcap-option-letter">B.</span> <span class="pcap-option-text">redyellowblue</span></label>
<label class="pcap-option"><input type="checkbox" value="C"> <span class="pcap-option-letter">C.</span> <span class="pcap-option-text">1 | red<br>2 |<br>3 | yellow<br>4 |<br>5 | blue</span></label>
<label class="pcap-option"><input type="checkbox" value="D"> <span class="pcap-option-letter">D.</span> <span class="pcap-option-text">The code is erroneous.</span></label>
<button type="button" class="pcap-check">Antwort prüfen</button>
<p class="pcap-feedback" aria-live="polite"></p>
</div>

<details class="pcap-solution" hidden markdown="1">

<summary>Lösung und Erklärung</summary>

**Answer: D.**

Explanation

![](../../assets/pcap_exam/image_rsrcFR6.jpg)

Topics:

<!-- page_243 -->

![](../../assets/pcap_exam/image_rsrcFR7.jpg)

The file gets closed too early. All operations on the file need the be finished before you can close it.

</details>
