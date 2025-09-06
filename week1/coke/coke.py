amount_due = 50
change_owed = 0

while True:
    print(f'Amount Due: {amount_due}')
    coin_amount = int(input('Insert Coin: '))

    # If coin_amount is a valid value
    if not (coin_amount == 25 or coin_amount == 10 or coin_amount == 5):
        continue

    # If the coin amount is greater than amount due then give back amount due - coin
    if coin_amount >= amount_due:
        change_owed += abs(amount_due - coin_amount)
        print(f'Change Owed: {change_owed}')
        break

    amount_due -= coin_amount
