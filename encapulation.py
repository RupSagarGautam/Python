class Vehicle:
# Public Function

    def displayName():
        return "B M W"
    
# Protected Function
    def _displayModel():
        return "M5 CS" 

# Private Punction
    def __engine():
        return "2.0L V8 Turbocharged Engine"
    
    def displayDetails():
        name = Vehicle.displayName()
        model = Vehicle._displayModel()
        engine = Vehicle.__engine()
        return f"Name: {name}\nModel: {model}\nEngine: {engine}"
    
# name = Vehicle.displayName()
# model = Vehicle._displayModel()
vehicleDetails = Vehicle.displayDetails()
print("\n" + vehicleDetails + "\n")