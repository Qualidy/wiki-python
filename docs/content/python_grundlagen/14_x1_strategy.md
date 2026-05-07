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

{{ task(file="tasks/python_grundlagen/14_x1_strategy/01_rabattberechnung.yaml") }}
{{ task(file="tasks/python_grundlagen/14_x1_strategy/02_benutzeranmeldungssystem.yaml") }}
