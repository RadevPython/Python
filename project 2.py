# Project #1 – Job Application Checker


# Get user's first and second name
first_name = input("Hello what's your first name? ")
second_name = input("What's your second name? ")
message = f"Hello {first_name} {second_name}, Welcome to the Job Application Centre"
print(message)

# Define available job positions

available_positions = ["developer", "designer", "manager", "tester"]
print("The available positions are:", ",".join(available_positions))

# Ask the user which position they are applying for

position = input("Which position are you applying for? ").lower()

# Validate the chosen position

if position not in available_positions:
    print("Invalid position - restart.")
    exit()


# Ask for user's age and convert to integer

age = input("What's your age? ")
years_old = int(age)

# Ask if the user knows English and convert to boolean

english_answer = input("Do you know English? (yes/no) ").lower() == "yes"

if position == "developer":
    approved = years_old >= 18 and english_answer
elif position == "designer":
    approved = years_old >= 16
elif position == "manager":
    approved = years_old >= 25 and english_answer
elif position == "tester":
    approved = english_answer
else:
    approved = False
print("Approved." if approved else "Rejected.")
