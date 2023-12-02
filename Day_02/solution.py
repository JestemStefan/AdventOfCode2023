from utils import benchmark

TEST_DATA = "test_input.txt"
REAL_DATA = "input_data.txt"


@benchmark(repeat=1000)
def solution_part_1():
    solution = 0

    with open(REAL_DATA) as file:
        for line in file:
            game_id_part, game_sets_part = line.strip().split(":")

            _, game_id = game_id_part.split(" ")
            game_sets = game_sets_part.split(";")

            legit = True
            for game_set in game_sets:
                if not legit:
                    break

                for cd in game_set.split(","):
                    count, cube_color = cd.strip().split(" ")

                    count = int(count)
                    if cube_color == "red" and count > 12:
                        legit = False
                        break

                    if cube_color == "green" and count > 13:
                        legit = False
                        break

                    if cube_color == "blue" and count > 14:
                        legit = False
                        break

            if legit:
                solution += int(game_id)

    return solution


@benchmark(1000)
def solution_part_2():
    solution = 0
    with open(REAL_DATA) as file:
        for line in file:
            game_id_part, game_sets_part = line.strip().split(":")

            _, game_id = game_id_part.split(" ")
            game_sets = game_sets_part.split(";")

            cube_counts = {
                "red": [],
                "green": [],
                "blue": [],
            }
            for game_set in game_sets:
                for cd in game_set.split(","):
                    count, cube_color = cd.strip().split(" ")
                    cube_counts[cube_color].append(int(count))

            game_power = (
                max(cube_counts["red"])
                * max(cube_counts["green"])
                * max(cube_counts["blue"])
            )
            solution += game_power

    return solution


if __name__ == "__main__":
    solution_part_1()
    print("\n")
    solution_part_2()
