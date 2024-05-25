def binary_to_decimal(binary):
    try:
        decimal_value = 0
        for digit in binary:
            if digit != '0' and digit != '1':
                raise ValueError("Invalid binary string. Only '0' and '1' characters allowed.")
            decimal_value = decimal_value * 2 + int(digit)
        return decimal_value
    except ValueError as err:
        print("Error: {}".format(err))
        return None

binary_number = input("Enter a binary number: ")
decimal_equivalent = binary_to_decimal(binary_number)

if decimal_equivalent is not None:
    print("The decimal equivalent of {} is {}".format(binary_number, decimal_equivalent))
