# Python PCAP Quiz -- 20 Questions

---

### Q1 (Single Choice) -- Division

**What is the output of `print(10 / 2)`?**

- A) `5`
- B) `5.0`
- C) `5.00`
- D) `TypeError`

**Correct: B** -- Division `/` always returns a float in Python 3.

---

### Q2 (Single Choice) -- Floor Division with Negatives

**What is the output of `print(-17 // 2)`?**

- A) `-8`
- B) `-9`
- C) `-8.5`
- D) `8`

**Correct: B** -- Floor division rounds toward negative infinity.

---

### Q3 (Single Choice) -- String Immutability

**What happens when you run the following code?**

```python
s = "Hello"
s[0] = "h"
```

- A) `s` becomes `"hello"`
- B) `TypeError`
- C) `IndexError`
- D) `s` stays `"Hello"`

**Correct: B** -- Strings are immutable; item assignment raises `TypeError`.

---

### Q4 (Multiple Choice) -- Falsy Values

**Which of the following evaluate to `False` in a boolean context? (Select all that apply)**

- A) `[]`
- B) `"0"`
- C) `0`
- D) `None`

**Correct: A, C, D** -- `"0"` is a non-empty string and therefore truthy.

---

### Q5 (Single Choice) -- Range

**What does `list(range(2, 10, 3))` return?**

- A) `[2, 5, 8]`
- B) `[2, 5, 8, 11]`
- C) `[3, 6, 9]`
- D) `[2, 4, 6, 8]`

**Correct: A** -- Starts at 2, steps by 3, stops before 10.

---

### Q6 (Single Choice) -- Loop else

**What is the output?**

```python
for i in range(3):
    if i == 5:
        break
else:
    print("done")
```

- A) Nothing is printed
- B) `done`
- C) `SyntaxError`
- D) `0 1 2 done`

**Correct: B** -- The `else` block runs when the loop completes without `break`.

---

### Q7 (Single Choice) -- Mutable Arguments

**What is the output?**

```python
def change(lst):
    lst.append(4)

my_list = [1, 2, 3]
change(my_list)
print(my_list)
```

- A) `[1, 2, 3]`
- B) `[1, 2, 3, 4]`
- C) `[4]`
- D) `None`

**Correct: B** -- Lists are passed by reference; `append` modifies the original.

---

### Q8 (Single Choice) -- Default Parameter Order

**Which function definition is valid?**

- A) `def f(a=1, b): pass`
- B) `def f(a, b=1): pass`
- C) `def f(a=1, b=2, c): pass`
- D) `def f(=1, b): pass`

**Correct: B** -- Parameters with defaults must come after those without.

---

### Q9 (Single Choice) -- Tuple Single Element

**What is `type((42))`?**

- A) `<class 'tuple'>`
- B) `<class 'int'>`
- C) `<class 'list'>`
- D) `SyntaxError`

**Correct: B** -- A single-element tuple requires a trailing comma: `(42,)`.

---

### Q10 (Multiple Choice) -- Set Properties

**Which statements about Python sets are true? (Select all that apply)**

- A) Sets are ordered
- B) Sets contain only unique elements
- C) Sets support indexing with `[]`
- D) Sets can contain only immutable types

**Correct: B, D** -- Sets are unordered, unique, and elements must be hashable (immutable).

---

### Q11 (Single Choice) -- Dictionary Access

**What is the output?**

```python
d = {"a": 1, "b": 2}
print(d.get("c", 0))
```

- A) `KeyError`
- B) `None`
- C) `0`
- D) `"c"`

**Correct: C** -- `.get()` returns the default value `0` when the key is missing.

---

### Q12 (Single Choice) -- List Comprehension

**What does `[x**2 for x in range(5) if x % 2 != 0]` return?**

- A) `[0, 1, 4, 9, 16]`
- B) `[1, 9]`
- C) `[1, 9, 25]`
- D) `[0, 4, 16]`

