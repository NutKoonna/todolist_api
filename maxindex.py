def max_index(array):
    max_val = array[0]
    index = 0
    for i in range(len(array)):
        if array[i] > max_val:
            max_val = array[i]
            index = i
    print("max index is {} and values is {}".format(index, max_val))


if __name__ == '__main__':
    array = [1, 2, 1, 3, 5, 6, 4]
    max_index(array)
