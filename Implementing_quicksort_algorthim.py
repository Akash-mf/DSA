#Implementing the quicksort algorithm
#In this exercise, you will implement the quicksort algorithm to sort a list of numbers.

#In the first step, you will implement the partition() function, which returns the index of the pivot after having processed the list of numbers so that all the elements that are to the left of the pivot are less than the pivot and all the elements that are to the right of the pivot are greater than the pivot.

#In the second step, you will implement the quicksort() function, which will call the partition() function.


def partition(my_list, first_index, last_index):
    pivot = my_list[first_index]
    left_pointer = first_index + 1
    right_pointer = last_index

    while True:
        while pivot < my_list[left_pointer] and last_index < left_pointer:
            left_pointer += 1

        while my_list[right_pointer] > pivot and right_pointer >= first_index:
            right_pointer -= 1
        if left_pointer >= right_pointer:
            break
        my_list[left_pointer], my_list[right_pointer] = my_list[right_pointer], my_list[left_pointer]

    my_list[first_index], my_list[right_pointer] = my_list[right_pointer], my_list[first_index]
    return right_pointer


def quicksort(my_list, first_index, last_index):
    if first_index < last_index:
        # Call the partition() function with the appropriate parameters
        partition_index = partition(my_list, first_index, last_index)
        # Call quicksort() on the elements to the left of the partition
        quicksort(my_list, first_index, partition_index)
        quicksort(my_list, partition_index + 1, last_index)


my_list = [6, 2, 9, 7]
quicksort(my_list, 0, len(my_list) - 1)
print(my_list)
