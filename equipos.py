import random 

class Fichas():
    def __init__(self):
        self.fichas = []
        self.jugadores = {}
    
    def obtener_fichas(self):
        """
        Devuelve una lista de tuplas que contienen 2 elementos numericos.
        """
        try:
            for i in range(7):
                for j in range(i, 7):
                    self.fichas.append((i,j))
            return self.fichas
        except Exception as e:
            return f"Error inesperado {str(e)}"
    
    def revolver_fichas(self, cantidad):
        """
        Toma la lista de fichas y devuelve la lista con los elementos (las tuplas de numeros) puestos de forma aleatoria.

        :param cantidad: una cantidad numerica.
        :type cantidad: int
        """
        try:
            fichas_revueltas = random.sample(self.fichas, cantidad)
            return fichas_revueltas
        except ValueError as e:
            return f"Error: {e}"
        except Exception as e:
            return f"Error inesperado {str(e)}"
        
    def fichas_a_repartir(self, cantidad):
        """
        Devuelve un diccionario con 4 jugadores con 7 fichas c/u.

        :param cantidad: una cantidad numerica.
        :type cantidad: int
        """
        try:
            revolver_fichas = self.revolver_fichas(cantidad)
            for i in range(4):
                self.jugadores[f"jugador {i+1}"] = revolver_fichas[i*7:(i+1)*7] 
            return self.jugadores
        except Exception as e:
            return f"Error inesperado {str(e)}"

class Equipo(Fichas):
    def __init__(self):
        super().__init__()
        self.equipos = {
            "equipo 1": {
                "puntuacion": 0,
            },
            "equipo 2": {
                "puntuacion": 0,
            }
        }
        self.orden = {'jugador 1': 1, 'jugador 2': 3, 'jugador 3': 2, 'jugador 4': 4}
        
    def asignar_equipos(self):
        """
        Esta funcion utiliza el diccionario de jugadores, lo reordena utilizando las directrices dadas en la variable orden
        y añade 2 a cada equipo, devolviendo un diccionario de diccionarios.
        """
        try:
            self.jugadores = self.fichas_a_repartir(len(self.obtener_fichas()))
            jugadores_ordenados = sorted(self.jugadores, key=self.orden.get)
            for i in range(len(jugadores_ordenados)):
                if i < len(jugadores_ordenados) / 2:
                    self.equipos["equipo 1"][jugadores_ordenados[i]] = self.jugadores[jugadores_ordenados[i]]
                else:
                    self.equipos["equipo 2"][jugadores_ordenados[i]] = self.jugadores[jugadores_ordenados[i]]
            return self.equipos
        except Exception as e:
            return f"Error inesperado {str(e)}"
        
    def redistribuir_fichas(self): 
        """
        Esta funcion llama a la asignacion de equipos para devolver el diccionario de diccionarios con nuevas fichas.
        """
        try:
            return self.asignar_equipos()
        except Exception as e:
            return f"Error inesperado {str(e)}"

equipo_objeto = Equipo() #se inicializa una instancia de Equipo()

