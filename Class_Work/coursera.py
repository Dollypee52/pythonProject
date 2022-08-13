


def calculate_subtotal(order):
    """ Calculates the subtotal of an order

    [IMPLEMENT ME]
        1. Add up the prices of all the items in the order and return the sum

    Args:
        order: list of dicts that contain an item name and price

    Returns:
        float = The sum of the prices of the items in the order
    """
    print('Calculating bill subtotal...')
    ### WRITE SOLUTION HERE{"name" : "rice", "price": 123}
    sum = 0
    for item in order:
        for i, j in item.items():
            if i == "price":
                sum += j
    return sum


order = [{"name" : "rice", "price": 123}, {"name" : "beans", "price": 111}]
print(calculate_subtotal(order))