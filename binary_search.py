import random

def binary_search(array_of_random_elements, target):
    low, high = 0, len(array_of_random_elements) - 1
    
    while low <= high: 
        mid = (low + high) // 2
        print(f"Mid is ${mid}")
        guess = array_of_random_elements[mid]
        print(f"Our target is {target}")
        print(f"Our guess is {guess}")
        if guess == target :
            return mid
        elif guess > target : 
            print(f"{guess} > {target}")
            print(f"{high} = {mid} - 1")
            high = mid - 1
            print(high)
        else:
            print(f"{guess} < {target}")
            print(f"{low} = {mid} + 1")
            low = mid + 1
            print(low)
    return -1

array_of_random_elements = random.sample(range(1, 100000), 20)
array_of_random_elements.sort()
arr = array_of_random_elements
target = random.choice(arr)
index = binary_search(arr, target)
print(index)
