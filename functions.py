import random
import string

# ─────────────────────────────────────────
# FUNCTION 1: Password Generator
# Logic: We pick random characters ourselves
# No API needed — pure Python logic!
# ─────────────────────────────────────────
def generate_password(length=12):
    """Generate a strong random password"""

    # Character sets
    lowercase = string.ascii_lowercase  # a-z
    uppercase = string.ascii_uppercase  # A-Z
    numbers = string.digits             # 0-9
    symbols = "!@#$%^&*"               # special chars

    # Guarantee at least one of each type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(numbers),
        random.choice(symbols)
    ]

    # Fill remaining length with random characters
    all_characters = lowercase + uppercase + numbers + symbols
    for i in range(length - 4):
        password.append(random.choice(all_characters))

    # Shuffle so order is random
    random.shuffle(password)

    # Join list into string
    final_password = "".join(password)

    return f"""
Generated Password:
- Password: {final_password}
- Length: {length} characters
- Contains: Uppercase, Lowercase, Numbers, Symbols
- Strength: Strong 💪
"""

# ─────────────────────────────────────────
# FUNCTION 2: OTP Generator
# Logic: We pick random digits ourselves
# No API needed — pure Python logic!
# ─────────────────────────────────────────
def generate_otp(digits=6):
    """Generate a random OTP"""

    # Pick random digits one by one
    otp = ""
    for i in range(digits):
        otp += str(random.randint(0, 9))

    return f"""
Generated OTP:
- OTP: {otp}
- Length: {digits} digits
- Valid for: 10 minutes
- Do not share this with anyone!
"""

# ─────────────────────────────────────────
# FUNCTION 3: BMI Calculator
# Logic: We write the BMI formula ourselves
# Formula: weight / (height in meters)²
# No API needed — pure math!
# ─────────────────────────────────────────
def calculate_bmi(height_cm, weight_kg):
    """Calculate BMI and give health advice"""

    # Convert height from cm to meters
    height_m = height_cm / 100

    # BMI Formula: weight / height²
    bmi = weight_kg / (height_m ** 2)

    # Round to 1 decimal place
    bmi = round(bmi, 1)

    # Determine BMI category
    if bmi < 18.5:
        category = "Underweight"
        advice = "You need to eat more nutritious food and gain some weight!"
        emoji = "⚠️"
    elif 18.5 <= bmi < 25:
        category = "Normal Weight"
        advice = "Great! You have a healthy weight. Keep it up!"
        emoji = "✅"
    elif 25 <= bmi < 30:
        category = "Overweight"
        advice = "Consider exercising regularly and eating balanced meals!"
        emoji = "⚠️"
    else:
        category = "Obese"
        advice = "Please consult a doctor for a proper health plan!"
        emoji = "❗"

    # Calculate ideal weight range
    ideal_min = round(18.5 * (height_m ** 2), 1)
    ideal_max = round(24.9 * (height_m ** 2), 1)

    return f"""
BMI Calculator Results:
- Height: {height_cm} cm
- Weight: {weight_kg} kg
- BMI: {bmi}
- Category: {emoji} {category}
- Advice: {advice}
- Ideal weight range for your height: {ideal_min}kg to {ideal_max}kg
"""

# ─────────────────────────────────────────
# FUNCTION 4: EMI Calculator
# Logic: We write the EMI formula ourselves
# Formula: P * R * (1+R)^N / ((1+R)^N - 1)
# No API needed — pure math!
# ─────────────────────────────────────────
def calculate_emi(principal, years, annual_interest_rate):
    """Calculate loan EMI and total payment"""

    # Convert annual rate to monthly rate
    monthly_rate = annual_interest_rate / (12 * 100)

    # Convert years to months
    months = years * 12

    # EMI Formula
    if monthly_rate == 0:
        emi = principal / months
    else:
        emi = principal * monthly_rate * (1 + monthly_rate) ** months / ((1 + monthly_rate) ** months - 1)

    # Round EMI to 2 decimal places
    emi = round(emi, 2)

    # Calculate total payment and interest
    total_payment = round(emi * months, 2)
    total_interest = round(total_payment - principal, 2)

    # Format numbers with commas
    emi_formatted = f"₹{emi:,.2f}"
    total_payment_formatted = f"₹{total_payment:,.2f}"
    total_interest_formatted = f"₹{total_interest:,.2f}"
    principal_formatted = f"₹{principal:,.2f}"

    return f"""
EMI Calculator Results:
- Loan Amount: {principal_formatted}
- Loan Tenure: {years} years ({months} months)
- Annual Interest Rate: {annual_interest_rate}%
- Monthly EMI: {emi_formatted}
- Total Payment: {total_payment_formatted}
- Total Interest Paid: {total_interest_formatted}
- Tip: Pay one extra EMI per year to save on interest!
"""