# polymorphism.py

class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚢")

# Example usage
if __name__ == "__main__":
    vehicles = [Car(), Plane(), Boat()]
    for vehicle in vehicles:
        vehicle.move()
