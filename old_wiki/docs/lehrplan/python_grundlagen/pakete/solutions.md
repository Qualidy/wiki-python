### Aufgabe: Türen auf
Angepasstes `casino_games.py` (Nur erste 2 Zeilen sind anders):

```python
from my_casino.secure_input import input_int_in_between
from my_casino.my_random import random_squares


def bet_under_squares(my_bet, faktor):
    random_square = random_squares(faktor)
    print(f"Randomly roled:{random_square}")
    return 0 if my_bet < random_square else faktor * my_bet


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

[🔽Download Full Package](my_casino.zip)