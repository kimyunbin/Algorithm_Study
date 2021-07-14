import sys
sys.stdin = open("input.txt")

N = int(input())
dic = {}

def memo(n):
	a = 1
	while n >= a:
		if a == 1:
			dic[1] = 0
		else:
			keys = []
			if (a/3) in dic:
				keys.append(dic[a/3])
			if (a / 2) in dic:
				keys.append(dic[a/2])
			if (a-1) in dic:
				keys.append(dic[a-1])
			dic[a] = min(keys)+1
		a += 1
	return dic

memo(N)
print(dic[N])