# ou are given an array A of N elements. Sort the given array in increasing order of number of distinct factors of each element, i.e., element having the least number of factors should be the first to be displayed and the number having highest number of factors should be the last one. If 2 elements have same number of factors, then number with less value should come first.
#
# Note: You cannot use any extra space
#
# Example Input
# Input 1:
# A = [6, 8, 9]
# Input 2:
# A = [2, 4, 7]
#
#
# Example Output
# Output 1:
# [9, 6, 8]
# Output 2:
# [2, 7, 4]

import math

# Helper function to calculate the number of distinct factors of a number
def num_distinct_factors(n):
    factors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            if n//i!=i:
                factors.append(n // i)
    return len(factors)

# Main function to sort the array
def sort_by_num_distinct_factors(arr):
    return sorted(arr, key=lambda x: (num_distinct_factors(x), x))

# Example usage
arr = [6,8,9]
sorted_arr = sort_by_num_distinct_factors(arr)
print(sorted_arr)