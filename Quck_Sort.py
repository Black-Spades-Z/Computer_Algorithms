
#
# array = list()

array = [3,4,12,14,43,2,1,33,22,5]

# size = int(input("Enter the size of array : "))

size = len(array)


# for index in range(size):
#     number = int(input(f"array[{index}] : "))
#     array.append(number)

def pivot(array: list, start: int, end: int):

        p = array[end]
        i = start - 1


        for j in range(start, end):
                ja = array[j]
                if array[j] < p:
                        ai = array[i]
                        i += 1
                        temp = array[j]
                        array[j] = array[i]
                        array[i] = temp

        i += 1
        j += 1
        temp = array[j]
        array[j] = array[i]
        array[i] = temp
        return i

def quicksort(array: list, start: int, end: int):
        if start >= end:
            return
        p = pivot(array, start, end)


        quicksort(array, start, p - 1)
        quicksort(array, p + 1, end)


quicksort(array, 0, size -1 )
print(array)