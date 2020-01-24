#Geg.: Temperatur in Celsius C
#Ges.> Temperatur in Kelvin K
# K = C + 273.15

def get_temperature():
    while True:
        C = input('Gib die Temperatur in Grad Celsius ein:')
        try:
            C = float(C)
            return C
        except ValueError:
                print('Das ist keine Temperaturangabe')
def convert_to_kelvin(C):             
    K = C + 273.15
    return K
if __name__ == '__main__':
        C = get_temperature()
        print('Das sind ' + str(convert_to_kelvin(C)) + ' Kelvin')

#Fertig