import sys

def solve(s):
    x = y = 0
    for ch in s:
        if ch == "E": x += 1
        elif ch == "W": x -= 1
        elif ch == "N": y += 1
        elif ch == "S": y -= 1
    return f"Position = ({x}, {y}), Distance = {abs(x) + abs(y)}"

data = sys.stdin.read().splitlines()
t = int(data[0])
for i in range(1, t + 1):
    print(solve(data[i].strip()))
