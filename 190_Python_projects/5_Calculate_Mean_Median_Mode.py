# Mean, Median and Mode are the fundamentals of statistics
# used in almost every domain where we deal with numbers.

# Mean
"""
 The mean is the average value of all the values in a dataset.
 To calculate the mean value of a dataset, we first need to find the sum of all the values
 and then divide the sum of all the values by the total number of values.
"""

list = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    list.append(int(input(f"Enter element {i+1}: ")))
print(f"The list is: {list}\n")

mean = sum(list) / len(list)
print(f"Mean: {round(mean, 2)}")

# Median
"""
 The median is the middle value of a dataset.
 To calculate the median value of a dataset, we first need to sort the dataset in ascending order.
 If the dataset has an odd number of values, the median is the middle value.
 If the dataset has an even number of values, the median is the average of the two middle values.

 There are two different ways of calculating the median value:
    -> when the total number of values is even: Median  = [(n/2)th term + {(n/2)+1}th]/2
    -> when the total number of values is odd: Median = {(n+1)/2}thterm
"""

list.sort()  # sort the list in ascending order
print(f"\nSorted list: {list}")

if len(list) % 2 == 0:  # when the total number of values is even
    median1 = list[len(list) // 2]  # n/2th term
    median2 = list[len(list) // 2 - 1]  # (n/2)+1th term
    median = (median1 + median2) / 2  # median = [(n/2)th term + {(n/2)+1}th]/2
else:  # when the total number of values is odd
    median = list[len(list) // 2]  # median = {(n+1)/2}thterm
print(f"Median: {round(median,2)}")  # print the median value

# Mode
"""
Mode is the most frequently occurring value among all the values.
"""
frequency = {}  # create an empty dictionary
for item in list:  # iterate through the list
    frequency.setdefault(item, 0)  # set the default value of the key to 0
    # increment the value of the key by 1
    frequency[item] = frequency[item] + 1

frequent = max(frequency.values())  # find the maximum value in the dictionary
for i, j in frequency.items():  # iterate through the dictionary
    if j == frequent:  # check if the value is equal to the maximum value
        mode = i  # assign the key to the variable mode

print(f"\nMode: {mode}")  # print the mode value
