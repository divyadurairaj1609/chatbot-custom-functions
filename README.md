# chatbot-custom-functions
A Python chatbot that uses Claude's function calling feature
with custom functions written completely from scratch.
No external APIs needed — pure Python logic!

### Functions We Built

### Password Generator
Generates a strong random password using:
- Random uppercase and lowercase letters
- Random numbers
- Random symbols
- Shuffled for true randomness

### OTP Generator
Generates a random One Time Password using:
- Random digits picked one by one
- Configurable length (4, 6, 8 digits)
- Different every single time!

### BMI Calculator
Calculates Body Mass Index using our own formula:
- BMI = weight / (height in meters)²
- Returns category (Underweight/Normal/Overweight)
- Gives health advice
- Shows ideal weight range

### EMI Calculator
Calculates Loan EMI using our own formula:
- EMI = P × R × (1+R)^N / ((1+R)^N - 1)
- Returns monthly payment
- Shows total interest paid
- Shows total payment amount
