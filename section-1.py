'''Sections 1: How to Debug Python'''
'''
The following code has errors in it so that it doesn't run correctly.
Use the the resulting Python exceptions and the debugger to find the bugs and fix them.
'''
if __name__ == '__main__':
    int_variable = input("Enter a number: ") # This returns a string

    list_of_numbers = [4, 5, 6, 7, 8, 9, 10, int_variable]

    for i in range(0, len(list_of_numbers) + 1):
        list_of_numbers[i] = 2*list_of_numbers[i]
    
    print("List of numbers: " + list_of_numbers) 