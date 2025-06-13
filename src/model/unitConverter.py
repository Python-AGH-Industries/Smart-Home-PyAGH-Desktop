class UnitConverter:
    def __init__(self):
        pass

    def convert_units(self, title, old_unit, new_unit, data):
        if old_unit == new_unit:
            return data

        if title == "Temperature":
            return self.convert_temperature(old_unit, new_unit, data)
        elif title == "Humidity":
            return self.convert_humidity(old_unit, new_unit, data)
        elif title == "Pressure":
            return self.convert_pressure(old_unit, new_unit, data)
        else:
            return data

    def convert_temperature(self, old_unit, new_unit, data):
        if old_unit == "C":
            if new_unit == "F":
                return [(t * 9 / 5) + 32 for t in data]
            elif new_unit == "K":
                return [t + 273 for t in data]
            else:
                return data
        elif old_unit == "F":
            if new_unit == "C":
                return [(t - 32) * 5 / 9 for t in data]
            elif new_unit == "K":
                return [(t - 32) * 5 / 9 + 273 for t in data]
            else:
                return data
        elif old_unit == "K":
            if new_unit == "C":
                return [t - 273 for t in data]
            elif new_unit == "F":
                return [(t - 273) * 9 / 5 + 32 for t in data]
            else:
                return data
        else:
            return data

    def convert_humidity(self, old_unit, new_unit, data):
        if old_unit == "%":
            if new_unit == "g/m³":
                return [rh * 0.00878 for rh in data]
            elif new_unit == "kg/m³":
                return [rh * 0.00000878 for rh in data]
            else:
                return data
        elif old_unit == "g/m³":
            if new_unit == "%":
                return [ah / 0.00878 for ah in data]
            elif new_unit == "kg/m³":
                return [(ah / 1000) for ah in data]
            else:
                return data
        elif old_unit == "kg/m³":
            if new_unit == "%":
                return [(ah * 1000) / 0.00878 for ah in data]
            elif new_unit == "g/m³":
                return [(ah * 1000) for ah in data]
            else:
                return data
        else:
            return data

    def convert_pressure(self, old_unit, new_unit, data):
        if old_unit == "hPa":
            if new_unit == "bar":
                return [p / 1000 for p in data]
            elif new_unit == "atm":
                return [p / 1013.25 for p in data] 
            else:
                return data
        elif old_unit == "bar":
            if new_unit == "hPa":
                return [p * 1000 for p in data] 
            elif new_unit == "atm":
                return [p / 1.01325 for p in data]
            else:
                return data
        elif old_unit == "atm":
            if new_unit == "bar":
                return [p * 1.01325 for p in data] 
            elif new_unit == "hPa":
                return [p * 1013.25 for p in data]
            else:
                return data
        else:
            return data
        