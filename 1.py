def myhash(n,m,s):
    a=0
    for i in range(len(s)):
    	a=((a*n)%m+ord(s[i]))%m
    return a
n,m=map(int,input().split()) #n=257 m=2**61-1
s=input()
print(myhash(n,m,s))
