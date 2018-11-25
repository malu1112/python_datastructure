a = [5, 7, 234, 4, 7, 8]

for index, value in enumerate(a):
	for i, v in enumerate(a):
		if index > i:
			s = value + v
			if s == 12:
				print(i, index)
