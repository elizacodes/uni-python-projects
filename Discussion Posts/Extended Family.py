def user_input():
        name = input("Enter a name: \n")
        birthdate = input("Enter the birthday as 'MM DD YYYY':\n")
        relationship = input("Enter your relationship with this person:\n")
        address = input("Enter the address of where they live: \n")
        return name, birthdate, relationship, address

def ext_family(name, birthdate, relationship, address):
    family = []
    extended_family = {
        'Name': name,
        'Birthdate': birthdate,
        'Relationship': relationship,
        'Address': address
    }
    family.append(extended_family)
    print(f"Family Member List: {family}")

def main():
    name, birthdate, relationship, address = user_input()
    ext_family(name, birthdate, relationship, address)

main()
