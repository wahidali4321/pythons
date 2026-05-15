# Smart Game Access System

print("=== Gaming Tournament System ===")

age = int(input("Enter your age: "))

if age >= 18:

    membership = input("Do you have active membership? (yes/no): ")

    if membership == "yes":

        level = input("Enter your level (Beginner/Intermediate/Pro): ")

        if level == "Intermediate" or level == "Pro":

            payment = input("Payment completed? (yes/no): ")

            if payment == "yes":

                print("Tournament Access Granted")

            else:
                print("Complete payment first")

        else:
            print("Only Intermediate and Pro players are allowed")

    else:
        print("Membership required")

else:
    print("Not allowed for tournament")