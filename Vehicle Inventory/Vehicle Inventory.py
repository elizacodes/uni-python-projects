# This program is designed to be used for a dealership
# so they can have a vehicle inventory program.

import pyinputplus as pyip

class Vehicle:
    def __init__(self,  make, model, year, mileage, color, status):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
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
        return("""%s %s %s
               Color: %s
               Mileage: %s
               Status: %s""" % (self.year,
                                self.make,
                                self.model,
                                self.color,
                                self.mileage,
                                self.status))


def add_vehicle(inventory):
    make = input("Enter the make of the vehicle: \n")
    model = input("Enter the vehicle model: \n")
    year = input("Enter the year of the vehicle: \n")
    mileage = input("Enter the vehicle's mileage: \n")
    color = input("Enter the color of the vehicle: \n")
    status = input("Enter the status of the vehicle (Sold/In Stock): \n")
    car = Vehicle(make, model, year, mileage, color, status)
    inventory.append(car)

def remove_vehicle(inventory):
    position = int(input("Enter the  position of the vehicle to be removed: \n"))
    inventory.pop(position)

def modify_vehicle(inventory):
    position = int(input("Enter the position of the vehicle: \n"))
    print("Provide new details of the below. \n \n")
    make = input("Enter the make of the vehicle: \n")
    model = input("Enter the vehicle model: \n")
    year = input("Enter the year of the vehicle: \n")
    mileage = input("Enter the vehicle's mileage: \n")
    color = input("Enter the color of the vehicle: \n")
    status = input("Enter the status of the vehicle (Sold/In Stock): \n")
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
          4. Update Inventory
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
        print("In the works.")
    elif command == 6:
        user = False
    else:
        print("That is not a valid option. Try again.")
