# motorbike.py
class SuperSportCruizerMotorbike:
    def __init__(self, model="naked", fuel_type="gasoline", power_supply="12V", custom_features=None):
        self.model = model
        self.fuel_type = fuel_type
        self.power_supply = power_supply
        self.custom_features = custom_features or []

    def upgrade(self, upgrade_type):
        print(f"Upgrading motorbike to {upgrade_type} configuration...")
        self.model = upgrade_type
        return f"Motorbike upgraded to {self.model}"

    def set_fuel_type(self, fuel_type):
        self.fuel_type = fuel_type
        return f"Fuel type set to {self.fuel_type}"

    def configure_power(self, power_supply):
        self.power_supply = power_supply
        return f"Power supply set to {self.power_supply}"

    def add_custom_feature(self, feature):
        self.custom_features.append(feature)
        return f"Custom feature '{feature}' added."

    def display_configuration(self):
        return f"Model: {self.model}\nFuel: {self.fuel_type}\nPower: {self.power_supply}\nCustom Features: {self.custom_features}"
