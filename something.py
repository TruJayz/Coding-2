#The Constructor (__init__): Should accept 3 parameters; brand, model, and battery_level (an integer).

#Your class should have a method called charge. This method should use a loop to continuously add 10 to the battery_level if the user selects yes to charge. If the battery 
# gets to 100, the loop should stop and tell the user the battery is charged.

#There should another method called get_status. This should print out a string that shows the phone object Brand and model.



#class SmartPhone:
    def __init__(self, brand, model, batterylevel):
        self.brand = brand
        self.model = model
        self.batterylevel = batterylevel

    def charge(self):
        while self.batterylevel < 100:
            chargeinput = input("Do you want to charge the phone? (yes/no): ")
            if chargeinput.lower() == 'yes':
                self.batterylevel += 10
                print(f"Battery level: {self.batterylevel}%")
            else:
                print("Charging stopped.")
                break
        if self.batterylevel >= 100:
            print("Battery is fully charged.")

    def status(self):
        print(f"Phone Brand: {self.brand}, Model: {self.model}")

SmartPhone()








# Create a function that will multiply a numbers between the range of 1 and 10 by another number passed into the function as a parameter. Your function should use a loop to
# go through the range of numbers. 
# hint: use the range function to get numbers between 1-10

def multiplynumber(multiplier):
    for i in range(1, 11):
        print(f"{i} * {multiplier} = {i * multiplier}")

multiplynumber()
