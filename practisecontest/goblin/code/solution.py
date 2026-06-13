import sys

def solve(arr, m):
    even_total = sum(x for x in arr if x % 2 == 0)
    big_boxes = sum(1 for x in arr if x >= m)
    return f"Even total = {even_total}, Big boxes = {big_boxes}"

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    answers = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        boxes = list(map(int, data[idx:idx+n]))
        idx += n
        m = int(data[idx])
        idx += 1
        answers.append(solve(boxes, m))
    print("\n".join(answers))

if __name__ == "__main__":
    main()
