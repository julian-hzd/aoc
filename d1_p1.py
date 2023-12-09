def main():
    total = 0

    with open("d1.txt", "r") as f:
        for l in f:
            total += line_value(l)

    print(total)


def line_value(line: str) -> int:
    for c in line:
        t_s: str
        if c.isdigit():
            t_s = c
            for r_c in reversed(line):
                if r_c.isdigit():
                    t_s += r_c
                    return int(t_s)
    return -1


main()
