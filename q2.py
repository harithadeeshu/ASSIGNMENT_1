#Q2. Write a program to reverse an array in place? In place means you cannot create a new array. You 
#have to update the original array.
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(arr)
arr = arr[::-1]
print("Reversed array is")
print(arr)

def reverse_arr(arr):
    arr = reversed(arr)
    return list(arr)
arr = [11,12,13,14,15]
reverse_arr(arr)
[15, 14, 13, 12, 11]