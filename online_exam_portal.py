# Smart Online Exam System

print("=== Online Exam Portal ===")

username = input("Enter username: ")

if username == "student123":

    password = input("Enter password: ")

    if password == "python":

        attendance = int(input("Enter attendance percentage: "))

        if attendance >= 75:

            fee = input("Fee paid? (yes/no): ")

            if fee == "yes":

                print("You are allowed to enter the exam")

            else:
                print("Please pay your fee first")

        else:
            print("Attendance is too low for exam entry")

    else:
        print("Incorrect password")

else:
    print("Invalid username")