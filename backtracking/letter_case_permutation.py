def letter_case_permutation(S):
    final_result = set()
    def util(string, start, end):
        if start == end:
            final_result.add(''.join(string[:]))
            return
        if string[start].isdigit():
            util(string, start+1, end)
        else:
            string[start] = string[start].upper()
            util(string, start+1, end)
            string[start] = string[start].lower()
            util(string, start + 1, end)
    util(list(S), 0, len(S))
    print(final_result)
    return list(final_result)

letter_case_permutation('a1b2')