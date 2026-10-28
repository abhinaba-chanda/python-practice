"""Body mass index calculator."""


def bmi(weight_kg, height_m):
    if height_m <= 0:
        raise ValueError("height must be positive")
    return round(weight_kg / (height_m ** 2), 1)


def category(value):
    if value < 18.5:
        return "Underweight"
    if value < 25:
        return "Normal"
    if value < 30:
        return "Overweight"
    return "Obese"


if __name__ == "__main__":
    w = float(input("Weight (kg): "))
    h = float(input("Height (m): "))
    b = bmi(w, h)
    print(f"BMI {b} - {category(b)}")
