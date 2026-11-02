def calculator():
    print("\ncalculator(+-*/q)")##\n for the spacing and next line moving
    while True:
        op=input("operator:").strip()##strip for removing uselessspacing
        if op=="q":
            print("bye")
            break
        if op not in "+-*/" or op=="":##if the op we select not in it
            print("unkownoperator")##print unknown and stops the program here itself
            continue
        a=float(input("first num"))##when the operator is present among them the program continue
        b=float(input("second num"))
        if op=="+":
            result=a+b
        elif op=="-":
            result=a-b
        elif op=="*":
            result=a*b
        else:
            if b==0:
                print("invalid")
                continue
            result=a/b
        print(f"{a}{op}{b}={result}")##indendation important
calculator()

