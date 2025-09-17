camel_case = input('camelCase: ')
snake_case = []

# Loop through all the letters
for c in range(len(camel_case)):
    #print(camel_case[c])

    # If the letter is capitalized
    if camel_case[c].isupper():
        # Add an underscore
        snake_case.insert(len(snake_case), '_')

        # Add the lowercase to snake_case array
        snake_case.append(camel_case[c].lower())
    else:
        # Add the same character from camel to snake
        snake_case.append(camel_case[c])

snake_case = ''.join(snake_case)

print(f'snake_case: {snake_case}')
