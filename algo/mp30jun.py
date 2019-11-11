import sys
def sol(data, prev, result):
    LEN = len(data)
    if LEN == 1:
        prev+=data
        result.append(prev)
        prev = prev[:-1]
    else:
        for char in data:
            prev+=char
            sol(data.replace(char, ""),prev,result)
            prev = prev[:-1]

if __name__ == "__main__":
    result = []
    sol("ABC","", result)
    for one in result:
        sys.stdout.write(one)
        sys.stdout.write(" ")
