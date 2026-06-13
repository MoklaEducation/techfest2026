import random, zipfile, os

def solve(arr,M):
    even=sum(x for x in arr if x%2==0)
    big=sum(1 for x in arr if x>=M)
    return f"Even total = {even}, Big boxes = {big}"

def write(name,cases):
    with open(f"{name}.in","w") as f:
        f.write(str(len(cases))+"\n")
        for arr,M in cases:
            f.write(str(len(arr))+" "+" ".join(map(str,arr))+" "+str(M)+"\n")
    with open(f"{name}.out","w") as f:
        f.write("\n".join(solve(a,m) for a,m in cases))

sample=[([5,8,11,12,8],10),([1,3,5],4),([20,20,19,2],20)]
edge=[([0],0),([1],0),([2],3),([100000],100000),([99999],100000),([0,0,0],1),([2,4,6,8],5),([1,3,5,7],5),([10,10,10],10),([9,8,7,6,5],7)]
random.seed(7)
big=[]
for i in range(5000):
    n=random.choice([1,2,3,5,10,20,50]) if i<200 else random.randint(1,100)
    if i%1000==0: n=1000
    arr=[random.randint(0,100000) for _ in range(n)]
    M=random.randint(0,100000)
    big.append((arr,M))
write('goblin.1',sample); write('goblin.2',edge); write('goblin.3',big)
open('solution.py','w').write('''import sys\n\ndef solve(arr, m):\n    even_total = sum(x for x in arr if x % 2 == 0)\n    big_boxes = sum(1 for x in arr if x >= m)\n    return f"Even total = {even_total}, Big boxes = {big_boxes}"\n\ndef main():\n    data = sys.stdin.read().strip().split()\n    if not data:\n        return\n    t = int(data[0])\n    idx = 1\n    answers = []\n    for _ in range(t):\n        n = int(data[idx])\n        idx += 1\n        boxes = list(map(int, data[idx:idx+n]))\n        idx += n\n        m = int(data[idx])\n        idx += 1\n        answers.append(solve(boxes, m))\n    print("\\n".join(answers))\n\nif __name__ == "__main__":\n    main()\n''')
open('solution.cpp','w').write('''#include <iostream>\n#include <vector>\nusing namespace std;\n\nint main() {\n    int t;\n    cin >> t;\n\n    for (int caseNum = 0; caseNum < t; caseNum++) {\n        int n;\n        cin >> n;\n\n        vector<int> boxes(n);\n        for (int i = 0; i < n; i++) {\n            cin >> boxes[i];\n        }\n\n        int m;\n        cin >> m;\n\n        long long evenTotal = 0;\n        int bigBoxes = 0;\n\n        for (int value : boxes) {\n            if (value % 2 == 0) {\n                evenTotal += value;\n            }\n            if (value >= m) {\n                bigBoxes++;\n            }\n        }\n\n        cout << "Even total = " << evenTotal << ", Big boxes = " << bigBoxes;\n        if (caseNum < t - 1) {\n            cout << endl;\n        }\n    }\n\n    return 0;\n}\n''')
open('Solution.java','w').write('''import java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int t = sc.nextInt();\n\n        for (int caseNum = 0; caseNum < t; caseNum++) {\n            int n = sc.nextInt();\n            int[] boxes = new int[n];\n\n            for (int i = 0; i < n; i++) {\n                boxes[i] = sc.nextInt();\n            }\n\n            int m = sc.nextInt();\n\n            long evenTotal = 0;\n            int bigBoxes = 0;\n\n            for (int value : boxes) {\n                if (value % 2 == 0) {\n                    evenTotal += value;\n                }\n                if (value >= m) {\n                    bigBoxes++;\n                }\n            }\n\n            System.out.print("Even total = " + evenTotal + ", Big boxes = " + bigBoxes);\n            if (caseNum < t - 1) {\n                System.out.println();\n            }\n        }\n    }\n}\n''')
open('README.txt','w').write('''The Goblin Snack Boxes\n\nInput format used in test files:\nFirst line: number of test cases T\nFor each test case: N followed by N box values followed by M\n\nExample:\n3\n5 5 8 11 12 8 10\n3 1 3 5 4\n4 20 20 19 2 20\n\nOutput format:\nEven total = X, Big boxes = Y\n\nFiles:\ngoblin.1.in / goblin.1.out - official sample tests\ngoblin.2.in / goblin.2.out - edge and medium tests\ngoblin.3.in / goblin.3.out - 5000 randomized tests\nsolution.py - Python solution\nSolution.java - Java solution\nsolution.cpp - C++ solution\n''')
with zipfile.ZipFile('/mnt/data/goblin_snack_boxes_solutions_tests.zip','w',zipfile.ZIP_DEFLATED) as z:
    for fn in os.listdir('.'):
        z.write(fn)
print('/mnt/data/goblin_snack_boxes_solutions_tests.zip')
