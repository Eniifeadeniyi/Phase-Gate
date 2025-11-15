sum = 0
for count in range(1,11):
	if count % 4 == 0:
		for counter in range(1,6):
			sum += count ** counter
print(sum ** 2, end = "")