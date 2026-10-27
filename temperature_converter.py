# Temperature converter
# Converts between Celsius and Fahrenheit.
# Practice: functions, float maths, rounding, user input.


def c_to_f(celsius):
    """Celsius -> Fahrenheit."""
    return round(celsius * 9 / 5 + 32, 2)


def f_to_c(fahrenheit):
    """Fahrenheit -> Celsius."""
    return round((fahrenheit - 32) * 5 / 9, 2)


if __name__ == "__main__":
    choice = input("Convert (1) C to F or (2) F to C? ")
    value = float(input("Temperature: "))
    if choice == "1":
        print(f"{value} C = {c_to_f(value)} F")
    else:
        print(f"{value} F = {f_to_c(value)} C")
