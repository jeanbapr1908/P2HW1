
print('Budget and Expense Tracker')
print('25OCT2023')
print('CTI-110 P2HW1-Travel')
print('Reggie Jean Baptiste')

budget = float(input("Enter Budget: "))

destination = input("\nEnter your travel destination: ")

gas = float(input("\nHow much do you think you will spend on gas? "))

accomodation = float(input("\nApproximately, how much will you need for accomodation/hotel? "))

food = float(input("\nLast, how much do you need for food? "))

expenses=gas+accomodation+food

print("---------------Travel Expense---------------")
print(f"{'Location:' : <20}", f"{ destination : <20}")
print(f"{'Initial budget:' : <20}", f"{ '$'+str(float(budget)) : <20}")
print(f"{'Fuel:' : <20}", f"{'$'+str(float(gas)) : <20}")
print(f"{'Accommodation:' : <20}", f" {'$'+str(float(accomodation)) : <20}")
print(f"{'Food:' : <20}", f"{'$'+str(float(food)) : <20}")

balance = budget - gas - accomodation - food

print("--------------------------------------------")
print(f"{'Remaining balance:' : <20}", f"{'$'+str(float(balance)) : <20}")
