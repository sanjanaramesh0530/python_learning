for i in range(5):
    value = int(input("Please enter a value: "))
    if value > 89:
        print("You have an A grade.")
    elif 80 <= value < 90:
        print("You have a B grade.")
    elif 70 <= value < 80:
        print("You have a C grade.")
    else:
        print("fail")
        
