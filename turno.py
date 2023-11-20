from collections import deque
from equipos import equipo_objeto

equipos = equipo_objeto.asignar_equipos()

def primer_turno(equipos):
    """
    Apartir de mi diccionario de listas 'equipos', devuelve una lista enlazada con el orden en el que comenzara la partida.

    :param equipos: un diccionario que contiene 2 diccionarios, con la puntuacion y los jugadores con sus fichas.
    :type equipos: dict[str, dict[str, Any]]
    """
    try:

        for equipo in equipos.values():
            for nombre_jugador, ficha in equipo.items():
                if isinstance(ficha, list) and (6,6) in ficha: #El isinstance() se utiliza para asegurarse de buscar solamente las listas, sin tomar en cuenta la puntuacion
                    primer_jugador = nombre_jugador
        # Crear un deque con 4 índices
        jugadores = deque()
        for i in range(len(equipos['equipo 1']) + len(equipos['equipo 2'])): # para que recorra el total de jugadores de ambos equipos (son 4 jugadores) 
            equipo_actual = f'equipo {i % len(equipos) + 1}' # aqui determina en que equipos estamos, si el resultado da 0 (es par) estamos en el equipo 1, de lo contrario, estamos en el equipo 2 
            for clave in equipos[equipo_actual].keys():
                if clave.startswith('jugador') and clave not in jugadores: #startswith() revisa el string y lo compara (a ver si la key tiene 'jugador') y tambien revisa si no esta en la lista enlazada
                    jugadores.append(clave)
                    break #esto para que se añada un jugador en cada iteracion
        while jugadores[0] != primer_jugador:
            jugadores.rotate(-1) #El rotate() rota la lista enlazada de derecha a izquierda hasta que encuentre el jugador con la cochina o (6,6)
        return jugadores  
   
    except UnboundLocalError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"Error inesperado {str(e)}"

primer_turno = primer_turno(equipos)

# Generador para recorrer y cambiar la persona que comienza 
def cambiar_jugador(rotacion):
    """
    Funcion generadora que rota el turno de cada jugador al contrario de las agujas del reloj.

    :param rotacion: la lista enlazada de jugadores a rotar.
    :type rotacion: deque
    """
    try:
        
        while True:
            yield rotacion[0]
            rotacion.rotate(-1) 
   
    except Exception as e:
        return f"Error inesperado {str(e)}"

def fichas_jugador(orden_jugadores, equipos):
    """
    Funcion generadora que rota el turno de las fichas de cada jugador al contrario de las agujas del reloj.

    :param orden_jugadores: la lista enlazada de jugadores a rotar.
    :type orden_jugadores: deque
    :param equipos: un diccionario que contiene 2 diccionarios, con la puntuacion y los jugadores con sus fichas.
    :type equipos: dict[str, dict[str, Any]]
    """        
    try:

        while True:  
            jugador_actual = orden_jugadores[0] 
            equipo_jugador_actual = None #si no coloco esto, me da un error de acceso, ya que de otra forma, solo lo declararia dentro del bloque for
            for nombre_equipo, equipo in equipos.items(): #el nombre_equipo es la key de equipos 
                for nombre_jugador in equipo: # el nombre_jugador es el key del valor de equipos (cada uno de los equipos)
                    if nombre_jugador == jugador_actual:
                        equipo_jugador_actual = nombre_equipo
                        break # para que salga del for en cuanto tenga el jugador actual
            fichas_jugador = equipos[equipo_jugador_actual][jugador_actual] 
            yield fichas_jugador  
            orden_jugadores.rotate(-1)  
   
    except KeyError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"Error inesperado {str(e)}"
    
