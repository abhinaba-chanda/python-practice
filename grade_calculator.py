# Grade calculator
# Takes marks out of 100, works out the average and gives a grade.
# Practice: lists, input validation, if/elif chains.


def grade(mark):
    """Turn a mark (0-100) into a letter grade."""
    if not 0 <= mark <= 100:
        raise ValueError("Mark must be between 0 and 100")
    if mark >= 90:
        return "A+"
    if mark >= 80:
        return "A"
    if mark >= 70:
        return "B"
    if mark >= 60:
        return "C"
    if mark >= 50:
        return "D"
    return "F"


def average(marks):
    if not marks:
        raise ValueError("Need at least one mark")
    return round(sum(marks) / len(marks), 2)


if __name__ == "__main__":
    marks = [float(m) for m in input("Enter marks separated by spaces: ").split()]
    avg = average(marks)
    print(f"Average: {avg}  Grade: {grade(avg)}")
