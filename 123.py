def list(_list, number):
    a = len(_list)
    for i in _list:
        if number == i:
            return True
    return False

        
print(list([1, 2, 33, 45], 2))