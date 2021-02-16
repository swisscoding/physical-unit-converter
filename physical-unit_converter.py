#!/usr/local/bin/python3
# Made by @swisscoding on Instagram

from colored import stylize, fg

# decoration
print(stylize("\n---- | Convert physical units | ----\n", fg("red")))

# class
class Converter:
    def __init__(self, choice, value):
        self.choice = choice
        self.value = value

    # output magic method
    def __repr__(self):
        return self.convert(self.choice, self.value)

    # methods
    def convert(self, choice, value):
        if choice == "1":
            output = round(value * 0.62137119223733)
            return f"\n{value} kmh = {output} mph\n"
        elif choice == "2":
            output = round(value * 1.609344)
            return f"\n{value} mph = {output} kmh\n"
        else:
            return "\nInvalid Input\n"

# main execution
if __name__ == "__main__":
    # options
    print(stylize("Options:", fg("green")))
    print("'1' for kmh to mph\n'2' for mph to kmh\n")

    # user interaction
    choice = input(": ")
    value = float(input("Value: "))

    print(Converter(choice, value))
