#In this exercise, you will work with Python's SimpleQueue().
# You will create a queue called my_orders_queue to add the orders of a restaurant and remove them
# from it when required.

import queue

# Create the queue
my_orders_queue = queue.SimpleQueue()

# Add an element to the queue
my_orders_queue.put("samosas")

# Remove an element from the queue and print it
order = my_orders_queue.get()
print(order)  # Output: samosas
