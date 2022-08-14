from decimal import Decimal


def convertToBinary(n):
    if n > 1:
        convertToBinary(n // 2)

    print(n % 2, end='')


# decimal number
dec = Decimal(input("Enter a number: "))

convertToBinary(dec)
print()
