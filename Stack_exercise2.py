#In this exercise, you will work with Python's LifoQueue().
#You will create a stack called my_book_stack to add books and remove them from it.

# Import the module to work with Python's LifoQueue
import queue

# Create an infinite LifoQueue (LIFO stack)
my_book_stack = queue.LifoQueue(maxsize=0)

# Add an element to the stack
my_book_stack.put("Don Quixote")

# Remove an element from the stack and capture the result
removed_book = my_book_stack.get()

# Print the removed book
print(removed_book)
