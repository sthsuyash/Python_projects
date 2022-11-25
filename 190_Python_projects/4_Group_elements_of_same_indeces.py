# Group Elements of Same Indices using Python

# Grouping elements of the same indices means grouping elements
# of two or more data structures according to their indices.

# To group elements of the same index,
# you will initially have two or more lists inside a list like [[a, b], [c, d]].
# To group the elements of these lists, you need to create two new lists
# where you will store the elements of both the lists at index 0 [a, c] and index 1 [b, d].
# That is the meaning of grouping the elements of the same indices.

inputLists = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]  # list to store inputs
outputLists = []  # list to store outputs

# loop through the input lists
for i in range(len(inputLists[0])):
    # create a list to store the elements of the same index
    temp = []
    for j in range(len(inputLists)):
        temp.append(inputLists[j][i])
    outputLists.append(temp)

# a, b, c = outputLists[0], outputLists[1], outputLists[2] # assign the output lists to variables
# print(a, b, c) # print the grouped elements

# loop through the output lists and print the grouped elements
for i in range(len(outputLists[0])):
    print(outputLists[0][i], outputLists[1][i], outputLists[2][i])
