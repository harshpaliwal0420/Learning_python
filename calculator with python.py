first_num = int(input("Enter First Number : "))
operation = input("Enter Operation \"+ - * / \" : ")
second_num = int(input("Enter Second Number : "))
if operation == "+":
   print(first_num + second_num)
elif operation == "-":
   print(first_num - second_num)
elif operation == "/":
   print(first_num / second_num)
elif operation == "*":
   print(first_num * second_num)
else: 
   print("Invalid Operation")