# declare original array
original_array = [-1, 8, 1, 8, -1, 5, 1, -3]

def find(original_array):
    # Declare an array which will store all the duplicate elements
    duplicate_array = []

    # Iterate on the elements of array to find duplicate elements
    for i in original_array:
        if original_array.count(i) > 1 and i not in duplicate_array:
            duplicate_array.append(i)
    
    print("Duplicate Array= ", duplicate_array)

# print(array)
print("Array= ", original_array)

find(original_array)