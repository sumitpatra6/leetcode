import math
def one_distance_away(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    shorter = s1 if len(s1) < len(s2) else s2
    longer = s1 if len(s1) > len(s2) else s2
    index_long = 0 
    index_short = 0
    found_difference = False
    while index_long < len(longer) and index_short  < len(shorter):
        if longer[index_long] != shorter[index_short]:
            if found_difference:
                return False
            found_difference = True
            if index_long == index_long:
                index_short += 1
        else:
            index_short += 1
        index_long += 1
    return True

print(one_distance_away('pale', 'ple'))
