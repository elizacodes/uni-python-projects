# This vehicle inventory program is designed
# for a car dealership to keep track of their
# vehicles for further analysis and use.

class Vehicle:
    def __init__(self, make, model, year, mileage, color, status):
        self.make = make
        self.model = model
        self.year = int(year)
        self.mileage = int(mileage)
        self.color = color
        self.status = status
        
    def edit(self, make, model, year, mileage, color, status):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.color = color
        self.status = status 

    def __str__(self):
        return("""%d %s %s
               Color: %s
               Mileage: %d
               Status: %s \n""" % (self.year,
                                self.make,
                                self.model,
                                self.color,
                                self.mileage,
                                self.status))

def enter_info():
    make = input("Enter the make of the vehicle: \n")
    model = input("Enter the vehicle model: \n")
    year = input("Enter the year of the vehicle: \n")
    mileage = input("Enter the vehicle's mileage: \n")
    color = input("Enter the color of the vehicle: \n")
    status = input("Enter the status of the vehicle (Sold/In Stock): \n")
    return make, model, year, mileage, color, status

def add_vehicle(inventory):
    make, model, year, mileage, color, status = enter_info()
    car = Vehicle(make, model, year, mileage, color, status)
    inventory.append(car)

def remove_vehicle(inventory):
    position = int(input("Enter the  position of the vehicle to be removed: \n"))
    inventory.pop(position)

def modify_vehicle(inventory):
    position = int(input("Enter the position of the vehicle: \n"))
    print("Provide new details of the below.")
    make, model, year, mileage, color, status = enter_info()
    inventory[position].edit(make, model, year, mileage, color, status)
    
def vehicle_output(inventory):
    for i in inventory:
        print(i)

def write_txt_file(inventory):
    f = open("vehicle_inventory.txt","w")
    for i in inventory:
        f.write(str(i))
    f.close()

inventory = []

user = True
while user:
    print("""
          1. Add New Vehicle
          2. Remove Vehicle
          3. View Inventory List
          4. Update Inventory List
          5. Export Inventory List
          6. Exit
          """)
    
    command = int(input("Please enter a command based on number: \n"))
    if command == 1:
        add_vehicle(inventory)
    elif command == 2:
        remove_vehicle(inventory)
    elif command == 3:
        vehicle_output(inventory)
    elif command == 4:
        modify_vehicle(inventory)
    elif command == 5:
        write_txt_file(inventory)
    elif command == 6:
        user = False
    else:
        print("That is not a valid option. Try again.")
