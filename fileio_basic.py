my_list = [i**2 for i in range(1,11)]

my_file = open("output.txt", "r+")

for item in my_list:
    my_file.write(str(item))
    my_file.write("\n")
my_file.close()