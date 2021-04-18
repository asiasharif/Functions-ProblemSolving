# #functions
# def say_hello(name):
#     print(f'Hello {name}')
#     say_hello()
#
#
# def myfunc(a,b):
#     print(a + b)
#     return a+b
# result = myfunc(10,20)
#
# #functions with login:
# def even_check(number):
#     return number % 2 == 0
# even_check(21)
#
# #return true f any number in list is true
# def check_even_list(num_list):
#     for number in num_list:
#         if number & 2 == 0:
#             return True
#         else:
#             pass #pass means dont do anything
# check_even_list([1,3,5])
# check_even_list([2,4,6])
#
# #tuples and packing
# stock_prices = [('Appl' , 200), ('GOOG', 300), ('MICRO', 400)]
# for item in stock_prices:
#     print(item)
# for ticker,price in stock_prices:
#     print(price+(0.1*price)) #tuple unpacking

    #can use a function to return things as tuples and unpack it

work_hours = [('Asia', 100), ('Faye', 200), ('Jamal', 300)]
#wanna return the employee who has worked the most hours
def employee_check(work_hours):
    current_max = 0 #start at zero  then compare each employee hours
    #have to do for loop and tuple unpacking
    for employee, hours in work_hours:
        if hours > current_max: # if so reset hours
            current_max = hours
            employee_of_month = employee
        else:
            pass
    employee_of_month = ''
    return (employee_of_month, current_max)
employee_check(work_hours)




