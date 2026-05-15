age = 20
result = 80
percentage = 90   # remove %

# Admission check
if age >= 18:
    print("You are eligible for admission")

    if result >= 80:
        print("Eligible for top programs")

    elif 60 <= result <= 79:
        print("Normal admission")

    else:
        print("Not eligible based on result")

# Percentage check
if percentage >= 80:
    print("Fully eligible")

elif 70 <= percentage < 80:
    print("Conditional admission")

else:
    print("Rejected")

# Fees check
fees = input("Enter fees status (paid / not paid): ")

if fees == "paid":
    print("Admission confirmed")

elif fees == "not paid":
    print("Admission on hold")