input_value = input("enter a value")

try:
    value = int(input_value)
    print(f"the value you enter is int:{value} | Type: {type(value)}")
except ValueError:
    try:
        value = float(input_value)
        print(f"the value you entered in float: {value} | Type : {type(value)}")
    except ValueError:
        print(f"you entered a string !  |type {type(input_value)}")
