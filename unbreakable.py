def get_number():
    while True:
        try:
            number = int(input("Enter a whole number: "))
            return number
        except ValueError:
            print("Invalid input. Please enter a whole number.")


number = get_number()
print("You entered:", number) 