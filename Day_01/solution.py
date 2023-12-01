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


@benchmark(1000)
def solution_part_2():
    words_to_int_mapping = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    # with open("input_data.txt") as file:
    with open("input_data.txt") as file:
        partial_solutions = []
        for line in file:
            first_digit = None
            last_digit = None
            partial_string = ""

            for c in line:
                if c.isdigit():
                    first_digit = int(c)
                    break

                else:
                    partial_string += c
                    if len(partial_string) < 3:
                        continue

                    for word in words_to_int_mapping:
                        l_words_idx = partial_string.find(word)
                        if l_words_idx != -1:
                            first_digit = words_to_int_mapping[word]
                            break

                if first_digit is not None:
                    break

            partial_string = ""
            for c in reversed(line):
                if c.isdigit():
                    last_digit = int(c)
                    break

                else:
                    partial_string = c + partial_string
                    for word in words_to_int_mapping:
                        r_words_idx = partial_string.find(word)

                        if r_words_idx != -1:
                            last_digit = words_to_int_mapping[word]
                            break

                if last_digit is not None:
                    break

            digit = first_digit * 10 + last_digit

            partial_solutions.append(digit)

    return sum(partial_solutions)


if __name__ == "__main__":
    solution_part_1()
    print("\n")
    solution_part_2()
