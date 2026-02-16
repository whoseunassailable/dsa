from array import array

class Solution:
    def find_smallest_number(*, array_of_elements: array) -> int:
        smallest = array_of_elements[0]
        smallest_index = 0
        for i in range(1, len(array_of_elements)):
            if(array_of_elements[i] < smallest):
                smallest = array_of_elements[i]
                smallest_index = i
        return smallest
    
    def selection_sort(*, array_of_elements: array):
        list_of_sorted_elements = []
        for _ in range(len(array_of_elements)):
            smallest_number = Solution.find_smallest_number(array_of_elements=array_of_elements)
            list_of_sorted_elements.append(smallest_number)
            array_of_elements.remove(smallest_number)
        return list_of_sorted_elements

if __name__ == "__main__":
    arr = array('i', [58, 12, 91, 37, 4, 76, 29, 83, 65, 10, 99, 41, 7, 88, 23, 54, 16, 72, 31, 6])
    print(Solution.selection_sort(array_of_elements=arr))
