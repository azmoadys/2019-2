def sum_digit(num):
	digit = 0
	for i in range(len(num)):
		digit = digit+int(num[i])
	return digit

num = input()
digit = sum_digit(num)

while digit%4 != 0:
	num = int(num)+1
	digit = sum_digit(str(num))
print(num)
