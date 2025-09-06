input = input('Greeting: ').strip()

#print(input.find(input))

if input.find('Hello') == 0:
    print('$0')
elif input.find('H') == 0:
    print('$20')
else:
    print('$100')
