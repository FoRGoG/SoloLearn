# try:
#     num1 = 7
#     num2 = 0
#     print (num1 / num2)
#     print("Done calculation")
# except ZeroDivisionError:
#     print("An error occurred")
#     print("due to zero division")

# try:
# #     variable = 10
# #     print(variable + "hello")
# #     print(variable / 2)
# # except ZeroDivisionError:
# #     print("Divided by zero")
# # except (ValueError, TypeError):
# #     print("Error occurred")

# try:
#     word = 'spam'
#     print(word / 0)
# except:
#     print('An error occurred')

"""Cash Out

An ATM machine takes the amount to be withdrawn as input and calls the corresponding withdrawal method.
In case the input is not a number, the machine should output "Please enter a number".
Use exception handling to take a number as input,
call the withdraw() method with the input as its argument,
and output "Please enter a number", in case the input is not a number."""

def withdraw(amount):
    return(str(amount) + ' withdrawn!')


try:
    amount = int(input())
    print(withdraw(amount))
except ValueError:
    print('Please enter a number')