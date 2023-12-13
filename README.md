# Simulador de Domino

Proyecto final de curso de Python, el objetivo de este proyecto es crear una simulacion de un juego de dominó y mostrar su resultado en la consola.

### Conceptos de Python utilizados para la creacion de este proyecto:
- Variables y tipos de datos
-	Bucles (for, while)
-	Condicionales (if, elif, else)
-	Funciones
- Listas y manipulación de listas
- Diccionarios
- Clases
- Manejo de excepciones
- Funciones generadoras
- Listas enlazadas

### Clases de equipo.py
1. `Fichas`: Esta clase está diseñada para manejar un conjunto de fichas de dominó y jugadores. Tiene los siguientes métodos:
    - `__init__`: Este es el método constructor que inicializa una instancia de la clase. Configura una lista vacía para `fichas` y un diccionario vacío para `jugadores`.
    - `obtener_fichas`: Este método genera una lista de tuplas que representan todas las posibles fichas de dominó y la devuelve.
    - `revolver_fichas`: Este método toma un número como entrada y devuelve una lista de fichas de dominó seleccionadas al azar de la lista de todas las posibles fichas.
    - `fichas_a_repartir`: Este método toma un número como entrada, baraja las fichas de dominó y las asigna a cuatro jugadores. Devuelve un diccionario con los jugadores y sus fichas asignadas.

2. `Equipo`: Esta clase hereda de la clase `Fichas` y está diseñada para manejar equipos de jugadores. Tiene los siguientes métodos:
    - `__init__`: Este es el método constructor que inicializa una instancia de la clase. Llama al constructor de la clase padre (`Fichas`) usando `super().__init__()`, y configura un diccionario para `equipos` y un orden para los jugadores.
    - `asignar_equipos`: Este método asigna jugadores a equipos basándose en el orden definido en `self.orden`. Devuelve un diccionario con los equipos y sus jugadores y fichas asignadas.
    - `redistribuir_fichas`: Este método llama a `asignar_equipos` para redistribuir las fichas entre los jugadores.

### Funciones de turno.py
En primer lugar tenemos la funcion `primer_turno`:
1. **Identificación del primer jugador**: La función comienza recorriendo cada equipo en el diccionario `equipos`. Para cada equipo, recorre cada jugador y sus fichas. Si encuentra la ficha (6,6), guarda el nombre del jugador como `primer_jugador`.
2. **Creación de la cola de jugadores**: Luego, crea una cola `jugadores` y la llena con los nombres de los jugadores en un orden específico. El orden se determina por el número de equipo (equipo 1 o equipo 2) y se asegura de que cada jugador se añada una vez.
3. **Rotación de la cola de jugadores**: A continuación, rota la cola de jugadores hasta que el jugador con la ficha (6,6) esté en el frente.
4. **Retorno de la cola de jugadores**: Finalmente, devuelve la cola de jugadores, que ahora está en el orden correcto para comenzar el juego.
5. **Manejo de excepciones**: La función tiene un bloque `try/except` para manejar cualquier error inesperado que pueda ocurrir durante la ejecución.

Luego tenemos la función `cambiar_jugador`, que es una función generadora que se utiliza para rotar los turnos de los jugadores en un juego, y se desglosa de la siguiente forma:
1. **Ciclo infinito**: La función comienza con un ciclo `while True`, lo que significa que continuará indefinidamente hasta que se detenga explícitamente. Esto es típico de las funciones generadoras, que están diseñadas para ser utilizadas con la instrucción `next()` en otro lugar del código.
2. **Yield**: La instrucción `yield` se utiliza en las funciones generadoras para "producir" un valor que puede ser iterado. En este caso, `yield rotacion[0]` produce el primer jugador en la lista de rotación.
3. **Rotación**: Después de producir un jugador, la función rota la lista de jugadores una posición hacia la izquierda con `rotacion.rotate(-1)`. Esto mueve al primer jugador al final de la lista, y al segundo jugador al principio, preparándolo para ser el próximo en ser producido cuando se llame a `next()` en la función generadora.
4. **Manejo de excepciones**: Finalmente, la función tiene un bloque `try/except` para manejar cualquier error inesperado que pueda ocurrir durante la ejecución.

