### Aufgabe: Zufälle gibts...

```python
from random import randint


def random_squares(n):
    return randint(1, n) ** 2
```

```python
from my_random import random_squares

print(random_squares(5))
```

### Aufgabe: Abzocke ausdenken

```python
def bet_under_squares(my_bet, faktor):
    random_square = random_squares(faktor)
    print(f"Randomly roled:{random_square}")
    return 0 if my_bet < random_square else faktor * my_bet
```

### Aufgabe: Sicherheit muss sein

```python
def input_int_in_between(prompt, minimum, maximum):
    user_input = 0
    while True:
        try:
            user_input = int(input(prompt))
        except ValueError:
            print(f"Eingabe ist nicht vom Typ int")

        if minimum <= user_input <= maximum:
            return user_input
        else:
            print(f"Eingabe ist nicht gültig.")
```

### Aufgabe: Tische bereit machen

```python
from secure_input import input_int_in_between
from my_random import random_squares

def play_game(rounds=5, money=10):
    for i in range(rounds):
        print(f"Round {i}. Money={money}")
        bet = input_int_in_between("Wie viel Geld willst du setzen?", 0, money)
        money -= bet
        faktor = input_int_in_between("Welchen Faktor willst du?", 1, 10 ** 100)
        money += bet_under_squares(bet, faktor)
        if not money:
            break
    else:
        print(f"Du hast {money} gewonnen")
        return

    print("Leider alles verzockt")
```