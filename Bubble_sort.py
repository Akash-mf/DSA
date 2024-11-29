#Bubble sort
#Correcting a bug in the bubble sort algorithm

#You have been given a program that sorts a list of numbers using the bubble sort algorithm.
# While testing it, you realize that the code is not correct. Could you correct the algorithm so that it works correctly?


def bubble_sort(my_list):
  list_length = len(my_list)
  # Correct the mistake
  is_sorted = False
  while not is_sorted:
    is_sorted = True
    for i in range(list_length-1):
      # Correct the mistake
      if my_list[i] > my_list[i+1]:
        my_list[i] , my_list[i+1] = my_list[i+1] , my_list[i]
        is_sorted = False
    # Correct the mistake
    list_length -= 1
  return my_list

print(bubble_sort([5, 7, 9, 1, 4, 2]))