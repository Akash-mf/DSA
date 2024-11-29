#Towers of Hanoi

#In this exercise, you will implement the Towers of Hanoi puzzle with a recursive algorithm.
# The aim of this game is to transfer all the disks from one of the three rods to another,
# following these rules:

#You can only move one disk at a time.
# You can only take the upper disk from one of the stacks and place it on top of another stack.
# You cannot put a larger disk on top of a smaller one. Picture of the game Tower of Hanoi

#The algorithm shown is an implementation of this game with four disks and three rods called 'A', 'B' and 'C'.
# The code contains two mistakes.
# In fact, if you execute it, it crashes the console because it exceeds the maximum recursion depth.
# Can you find the bugs and fix them?.


def hanoi(num_disks, from_rod, to_rod, aux_rod):
  # Correct the base case
  if num_disks >= 1:
    # Correct the calls to the hanoi function
    hanoi(num_disks - 1, from_rod, aux_rod, to_rod)
    print("Moving disk", num_disks, "from rod", from_rod,"to rod",to_rod)
    hanoi(num_disks - 1, aux_rod, to_rod, from_rod)

num_disks = 4
source_rod = 'A'
auxiliar_rod = 'B'
target_rod = 'C'

hanoi(num_disks, source_rod, target_rod, auxiliar_rod)