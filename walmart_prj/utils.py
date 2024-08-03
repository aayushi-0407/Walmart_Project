# utils.py

def calculate_bmi(height, weight):
    """Calculate BMI from height (in meters) and weight (in kilograms)."""
    if height <= 0:
        raise ValueError("Height must be greater than zero.")
    if weight <= 0:
        raise ValueError("Weight must be greater than zero.")
    return weight / (height ** 2)

def suggest_food(bmi):
    """Suggest healthy food options based on BMI."""
    if bmi < 18.5:
        return [
            "Nuts and seeds",
            "Lean meats and poultry",
            "Whole grains",
            "Avocado",
            "Nut butters"
        ]
    elif 18.5 <= bmi < 24.9:
        return [
            "Fruits and vegetables",
            "Lean proteins",
            "Whole grains",
            "Low-fat dairy products",
            "Healthy fats (e.g., olive oil)"
        ]
    elif 25 <= bmi < 29.9:
        return [
            "Leafy greens",
            "Whole grains",
            "Lean proteins",
            "Low-fat dairy",
            "Fruits and vegetables"
        ]
    else:  # BMI >= 30
        return [
            "Vegetables",
            "Lean proteins (e.g., chicken, tofu)",
            "Whole grains",
            "Low-fat or non-fat dairy",
            "High-fiber foods"
        ]
