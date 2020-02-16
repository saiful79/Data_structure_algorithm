
def binarySearch(arr, start, end, x): 
    while start <= end: 
        mid = start + (end - start) // 2; 
        if arr[mid] == x: 
            return mid 
        elif arr[mid] < x: 
            start = mid + 1
        else: 
            end = mid - 1
    return -1
    
print("Please Enter number of input : \n")
number_of_input = int(input())
print("Please search list: \n")
arr = [input() for _ in range(number_of_input)]
print("Please search value: \n")
x = int(input())
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array") 
