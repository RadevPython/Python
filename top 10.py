#Top 10 Challenge
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~                              ~")
print("~       TOP 10 CHALLENGE       ~")
print("~                              ~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("")

#Top 10 largest countries in the world per area
largestCountries = ["Russia", "Canada", "China", "United States", "Brazil", "Australia", "India", "Argentina", "Kazakhstan", "Algeria"]

#Retrieve user input
message = input("Enter one of the top 10 largest countries in the world: ")

msg_lower = message.lower()

# Build a lowercase version of the list
largestCountriesLower = [country.lower() for country in largestCountries]

# Check
if msg_lower in largestCountriesLower:
    position = largestCountriesLower.index(msg_lower) + 1
    print(f"You are correct {message} is in position {position}.")
else:
    print(f"{message} is not in top 10 largest countries in the world.")
