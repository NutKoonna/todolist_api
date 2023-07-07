def trailingZeros(number):
    count = 0
    integer = 5
    while number / integer >= 1:
        count += number // integer
        integer = integer * integer
    return count


if __name__ == '__main__':
    number_of_input = int(input("Enter number: "))
    print("trailing zero of  %d! = %d" % (number_of_input, trailingZeros(number_of_input)))
