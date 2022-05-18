# import fileinput


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    for line1 in lines:
        for line2 in lines:
            x = "".join(a for a, b in zip(line1, line2) if a == b)
            if len(x) == len(line1) - 1:
                print(x)
                break


main()
