# The execution or running time of the program indicates how quickly the output is delivered 
# based on the algorithm you used to solve the problem. 
# To calculate the execution time of the program,
# we need to calculate the time taken by the program from its initiation 
# to the final result.

# Execution Time of a Python Program
'''
It is important to calculate the execution time when working on a large project. 
When working on a large project, we have several approaches in mind. 
The best should be the one that takes the shortest execution time in all scenarios.

So to calculate the execution time of a Python program, we need to follow the steps mentioned below:

- First, store the time of initiation of the program into a variable;
- Write the Python program;
- Store the end time of the program into a variable;
- Subtract the time of initiation of the program from the end time of the program;
- In the end, you will get the execution time of your program in seconds.
'''

from time import time # import time module
start = time() # varialbe to store the time of initiation of the program

# Write your program here

# Python program to create acronyms
word = "Artificial Intelligence"
text = word.split()
a = " "
for i in text:
    a = a+str(i[0]).upper()
print(a)

end = time() # variable to store the end time of the program
execution_time = end - start # execution time of the program
print(execution_time) # print the execution time of the program
