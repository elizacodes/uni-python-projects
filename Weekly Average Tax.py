# This program calculates the weekly average tax
# withholding for a customer, based on their given income
# as their following input

import pyinputplus as pyip

def user_input():
    while True:
        print("Enter your weekly income:")
        income = pyip.inputInt()
        return income

def tax_calculation(income):
    # adding tuples in dictionary
    tax_rates = {(0, 500): 10,
                 (500, 1500): 15,
                 (1500,2500): 20,
                 (2500,): 30}
    for i in tax_rates.keys():
        if (income >= i[0]):
            if (len(i) > 1):
                if (income < i[1]):
                    rate = tax_rates[i]
                    break
            else:
                rate = tax_rates[i]
    tax = int(income * (rate / 100))
    after_tax_income = int(income - tax)
    return tax, after_tax_income, rate

def display_output(tax, after_tax_income, rate):
    print(f"Income: {after_tax_income}")
    print(f"Tax Rate: {rate}%")
    print(f"Tax: {tax}")

def main():
    income = user_input()
    tax, after_tax_income, rate = tax_calculation(income)
    display_output(tax, after_tax_income, rate)
    

main()
