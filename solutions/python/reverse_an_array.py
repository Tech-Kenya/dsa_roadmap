import random
def reverse_array(array: list) -> list:
    """
    Takes in an array and returns the reverse.
    Args:
        array(list): a list.
    Returns:
        list: elements in a reversed order.
    """
    return array[::-1]

if __name__ == '__main__':
    random_list = [random.randint(1, 100) for _ in range(10)]
    reversed_list  = reverse_array(random_list)
    print(f"The list elements are : {random_list}.")
    print(f"The reversed list elements are : {reversed_list}.")
