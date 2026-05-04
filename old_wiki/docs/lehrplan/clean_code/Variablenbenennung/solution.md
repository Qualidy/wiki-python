# Lösung Aufgabe 1
```python
articles = [3, 5, 2]  # Anzahl der Artikel
prices = [10.99, 5.99, 7.49]  # Preis pro Artikel

# Methode zum Berechnen der Summe des Warenwerts


def calculate_total(items, prices):
    total = 0
    for i in range(len(items)):
        total += items[i] * prices[i]
    return total


# Warenkorb berechnen
warenkorb_wert = calculate_total(articles, prices)

# Ausgabe des Warenwerts
print("Warenwert: $" + str(warenkorb_wert))
```


# Lösung Aufgabe 2

```python
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, marker):
    # Überprüfe Zeilen, Spalten und Diagonalen auf einen Sieg
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == marker: 
            return True
        if board[0][i] == board[1][i] == board[2][i] == marker: 
            return True
    if board[0][0] == board[1][1] == board[2][2] == marker: 
        return True
    if board[0][2] == board[1][1] == board[2][0] == marker: 
        return True
    return False

def start_game():
    game_board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(game_board)
        row, column = map(int, input(f"Player {current_player}, enter row and column (0-2): ").split())
        
        if game_board[row][column] == " ":
            game_board[row][column] = current_player
            if check_win(game_board, current_player):
                print(f"Player {current_player} wins!")
                break
            current_player = "X" if current_player == "O" else "O"
        else:
            print("Invalid move, try again.")

        print_board(game_board)

start_game()
```
* `prntBrd(b)` wurde zu `print_board(board)` umbenannt, um die Funktion des Ausdruckens des Spielbretts klarer zu machen.
* `chckWin(b, m)` wurde zu `check_win(board, marker)` umbenannt, was die Funktion des Überprüfens auf einen Gewinn besser beschreibt.
* Die Variablennamen innerhalb der Funktionen wurden verbessert:
  * `b` wurde zu `board`
  * `r` und `c` wurden zu `row` und `column`
  * `m` wurde zu `marker`
  * `brd` wurde zu `game_board`
  * `curP` wurde zu `current_player`
* Kommentare und Formatierung wurden für eine bessere Lesbarkeit hinzugefügt. Diese Änderungen machen den Code lesbarer und es ist leichter zu verstehen, was jede Variable und Funktion repräsentiert.
