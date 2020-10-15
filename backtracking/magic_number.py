def superDigit(n, k):
    print(n)
    n = str(n)*k
    def util(n):
        # print(n)
        if len(n) == 1:
            return n
        add = 0
        for i in n:
            add += int(i)
        return util(str(add))
    return util(n)
fp = open('test_file.txt', 'r')
lines = fp.readlines()
line = lines[0].strip()
n = line.split(' ')[0]
k = int(line.split(' ')[1])
print(superDigit(n, k))
