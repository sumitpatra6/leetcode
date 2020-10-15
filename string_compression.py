input_string = 'aabcccccaaa'
def compress_string(inpput_string):
    output_str = ""
    arr = []
    if len(input_string) == 1:
        print(input_string)
        return
    start = input_string[0]
    count = 1
    for i in range(1, len(input_string)):
        if start != input_string[i]  or i+1 >= len(input_string):
            arr.append(start + str(count))
            start = input_string[i]
            count = 1
        else:
            count += 1
    print(''.join(arr))
compress_string(input_string)
