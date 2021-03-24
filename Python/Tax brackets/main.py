income = int(input())

if 0 <= income <= 15527:
    tax = 0
elif 15527 < income <= 42707:
    tax = 15
elif 42707 < income <= 132406:
    tax = 25
elif income >= 132407:
    tax = 28
else:
    tax = 0

calculated_tax = round((income * tax) / 100)

print(f"The tax for {income} is {tax}%. That is {calculated_tax} dollars!")
