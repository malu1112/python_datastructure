# File index of specific element in the list
my_list = [3,5,63,235,21,5,3,3,5,6]

def search(my_list, elt):
    for index, value in enumerate(my_list):
        if elt == value:
            return index, value
    else:
        return None, None

index, value = search(my_list, 3)

print("Element: {} present at index: {}".format(value, index))
