import sys
def DFS(num,keys, values, trys):
    global nums
    global result
    global N
    if trys >= N:
        return
    keys.append(num)
    values.append(nums[num])
    print(keys,nums)
    if set(keys) == set(values):
        result+=values
        print("OUT!", result)
        return
    else:
        trys+=1
        DFS(nums[num],keys,values, trys)


N = int(sys.stdin.readline())
nums = [0]
for _ in range(N):
    nums.append(int(sys.stdin.readline()))
result = []
done = [True for _ in range(N)]
for i in range(1,N+1):
    if i not in result:
        DFS(i,[],[],0)
LEN = len(set(result))
result = list(set(result))
result.sort()
print()
print(LEN)
for i in result:
    print(i)
