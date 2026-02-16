class Solution:
    def find_element(*, list_of_elements: list, item: int):
        low_index = 0
        
        high_index = len(list_of_elements) - 1
        print (f"Low index is {low_index}")                
        print (f"High index is {high_index}")

        while low_index <= high_index:
            mid_index = (low_index + high_index) // 2
            print (f"Mid index is {mid_index}")
            mid_element = list_of_elements[mid_index]
            print (f"Mid index is {mid_index}")

            if mid_element < item:
                low_index = mid_index + 1
                print (f"Low index is {low_index}")
            elif mid_element > item:
                high_index = mid_index - 1
                print (f"High index is {high_index}")
            else :
                return f"Item is located at {mid_index}"
        return "Item not found at any location"
    
if __name__ == "__main__":
    import random

    nums = [random.randint(1, 10_000_000) for _ in range(1_000_000)]
    nums.sort()

    print(Solution.find_element(list_of_elements=nums, item=73))
    