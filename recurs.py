def binari_search_recursion(data, target):
    if data == []:
        return False
    elif len(data) == 1:
        return data[0] == target
    else: 
        half = len(data) // 2
        if data[half] > target:
            return binari_search_recursion(data[:half], target)
        else:
            return binari_search_recursion(data[half:], target)
    
print (binari_search_recursion([1, 20, 33, 42, 52, 66, 74, 86, 91], 33) )   