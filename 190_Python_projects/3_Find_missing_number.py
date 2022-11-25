# Find Missing Number using Python
# Finding the missing number in an array means finding the numbers missing from the array according to the range of values inside the array.
# Most of the time, the question you get based on this problem is like:
# # Given an array containing a range of numbers from 0 to n with a missing number, find the missing number in the input array.
# To find the missing number in an array, we need to iterate over the input array and store the numbers in another array that we didn’t find in the input array while iterating over it.

def findMissingNumber(arr):
    numbers = set(arr)
    length = arr[-1]+1
    output = []

    j = 0
    for i in range(1, length):
        if i not in numbers:
            output.append(i)
            arr.insert(j, i)
        j += 1
    return output


listOfNumbers = [1, 2, 3, 5, 6, 8, 9, 12, 14, 15, 15, 20]
print(f"\nMissing Numbers:\n{findMissingNumber(listOfNumbers)}")
print(f"\nList of Numbers:\n{listOfNumbers}")
