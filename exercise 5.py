#Exercise 5: Check if the first and last number of a list is the same
#Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

def checking(number_list):
    
    first_number = number_list[0]
    last_number = number_list[4]

    if first_number - last_number == 0:
        return True
    else:
        return False

first_list = [10, 20, 30, 40, 10]
print(first_list,"The result is", checking(first_list))
second_list = [75, 65, 35, 75, 30]
print(second_list,"The result is", checking(second_list))

