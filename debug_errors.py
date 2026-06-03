def calculate_average(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    try:
        return total / len(numbers)
    except ZeroDivisionError:
        print(f"Zero division error has occured, an empty list has been passed as an argument.\nERROR: {ZeroDivisionError}")

data1 = [10, 20, 30, 40, 50]
data2 = [5, 15]
data3 = [] # This will cause an error
print(f"Average of data1: {calculate_average(data1)}")
print(f"Average of data2: {calculate_average(data2)}")
print(f"Average of data3: {calculate_average(data3)}")
print("\n")
#line 1: numbers argument is initialized as an empty list
#line 2: total is initialized to 0
#line 3: for loop is skipped because the list is empty
#line 6: an exception gets thrown, ZeroDivisionError, because len(numbers) is 0
#
#Exception has occurred: ZeroDivisionError
#division by zero
#  File "C:\Users\OIP\Desktop\dev_assessment\debug_errors.py", line 7, in calculate_average
#    return total / len(numbers)
#           ~~~~~~^~~~~~~~~~~~~~
#  File "C:\Users\OIP\Desktop\dev_assessment\debug_errors.py", line 14, in <module>
#    print(f"Average of data3: {calculate_average(data3)}")
#                               ^^^^^^^^^^^^^^^^^^^^^^^^
#ZeroDivisionError: division by zero

def get_list_element(my_list, index):
    try:
        return my_list[index]
    except IndexError:
        print(f"ERROR: Index passed is out of bounds, the number of elements is {len(my_list)}, but index {index} was requested\nERROR: {IndexError}")
        return None
    except TypeError:
        print(f"ERROR: Argument passed is not a list.\nERROR: {TypeError}")
        return None
    
list = [1,2,3]
print(get_list_element(list,2))
print(get_list_element(list,10))
print(get_list_element(150,10))