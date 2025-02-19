import random
class dice:
	def roll(self):
		first=random.randint(1,6)
		second=random.randint(1,6)
		return first,second


now= dice()
print(now.roll())	