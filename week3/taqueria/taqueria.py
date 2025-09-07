total_price = 0
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


while True:
    try:
        item = input('Item: ').title()
        item_price = menu.get(item)
        total_price += item_price
        print(f'Total: ${total_price:.2f}')
    except EOFError:
        print()
        break
    except KeyError:
        ...
    except TypeError:
        ...
