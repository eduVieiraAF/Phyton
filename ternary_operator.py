age = 25
smokes = False


# Health classification using ternary operator
health = "poor" if age > 60 or smokes else ("good" if age < 18 else "excellent")
print("Health status: " + health)

# equivalent
print("Health status: " + ("poor" if age > 60 or smokes else ("good" if age < 18 else "excellent")))

# instead of if-else
if age > 60 or smokes:
    health = "poor"
elif age < 18:
    health = "good"
else:
    health = "excellent"

print("Health status: " + health)