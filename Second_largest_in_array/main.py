import sys
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    largest = -sys.maxsize - 1
    second_largest = -sys.maxsize - 1

    for i in arr:
        if largest < i:
            second_largest = largest
            largest = i

        elif second_largest < i and i != largest:
            second_largest = i

    print(second_largest)
