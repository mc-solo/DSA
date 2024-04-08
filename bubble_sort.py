my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)

for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
        if my_array[j] > my_array[j+1]:
                my_array[j], my_array[j+1] = my_array[j+1],my_array[j]   #python multiple assignment feature
                swapped = True

    if not swapped:
        break
print("Sorted array: ", my_array)

# bubble sort  could be optimized to break out of the loop if there's no swap in the inner loop