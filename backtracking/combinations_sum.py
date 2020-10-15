numbers = [1,2,3,4,5,6,7,8,9]

def combination_sum(k, n):
    find_combinations([],0, k, n)

def find_combinations(path, start, max_length, target):
    if sum(path) == target:
        if len(path) == max_length:
            print(path)
        return
    if sum(path) > target or len(path) > max_length:
        return
    for i in range(start, len(numbers)):
        if numbers[i] in path:
            continue
        path.append(numbers[i])
        find_combinations(path,i, max_length, target)
        path.pop(-1)
combination_sum(3, 7)
