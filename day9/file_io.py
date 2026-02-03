def write_numbers(filename, n):
    f = open(filename, "w")
    for i in range(1, n + 1):
        f.write(str(i) + "\n")
    f.close()


def read_numbers(filename):
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    return [int(x.strip()) for x in lines]


def append_number(filename, value):
    f = open(filename, "a")
    f.write(str(value) + "\n")
    f.close()


def sum_numbers(numbers):
    total = 0
    for n in numbers:
        total += n
    return total


def average_numbers(numbers):
    if len(numbers) == 0:
        return 0
    return sum_numbers(numbers) / len(numbers)


def main():
    filename = "numbers.txt"

    write_numbers(filename, 10)
    append_number(filename, 42)

    numbers = read_numbers(filename)

    total = sum_numbers(numbers)
    avg = average_numbers(numbers)

    print("Numbers:", numbers)
    print("Sum:", total)
    print("Average:", avg)


main()