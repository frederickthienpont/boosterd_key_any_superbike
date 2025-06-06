# install_wizard.py
from utilities import validate_fuel_type, validate_power_supply
from motorbike import SuperSportCruizerMotorbike

def installation_wizard():
    print("Welcome to the motorbike installation wizard.")
    
    fuel_type = input("Enter fuel type (gasoline, electric, hybrid): ")
    while not validate_fuel_type(fuel_type):
        fuel_type = input("Invalid fuel type. Please enter again: ")
    
    power_supply = input("Enter power supply (12V, 24V, 48V): ")
    while not validate_power_supply(power_supply):
        power_supply = input("Invalid power supply. Please enter again: ")
    
    bike = SuperSportCruizerMotorbike(fuel_type=fuel_type, power_supply=power_supply)
    print(f"Motorbike created with {fuel_type} and {power_supply}.")
    return bike
