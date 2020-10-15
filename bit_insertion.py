n = 1024
m = 19
i = 2
j = 6
print(bin(n))
print(bin(m))
# first bit cleaning significant bit through j
# and i through 0
left = ~0 << (j+1)
print("Left {}".format(bin(left)))
right = (1 << i) -1
mask = left | right
print("Mask {}".format(bin(mask)))
n_cleared = n & mask
print(bin(n_cleared))
m_rotated = m << i
answer = n_cleared | m_rotated
print(bin(answer))