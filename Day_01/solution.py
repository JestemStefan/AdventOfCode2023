from utils import benchmark


@benchmark(repeat=1000)
def solution_part_1():
    solution = 0

    with open("input_data.txt") as file:
        for line in file:
            # scan the line and fine the first digit
            first_digit = None
            for c in line:
                if c.isdigit():
                    first_digit = c
                    break

            # scan the line backwards and find the last digit
            last_digit = None
            for c in reversed(line):
                if c.isdigit():
                    last_digit = c
                    break

            solution += int(first_digit + last_digit)

    return solution


@benchmark(1)
def solution_part_2():
    solution = 0

    words = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "zero",
    ]

    with open("input_data.txt") as file:
        for line in file:
            # scan the line and fine the first digit
            first_digit = None
            for c in line:
                if c.isdigit():
                    first_digit = c
                    break

                if c in words:
                    first_digit = words.index(c) + 1
                    break

            # scan the line backwards and find the last digit
            last_digit = None
            for c in reversed(line):
                if c.isdigit():
                    last_digit = c
                    break

                if c in words:
                    last_digit = words.index(c) + 1
                    break

            solution += int(first_digit + last_digit)

    return solution


if __name__ == "__main__":
    solution_part_1()
    solution_part_2()
