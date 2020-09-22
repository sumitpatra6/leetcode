import time

n = 10

# iterative version
start = time.time()
c = [0] * n
c[0] = 1
for i in range(1,n):
    sum = 0
    for j in range(0, i):
        print(c[i] ,c[i-j])
        sum += c[j]*c[i-j]
    print(sum)
    c[i] = sum
print(c)
end = time.time()
print("time taken = {}".format(end-start))
# recursive version
