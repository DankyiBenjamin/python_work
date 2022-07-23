"""A class that can be used to represent a car."""

class Car():
    """A simple attempt to represent a car """

    def __init__(self,make,model,year):
        """Initialized attribute to describe a car"""
        self.make = make
        self.model =model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        # Return a neatly formatted descriptive name
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        # printing a statement showing the car's millage
        print(f"this car has {str(self.odometer_reading) } miles on it")

    def update_odometer(self,millage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if millage >= self.odometer_reading:
            self.odometer_reading = millage
        else:
            print("You cannot roll back odometer")

    def increment_odometer(self,miles):
        self.odometer_reading += miles


class Battery():
    """A simple attempt to model a battery for an electric car"""

    def __init__(self,battery_size = 70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size


    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-KWh battery")

    def get_range(self):
        battery_range = 0
        
        """Print a statement about the range this battey provides"""
        if self.battery_size ==70:
            battery_range = 240
            print("This car goes approximately " + str(battery_range) + " milles on a full charge")
        elif self.battery_size == 85:
            battery_range = 270
            print("This car goes approximately " + str(battery_range) + " milles on a full charge")
        else:
            print("Set battery size")
        

        
        
class ElectricCar(Car):
    """Model aspect to a car,specific to electric cars"""
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()

