def pow(x, n):
    if int(n) == 0:
        return 1
    temp = pow(x, n/2)
    if n % 2 ==0:
        return temp* temp
    else:
        return x * temp*temp

print(pow(2, 1))