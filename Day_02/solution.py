from utils import benchmark


@benchmark(repeat=1000)
def solution_part_1():
    solution = 0

    with open("input_data.txt") as file:
        for line in file:
            pass

    return solution


@benchmark(1000)
def solution_part_2():
    solution = 0
    with open("input_data.txt") as file:
        for line in file:
            pass

    return solution


if __name__ == "__main__":
    solution_part_1()
    print("\n")
    solution_part_2()
