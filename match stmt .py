day=int(input("enter the number"))##week days
match day:
    case 1:
     print("monday")
    case 2:
      print("tuesday")
    case _:
     print("invalid")

color=input("colour")##traffic signal
match color :
    case 1 :
      print("stop")
    case 2:
      print("wait")
    case 3:
      print("go")
    case _:
      print("invalid")

a=int(input("num"))##using operators
b=int(input("num"))
op=input("enter operator(+,-,*,/):")
match op:
   case "+":
       print(a+b)
   case "-":
       print(a-b)
   case "*":
       print(a*b)
   case "/" :
      print(a/b)
   case _:
      print("invalid")

a=input("enter letter")##using multiple options
match a :
   case "a"|"e"|"i"|"o"|"u ":
      print("vowels")
   case _:
      print("invalid")

item=input("selected item")##selection of item from the menu
match item:
     case "tea":
        print("tea")
     case "coffee":
        print("coffee")
     case _:
        print("none")