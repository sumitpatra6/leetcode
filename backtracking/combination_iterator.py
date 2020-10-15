def all_combinations(string, length):
    print(string)
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            end = j + length - 1
            if end <= len(string):
                print(string[i] + '' + string[j:end])

all_combinations('abcd', 3)