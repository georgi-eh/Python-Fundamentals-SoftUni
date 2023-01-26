def data_types(data_type, input):
    if data_type == "int":
        result = int(input) * 2
        print(result)
    elif data_type == "real":
        result = float(input) * 1.5
        print(f"{result:.2f}")
    elif data_type == "string":
        result = "$" + input + "$"
        print(result)

data_type = input()
input = input()

data_types(data_type, input)
