
class cine:
    def __init__(self, se) -> None:
        self.se = se
    
    def selec_peli (self, pelicula):
        print (' Elija su pelicula: 1. Crepusculo, 2. Iron man, 3. Hulk')
        se = input()
        
        if se == 1:
            print ('horas disponible: 3 pm, 6 pm, 9 pm')
            print ('digite la hora a la que quiere ver su pelicula')
            hora = input ()
            while hora != 3 or hora != 6 or hora != 9:
                 print ('la hora no es valida, digitela de nuevo')
                 hora = input ()
            
        