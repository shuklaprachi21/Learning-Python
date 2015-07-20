#for-loop iterates over start_list and appends the respective squares to square_list.
#sqaure_list should be sorted
 
start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for number in start_list:
    square_list.append(number ** 2)
square_list.sort()
print square_list