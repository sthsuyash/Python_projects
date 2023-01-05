import sys
smallest = sys.maxsize
output = []

if __name__ == '__main__':
    n = int(input())
    all = []

    for _ in range(n):
        name = input()
        score = float(input())
        all.append([name, score])

    for one in all:
        if smallest > one[1]:
            second_smallest = smallest
            smallest = one[1]

        elif second_smallest > one[1] and one[1] != smallest:
            second_smallest = one[1]

    for one in all:
        if one[1] == second_smallest:
            output.append(one[0])

    output.sort()
    for one in output:
        print(one)

