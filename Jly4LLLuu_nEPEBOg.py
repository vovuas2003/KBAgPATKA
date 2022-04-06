print('4ucJIo:',end=' ')
n=input()
print('u3 CC c OCHOBAHuEM:',end=' ')
a=int(input())
print('B CC c OCHOBAHuEM:',end=' ')
b=int(input())
n=int(n,a)
arr='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
if n<0:
    print('-',end='')
    n=-n
s=''
while n>0:
    s=arr[n%b]+s
    n=n//b
print(s)
input()
