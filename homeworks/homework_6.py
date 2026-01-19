class Distance:
    conversion_dict = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000
    }

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def convert(self):
        return self.value * Distance.conversion_dict.get(self.unit, 1)

    def __str__(self):
        return f"{self.value} {self.unit}"

    def __add__(self, other):
        if not isinstance(other,Distance):
            return NotImplemented
        total_meters = self.convert() + other.convert()
        return Distance(total_meters, "m")

    def __sub__(self, other):
        if not isinstance(other,Distance):
            return NotImplemented
        result_meters = self.convert() - other.convert()
        return Distance(result_meters, "m")



d1 = Distance(15, "m")
d2 = Distance(22, "m")
d3 = Distance(31, "m")
print(d1)
print(d2)
print(d3)

print("+")
print(d3+d2)
print(d1+d2)

print("-")
print(d2-d1)
print(d3-d2)