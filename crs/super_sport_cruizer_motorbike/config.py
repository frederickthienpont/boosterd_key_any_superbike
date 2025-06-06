# config.py
class MotorbikeConfig:
    def __init__(self, fuel_type="gasoline", power_supply="12V"):
        self.fuel_type = fuel_type
        self.power_supply = power_supply

    def update_fuel(self, fuel_type):
        self.fuel_type = fuel_type

    def update_power(self, power_supply):
        self.power_supply = power_supply
