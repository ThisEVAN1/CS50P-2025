from inflect import engine
p = engine()

names = []

try:
    while True:
        names.append(input('Name: '))
except EOFError:
    print(f'\nAdieu, adieu, to {p.join(names)}')


