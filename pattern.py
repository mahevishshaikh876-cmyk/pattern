n = int(input("Enter rows: "))
open("pattern.txt", "w").write("")

for i in range(n):
    txt = "####"
    print(txt)
    



for i in range(1, 5):
    txt = ""
    for j in range(1, i + 1):
        print(j, end="")
        txt += str(j)

    print()
    

n = int(input("Enter rows: "))


for i in range(n, 0, -1):
    print("*" * i)
    txt = "*" * i
    


for i in range(1, 5):
    txt = ""
    for j in range(i):
        print(i, end="")
        txt += str(i)

    print()
    



for i in range(1, 5):
    txt = "*" * i
    print(txt)
    open("pattern.txt", "a").write(txt + "\n")
