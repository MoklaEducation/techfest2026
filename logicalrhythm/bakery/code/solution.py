import sys
from collections import deque, defaultdict

def main():
    data=sys.stdin.read().strip().split();
    if not data: return
    it=iter(data); t=int(next(it)); out=[]
    for _ in range(t):
        n=int(next(it)); k=int(next(it)); names=[next(it) for _ in range(n)]
        q=deque(names); served=defaultdict(int); service=0; leave=[]
        while q:
            name=q.popleft(); service+=1; served[name]+=1
            if service % k == 0 and served[name] == 1:
                q.append(name)
            else:
                leave.append(name)
        out.append(', '.join(leave))
    print('\n'.join(out))
if __name__=='__main__': main()
