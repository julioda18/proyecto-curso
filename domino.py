import time
from collections import deque
from equipos import equipo_objeto
import turno

TIEMPO_MENSAJE = 0.5
MAX_RONDAS = 10

equipos = turno.equipos # utilizo esta version para que coincida con las listas enlazadas
primer_turno = turno.primer_turno


def jugar_turno(jugador_actual, fichas_actual, ronda_actual, tablero):
    """
    Esta funcion juega la ronda hasta que uno de los jugadores quede sin fichas
    agregando cada una de las fichas que coincidan con los extremos del tablero en la lista enlazada "tablero".
    Al final del turno se realiza una sumatoria para asignar los puntos al equipo ganador.

    :param jugador_actual: el nombre del jugador actual.
    :type jugador_actual: str
    :param fichas_actual: una lista de tuplas que representa las fichas del jugador actual.
    :type fichas_actual: list
    :param ronda_actual: la ronda en donde se esta jugando.
    :type ronda_actual: int
    :param tablero: una lista enlzada vacia en donde se introduciran las fichas que se vayan jugando en la ronda.
    :type tablero: deque()
    """
    try:

        print(f"Turno del {jugador_actual}. Fichas: {fichas_actual}")
        time.sleep(TIEMPO_MENSAJE)

        if ronda_actual == 0 and (6,6) in fichas_actual:
            fichas_actual.remove((6,6))  
            tablero.append((6,6))
            print(f"Ficha (6, 6) agregada al tablero. Tablero actual: {tablero}")
            time.sleep(TIEMPO_MENSAJE)

        elif ronda_actual > 0 and len(tablero) == 0 and len(fichas_actual) > 0:
            primera_ficha = fichas_actual.pop(0)
            tablero.append(primera_ficha)
            print(f"Ficha {primera_ficha} agregada al tablero. Tablero actual: {tablero}")
            time.sleep(TIEMPO_MENSAJE)

        else:
            coincidencia_encontrada = False
            pasar = False

            for ficha in list(fichas_actual): #list() se utiliza para crear una copia de la lista
                if jugador_actual in equipos['equipo 1']:
                    equipo = 'equipo 1'
                else:
                    equipo = 'equipo 2'  

                for numero in ficha:
                    if numero == tablero[0][0] or numero == tablero[-1][1]:

                        if numero == tablero[0][0]:
                            if ficha[1] == tablero[0][0]:
                                ficha_a_agregar = ficha
                            else:
                                ficha_a_agregar = ficha[::-1]
                            tablero.appendleft(ficha_a_agregar)
                            print(f"Ficha {ficha_a_agregar} agregada al principio del tablero. Tablero actual: {tablero}")
                            time.sleep(TIEMPO_MENSAJE)

                        else:
                            if ficha[0] == tablero[-1][1]:
                                ficha_a_agregar = ficha
                            else:
                                ficha_a_agregar = ficha[::-1]
                            tablero.append(ficha_a_agregar)
                            print(f"Ficha {ficha_a_agregar} agregada al final del tablero. Tablero actual: {tablero}")
                            time.sleep(TIEMPO_MENSAJE)

                        if ficha in fichas_actual:
                            fichas_actual.remove(ficha)
                            print(f"Ficha {ficha} eliminada del arreglo de fichas del {jugador_actual}. Fichas de dominó actuales del {jugador_actual}: {fichas_actual}")
                            time.sleep(TIEMPO_MENSAJE)
                        coincidencia_encontrada = True
                        break

                if coincidencia_encontrada: # esta condicion se realiza para que salga al momento de la primera coincidencia
                    break

            if not coincidencia_encontrada:
                pasar = True

            if pasar:
                print(f"El {jugador_actual} no puede jugar una ficha. Pasando al siguiente jugador.")
                time.sleep(TIEMPO_MENSAJE)
                return False
                        
        if not fichas_actual:
            print(f"El {jugador_actual} se quedó sin fichas.")
            if equipo == 'equipo 2':
                equipo_contrario = 'equipo 1'
            else:
                equipo_contrario = 'equipo 2'

            total = 0
            for jugador_contrario, fichas_contrario in equipos[equipo_contrario].items():
                if jugador_contrario != 'puntuacion':
                    for ficha in fichas_contrario:
                        total += sum(ficha)
            equipos[equipo]['puntuacion'] += total
            print(f"Se añadieron {total} puntos al {equipo}")
            print(f"Puntuación actual del {equipo}: {equipos[equipo]['puntuacion']}")
            print(f"Puntuación actual del {equipo_contrario}: {equipos[equipo_contrario]['puntuacion']}")
            time.sleep(TIEMPO_MENSAJE)
            return True

        return False
    
    except TypeError as e:
        return f"Error: {e}"
    except KeyError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"Error inesperado {str(e)}"

