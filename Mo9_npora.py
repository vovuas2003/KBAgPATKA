arr='0123456789abc'
dlina=int(input())
l=len(arr)
for i in range(l**dlina):
    x=i
    s=''
    while x>0:
        s=arr[x%l]+s
        x=x//l
    while len(s)<dlina:
        s=arr[0]+s
    print(s)
