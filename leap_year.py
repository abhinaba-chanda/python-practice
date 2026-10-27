# Leap year checker
# A year is a leap year if it divides by 4, except century years,
# which must also divide by 400 (so 2000 is a leap year, 1900 is not).
# Practice: conditions, boolean logic, modulo.


def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def leap_years_between(start, end):
    """All leap years from start to end, both included."""
    return [y for y in range(start, end + 1) if is_leap(y)]


if __name__ == "__main__":
    year = int(input("Enter a year: "))
    print(f"{year} is {'a leap year' if is_leap(year) else 'not a leap year'}")
