import sys

def main():
    it=iter(sys.stdin.read().split()); T=int(next(it)); outs=[]
    dirs='NESW'; dr=[-1,0,1,0]; dc=[0,1,0,-1]
    for _ in range(T):
        R=int(next(it)); C=int(next(it)); r=int(next(it)); c=int(next(it)); d=next(it); cmds=next(it)
        di=dirs.index(d)
        for ch in cmds:
            if ch=='L': di=(di-1)%4
            elif ch=='R': di=(di+1)%4
            else:
                nr=r+dr[di]; nc=c+dc[di]
                if 1<=nr<=R and 1<=nc<=C: r,c=nr,nc
        outs.append(f"Final = ({r}, {c}, {dirs[di]})")
    print('\n'.join(outs))
if __name__=='__main__': main()
