q = int(input())
for i in range(q):
	count = 0
	num = int(input())
	candy = list(map(int, input().split()))
	mylist = [0]*(max(candy)+1)
	for i in range(1, max(candy)+1):
#		print('this is :', i)
		mylist[i] = candy.count(i)
	new_list = sorted(mylist,reverse = True)
	sum_candy = max(mylist)
	temp = max(mylist)
	for i in range(1, len(mylist)):
		if temp <= 0:
			break
		if new_list[i] == 0:
			continue
		elif new_list[i]>=temp:
			sum_candy = sum_candy+temp -1
			temp = temp -1
		else:
			sum_candy = sum_candy + new_list[i]
			temp = new_list[i]

	print(sum_candy)
			
