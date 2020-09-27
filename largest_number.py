from functools import cmp_to_key
def sort_numbers(num1, num2):
    print(num1, num2)
    num1 = str(num1)
    num2 = str(num2)
    smaller = num1 if len(num1) <= len(num2) else num2
    bigger = num1 if len(num1) > len(num2) else num2
    for i in range(len(smaller)):
        if int(smaller[i])<= int(bigger[i]):
            if smaller == num1:
                return -1
            else:
                return 1
    if smaller == -1:
        return -1
    else:
        return 1
        

def largest_number(nums):
    nums = sorted(nums, key=cmp_to_key(sort_numbers))
    print(nums)
    return ''.join(map(str,nums))

array = [2, 1,3]
print(largest_number(array))