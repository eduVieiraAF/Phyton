def calculate_bmr(weight, height, age, sex):
    if sex.lower() == "male":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height * 100) - (5.677 * age)
    elif sex.lower() == "female":
        bmr = 447.593 + (9.247 * weight) + (3.098 * height * 100) - (4.330 * age)
    else:
        raise ValueError("Invalid sex provided. Please enter 'male' or 'female'.")
    return bmr

# Example usage
weight = 76.8  # in kilograms
height = 1.66  # in meters
age = 40  # in years
sex = "male"

bmr = calculate_bmr(weight, height, age, sex)
print("Your Basal Metabolic Rate (BMR) is:", bmr)
