# custombuild.py
from motorbike import SuperSportCruizerMotorbike

def custom_build_motorbike():
    print("Building custom motorbike...")
    bike = SuperSportCruizerMotorbike()
    bike.upgrade("custom")
    bike.add_custom_feature("Carbon fiber body")
    bike.add_custom_feature("Turbo engine")
    bike.configure_power("24V")
    bike.set_fuel_type("electric")
    return bike
