# 🛡️ Teraware Tactical Hub (TTH)

**Teraware Tactical Hub (TTH)** es un entorno de automatización de escritorio y estación táctica desarrollado en Python utilizando `CustomTkinter` y `psutil`. Cuenta con una arquitectura modular basada en un registro dinámico de comandos operativos y un motor arcade de supervivencia integrado.

---

## 🚀 Características Principales
* **21 Comandos Operativos:** Sistema centralizado e independiente para gestión del sistema, herramientas de red, entretenimiento y accesos directos.
* **Monitoreo en Vivo (`psutil`):** Telemetría en tiempo real de CPU, RAM y consumo de procesos de la estación.
* **Modo Arcade de Supervivencia:** Miniserie integrada de combate y esquive con colisión letal y sistema de puntuación.
* **Interfaz Oscura Moderna:** Diseño estilizado optimizado mediante `CustomTkinter`.

---

## ⌨️ Listado de Comandos Operativos
1. `hola` : Saludo táctico operativo y reconocimiento de identidad.
2. `estado` : Reporte detallado del búnker, estación y operador.
3. `hora` : Hora del sistema en tiempo real.
4. `fecha` : Fecha actual del sistema.
5. `calendario` : Visualizador mensual y registro persistente.
6. `directorio` : Historial automático de comandos ejecutados.
7. `mundo` : Módulo global de información y hora UTC.
8. `chiste` : Humor y bromas de programador.
9. `telemetria` : Monitoreo en vivo de CPU, RAM y Disco.
10. `procesos` : Top de aplicaciones con mayor consumo de memoria.
11. `bass` : Panel de ajuste de audio y efectos de graves.
12. `buscar <txt>` : Localizador rápido en la ruta de usuario.
13. `minijuego` : Entretenimiento interactivo alternativo.
14. `tiktok` : Lanzamiento rápido al estudio de creador.
15. `youtube` : Lanzamiento rápido de YouTube.
16. `abrir <app>` : Ejecutor de programas del sistema (ej: `abrir notepad`).
17. `jugar` : Inicia el motor arcade de supervivencia letal.
18. `detener` : Pausa el visor de juego.
19. `limpiar` : Limpia la consola y refresca el workspace.
20. `ayuda` : Muestra el menú completo de comandos.
21. `salir` : Cierra de forma segura la ejecución del sistema.

---

## 🎮 Controles del Minijuego Arcade
* **[A]** : Movimiento a la izquierda
* **[D]** : Movimiento a la derecha
* **[E]** : Movimiento hacia arriba
* **[X]** : Movimiento hacia abajo
* **[ESPACIO]** : Disparo de proyectiles tácticos contra los BUGS.

---

## 🛠️ Requisitos e Instalación
Asegúrate de tener instalado Python 3.x y las dependencias necesarias ejecutando en tu terminal:

```bash
pip install customtkinter psutil
