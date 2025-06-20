# Error Handling
# try: #implement the main logic here
#     result = 5/0
#     print(result)
# except ZeroDivisionError as e:
#     print(e ,"is the error")
    
# try:
#     result = 0/15
#     print(result)

# except ZeroDivisionError as e:
#     print(e ,"is the error")

# try:
#     num = int(input("Enter a Number: "))
#     print(num)
    
# except (ValueError, TypeError) as e:
#     print("Error contains ", e)


try:
    num1 = int(input("Enter the odd number: "))
    if num1%2 == 0:
        print("Number is even")
    else:
        print("Number is odd")
except ValueError as e:
    print("Error contains ", e)
    
else:
    print("Some other error occured")
    
finally:
    print("Finally is executed")