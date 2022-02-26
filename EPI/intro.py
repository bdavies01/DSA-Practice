def get_h_index(input):
    input.sort()
    print(input)
    l = len(input)
    max_h = 0
    for n in range(len(input)-1, -1, -1):
        if l-n <= input[n]:
            max_h = input[n]
        else:
            break
    return max_h

if __name__ == "__main__":
    test_cases = [
        [1,2,3,4,5],
        [1,4,1,4,2,1,3,5,6]
    ]
    for case in test_cases:
        print(get_h_index(case))