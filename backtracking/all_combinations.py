def all_combinations(tiles):
    all_results = set()
    def util(string, current, start, end):
        # print(current)
        if len(current) > 0:
            all_results.add(''.join(current[:]))
        if start >= end:
            return 
        for i in range(len(string)):
            string[0], string[i] = string[i], string[0]
            current.append(string[0])
            util(string[1:], current, 1, end)
            current.pop(-1)
            string[i], string[0] = string[0], string[i]
    util(list(tiles), [], 0, len(tiles))
    print(all_results)
    print(len(all_results))

tiles = 'AAABBC'
print(all_combinations(tiles))