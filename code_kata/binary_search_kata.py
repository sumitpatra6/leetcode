def recursive_binary_search(item, array):
    pass
def regular_binary_search(item, array):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = int((low+high) / 2)
        print(low, mid, high)
        current_item = array[mid]
        if current_item == item:
            print(mid)
            return mid
        elif item < current_item:
            high = mid
        else:
            low = mid
    print(-1)
    return -1

def test_chop():
    chop = regular_binary_search
    assert -1 == chop(3, [])
    assert -1 == chop(3, [1])
    assert 0 ==  chop(1, [1])
    #
    assert 0 ==  chop(1, [1, 3, 5])
    assert 1 ==  chop(3, [1, 3, 5])
    assert 2 ==  chop(5, [1, 3, 5])
    assert -1 == chop(0, [1, 3, 5])
    assert -1 == chop(2, [1, 3, 5])
    assert -1 == chop(4, [1, 3, 5])
    assert -1 == chop(6, [1, 3, 5])
     #
    assert 0 ==  chop(1, [1, 3, 5, 7])
    assert 1 ==  chop(3, [1, 3, 5, 7])
    assert 2 ==  chop(5, [1, 3, 5, 7])
    assert 3 ==  chop(7, [1, 3, 5, 7])
    assert -1 == chop(0, [1, 3, 5, 7])
    assert -1 == chop(2, [1, 3, 5, 7])
    assert -1 == chop(4, [1, 3, 5, 7])
    assert -1 == chop(6, [1, 3, 5, 7])
    assert -1 == chop(8, [1, 3, 5, 7])


test_chop()