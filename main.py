# Create program header"
print("========================")
print("Homer Minnick's")
print("Car Customization Form")
print("========================")
print()

# Create car model header
print("~ Make & Model ~")
print()
# Prompt user to select a type of vehicle from multiple choice list. Store user input into a variable.
print("1. What Make & Model of Car Would You Like?")
print("  a. Ford Elite")
print("  b. Pontiac Bonneville")
print("  c. Ford Mustang")
print("  d. Hyundai Elantra")
makeModel = input("Please enter 'a' - 'd': ")
print()

# Create exterior options header
print("~ Exterior Options ~")
print()

# Prompt user for option one and store in a variable. Yes or No question.
# First option is for sunroof.
print("2. Would you like a sunroof?")
sunroof = input("Please enter 'yes' or 'no': ")
print()

# Prompt user for option two and store in a variable. Open ended, short response
# Second option is color.
print("3. There are endless exterior color options.")
color = input("What exterior color would you like? ")
print()

# Create interior options header
print("~ Interior Options ~")
print()

# Prompt user for option three and store in a variable. Multiple choice.
# Third option is seat cover type.
print("4. What type of seat cover would you like?")
print("   Available options include: ")
print("  - Cloth")
print("  - Leather")
print("  - Neoprene")
seatCover = input("Please enter your selection: ")
print()

# Prompt user for option four and store in a variable. Yes or No question.
# Fourth option is power
print("5. Do you want power options (e.g. windows, door locks)?")
power = input("Please enter 'yes' or 'no': ")
print()

# Create general options header
print("~ General Options ~")
print()

# Prompt user for option five and store in a variable. Open ended, short response.
# Fifth option is new or used
neworUsed = input("6. Do you want a new or used car? ")
print()

# Create responses header
print("===========================")
print("Summary of your selections")
print("===========================")
print()

# Display user selections. 
print(f"Model selected: {makeModel}")
print(f"Sunroof desired: {sunroof}")
print(f"Color desired: {color}")
print(f"Seat cover type: {seatCover}")
print(f"Power windows & locks: {power}")
print(f"New or Used: {neworUsed}")
