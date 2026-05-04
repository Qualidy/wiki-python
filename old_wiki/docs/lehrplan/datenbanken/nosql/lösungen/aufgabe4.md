```python
from pymongo import MongoClient
from pprint import pprint

# Verbindung zur MongoDB herstellen
client = MongoClient('mongodb://localhost:27017/')

# Datenbank auswählen
db = client['shopDB']

# 1. Berechne den Gesamtpreis aller Bestellungen, gruppiert nach Produkt


def total_price_by_product():
    pipeline = [
        {"$unwind": "$products"},
        {"$lookup": {
            "from": "products",
            "localField": "products.productId",
            "foreignField": "_id",
            "as": "productDetails"
        }},
        {"$unwind": "$productDetails"},
        {"$group": {
            "_id": "$products.productId",
            "totalAmount": {"$sum": {"$multiply": ["$products.quantity", "$productDetails.price"]}}
        }}
    ]
    result = db.orders.aggregate(pipeline)
    pprint(list(result))

# 2. Berechne das Durchschnittsalter der Benutzer je Stadt


def average_age_by_city():
    pipeline = [
        {"$group": {
            "_id": "$city",
            "averageAge": {"$avg": "$age"}
        }}
    ]
    result = db.users.aggregate(pipeline)
    pprint(list(result))

# 3. Berechne die Anzahl der Bestellungen je Tag


def orders_count_by_day():
    pipeline = [
        {"$group": {
            "_id": "$date",
            "orderCount": {"$sum": 1}
        }}
    ]
    result = db.orders.aggregate(pipeline)
    pprint(list(result))

# 4. Berechne den Gesamtpreis der Produkte in jedem Warenkorb


def total_price_by_cart():
    pipeline = [
        {"$unwind": "$products"},
        {"$lookup": {
            "from": "products",
            "localField": "products.productId",
            "foreignField": "_id",
            "as": "productDetails"
        }},
        {"$unwind": "$productDetails"},
        {"$group": {
            "_id": "$_id",
            "totalAmount": {"$sum": {"$multiply": ["$products.quantity", "$productDetails.price"]}}
        }}
    ]
    result = db.carts.aggregate(pipeline)
    pprint(list(result))

# 5. Zähle Anzahl der Bestellungen je Kunde


def orders_count_by_customer():
    pipeline = [
        {"$group": {
            "_id": "$userId",
            "orderCount": {"$sum": 1}
        }}
    ]
    result = db.orders.aggregate(pipeline)
    pprint(list(result))

# 6. Berechne die durchschnittliche Anzahl der Produkte in einem Warenkorb


def average_products_per_cart():
    pipeline = [
        {"$project": {"totalProducts": {"$size": "$products"}}},
        {"$group": {
            "_id": None,
            "avgProducts": {"$avg": "$totalProducts"}
        }}
    ]
    result = db.carts.aggregate(pipeline)
    pprint(list(result))

# 7. Berechne den durchschnittlichen Gesamtpreis aller Artikel im Warenkorb


def average_cart_price():
    pipeline = [
        {"$unwind": "$products"},
        {"$lookup": {
            "from": "products",
            "localField": "products.productId",
            "foreignField": "_id",
            "as": "productDetails"
        }},
        {"$unwind": "$productDetails"},
        {"$group": {
            "_id": "$_id",
            "totalAmount": {"$sum": {"$multiply": ["$products.quantity", "$productDetails.price"]}}
        }},
        {"$group": {
            "_id": None,
            "avgCartPrice": {"$avg": "$totalAmount"}
        }}
    ]
    result = db.carts.aggregate(pipeline)
    pprint(list(result))

# 8. Gruppiere die Bestellungen nach Produkt und zähle, wie oft jedes Produkt gekauft wurde


def product_order_frequency():
    pipeline = [
        {"$unwind": "$products"},
        {"$group": {
            "_id": "$products.productId",
            "count": {"$sum": "$products.quantity"}
        }}
    ]
    result = db.orders.aggregate(pipeline)
    pprint(list(result))

# 9. Berechne den Gesamtwert aller Bestellungen unter Berücksichtigung der Produktmenge und des Einzelpreises


def total_value_of_all_orders():
    pipeline = [
        {"$unwind": "$products"},
        {"$lookup": {
            "from": "products",
            "localField": "products.productId",
            "foreignField": "_id",
            "as": "productDetails"
        }},
        {"$unwind": "$productDetails"},
        {"$group": {
            "_id": None,
            "totalValue": {"$sum": {"$multiply": ["$products.quantity", "$productDetails.price"]}}
        }}
    ]
    result = db.orders.aggregate(pipeline)
    pprint(list(result))

# 10. Zähle die Anzahl der Benutzer pro Stadt


def users_count_by_city():
    pipeline = [
        {"$group": {
            "_id": "$city",
            "userCount": {"$sum": 1}
        }}
    ]
    result = db.users.aggregate(pipeline)
    pprint(list(result))

# 11. Gruppiere die Bücher nach Autoren und erstelle eine Liste der Büchertitel für jeden Autor


def books_by_author():
    pipeline = [
        {"$group": {
            "_id": "$author",
            "books": {"$push": "$title"}
        }}
    ]
    result = db.books.aggregate(pipeline)
    pprint(list(result))


# Aufruf der Funktionen
print("1. Gesamtpreis aller Bestellungen, gruppiert nach Produkt:")
total_price_by_product()
print("\n2. Durchschnittsalter der Benutzer je Stadt:")
average_age_by_city()
print("\n3. Anzahl der Bestellungen je Tag:")
orders_count_by_day()
print("\n4. Gesamtpreis der Produkte in jedem Warenkorb:")
total_price_by_cart()
print("\n5. Anzahl der Bestellungen je Kunde:")
orders_count_by_customer()
print("\n6. Durchschnittliche Anzahl der Produkte in einem Warenkorb:")
average_products_per_cart()
print("\n7. Durchschnittlicher Gesamtpreis aller Artikel im Warenkorb:")
average_cart_price()
print("\n8. Häufigkeit der Produktkäufe:")
product_order_frequency()
print("\n9. Gesamtwert aller Bestellungen:")
total_value_of_all_orders()
print("\n10. Anzahl der Benutzer pro Stadt:")
users_count_by_city()
print("\n11. Bücher nach Autor:")
books_by_author()
```