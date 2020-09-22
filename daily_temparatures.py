def dailyTemperatures(T):
    if len(T) == 1:
        return [1]
    memory = []
    result = [0]*len(T)
    for i in range(len(T)):
        current_temp = T[i]
        while len(memory) > 0 and memory[-1][0] < current_temp:
            r = memory.pop()
            result[r[1]] = i - r[1]
        memory.append([current_temp, i])
    print(result)
    return result



T = [73, 74, 75, 71, 69, 72, 76, 73]
dailyTemperatures(T)