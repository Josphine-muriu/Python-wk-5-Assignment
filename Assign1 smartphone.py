# smartphone.py

class Smartphone:
    def __init__(self, brand, model, storage, battery_level=100):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery_level = battery_level  # in percentage

    def make_call(self, number):
        if self.battery_level > 0:
            print(f"{self.model} is calling {number} 📞")
            self.battery_level -= 5
        else:
            print("Battery is dead. Please charge your phone.")

    def charge(self):
        self.battery_level = 100
        print(f"{self.model} is fully charged 🔋")

    def __str__(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage, Battery: {self.battery_level}%"

# Inheritance and Encapsulation
class SmartWatch(Smartphone):
    def __init__(self, brand, model, storage, battery_level=100, heart_rate_monitor=True):
        super().__init__(brand, model, storage, battery_level)
        self.__heart_rate_monitor = heart_rate_monitor  # encapsulated attribute

    def track_heart_rate(self):
        if self.__heart_rate_monitor:
            print(f"{self.model} is tracking heart rate ❤️")
        else:
            print("Heart rate monitoring not supported.")

    def __str__(self):
        return f"{self.brand} {self.model} (Watch) - Battery: {self.battery_level}%"

# Example usage
if __name__ == "__main__":
    phone = Smartphone("Samsung", "Galaxy S21", 128)
    watch = SmartWatch("Apple", "Watch Series 7", 32)

    print(phone)
    phone.make_call("0712345678")
    phone.charge()

    print(watch)
    watch.track_heart_rate()