**Correct: B** -- Only odd numbers (1, 3) are squared: 1, 9.

---

### Q13 (Multiple Choice) -- Comprehension Syntax

**Which of the following Python collection types support comprehension syntax? (Select all that apply)**

- A) `list`
- B) `tuple`
- C) `dict`
- D) `set`

**Correct: A, C, D** -- Lists (`[x for x in ...]`), dicts (`{k: v for k, v in ...}`), and sets (`{x for x in ...}`) support comprehensions. Tuples do not -- parentheses with a comprehension expression create a generator, not a tuple.

---

### Q14 (Single Choice) -- Scope

**What is the output?**

```python
x = 10

def foo():
    x = 20
    print(x)

foo()
print(x)
```

- A) `20` then `20`
- B) `20` then `10`
- C) `10` then `10`
- D) `NameError`

**Correct: B** -- The local `x = 20` shadows the global; the global remains `10`.

---

### Q15 (Single Choice) -- *args Type

**Inside a function `def f(*args)`, what type is `args`?**

- A) `list`
- B) `tuple`
- C) `dict`
- D) `set`

**Correct: B** -- `*args` is always a tuple.

---

### Q16 (Single Choice) -- Exception Hierarchy

**What is the output?**

```python
try:
    x = 1 / 0
except ArithmeticError:
    print("caught")
```

- A) `ZeroDivisionError` (unhandled)
- B) `caught`
- C) `ArithmeticError`
- D) Nothing is printed

**Correct: B** -- `ZeroDivisionError` is a subclass of `ArithmeticError`, so it is caught.

---

### Q17 (Single Choice) -- Class vs Instance Attributes

**What is the output?**

```python
class Dog:
    species = "Canis"

d1 = Dog()
d1.species = "Lupus"
d2 = Dog()
print(d1.species, d2.species)
```

- A) `Lupus Lupus`
- B) `Canis Canis`
- C) `Lupus Canis`
- D) `AttributeError`

**Correct: C** -- `d1.species` is an instance attribute shadowing the class attribute; `d2` still reads the class attribute.

---

### Q18 (Single Choice) -- Name Mangling (Private)

**What is the output?**

```python
class Secret:
    def __init__(self):
        self.__code = 42

s = Secret()
print(s.__code)
```

- A) `42`
- B) `AttributeError`
- C) `None`
- D) `NameError`

**Correct: B** -- `__code` is name-mangled to `_Secret__code`; direct access raises `AttributeError`.

---

### Q19 (Single Choice) -- Magic Methods

**Which magic method is called by `print(obj)` when both `__str__` and `__repr__` are defined?**

- A) `__repr__`
- B) `__str__`
- C) `__print__`
- D) `__call__`

**Correct: B** -- `print()` calls `str()` on the object, which invokes `__str__`. If `__str__` is not defined, Python falls back to `__repr__`.

---

### Q20 (Multiple Choice) -- @staticmethod vs @classmethod

**Which statements are true? (Select all that apply)**

- A) A `@staticmethod` receives `self` as its first parameter
- B) A `@classmethod` receives `cls` as its first parameter
- C) A `@staticmethod` can be called on the class without creating an instance
- D) A `@classmethod` can be used as an alternative constructor

**Correct: B, C, D** -- Static methods have no implicit first parameter (no `self`, no `cls`).

---

## Summary by Topic

| Topic | Questions |
|---|---|
| Math Operations | Q1, Q2 |
| Strings | Q3 |
| Control Flow / Loops | Q4, Q5, Q6 |
| Functions | Q7, Q8 |
| Data Structures (Tuple, Set, Dict) | Q9, Q10, Q11 |
| Comprehensions | Q12, Q13 |
| Scopes | Q14 |
| *args/**kwargs | Q15 |
| Exceptions | Q16 |
| OOP Basics (Classes, Attributes) | Q17 |
| OOP Advanced (Private, Magic, Static/Class) | Q18, Q19, Q20 |
