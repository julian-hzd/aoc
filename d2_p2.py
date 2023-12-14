def main():
    with open("d2.txt", "r") as f:
        total = 0
        for l in f:
            total += evaluate_game(l)
        print(total)


def evaluate_game(l: str):
    min_cubes = {"red": 0, "blue": 0, "green": 0}
    line = l.split(":")
    sets = line[1].split(";")
    for s in sets:
        y = s.replace("\n", "")
        subset = y.split(",")

        for su in subset:
            y = su.split(" ")
            if min_cubes[y[2]] < int(y[1]):
                min_cubes[y[2]] = int(y[1])
    total = 1
    for x in min_cubes.items():
        total *= x[1]
    return total


main()
