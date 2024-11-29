#Understanding Recursion
#Fibonacci sequence

#In this exercise, you will implement the Fibonacci sequence, which is ubiquitous in nature. The sequence looks like this: "0, 1, 1, 2, 3, 5, 8…". You will create a recursive implementation of an algorithm that generates the sequence.

#The first numbers are 0 and 1, and the rest are the sum of the two preceding numbers.

#In the first step, you will code Fibonacci using recursion. In the second step, you will improve it by using dynamic programming, saving the solutions of the subproblems in the cache variable.


def fibonacci(n):
    # Define the base case
    if n <= 1:
        return n
    else:
        # Call recursively to fibonacci
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(6))

for i in range(20):
  print(fibonacci(i))