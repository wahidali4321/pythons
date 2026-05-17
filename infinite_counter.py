# Infinite Counter Stopper

i = 1

while True:

    print(i)

    stop = input("Do you want to stop? (yes/no): ")

    if stop == "yes":
        print("Loop Stopped")
        break

    i += 1