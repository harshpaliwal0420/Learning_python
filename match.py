x = int(input("Enter the value of x : "))

match x:
  case 0:
    print("x is 0")
  case 90:
    print("x is 90")
  case _:
    print("x is not 0, 90")