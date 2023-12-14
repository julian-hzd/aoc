def main():
    with open("d2_p1.txt", "r") as f:
        total = 0
        for l in f:
            total += evaluate_game(l)
        print(total)


def evaluate_game(l: str):
    bag = {"red": 0, "blue": 0, "green": 0}
    configuration = {"red": 12, "blue": 14, "green": 13}
    line = l.split(":")
    game_id = int(line[0].split(" ")[1])
    sets = line[1].split(";")
    for s in sets:
        y = s.replace("\n", "")
        subset = y.split(",")

        for su in subset:
            y = su.split(" ")
            add = bag[y[2]] + int(y[1])
            if add > configuration[y[2]]:
                return 0
            bag[y[2]] = add
        bag = {"red": 0, "blue": 0, "green": 0}
    return game_id


main()
