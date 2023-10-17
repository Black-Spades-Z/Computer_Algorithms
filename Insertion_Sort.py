
#
# array = list()

array = [4,3,12,14,43,2,1,33,22,5]

# size = int(input("Enter the size of array : "))



# for index in range(size):
#     number = int(input(f"array[{index}] : "))
#     array.append(number)

def insertion_sort(array):

    if array[0] > array[1]:
        temp = array[0]
        array[0] = array[1]
        array[1] = temp

    for i in range(2, len(array)):

        j = i
        while j > 0 and array[j] <= array[j-1]:
            temp = array[j]
            array[j] = array[j-1]
            array[j - 1] = temp
            j -= 1



print(array)
insertion_sort(array)
print(array)

