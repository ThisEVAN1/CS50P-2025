input = input('What is the Answer to the Great Question of Life, the Universe, and Everything? ')
input = input.lower().strip()

match input:
    case '42':
        print('Yes')
    case 'forty-two':
        print('Yes')
    case 'forty two':
        print('Yes')
    case _:
        print('No')
