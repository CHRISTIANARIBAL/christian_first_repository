print("+, -, x, /")
select = input("select from operation: ")

if select == "+":
    while True:
        try:

            first_num = float(input("First number: "))
        except ValueError:
            print("Sting is not allowed")
            continue

        try:

            second_num = float(input("Second number: "))
        except ValueError:
            print("Sting is not allowed")
            continue

        add = first_num + second_num

        print(first_num, "+", second_num, "=", add)

elif select == "-":
    while True:
        try:

            first_num = float(input("First number: "))
        except ValueError:
            print("Sting is not allowed")
            continue

        try:

            second_num = float(input("Second number: "))
        except ValueError:
            print("Sting is not allowed")
            continue

        add = first_num - second_num

        print(first_num, "-", second_num, "=", add)


elif select == "x":
    while True:
        try:

            first_num = float(input("First number: "))
        except ValueError:
            print("Sting is not allowed")
            continue

        try:

            second_num = float(input("Second number: "))
        except ValueError:
            print("Sting is not allowed")
            continue

        add = first_num * second_num

        print(first_num, "x", second_num, "=", add)


elif select == "/":
    while True:
        try:

            first_num = float(input("First number: "))
        except ValueError:
            print("Sting is not allowed")
            continue

        try:

            second_num = float(input("Second number: "))
        except ValueError:
            print("Sting is not allowed")
            continue

        add = first_num / second_num

        print(first_num, "/", second_num, "=", add)


else:
    print("wrong command")
