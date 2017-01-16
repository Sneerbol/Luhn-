card = input("Enter your credit card number here: ")
digit_sum = 0

for i, digit in enumerate(reversed(card)):
    n = int(digit)

    if i % 2 == 0:
        digit_sum += n
    elif i >= 5:
        digit_sum += n * 2 - 9
    else:
        digit_sum += n * 2

if digit_sum % 10 == 0:
    print("Всьо,нема грошей,пуста карта!")
else:
    print("Card is invalid!")
