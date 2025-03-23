# Python Class to implement the array methods

class ArrayOperations:
    def __init__(self, arr: list):
        self.arr = arr

    def max_min(self) -> tuple:
        """ Finds the maximum and minimum in an array. Returns as a tuple """
        return max(self.arr), min(self.arr)
    
    def reverse(self, arr: list = None) -> list:
        """ 
        Simply Does a reversal. 
        """
        return self.arr[::-1]
    
    def is_sorted(self) -> bool:
        """ Checks if the array is sorted """
        return self.arr == sorted(self.arr)
    
    def remove_duplicates(self) -> list:
        """ Removes duplicates from a sorted array """
        return list(set(self.arr))
    
    def linear_search(self, element: int) -> int:
        """ 
        Searches for an element in an array. 
        Returns the index of the element if found, -1 otherwise.
        """
        for i in range(len(self.arr)):
            if self.arr[i] == element:
                return i
        return -1

# sample test array array
# change this array to test the methods
number_arr = ['a', 'b','c','d','e']

# an instance of the class
array_ops = ArrayOperations(number_arr)

# Using the method
print(f"The Array: {number_arr}\n")
print(f"Max & Min: {array_ops.max_min()}")
print(f"Reversed: {array_ops.reverse()}")
print(f"Sorted (boolean): {array_ops.is_sorted()}")
print(f"No-Duplicates: {array_ops.remove_duplicates()}")
print(f"Linear Search (4): {array_ops.linear_search('e')}\n")