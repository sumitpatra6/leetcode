a = 29
b = 15
print("a = {}".format(bin(a)))
print("b = {}".format(bin(b)))
c  = a ^ b
print("c = {}".format(bin(c)))

count = 0
# now count th number of 1s in the binary representation
while c!= 0:
    print(c)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    count += 1
    c = c&(c-1)
print(count)