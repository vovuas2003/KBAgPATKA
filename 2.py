'''
Найти все вхождения (их номера) строки s в строку t, нумерация с 0
Если вхождений нет, выводим -1
Это алгоритм Рабина-Карпа
'''
def myhash(s):
    h=[0]
    p=1
    global n
    global m
    for c in s:
	    h.append(((h[-1]*n)%m+ord(c))%m)
	    p=(p*n)%m
    return h,p
s=input()
t=input()
m=2**61-1
n=257
s_hash,p=myhash(s) #p sdvig
s_hash=s_hash[-1]
h,_=myhash(t)#_ - это фиктивная переменная, нам здесь не нужен р
pos=[]
for l in range(len(t)-len(s)+1): #l left
    r=l+len(s) #r right
    if s_hash==(h[r]-(h[l]*p)%m)%m:
	    pos.append(str(l))
if not pos:
    print(-1)
else:
    print(" ".join(pos))
