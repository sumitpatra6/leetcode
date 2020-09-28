from functools import cmp_to_key
def compare(num1, num2):
    # if numb1 is smaller then return -1 else return +1
    return num1 + num2 > num2 + num1

class LargerNumber(str):
    def __lt__(x, y):
        return x +y > y+x

def largest_number(nums):
    nums = sorted(map(str, nums), key=LargerNumber)
    print(nums)
    return ''.join(map(str,nums))

array = [2, 1,3]
print(largest_number(array))
# print(compare(910, 999))