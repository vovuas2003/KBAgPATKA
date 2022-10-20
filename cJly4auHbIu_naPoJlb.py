import random
arr=''
for i in range(10):
    arr=arr+str(i)
for i in range(ord('a'),ord('z')+1):
    arr=arr+chr(i)
for i in range(ord('A'),ord('Z')+1):
    arr=arr+chr(i)
arr=arr+'_'
print('BBeguTe KoJlu4ECTBO:')
k=int(input())
print('BBeguTe gJluHY:')
dlina=int(input())
l=len(arr)
for i in range(k):
    x=random.randint(0,l**dlina-1)
    s=''
    while x>0:
        s=arr[x%l]+s
        x=x//l
    while len(s)<dlina:
        s=arr[0]+s
    print(s)
print('Enter - 3AKPbITb cmd')
input()
