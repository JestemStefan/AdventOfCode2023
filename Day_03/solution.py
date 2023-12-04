from utils import benchmark

TEST_DATA = "test_input.txt"
REAL_DATA = "input_data.txt"


@benchmark(repeat=1000)
def solution_part_1():
    solution = 0

    with open(REAL_DATA) as file:
        for line in file:
            pass

    return solution


@benchmark(1000)
def solution_part_2():
    solution = 0
    with open(REAL_DATA) as file:
        for line in file:
            pass

    return solution


if __name__ == "__main__":
    solution_part_1()
    print("\n")
    solution_part_2()
