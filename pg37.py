n=list(input())
for i in range(len(n)):
	t=n.copy()
	t.pop(i)
	if "".join(t)=="".join(t[::-1]):
		print("YES")
		break
else:
	print("NO")
