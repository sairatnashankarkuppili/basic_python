def find_missing_number(arr, n): 
    total_sum = n * (n + 1) //2
    array_sum = sum(arr)
    return total_sum - array_sum

n = int(input("Enter the total number of elements (n): "))
arr = list(map(int, input("Enter the array elements separated by space: ").split()))

missing_number = find_missing_number(arr, n)
print("Missing number:", missing_number)
