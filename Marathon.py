def check():
	counter = 0
	a,b,c,d = map(int, input().split())
	if b>a: 
		counter += 1
	if c>a:
		counter += 1
	if d>a:	
		counter += 1
	print(counter)	


t=int(input())
for _ in range(t):
	check()