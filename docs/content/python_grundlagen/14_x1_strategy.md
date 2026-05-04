# Strategy Pattern
[120min]


## Erklärung:

Das Strategy Pattern ist ein Verhaltensmuster, das es ermöglicht, eine Familie von Algorithmen zu definieren, sie zu kapseln und austauschbar zu machen. Es definiert eine Familie von Algorithmen, kapselt jeden Algorithmus und macht sie austauschbar. Das Muster ermöglicht es einem Client, den Algorithmus unabhängig von den Clients, die ihn verwenden, zu wählen und zu ändern.

Die Entscheidung welche Strategie genutzt werden soll wird dabei zur **Laufzeit** festgelegt. 

Beispiel:

```python
class PaymentStrategy:
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal")

class ShoppingCart:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def checkout(self, amount):
        self.payment_strategy.pay(amount)

# Verwendung des Strategy Patterns
cc_payment = CreditCardPayment()
paypal_payment = PayPalPayment()

cart1 = ShoppingCart(cc_payment)
cart1.checkout(100)

cart2 = ShoppingCart(paypal_payment)
cart2.checkout(150)
```

# Aufgaben:

## 1. Rabattberechnung 🌶️️🌶️️🌶️️

### Teilschritte:

a. Definiere eine Klasse `DiscountStrategy` als abstrakte Klasse mit einer Methode `calculate_discount`, die den Rabatt berechnet.

b. Implementiere konkrete Rabattstrategien, die von `DiscountStrategy` erben, z. B. `PercentageDiscount` und `FixedAmountDiscount`.

c. Erstelle eine Klasse `ShoppingCart`, die eine Instanz von `DiscountStrategy` als Attribut enthält.

d. Die Methode `apply_discount` der Klasse `ShoppingCart` sollte die Rabattberechnung unter Verwendung der übergebenen Rabattstrategie durchführen.

e. Demonstriere die Verwendung, indem du einen Einkaufswagen erstellst und verschiedene Rabattstrategien anwendest.

## 2. Benutzeranmeldungssystem 🌶️️🌶️️

### Teilschritte:

a. Erstelle eine Klasse `AuthenticationStrategy` als abstrakte Klasse mit einer Methode `authenticate`, die die Benutzeranmeldung behandelt.

b. Implementiere konkrete Authentifizierungsstrategien, die von `AuthenticationStrategy` erben, z. B. `UsernamePasswordAuthentication` und `TwoFactorAuthentication`.

c. Entwickle eine Klasse `UserAuthentication`, die eine Instanz von `AuthenticationStrategy` als Attribut enthält.

d. Die Methode `authenticate_user` der Klasse `UserAuthentication` sollte die Authentifizierung unter Verwendung der übergebenen Authentifizierungsstrategie durchführen.

e. Zeige die Anwendung, indem du einen Benutzer authentifizierst und verschiedene Authentifizierungsstrategien ausprobierst.
