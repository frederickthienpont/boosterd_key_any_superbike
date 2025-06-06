# utilities.py
import json

def load_default_config(config_file="resources/default_config.json"):
    with open(config_file, "r") as file:
        config = json.load(file)
    return config

def validate_fuel_type(fuel_type):
    valid_fuels = ["gasoline", "electric", "hybrid"]
    if fuel_type not in valid_fuels:
        raise ValueError(f"Invalid fuel type: {fuel_type}")
    return True

def validate_power_supply(power_supply):
    valid_powers = ["12V", "24V", "48V"]
    if power_supply not in valid_powers:
        raise ValueError(f"Invalid power supply: {power_supply}")
    return True
