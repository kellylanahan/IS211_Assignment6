def conversioncalcs(fromUnit, toUnit, value):
     if fromUnit.lower() == 'celsius' and toUnit.lower() == 'kelvin':
        kelvin = value + 273.15
        print('{} degrees Celsius is equal to {} degrees Kelvin'.format(value, kelvin))
        return float(kelvin)
     if fromUnit.lower() == 'celsius' and toUnit.lower() == 'fahrenheit':
        fahrenheit = (value * 9) / 5 + 32
        print('{} degrees Celsius is equal to {} degrees Fahrenheit'.format(value, fahrenheit))
        return float(fahrenheit)
     if fromUnit.lower() == 'fahrenheit' and toUnit.lower() == 'celsius':
        celsius = ((value - 32) * 5) / 9
        print('{} degrees Fahrenheir is equal to {} degrees Celsius'.format(value, celsius))
        return float(celsius)
     if fromUnit.lower() == 'fahrenheit' and toUnit.lower() == 'kelvin':
        kelvin = (value + 459.67) * 5 / 9
        print('{} degrees Fahrenheit is equal to {} degrees Kelvin'.format(value, kelvin))
        return float(kelvin)
     if fromUnit.lower() == 'kelvin' and toUnit.lower() == 'celsius':
        celsius = value - 273.15
        print('{} degrees Kelvin is equal to {} degrees Celsius'.format(value, celsius))
        return float(celsius)
     if fromUnit.lower() == 'kelvin' and toUnit.lower() == 'fahrenheit':
        fahrenheit = (value * 9 / 5) - 459.67
        print('{} degrees Kelvin is equal to {} degrees Fahrenheit'.format(value, fahrenheit))
        return float(fahrenheit)



def convert(fromUnit, toUnit, value):
    try:
            # miles to yards
        if str(fromUnit).lower() == 'miles' and str(toUnit).lower() == 'yards':
            return   value * 1760
        # miles to meters
        elif str(fromUnit).lower() == 'miles' and str(toUnit).lower() == 'meters':
            return   value * 1609.344
        #  yards to miles
        elif str(fromUnit).lower() == 'yards' and str(toUnit).lower() == 'miles':
            return   value * 0.0005681
        # yards to meters
        elif str(fromUnit).lower() == 'yards' and str(toUnit).lower() == 'meters':
            return   value * 0.9144
        # meters to miles
        elif str(fromUnit).lower() == 'meters' and str(toUnit).lower() == 'miles':
            return   value * 0.000621
        # meters to yards
        elif str(fromUnit).lower() == 'meters' and str(toUnit).lower() == 'yards':
            return   value * 1.09361
        elif str(fromUnit).lower() == fromUnit.lower() and toUnit.lower() == toUnit.lower():
            return value
        else:
            raise ConversionNotPossible("Conversion Not Possible")
    except ConversionNotPossible as error:
        print(error.message)
        return error.message




class ConversionNotPossible(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return str(self.message)