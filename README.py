# B.-Normal-Problem
t = int(input())
for _ in range(t):
    a = input().strip()
    b = ""
    for i in a:
        if i == "p":
            b += "q"
        elif i == "q":
            b += "p"
        elif i == "w":
            b += "w"
    rev = b[::-1]
    print(rev)
