
class cine:
    def __init__(self, sele) -> None:
        self.sele = sele
    
    def zona (self, pelicula):
        print (' Elija su pelicula: 1. Crepusculo, 2. Iron man, 3. Hulk')
        sele = input() #escogemos la pelicula
        
        if sele == 1:
            print ('horas disponible: 3 pm, 6 pm, 9 pm')
            print ('digite la hora a la que quiere ver su pelicula')
            hora = input ()
            while hora != 3 or hora != 6 or hora != 9:
                 print ('la hora no es valida, digitela de nuevo')
                 hora = input ()
            posicion = (1, 100)
            print ('elija su posicion')
            posicion = input()
            
            print('¿Cual es la cantidad de voletos que desea?')
            boletos = input ()

        