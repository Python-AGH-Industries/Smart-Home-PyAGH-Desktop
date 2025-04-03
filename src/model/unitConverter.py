class UnitConverter:
    def __init__(self):
        pass

    def convertUnits(self, title, oldUnit, newUnit, data):
        if oldUnit==newUnit:
            return data

        if title == "Temperature":
            return self.convertTemperature(oldUnit, newUnit, data)
        elif title == "Humidity":
            return self.convertHumidity(oldUnit, newUnit, data)
        elif title == "Pressure":
            return self.convertPressure(oldUnit, newUnit, data)
        else:
            print("Incorrect data title passed")
            return []

    def convertTemperature(self, oldUnit, newUnit, data):
        if oldUnit == "C":
            if newUnit == "F":
                return [(t * 9 / 5) + 32 for t in data]
            elif newUnit == "K":
                return [t + 273 for t in data]
        elif oldUnit == "F":
            if newUnit == "C":
                return [(t - 32) * 5 / 9 for t in data]
            elif newUnit == "K":
                return [(t - 32) * 5 / 9 + 273 for t in data]
        elif oldUnit == "K":
            if newUnit == "C":
                return [t - 273 for t in data]
            elif newUnit == "F":
                return [(t - 273) * 9 / 5 + 32 for t in data]
        else:
            print("Incorrect unit passed")
            return []

    def convertHumidity(self, oldUnit, newUnit, data):
        if oldUnit == "%":
            if newUnit == "g/m³":
                return [rh * 0.00878 for rh in data]
            elif newUnit == "kg/m³":
                return [rh * 0.00000878 for rh in data]
        elif oldUnit == "g/m³":
            if newUnit == "%":
                return [ah / 0.00878 for ah in data]
            elif newUnit == "kg/m³":
                return [(ah / 1000) for ah in data]
        elif oldUnit == "kg/m³":
            if newUnit == "%":
                return [(ah * 1000) / 0.00878 for ah in data]
            elif newUnit == "g/m³":
                return [(ah * 1000) for ah in data]
        else:
            print("Incorrect unit passed")
            return []

    def convertPressure(self, oldUnit, newUnit, data):
        if oldUnit == "Pa":
            if newUnit == "bar":
                return [p / 100000 for p in data]
            elif newUnit == "atm":
                return [p * 9.86923e-6 for p in data] 
        elif oldUnit == "bar":
            if newUnit == "Pa":
                return [p * 100000 for p in data] 
            elif newUnit == "atm":
                return [p * 0.986923 for p in data]
        elif oldUnit == "atm":
            if newUnit == "bar":
                return [p * 1.01325 for p in data] 
            elif newUnit == "Pa":
                return [p * 101325 for p in data]
        else:
            print("Incorrect unit passed")
            return []