def verificar_tranca(orden_jugadores, tablero):
    """
    Esta funcion verifica si al final de cada ronda existe una tranca
    En caso de que exista realiza una comprobacion para verificar quien obtuvo menos puntos, y asignar los puntos al ganador de la ronda

    :param orden_jugadores: una lista enlazada que contiene el orden de los jugadores.
    :type orden_jugadores: deque()
    :param tablero: una lista enlzada vacia en donde se introduciran las fichas que se vayan jugando en la ronda.
    :type tablero: deque()
    """
    try:

        tranca = True
        for jugador in orden_jugadores:
            if jugador in equipos['equipo 1']:
                fichas_a_jugador = equipos['equipo 1'][jugador]
            elif jugador in equipos['equipo 2']:
                fichas_a_jugador = equipos['equipo 2'][jugador]

            for ficha in fichas_a_jugador:
                if ficha[0] == tablero[0][0] or ficha[1] == tablero[-1][1]:
                    tranca = False
                    break

            if not tranca: 
                break

        if tranca:
            print("El juego está en un estado de 'tranca'. Nadie puede jugar una ficha.")
            time.sleep(TIEMPO_MENSAJE)
            
            total_equipo_1 = 0
            total_equipo_2 = 0
            for jugador, fichas in equipos['equipo 1'].items():
                if jugador != 'puntuacion':
                    for ficha in fichas:
                        total_equipo_1 += sum(ficha)
            for jugador, fichas in equipos['equipo 2'].items():
                if jugador != 'puntuacion':
                    for ficha in fichas:
                        total_equipo_2 += sum(ficha)
            
            print(f"Puntuacion del equipo 1: {total_equipo_1}")
            print(f"Puntuacion del equipo 2: {total_equipo_2}")
            time.sleep(TIEMPO_MENSAJE)

            if total_equipo_1 < total_equipo_2:
                equipos['equipo 1']['puntuacion'] += total_equipo_2
                print(f"El equipo 1 gana la ronda y obtiene {total_equipo_2} puntos. Puntuación actual del equipo 1: {equipos['equipo 1']['puntuacion']}")
            else:
                equipos['equipo 2']['puntuacion'] += total_equipo_1
                print(f"El equipo 2 gana la ronda y obtiene {total_equipo_1} puntos. Puntuación actual del equipo 2: {equipos['equipo 2']['puntuacion']}")
            time.sleep(TIEMPO_MENSAJE)
            return True

        return False
    
    except TypeError as e:
        return f"Error: {e}"
    except IndexError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"Error inesperado {str(e)}"

def jugar_rondas(primer_turno, max_rondas, equipos, ronda_actual=0):
    """
    Esta función maneja las rondas del juego mediante un ciclo While. 
    Cada ronda consiste en turnos de jugadores que juegan fichas hasta que se queden sin fichas o que ocurra una tranca.

    :param primer_turno: Una cola de jugadores que especifica el orden del primer turno.
    :type primer_turno: deque
    :param max_rondas: El número máximo de rondas a jugar.
    :type max_rondas: int
    :param equipos: un diccionario que contiene 2 diccionarios, con la puntuacion y los jugadores con sus fichas.
    :type equipos: dict[str, dict[str, Any]]
    :param ronda_actual: La ronda actual del juego. Por defecto es 0.
    :type tablero: int (opcional)
    """
    try:
        orden_jugadores = deque(primer_turno)
        tablero = deque()

        while ronda_actual < max_rondas:

            generador_jugadores = turno.cambiar_jugador(deque(orden_jugadores))  
            generador_fichas = turno.fichas_jugador(primer_turno, equipos) 
            print(f'Ronda {ronda_actual+1}')

            sin_fichas = False
            tranca = False
            
            while not sin_fichas and not tranca:

                for _ in range(len(orden_jugadores)):
                    jugador_actual = next(generador_jugadores)
                    fichas_actual = next(generador_fichas)
                    
                    sin_fichas = jugar_turno(jugador_actual, fichas_actual, ronda_actual, tablero)
                    if sin_fichas:
                        break

                if not sin_fichas:
                    tranca = verificar_tranca(orden_jugadores, tablero)

                if tranca:
                    break

            ronda_actual += 1 
            orden_jugadores.rotate(-1)
            equipo_objeto.redistribuir_fichas()
            tablero = deque()  # Vacía el tablero al final de la ronda


            if equipos['equipo 1']['puntuacion'] >= 100:
                print("El equipo 1 ha alcanzado 100 puntos. ¡El equipo 1 gana!")
                break
            elif equipos['equipo 2']['puntuacion'] >= 100:
                print("El equipo 2 ha alcanzado 100 puntos. ¡El equipo 2 gana!")
                break
            
            if ronda_actual == max_rondas:
                print("Se alcanzó el límite máximo de rondas sin 100 puntos.")
                print(f"Puntuacion del equipo 1: {equipos['equipo 1']['puntuacion']}")
                print(f"Puntuacion del equipo 2: {equipos['equipo 2']['puntuacion']}")
    except Exception as e:
        return f"Error inesperado {str(e)}"

jugar_rondas(primer_turno, MAX_RONDAS, equipos)