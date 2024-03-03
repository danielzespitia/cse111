import math
import datetime

current_datetime = datetime.datetime.now()

width = int(input("\nEnter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000
volume_liters = volume / 1000

print("\nThe approximate volume is %.2f liters" % volume_liters)

if width == 185 and aspect_ratio == 50 and diameter == 14:
    price = 100.00
elif width == 205 and aspect_ratio == 60 and diameter == 15:
    price = 150.00
elif width == 225 and aspect_ratio == 55 and diameter == 16:
    price = 200.00
else:
    price = None

if price is not None:
    print("\nThe price of the tire is $%.2f" % price)
else:
    print("\nPrice not found for the specified tire size.")

purchase_choice = input("\nDo you want to purchase tires with the entered dimensions? (yes/no): ")

if purchase_choice.lower() == "yes":
    phone_number = input("\nPlease enter your phone number: ")

    with open("volumes.txt", "a") as file:
        file.write("Date and Time: {}\n".format(current_datetime))
        file.write("Phone number: {}\n".format(phone_number))
        file.write("Width: {}\n".format(width))
        file.write("Aspect ratio: {}\n".format(aspect_ratio))
        file.write("Diameter: {}\n".format(diameter))
        file.write("Volume: %.2f\n" % volume_liters)
        file.write("\n")
else:
    print("\nThank you for using the tire volume calculator.\n")