def main():
    with open("input.txt", "r") as f:
        p = f.read().splitlines()

    validPass = 0
    for item in p:
        policy, password = item.split(":")
        rangeVal, char = policy.split(" ")
        minCount, maxCount = rangeVal.split("-")
        currCount = password.count(char)
        print(f"{minCount} # {maxCount} : {char} --> {password} => {currCount}")
        if currCount >= int(minCount) and currCount <= int(maxCount):
            validPass += 1

    print(validPass)


main()
