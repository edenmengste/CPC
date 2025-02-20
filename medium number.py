def compare():
	a,b,c = map(int, input().split())
	nums=sorted([a,b,c])
	print(nums[1])


t=int(input())
for _ in range(t):
	compare()	