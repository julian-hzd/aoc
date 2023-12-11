numbers = {
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


def main():
    total = 0
    # print(line_value("1threenine241gnrdfqn5"))
    # return

    with open("d1.txt", "r") as f:
        for l in f:
            x = line_value(l)
            print(x)
            total += x

    print(total)


def line_value(line: str) -> int:
    first_num = -1
    second_num = -1
    large_num = 999999
    min_pos: int = large_num
    max_pos: int = -1

    for _str, _int in numbers.items():
        print(_int)
        # if the number was not found then
        # assign 999999 to ignore it in the min()

        str_pos = line.find(_str)  # 'one'
        num_pos = line.find(str(_int))

        str_pos = str_pos if str_pos != -1 else large_num
        num_pos = num_pos if num_pos != -1 else large_num

        # if new minimum position save the new number
        temp = min_pos
        min_pos = min(str_pos, num_pos, min_pos)
        first_num = _int if temp != min_pos else first_num

        # if the number was not found then
        # assign -1 to ignore it in the max()

        str_pos = line.rfind(_str)  # 'one'
        num_pos = line.rfind(str(_int))

        str_pos = str_pos if str_pos != large_num else -1
        num_pos = num_pos if num_pos != large_num else -1

        # if new max position save the new number
        temp = max_pos
        max_pos = max(str_pos, num_pos, max_pos)
        second_num = _int if temp != max_pos else second_num
        print(f"{str(first_num)}{str(second_num)}")

    return int(f"{str(first_num)}{str(second_num)}")


main()
