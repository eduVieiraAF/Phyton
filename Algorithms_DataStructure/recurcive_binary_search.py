
def recursive_binary_search(list, target):
    """
    Return true if target is found, else return false
    """
    
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list)) // 2
        
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)

def verify(result):
    print("Target found:", result)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sorted_numbers = sorted(numbers)

result = recursive_binary_search(sorted_numbers, 12)
verify(result)

result = recursive_binary_search(sorted_numbers, 6)
verify(result)

