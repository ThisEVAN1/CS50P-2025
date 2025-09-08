grocery_list = []
'''
It should look something like this
[
    {
        'item': 'item_name'
        'amount': 'amount_of_items'
    }
]
'''

while True:
    try:
        # Place all the items the user listed into the list
        # Remember to put in the fruit name and add the amount using .append()
        item = input()

        # Check if grocery_list list is empty
        if grocery_list == []:
            grocery_list.append({'item': item, 'amount': 1})
            continue

        found = False
        # Search through every object
        for object in grocery_list:
            # If there is already an item there just update the amount
            if object.get('item') == item:
                object['amount'] += 1
                found = True
                break

        # If the item wasn't found then append the item
        if found == False:
            grocery_list.append({'item': item, 'amount': 1})


    except EOFError:
        # Make a new sorted dictionary
        sorted_grocery_list = sorted(grocery_list, key=lambda amount: amount['item'])
        #print(sorted_grocery_list)

        # Print the amount and name of every item
        for object in sorted_grocery_list:
            print(f'{object.get('amount')} {object.get('item').upper()}')
        break
