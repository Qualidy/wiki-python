# Lösung Aufgabe 1

```python
def calculate_discount_optimized(price, discount, is_member):
    if is_member and discount > 10:
        return price * 0.9
    if is_member:
        return price * 0.95
    if discount > 20:
        return price * 0.85
    return price
```

# Lösung Aufgabe 2

```python
def check_access_optimized(age, has_ticket, special_pass):
    if age > 18 and has_ticket:
        return "Access granted"
    if age <= 18 and special_pass:
        return "Access granted"
    if age > 18 and not has_ticket:
        return "No ticket"
    return "Access denied"
```

# Lösung Aufgabe 3

```python
def user_permission_check_optimized(role, age, account_status):
    if account_status != "active":
        return "Account inaktiv"

    if role != "admin" and age < 18:
        return "Zugriff verweigert"

    if role == "admin" and age >= 18:
        return "Zugriff gewährt"

    if age >= 18:
        return "Zugriff eingeschränkt"

    return "Zu jung"

print(user_permission_check_optimized("admin", 20, "active"))  # Erwartet: "Zugriff gewährt"
print(user_permission_check_optimized("admin", 17, "active"))  # Erwartet: "Zu jung"
print(user_permission_check_optimized("user", 20, "active"))   # Erwartet: "Zugriff eingeschränkt"
print(user_permission_check_optimized("user", 17, "inactive")) # Erwartet: "Account inaktiv"
```