Y por ultimo se encuentra la funcion `fichas_jugador`, esta es una función generadora que se utiliza para rotar las fichas de los jugadores en un juego, los pasos que realiza son los siguientes:
1. **Ciclo infinito**: La función comienza con un ciclo `while True`, lo que significa que continuará indefinidamente hasta que se detenga explícitamente. Esto es típico de las funciones generadoras, que están diseñadas para ser utilizadas con la instrucción `next()` en otro lugar del código.
2. **Identificación del jugador actual y su equipo**: En cada iteración del ciclo, la función identifica al jugador actual y a qué equipo pertenece. Esto se hace recorriendo cada equipo y cada jugador en ese equipo hasta encontrar una coincidencia con el jugador actual.
3. **Yield**: La instrucción `yield` se utiliza en las funciones generadoras para "producir" un valor que puede ser iterado. En este caso, `yield fichas_jugador` produce las fichas del jugador actual.
4. **Rotación**: Después de producir las fichas de un jugador, la función rota la lista de jugadores una posición hacia la izquierda con `orden_jugadores.rotate(-1)`. Esto mueve al primer jugador al final de la lista, y al segundo jugador al principio, preparándolo para ser el próximo en ser producido cuando se llame a `next()` en la función generadora.
5. **Manejo de excepciones**: Finalmente, la función tiene un bloque `try/except` para manejar cualquier error inesperado que pueda ocurrir durante la ejecución.

### Funciones de domino.py
En primer lugar, se crea la función `jugar_turno`:
1. **Inicio del turno**: La función comienza imprimiendo el nombre del jugador actual y sus fichas.
2. **Primer turno**: Si es la primera ronda (`ronda_actual == 0`) y el jugador tiene la ficha (6,6), esta ficha se juega primero y se elimina de las fichas del jugador.
3. **Turnos posteriores**: Si no es la primera ronda y el tablero está vacío, se juega la primera ficha del jugador.
4. **Jugada de fichas**: Si ninguna de las condiciones anteriores se cumple, se entra en un ciclo donde se intenta jugar una ficha que coincida con los extremos del tablero. Si se encuentra una coincidencia, se juega la ficha y se elimina de las fichas del jugador.
5. **Pasar turno**: Si no se encuentra ninguna coincidencia, el jugador pasa su turno.
6. **Fin del turno**: Si el jugador se queda sin fichas, se anuncia y se termina el turno.
7. **Manejo de excepciones**: Finalmente, la función tiene un bloque `try/except` para manejar cualquier error inesperado que pueda ocurrir durante la ejecución del turno.

Luego, creamos la función `verificar_tranca`:
1. **Verificación de tranca**: La función comienza asumiendo que hay una tranca (`tranca = True`). Luego, para cada jugador en el orden de jugadores, verifica si alguna de sus fichas puede ser jugada en el tablero. Si se encuentra una ficha que puede ser jugada, se establece `tranca = False` y se rompe el ciclo.
2. **Estado de tranca**: Si después de verificar todas las fichas de todos los jugadores, `tranca` sigue siendo `True`, entonces el juego está en un estado de tranca y nadie puede jugar una ficha.
3. **Cálculo de puntuación**: En caso de tranca, se calcula la puntuación total de cada equipo sumando los valores de todas sus fichas.
4. **Asignación de puntos**: Los puntos del equipo con mayor puntuación se suman a la puntuación del equipo contrario. El equipo con menos puntos gana la ronda.
5. **Manejo de excepciones**: Finalmente, la función tiene un bloque `try/except` para manejar cualquier error inesperado que pueda ocurrir durante la verificación de la tranca.


Por ultimo tenemos la funcion `jugar_rondas`:
1. **Inicialización**: La función comienza inicializando la cola de jugadores (`orden_jugadores`) y el tablero (`tablero`) con los valores del primer turno y un deque vacío, respectivamente.
2. **Ciclo de rondas**: Luego entra en un ciclo `while` que se ejecuta hasta que el número de rondas jugadas (`ronda_actual`) sea menor que el número máximo de rondas (`max_rondas`).
3. **Generadores de jugadores y fichas**: Dentro de este ciclo, se crean dos generadores: `generador_jugadores`, que cambia el jugador actual en cada turno, y `generador_fichas`, que genera las fichas del jugador actual.
4. **Ciclo de turnos**: A continuación, se entra en otro ciclo `while` que se ejecuta hasta que un jugador se queda sin fichas (`sin_fichas`) o se produce una tranca (`tranca`).
5. **Jugada de turno**: Dentro de este ciclo, se juega un turno para cada jugador en el orden actual. Si un jugador se queda sin fichas durante su turno, se rompe el ciclo de turnos.
6. **Verificación de tranca**: Si ningún jugador se quedó sin fichas, se verifica si hay una tranca en el tablero. Si hay una tranca, se rompe el ciclo de turnos.
7. **Final de la ronda**: Al final de cada ronda, se incrementa el número de rondas jugadas, se rota el orden de los jugadores, se redistribuyen las fichas y se vacía el tablero.
8. **Verificación de puntuación**: Se verifica si alguno de los equipos ha alcanzado 100 puntos. Si es así, se anuncia al ganador y se rompe el ciclo de rondas.
9. **Límite de rondas**: Si se alcanza el número máximo de rondas sin que ningún equipo alcance 100 puntos, se anuncian las puntuaciones finales de ambos equipos.
10. **Manejo de excepciones**: Finalmente, la función tiene un bloque `try/except` para manejar cualquier error inesperado que pueda ocurrir durante la ejecución del juego.

