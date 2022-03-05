#Taking the input from the user as number of rows and columns required for a 2D array
rows = int(input("Please Enter the number of rows : "))
cols = int(input("Please Enter the number of columns : "))

#A 2-D array is a list of lists

print("Add up elements to the 2D Array : ")
outer_list = []
for row in range(rows):
    inner_list = []
    for col in range(cols):
        value = int(input(f"Enter a value for {row}th row , {col}th column : "))
        inner_list.append(value)
    outer_list.append(inner_list)


def printArray(arrays_list):
    '''
    Function to print the 2D array
    :param arrays_list: The 2D array to be printed
    :return: prints each inner-list within an outer-list one by one
    '''
    for array in arrays_list:
        print(f"{array}")

#calling the above function to print the 2D array
printArray(outer_list)
