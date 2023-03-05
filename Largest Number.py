from functools import cmp_to_key

class Solution:
    # @param A : list of integers
    # @return a string
    def largestNumber(self, A):
        # Convert the integers to strings
        A = list(map(str, A))
        # Define the custom comparison function
        def compare(x, y):
            return int(y+x) - int(x+y)
        # Sort the strings using the comparison function
        A.sort(key=cmp_to_key(compare))
        # Concatenate the strings to form the result
        result = ''.join(A)
        # Remove leading zeros
        result = result.lstrip('0')
        # Return the result
        if result:
            return result
        else:
            return '0'
