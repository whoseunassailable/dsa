
from array import array

class Solution:
    def find_smallest_number(*, array_of_elements : array) -> int:
        smallest = array_of_elements[0]
        smallest_index = 0
        for i in range (1, len(array_of_elements)):
            if (array_of_elements[i] < smallest):
                print(f"Smallest number is : {array_of_elements[i]}")
                smallest = array_of_elements[i]
                smallest_index = i
        return smallest
            
if __name__ == "__main__":
    arr = [42, 89, 93, 15, 68, 24, 81, 3, 56, 19, 77, 1, 99, 35, 62]
    print(Solution.find_smallest_number(array_of_elements=arr))