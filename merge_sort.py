import math

#
# array = list()

array = [4,3,12,14,43,2,1,33,22,5]

# size = int(input("Enter the size of array : "))



# for index in range(size):
#     number = int(input(f"array[{index}] : "))
#     array.append(number)


def merge(left_array, right_array, array):
    left_size = len(left_array)
    right_size = len(right_array)
    i = 0
    l = 0
    r = 0
    while l < left_size and r < right_size:
        if left_array[l] < right_array[r]:
            array[i] = left_array[l]
            l +=1
            i +=1
        else:
            array[i] = right_array[r]
            r += 1
            i += 1
    while l < left_size:
        array[i] = left_array[l]
        l += 1
        i += 1
    while r < right_size:
        array[i] = right_array[r]
        r += 1
        i += 1


def merge_sort(array):
    if len(array) <= 1:
        return array

    middle = int(math.ceil(len(array) / 2))

    left_array = array[: middle]
    right_array = array[ middle:]

    print(left_array)
    print(right_array)

    merge_sort(left_array)
    merge_sort(right_array)
    merge(left_array, right_array, array)



print(array)
merge_sort(array)
print(array)