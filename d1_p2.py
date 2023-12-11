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

    # with open("d1.txt", "r") as f:
    #     for l in f:
    #         total += line_value(l)

    print(line_value("kjony1kjoneoptwo"))


def line_value(line: str) -> int:
    large_num = 999999
    m: int = large_num

    for _str, _int in numbers.items():
        str_pos = line.find(_str)  # 'one'
        str_pos = str_pos if str_pos != -1 else large_num

        num_pos = line.find(str(_int))
        num_pos = num_pos if num_pos != -1 else large_num

        print(f"str pos {str_pos}")
        print(f"num pos {num_pos}")
        print("\n")

        m = min(str_pos, num_pos, min)

        # if num_pos != -1:
        #     min = num_pos if num_pos < min else min
        # if str_pos != -1:
        #     min = str_pos if str_pos < num_pos else num_pos  # '1'

    return min


main()
