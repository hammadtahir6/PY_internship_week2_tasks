current_year =2025

birth_year = int(input("what is your birth year: "))

age = current_year - birth_year

if age >= 18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote ")