
import sys,string, itertools
n,k = input().split()
n,k = int(n),int(k)
L = [ int(x) for x in input().split()]
while k in L :
    L.remove(k)
if len(L) > 0 :
    print(*L)
else :
    print('empty')
