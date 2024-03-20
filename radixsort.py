import random
import time

def counting_sort(arr, exp, base):
    n = len(arr)
    output = [0] * n
    count = [0] * base

    # Store count of occurrences in count[]
    for i in range(n):
        index = (arr[i] // exp) % base
        count[index] += 1

    # Change count[i] so that count[i] now contains
    # actual position of this digit in output[]
    for i in range(1, base):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % base
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copy the output array to arr[], so that arr[] now
    # contains sorted numbers according to the current digit
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr, base=65536):
    # Find the maximum number to know number of digits
    max_num = max(arr)

    # Do counting sort for every digit. Note that
    # instead of passing digit number, exp is passed.
    # exp is base^i where i is the current digit number
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp, base)
        exp *= base
arr=[]
f = open("random_numbers[1].txt", "r")
for line in f.readlines():
    arr.append(int(line))
start_time = time.time()
radix_sort(arr)
#arr=sorted(arr)
print(f"{time.time()-start_time} seconds")