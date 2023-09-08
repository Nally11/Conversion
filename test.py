def cm_to_inch(cm):
    return cm / 2.54

def inch_to_cm(inch):
    return inch * 2.54

def meters_to_feet(meters):
    return meters * 3.281

def feet_to_meters(feet):
    return feet / 3.281

def liters_to_gallons(liters):
    return liters * 0.264172

def gallons_to_liters(gallons):
    return gallons / 0.264172

# Test the functions.
cm = 100
inch = 10
meters = 5
feet = 16
liters = 10
gallons = 2.5

print(f"{cm} cm is equal to {cm_to_inch(cm):.2f} inches")
print(f"{inch} inches is equal to {inch_to_cm(inch):.2f} cm")
print(f"{meters} meters is equal to {meters_to_feet(meters):.2f} feet")
print(f"{feet} feet is equal to {feet_to_meters(feet):.2f} meters")
print(f"{liters} liters is equal to {liters_to_gallons(liters):.2f} gallons")
print(f"{gallons} gallons is equal to {gallons_to_liters(gallons):.2f} liters")
