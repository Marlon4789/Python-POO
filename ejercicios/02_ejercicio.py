# Nave espacial

class Nave:
    def __init__(self, motor, sistema, radar):
        self.motor = motor
        self.sistema = sistema
        self.radar = radar

    def statusOn(self):
        print("Nave lista para despegar...")

    def statusOff(self):
        print("La nave no puede despegar, sorry")

while True:
    print(f"""
Para iniciar el despegue activar con 'on' 
y para abortar despegue 'off'\n 
""")

    motor = input('Encender motor: ')
    sistema = input('Encender sistema: ')
    radar = input('Encender radar: ')

    statusNave = Nave(motor,sistema,radar)

    if (motor.lower() == 'on' and sistema.lower()== 'on' and radar.lower()=='on'):
        statusNave.statusOn()
        exit()
    else:
        statusNave.statusOff()
        exit()





