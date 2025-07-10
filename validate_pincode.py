def is_indian_pin(code):
    return len(code)==6 and code.isdigit()

codes =[
    "700103",
    "4004",
    "A8901",
    "560064",
    "1234567"
]

for code in codes:
    print(code, "->", is_indian_pin(code))