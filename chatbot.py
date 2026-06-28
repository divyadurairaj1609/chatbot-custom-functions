import anthropic
import os
from dotenv import load_dotenv
from functions import generate_password, generate_otp, calculate_bmi, calculate_emi

load_dotenv()

claude = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

print("=" * 50)
print("   Claude Chatbot — Custom Functions")
print("=" * 50)
print("I can help you with:")
print("  🔐 Password → Generate a strong password")
print("  🔢 OTP      → Generate a 6 digit OTP")
print("  💪 BMI      → Calculate your BMI")
print("  💰 EMI      → Calculate your loan EMI")
print("Type 'quit' to exit\n")

# Define all 4 tools for Claude
tools = [
    {
        "name": "generate_password",
        "description": "Generate a strong random password. Use when user asks for a password, secure password, or random password.",
        "input_schema": {
            "type": "object",
            "properties": {
                "length": {
                    "type": "integer",
                    "description": "Length of password. Default is 12. Example: 8, 12, 16"
                }
            },
            "required": []
        }
    },
    {
        "name": "generate_otp",
        "description": "Generate a random OTP. Use when user asks for an OTP, one time password, or verification code.",
        "input_schema": {
            "type": "object",
            "properties": {
                "digits": {
                    "type": "integer",
                    "description": "Number of digits in OTP. Default is 6. Example: 4, 6, 8"
                }
            },
            "required": []
        }
    },
    {
        "name": "calculate_bmi",
        "description": "Calculate BMI and give health advice. Use when user asks about BMI, body mass index, or healthy weight.",
        "input_schema": {
            "type": "object",
            "properties": {
                "height_cm": {
                    "type": "number",
                    "description": "Height in centimeters. Example: 165, 170, 180"
                },
                "weight_kg": {
                    "type": "number",
                    "description": "Weight in kilograms. Example: 60, 70, 80"
                }
            },
            "required": ["height_cm", "weight_kg"]
        }
    },
    {
        "name": "calculate_emi",
        "description": "Calculate loan EMI and total payment. Use when user asks about loan EMI, monthly payment, or loan calculation.",
        "input_schema": {
            "type": "object",
            "properties": {
                "principal": {
                    "type": "number",
                    "description": "Loan amount in rupees. Example: 500000, 1000000"
                },
                "years": {
                    "type": "number",
                    "description": "Loan tenure in years. Example: 1, 2, 3, 5, 10"
                },
                "annual_interest_rate": {
                    "type": "number",
                    "description": "Annual interest rate in percentage. Example: 8.5, 10, 12"
                }
            },
            "required": ["principal", "years", "annual_interest_rate"]
        }
    }
]

# Conversation history
history = []

def handle_tool_call(tool_name, tool_input):
    """Call the right function based on what Claude requests"""
    if tool_name == "generate_password":
        length = tool_input.get("length", 12)
        return generate_password(length)
    elif tool_name == "generate_otp":
        digits = tool_input.get("digits", 6)
        return generate_otp(digits)
    elif tool_name == "calculate_bmi":
        return calculate_bmi(
            tool_input["height_cm"],
            tool_input["weight_kg"]
        )
    elif tool_name == "calculate_emi":
        return calculate_emi(
            tool_input["principal"],
            tool_input["years"],
            tool_input["annual_interest_rate"]
        )
    return "Function not found"

# Main chat loop
while True:
    user_input = input("\nYou: ").strip()

    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    if not user_input:
        continue

    history.append({
        "role": "user",
        "content": user_input
    })

    response = claude.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1000,
        system="You are a helpful assistant. You have access to custom functions that generate passwords, OTPs, calculate BMI and EMI. Always use these functions when relevant — never try to calculate or generate these yourself!",
        tools=tools,
        messages=history
    )

    # Handle tool calls
    while response.stop_reason == "tool_use":
        tool_use = next(block for block in response.content
                       if block.type == "tool_use")

        tool_name = tool_use.name
        tool_input = tool_use.input

        print(f"\nClaude is calling: {tool_name}({tool_input})")

        result = handle_tool_call(tool_name, tool_input)
        print(f"Result received!")

        history.append({
            "role": "assistant",
            "content": response.content
        })

        history.append({
            "role": "user",
            "content": [
                {
                    "type": "tool_result",
                    "tool_use_id": tool_use.id,
                    "content": result
                }
            ]
        })

        response = claude.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1000,
            system="You are a helpful assistant. You have access to custom functions that generate passwords, OTPs, calculate BMI and EMI. Always use these functions when relevant — never try to calculate or generate these yourself!",
            tools=tools,
            messages=history
        )

    reply = response.content[0].text
    history.append({
        "role": "assistant",
        "content": reply
    })

    print(f"\nClaude: {reply}")
    print("-" * 50)