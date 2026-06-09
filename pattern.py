n = int(input("Enter rows for Pattern 1: "))

with open("pattern.txt", "w") as f:

    # Pattern 1
    f.write("Pattern 1\n")
    for i in range(n):
        txt = "####"
        print(txt)
        f.write(txt + "\n")

    f.write("\n")

    # Pattern 2
    f.write("Pattern 2\n")
    for i in range(1, 5):
        txt = ""
        for j in range(1, i + 1):
            txt += str(j)

        print(txt)
        f.write(txt + "\n")

    f.write("\n")

    # Pattern 3
    f.write("Pattern 3\n")
    n2 = int(input("Enter rows for Pattern 3: "))

    for i in range(n2, 0, -1):
        txt = "*" * i
        print(txt)
        f.write(txt + "\n")

    f.write("\n")

    # Pattern 4
    f.write("Pattern 4\n")
    for i in range(1, 5):
        txt = str(i) * i
        print(txt)
        f.write(txt + "\n")

    f.write("\n")

    # Pattern 5
    f.write("Pattern 5\n")
    for i in range(1, 5):
        txt = "*" * i
        print(txt)
        f.write(txt + "\n")

    # Pattern 6
    f.write("Pattern 6\n")
    num = 1

    for i in range(1, 5):
        txt = ""
        for j in range(i):
            txt += str(num)
            num += 1

        print(txt)
        f.write(txt + "\n")

print("All patterns saved in pattern.txt")
