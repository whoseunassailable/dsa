from array import array

class Solution:
    def quicksort(*, array_of_elements: array):
        if len(array_of_elements) < 2:
            return array_of_elements
        pivot = array_of_elements[len(array_of_elements) // 2]
        left = [x for x in array_of_elements if x < pivot]
        mid = [x for x in array_of_elements if x == pivot]
        right = [x for x in array_of_elements if x > pivot]
        return Solution.quicksort(array_of_elements=left) + mid + Solution.quicksort(array_of_elements=right)
    
if __name__ == "__main__":
    arr = [42, 7, 19, 88, 3, 56, 23, 91, 14, 60, 2, 37]
    print(Solution.quicksort(array_of_elements=arr))