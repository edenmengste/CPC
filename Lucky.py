def check():
	s = input()
	x = int(s[0]) + int(s[1]) + int(s[2])
	y = int(s[3]) + int(s[4]) + int(s[5])
	if x == y :
		print("YES")
	else:
		print("NO")


t = int(input())		
for _ in range(t):
	check()