import timeit
from random import randint


def merge_sort(collection, length):
    global counter
    if len(collection) > 1:
        middle_position = len(collection) // 2
        left = collection[:middle_position]
        right = collection[middle_position:]
        merge_sort(left, length), merge_sort(right, length)

        left_index, right_index, index = 0, 0, 0
        while (left_index < len(left)) and (right_index < len(right)):
            if left[left_index] < right[right_index]:
                collection[index] = left[left_index]
                left_index += 1
            else:
                collection[index] = right[right_index]
                right_index += 1
            index += 1

        while left_index < len(left):
            collection[index] = left[left_index]
            left_index += 1
            index += 1

        while right_index < len(right):
            collection[index] = right[right_index]
            right_index += 1
            index += 1

        counter += 1
        print("Step %i -->" % counter, left, "<-->", right)

    if len(collection) == length:
        return collection


def visualization():
    length = 10
    collection = [randint(0, length) for _ in range(length)]

    print("Initial list:", collection)
    print("Visualization of algorithm work.")

    collection = merge_sort(collection, length)

    print("Final list:", collection)
    print("Total numbers of passages:", counter)


def main():
    elapsed_time = timeit.timeit(visualization, number=1)
    print("Elapsed time: ", round(elapsed_time, 7), "sec.")


if __name__ == '__main__':
    counter = 0
    main()
