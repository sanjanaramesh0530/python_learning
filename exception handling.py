while True:
    try:
        age = int(input("Enter your age: "))

        if age < 18:
            raise ValueError("You must be at least 18 years old.")

        print("Welcome!")

    except ValueError as e:
        print(e)

    choice = input("Do you want to continue? (y/n): ")

    if choice.lower() != "y":
        print("Program ended")
        break
