import random
import array

def Generate(count,tempMin,tempMax,pressMin, pressMax,wetMin,wetMax,radMin,radMax,windStrMin, windStrMax):
    #GeneratorList = []
    jsonTmp = {}
    if count == 3:
        #GeneratorList.append(tempGenerator(tempMin, tempMax))
        #GeneratorList.append(pressureGenerator(pressMin,pressMax))
        #GeneratorList.append(wetGenerator(wetMin,wetMax))
        jsonTmp ={'temp':tempGenerator(tempMin, tempMax),'pressure':pressureGenerator(pressMin,pressMax),'wet':wetGenerator(wetMin,wetMax)}
    if count == 4:
        #GeneratorList.append(tempGenerator(tempMin, tempMax))
        #GeneratorList.append(pressureGenerator(pressMin, pressMax))
        #GeneratorList.append(wetGenerator(wetMin, wetMax))
        #GeneratorList.append(windStrengthGenerator(windStrMin,windStrMax))
        jsonTmp = {'temp': tempGenerator(tempMin, tempMax), 'pressure': pressureGenerator(pressMin, pressMax),
                   'wet': wetGenerator(wetMin, wetMax),'wind_strength':windStrengthGenerator(windStrMin,windStrMax)}
    if count == 5:
        #GeneratorList.append(tempGenerator(tempMin, tempMax))
        #GeneratorList.append(pressureGenerator(pressMin, pressMax))
        #GeneratorList.append(wetGenerator(wetMin, wetMax))
        #GeneratorList.append(windStrengthGenerator(windStrMin, windStrMax))
        #GeneratorList.append(radiationGenerator(radMin,radMax))
        jsonTmp = {'temp': tempGenerator(tempMin, tempMax), 'pressure': pressureGenerator(pressMin, pressMax),
                   'wet': wetGenerator(wetMin, wetMax), 'wind_strength': windStrengthGenerator(windStrMin, windStrMax),'radiation':radiationGenerator(radMin,radMax)}
    return jsonTmp

def tempGenerator(min,max):
    temp=random.randint(min,max)
    return temp

def pressureGenerator(min,max):
    pressure=random.randint(min,max)
    return pressure

def wetGenerator(min,max):
    wet = random.randint(min,max)
    return wet

def radiationGenerator(min,max):
    radiation = random.uniform(min,max)
    return round(radiation,3)

def windStrengthGenerator(min,max):
    windStrength = random.uniform(min,max)
    return  round(windStrength,3)
