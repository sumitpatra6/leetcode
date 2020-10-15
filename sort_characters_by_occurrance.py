def sort(s1):
    register = {}
    for c in s1:
        if c not in register:
            register[c] = 1
        else:
            register[c] += 1
    print(register)
    register = {k:v for k,v in sorted(register.items(), key=lambda item:item[1], reverse=True)}
    print(register)
    result = ''
    for k, v in register.items():
        print(k,v)
        result += k*v
    print(result)

# sort('tree')
def longest_substring_non_repeating_character(s):
    # res = 0
    # for i in range(len(s)):
    #     visited = []
    #     for j in range(i, len(s)):
    #         if s[j] in visited:
    #             break
    #         else:
    #             res = max(res, j - i + 1)
    #             visited.append(s[j])

    # return res
    visited = [-1]*256
    i = 0
    res = 0
    for j in range(len(s)):
        i = max(i, visited[ord(s[j])] + 1)
        res = max(res, j - i + 1)
        visited[ord(s[j])] = j
    return res


def shift_array(array):
    i = 0
    n = len(array)
    total_shifts = 0
    while i < n:
        j = i + 1
        while j < n and array[j] == array[i]:
            j += 1
        shift = j - i - 1
        total_shifts += shift
        while j < n:
            array[j-shift] = array[j]
            j += 1
        n = n - shift
        i += 1
    print(total_shifts)
    for i in range(total_shifts):
        array.pop(-1)
    print(array)
    return array

def shift_array_only_count(nums):
    i = 0
    n = len(nums)
    count = 0
    while i < n:
        count += 1
        j = i + 1
        while j < n and nums[j] == nums[i]:
            j += 1
        i = j
    print(count)
    return count

array = [0,0,1,1,1,2,2,3,3,4]
shift_array_only_count(array)            
# print(longest_substring_non_repeating_character("qrsvbspk"))