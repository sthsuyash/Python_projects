# main program
if __name__ == '__main__':

    # input number of commands to be executed
    N = int(input(f"Enter number of commands: "))

    # create empty list
    lst = []

    # loop through total number of commands
    for i in range(N):
        # input one command at a time
        inp = input()

        # split the command into command and data

        # split the first word from the rest of the string as command
        command = inp.split(" ")[0]
        # split the rest of the string as data
        data = inp.partition(" ")[2]
        # split the data into list of data
        data = data.split(" ")

        # print(data)

        # check the command and execute the command

        if command == "insert":
            # if command is insert, insert the data at the specified index
            # insert(index, value) # int() as the data are as string
            lst.insert(int(data[0]), int(data[1]))

        elif command == "print":
            # print the list
            print(lst)

        elif command == "remove":
            # remove the data from the list
            lst.remove(int(data[0]))

        elif command == "append":
            # append the data to the list
            lst.append(int(data[0]))  # int() as the data are as string

        elif command == "sort":
            # sort the list
            lst.sort()

        elif command == "pop":
            # pop the last element from the list
            lst.pop()

        elif command == "reverse":
            # reverse the list
            lst.reverse()

        else:
            # if command is invalid
            print("Invalid command")
