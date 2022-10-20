'''
Вводится постфиксное выражение с переменными (не могут начинаться с цифры)
Далее присваивание переменным значения тоже в постфиксной форме
Найти результат
Например x + x * x = 6 при x = 2 => ввод имеет вид:
x x x * + =
x 2 =
'''
#ЦЕЛЫЕ ЧИСЛА
a=input().split()[:-1]
per_name=[]
per_zna4=[]
op=['+','-','*','/']
for x in a:
	try:
		_=int(x)
	except:
		if (x not in op) and (x not in per_name):
			per_name.append(x)
n=len(per_name)
for _ in range(n):
	per_zna4.append('')
f=False
for i in range(n):
	inp=input().split()[:-1]
	if inp[0] not in per_name:
		f=True
	if not f:
		per_zna4[per_name.index(inp[0])]=int(inp[1])
check=True
for x in per_name:
	if x[0] in [0,1,2,3,4,5,6,7,8,9]:
		check=False
		break
if f:
	print('incorrect')
elif not check:
	print('incorrect')
else:
	err=False
	for i in range(n):
		pe=per_name[i]
		zn=per_zna4[i]
		for j in range(len(a)):
			if a[j]==pe:
				a[j]=zn
	s=[]
	for x in a:
		if x in op:
			if len(s)<2:
				err=True
				break
			op2=s.pop()
			op1=s.pop()
			if x=='+':
				res=op1+op2
			elif x=='-':
				res=op1-op2
			elif x=='*':
				res=op1*op2
			elif x=='/':
				if op2==0:
					err=True
					break
				else:
					res=op1//op2
			s.append(res)
		else:
			s.append(int(x))
	if err or len(s)!=1:
		print('incorrect')
	else:
		print(s[0])
