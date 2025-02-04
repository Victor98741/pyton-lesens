m = [1, 5, 3, 6, 12, 7]
arr=m

def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)
        
def partition(arr, low, high):
     i = (low - 1)
     pivot = arr[high]
     
     for j in range(low, high):
         if arr[j] < pivot:
             i = i + 1
             arr[i], arr[j] = arr[j], arr[i]
     arr[i + 1], arr[high] = arr[high], arr[i + 1]
     
     return i + 1
quick_sort(arr, 0, 5)
print(arr)
 #piton_tutor.com