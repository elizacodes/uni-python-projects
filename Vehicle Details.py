import pyinputplus as pyip

def user_input():
    while True:
        print("Enter a car brand:")
        brand = pyip.inputStr().capitalize().strip()
        print("Enter the model:")
        model = pyip.inputStr().capitalize().strip()
        print("Enter the year of the car:")
        year = pyip.inputInt()
        print("Enter the starting odometer reading:")
        odo_start = pyip.inputInt()
        print("Enter the ending odometer reading:")
        odo_end = pyip.inputInt()
        print("Enter the estimated miles per gallon:")
        est_mpg = pyip.inputInt()
        return brand, model, year, odo_start, odo_end, est_mpg
    
def car_info(brand, model, year, odo_start, odo_end, est_mpg):
    car_list = []
    cars = {
        "Brand": brand,
        "Model": model,
        "Year": year,
        "Starting Odometer Reading": odo_start,
        "Ending Odometer Reading": odo_end,
        "Estimated Miles Per Gallon": est_mpg
    }
    car_list.append(cars)
    print(f"Car Information: {car_list}")

def ask_again():
    print("""Would you like to enter another vehicle's information?
          Enter YES/NO or Y/N to continue:""")
    user_prompt = pyip.inputStr().capitalize().strip()
    # Condition statement does not work; continues to return user_input()
    # regardless of user_prompt / does not return user_input()
    if user_prompt == "YES" or "Y":
        return user_input()
    elif user_prompt == "NO" or "N":
        print("Thank you. Goodbye.")
    else:
        print("That information is invalid. Please try again.")
        
def main():
    brand, model, year, odo_start, odo_end, est_mpg = user_input()
    car_info(brand, model, year, odo_start, odo_end, est_mpg)
    ask_again()

main()
