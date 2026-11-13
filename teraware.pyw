import calendar
from datetime import datetime
import os
import platform
import random
import subprocess
import threading
import time
import webbrowser
import customtkinter as ctk

try:
  import psutil
except ImportError:
  psutil = None

historial_comandos = []


def cmd_hola(*args):
  return "• hola         : Saludo táctico operativo y reconocimiento de identidad"


def cmd_estado(*args):
  return "• estado       : Reporte detallado del búnker, estación y Comandante"


def cmd_hora(*args):
  return f"• hora         : Hora del sistema en tiempo real -> {datetime.now().strftime('%H:%M:%S')}"


def cmd_fecha(*args):
  return f"• fecha        : Fecha actual del sistema -> {datetime.now().strftime('%A, %d de %B de %Y')}"


def cmd_calendario(*args):
  cal_txt = calendar.month(datetime.now().year, datetime.now().month)
  return f"• calendario   : Visualizador mensual y registro persistente:\n{cal_txt}"


def cmd_directorio(*args):
  return f"• directorio   : Historial automático y persistente. Total ejecutados: {len(historial_comandos)}"


def cmd_mundo(*args):
  return f"• mundo        : Módulo global de información y hora mundial (UTC: {datetime.utcnow().strftime('%H:%M:%S')})"


def cmd_chiste(*args):
  chistes = [
      "¿Por qué los programadores prefieren el invierno? ¡Porque odian los bugs!",
      "Hay 10 tipos de personas: los que entienden binario y los que no.",
      "Un SQL entra a un bar, se acerca a dos mesas y pregunta: '¿Puedo unirme?'",
  ]
  return f"• chiste       : {random.choice(chistes)}"


def cmd_telemetria(*args):
  if psutil:
    cpu = psutil.cpu_percent(interval=0.1)
    ram = psutil.virtual_memory().percent
    disco = psutil.disk_usage("/").percent
    return f"• telemetria   : Monitoreo en vivo -> CPU: {cpu}% | RAM: {ram}% | Disco: {disco}%"
  return "• telemetria   : psutil no disponible."


def cmd_procesos(*args):
  if psutil:
    procs = []
    for p in psutil.process_iter(["name", "memory_percent"]):
      try:
        procs.append(p.info)
      except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass
    procs = sorted(procs, key=lambda x: x["memory_percent"] or 0, reverse=True)[
        :4
    ]
    res = "• procesos     : Top apps con más consumo de memoria:\n"
    for p in procs:
      mem = round(p["memory_percent"] or 0, 2)
      res += f"   - {p['name']} ({mem}% RAM)\n"
    return res
  return "• procesos     : psutil no disponible."


def cmd_bass(*args):
  return "• bass         : Panel de ajuste de audio y efecto de graves (LD-S623)"


def cmd_buscar(argumento):
  if not argumento:
    return "⚠️ Uso incorrecto. Escribe por ejemplo: `buscar documento`"
  return f"• buscar <texto>: Localizador rápido ejecutado para: '{argumento}'"


def cmd_minijuego(*args):
  num = random.randint(1, 10)
  return f"• minijuego    : Módulo interactivo de entretenimiento (Adivina el Número 1-10, secreto: {num})"


def cmd_tiktok(*args):
  webbrowser.open("https://www.tiktok.com/live/creator")
  return (
      "• tiktok       : Lanzamiento rápido de TikTok / Estudio de Creador"
      " (Gamer Latino)"
  )


def cmd_youtube(*args):
  webbrowser.open("https://www.youtube.com")
  return "• youtube      : Lanzamiento rápido de YouTube en el navegador"


def cmd_abrir(argumento):
  if not argumento:
    return (
        "⚠️ Uso incorrecto. Escribe por ejemplo: `abrir notepad` o `abrir"
        " chrome`"
    )
  try:
    if platform.system() == "Windows":
      os.system(f"start {argumento}")
    else:
      subprocess.Popen([argumento])
    return f"• abrir <app>  : Programa '{argumento}' iniciado con éxito"
  except Exception as e:
    return f"❌ [ERROR]: No se pudo abrir '{argumento}' ({e})"


def cmd_jugar(*args):
  return "ACTIVAR_VISOR_JUEGO"


def cmd_detener(*args):
  return "DETENER_VISOR_JUEGO"


def cmd_limpiar(*args):
  return "LIMPIAR_PANTALLA_COMANDO"


def cmd_ayuda(*args):
  return (
      "🛠️ [MENÚ DE AYUDA - TTH v3.23 (FINAL PULIDO)]:\n"
      "1. hola         : Saludo táctico operativo y reconocimiento de identidad\n"
      "2. estado       : Reporte detallado del búnker, estación y Comandante\n"
      "3. hora         : Hora del sistema en tiempo real\n"
      "4. fecha        : Fecha actual del sistema\n"
      "5. calendario   : Visualizador mensual y registro persistente de comandos\n"
      "6. directorio   : Historial automático y persistente de todo lo ejecutado en el TTH\n"
      "7. mundo        : Módulo global de información y hora mundial del planeta\n"
      "8. chiste       : Humor y bromas de programador\n"
      "9. telemetria   : Monitoreo en vivo de CPU, RAM y Disco\n"
      "10. procesos    : Listado de las apps con más consumo de memoria\n"
      "11. bass        : Panel de ajuste de audio y efecto de graves (LD-S623)\n"
      "12. buscar <txt>: Localizador rápido en la carpeta de usuario\n"
      "13. minijuego   : Módulo interactivo de entretenimiento (Adivina el Número)\n"
      "14. tiktok      : Lanzamiento rápido de TikTok / Estudio de Creador\n"
      "15. youtube     : Lanzamiento rápido de YouTube\n"
      "16. abrir <app> : Inicia un programa (ej: abrir spotify, notepad, chrome)\n"
      "17. jugar       : Inicia el motor arcade de Supervivencia\n"
      "18. detener     : Pausa el visor de juego\n"
      "19. limpiar     : Limpia la pantalla y refresca la interfaz\n"
      "20. ayuda       : Muestra este menú de ayuda\n"
      "21. salir       : Cierra la ejecución del sistema"
  )


def cmd_salir(*args):
  return "CERRAR_SISTEMA_COMANDO"


COMANDOS_REGISTRO = {
    "hola": cmd_hola,
    "saludos": cmd_hola,
    "estado": cmd_estado,
    "status": cmd_estado,
    "hora": cmd_hora,
    "fecha": cmd_fecha,
    "calendario": cmd_calendario,
    "directorio": cmd_directorio,
    "mundo": cmd_mundo,
    "chiste": cmd_chiste,
    "telemetria": cmd_telemetria,
    "procesos": cmd_procesos,
    "bass": cmd_bass,
    "buscar": cmd_buscar,
    "minijuego": cmd_minijuego,
    "tiktok": cmd_tiktok,
    "youtube": cmd_youtube,
    "abrir": cmd_abrir,
    "jugar": cmd_jugar,
    "proyectar": cmd_jugar,
    "detener": cmd_detener,
    "stop": cmd_detener,
    "limpiar": cmd_limpiar,
    "clear": cmd_limpiar,
    "ayuda": cmd_ayuda,
    "help": cmd_ayuda,
    "salir": cmd_salir,
    "exit": cmd_salir,
}


def ejecutar_comando_local(prompt_usuario):
  global historial_comandos
  comando_raw = prompt_usuario.strip()
  historial_comandos.append(
      f"[{datetime.now().strftime('%H:%M:%S')}] {comando_raw}"
  )
  time.sleep(0.02)

  partes = comando_raw.split(" ", 1)
  cmd_principal = partes[0].lower()
  argumento = partes[1] if len(partes) > 1 else ""

  if cmd_principal in COMANDOS_REGISTRO:
    return COMANDOS_REGISTRO[cmd_principal](argumento)
  else:
    return (
        f"Comando '{prompt_usuario}' no reconocido. Escribe 'ayuda' para ver el"
        " menú."
    )


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")


class TerawareApp(ctk.CTk):

  def __init__(self):
    super().__init__()

    self.geometry("1100x780")
    self.title("Teraware Tactical Hub (TTH) - v3.23 | ULTIMATE ARCADE")
    self.resizable(True, True)

    self.grid_columnconfigure(1, weight=1)
    self.grid_rowconfigure(1, weight=1)

    self.juego_activo = False
    self.game_over = False
    self.pos_x = 100
    self.pos_y = 150
    self.velocidad = 12
    self.balas = []
    self.obstaculos = [
        {"x": 600, "y": 80, "w": 40, "h": 40, "boom": 0},
        {"x": 500, "y": 190, "w": 40, "h": 40, "boom": 0},
        {"x": 700, "y": 140, "w": 40, "h": 40, "boom": 0},
    ]
    self.puntuacion = 0

    # Barra Superior
    self.top_bar = ctk.CTkFrame(
        self, height=42, corner_radius=0, fg_color="#181818"
    )
    self.top_bar.grid(row=0, column=0, columnspan=2, sticky="nsew")

    self.lbl_title_top = ctk.CTkLabel(
        self.top_bar,
        text="🛡️ TTH v3.23 | 21 COMANDOS & SUPERVIVENCIA LETAL",
        font=("Consolas", 14, "bold"),
        text_color="#FFFFFF",
    )
    self.lbl_title_top.pack(side="left", padx=20)

    self.lbl_live_hud = ctk.CTkLabel(
        self.top_bar,
        text="CPU: --%  |  RAM: --%  🟢",
        font=("Consolas", 12, "bold"),
        text_color="#00FF66",
    )
    self.lbl_live_hud.pack(side="right", padx=20)

    # Panel Lateral
    self.sidebar = ctk.CTkFrame(
        self, width=220, corner_radius=0, fg_color="#121212"
    )
    self.sidebar.grid(row=1, column=0, sticky="nsew")

    self.lbl_side_title = ctk.CTkLabel(
        self.sidebar,
        text="TERAWARE\nSTUDIO V3.23",
        font=("Consolas", 12, "bold"),
        justify="left",
        text_color="#3399FF",
    )
    self.lbl_side_title.pack(padx=15, pady=(15, 10), anchor="w")

    cmds_rapidos = [
        ("> Jugar Arcade", "jugar"),
        ("> Detener Visor", "detener"),
        ("> Ver Telemetría", "telemetria"),
        ("> Ver Procesos", "procesos"),
        ("> Abrir TikTok", "tiktok"),
        ("> Abrir YouTube", "youtube"),
        ("> Ayuda / Menú", "ayuda"),
        ("> Limpiar Consola", "limpiar"),
        ("> Salir del Hub", "salir"),
    ]

    for texto_btn, cmd_val in cmds_rapidos:
      btn = ctk.CTkButton(
          self.sidebar,
          text=texto_btn,
          font=("Consolas", 11),
          fg_color="#1a1a1a",
          hover_color="#262626",
          anchor="w",
          command=lambda c=cmd_val: self.ejecutar_comando_directo(c),
      )
      btn.pack(fill="x", padx=12, pady=3)

    # Telemetría
    self.tele_frame = ctk.CTkFrame(
        self.sidebar,
        fg_color="#161616",
        corner_radius=6,
        border_width=1,
        border_color="#2b2b2b",
    )
    self.tele_frame.pack(side="bottom", fill="x", padx=12, pady=15)

    self.lbl_cpu_val = ctk.CTkLabel(
        self.tele_frame, text="CPU  : --", font=("Consolas", 10), text_color="#00FF66"
    )
    self.lbl_cpu_val.pack(padx=10, pady=2, anchor="w")
    self.lbl_ram_val = ctk.CTkLabel(
        self.tele_frame, text="RAM  : --", font=("Consolas", 10), text_color="#00FF66"
    )
    self.lbl_ram_val.pack(padx=10, pady=(2, 6), anchor="w")

    # Área Central
    self.main_workspace = ctk.CTkFrame(
        self, fg_color="#0e0e0e", corner_radius=0
    )
    self.main_workspace.grid(row=1, column=1, sticky="nsew")
    self.main_workspace.grid_columnconfigure(0, weight=1)
    self.main_workspace.grid_rowconfigure(0, weight=3)
    self.main_workspace.grid_rowconfigure(1, weight=2)

    # Visor Superior
    self.viewport_frame = ctk.CTkFrame(
        self.main_workspace,
        fg_color="#080808",
        corner_radius=8,
        border_width=1,
        border_color="#2a2a2a",
    )
    self.viewport_frame.grid(
        row=0, column=0, sticky="nsew", padx=15, pady=(15, 7)
    )

    self.viewport_header = ctk.CTkFrame(
        self.viewport_frame, height=28, fg_color="#141414", corner_radius=6
    )
    self.viewport_header.pack(fill="x", padx=4, pady=4)

    self.lbl_viewport_info = ctk.CTkLabel(
        self.viewport_header,
        text=(
            "🎮 CONTROLES: [A] Izq | [D] Der | [E] Sub | [X] Baj | [ESPACIO]"
            " Disparo"
        ),
        font=("Consolas", 10, "bold"),
        text_color="#3399FF",
    )
    self.lbl_viewport_info.pack(side="left", padx=10)

    self.game_canvas = ctk.CTkCanvas(
        self.viewport_frame, bg="#050505", highlightthickness=0
    )
    self.game_canvas.pack(fill="both", expand=True, padx=6, pady=(0, 6))
    self.dibujar_pantalla_espera()

    self.bind("<Key>", self.manejar_tecla)

    # Consola Inferior
    self.console_frame = ctk.CTkFrame(
        self.main_workspace,
        fg_color="#121212",
        corner_radius=8,
        border_width=1,
        border_color="#242424",
    )
    self.console_frame.grid(
        row=1, column=0, sticky="nsew", padx=15, pady=(7, 15)
    )

    self.chat_log = ctk.CTkTextbox(
        self.console_frame,
        height=270,
        corner_radius=6,
        fg_color="#0a0a0a",
        text_color="#00FF99",
        font=("Consolas", 11),
    )
    self.chat_log.pack(fill="both", expand=True, padx=10, pady=(10, 6))
    self.chat_log.configure(state="disabled")

    self.input_frame = ctk.CTkFrame(
        self.console_frame, fg_color="#161616", height=44, corner_radius=6
    )
    self.input_frame.pack(fill="x", padx=10, pady=(0, 10))

    self.entry_msg = ctk.CTkEntry(
        self.input_frame,
        height=32,
        placeholder_text="Escribe comando (ej: ayuda, jugar, telemetria, bass)...",
        font=("Consolas", 11),
        fg_color="#0d0d0d",
    )
    self.entry_msg.pack(side="left", fill="x", expand=True, padx=(8, 8), pady=6)
    self.entry_msg.bind("<Return>", lambda event: self.iniciar_proceso_envio())

    self.btn_enviar = ctk.CTkButton(
        self.input_frame,
        width=85,
        height=32,
        text="ENVIAR",
        font=("Consolas", 11, "bold"),
        fg_color="#1f538d",
        hover_color="#14375b",
        command=self.iniciar_proceso_envio,
    )
    self.btn_enviar.pack(side="right", padx=(0, 8), pady=6)

    self.mostrar_en_pantalla(
        "Comandante, Teraware Tactical Hub v3.23 listo y optimizado.\n"
        " • Escribe 'ayuda' para ver los 21 comandos operativos.\n"
        " • Escribe 'jugar' para iniciar la supervivencia arcade letal.\n\n"
    )

    self.actualizar_telemetria_continua()

  def actualizar_telemetria_continua(self):
    if psutil:
      cpu = psutil.cpu_percent(interval=None)
      ram = psutil.virtual_memory().percent
      self.lbl_cpu_val.configure(text=f"CPU  : {cpu}%")
      self.lbl_ram_val.configure(text=f"RAM  : {ram}%")
      self.lbl_live_hud.configure(text=f"CPU: {cpu}%  |  RAM: {ram}%  🟢")
    self.after(1500, self.actualizar_telemetria_continua)

  def dibujar_pantalla_espera(self):
    self.game_canvas.delete("all")
    self.game_canvas.create_text(
        380,
        130,
        text=(
            "[ TTH v3.23 EN ESPERA ]\nEscribe 'jugar' para iniciar arcade o"
            " 'ayuda' para los comandos"
        ),
        fill="#666666",
        font=("Consolas", 12),
        justify="center",
    )

  def iniciar_juego(self):
    self.juego_activo = True
    self.game_over = False
    self.pos_x = 100
    self.pos_y = 150
    self.puntuacion = 0
    self.balas = []
    self.obstaculos = [
        {"x": 650, "y": 80, "w": 40, "h": 40, "boom": 0},
        {"x": 550, "y": 190, "w": 40, "h": 40, "boom": 0},
        {"x": 750, "y": 140, "w": 40, "h": 40, "boom": 0},
    ]
    self.focus_force()
    self.lbl_viewport_info.configure(
        text="🎮 MISIÓN ACTIVA | ¡Los BUGS te acechan! ¡Dispara! 🟢",
        text_color="#00FF66",
    )
    self.bucle_juego()

  def detener_juego(self):
    self.juego_activo = False
    self.lbl_viewport_info.configure(
        text="🎮 COMBATE PAUSADO 🔴", text_color="#FF5555"
    )
    self.game_canvas.delete("all")
    self.game_canvas.create_text(
        380,
        130,
        text="[ JUEGO PAUSADO ]\nEscribe 'jugar' para reanudar",
        fill="#FF5555",
        font=("Consolas", 12),
        justify="center",
    )

  def manejar_tecla(self, event):
    if not self.juego_activo or self.game_over:
      return
    if self.focus_get() == self.entry_msg:
      return

    tecla = event.char.lower()
    ancho = self.game_canvas.winfo_width() or 750
    alto = self.game_canvas.winfo_height() or 260

    if tecla == "a":
      self.pos_x = max(20, self.pos_x - self.velocidad)
    elif tecla == "d":
      self.pos_x = min(ancho - 45, self.pos_x + self.velocidad)
    elif tecla == "e":
      self.pos_y = max(20, self.pos_y - self.velocidad)
    elif tecla == "x":
      self.pos_y = min(alto - 45, self.pos_y + self.velocidad)
    elif event.keysym == "space":
      self.balas.append({"x": self.pos_x + 35, "y": self.pos_y + 18, "r": 6})

  def bucle_juego(self):
    if not self.juego_activo:
      return

    ancho = self.game_canvas.winfo_width() or 750
    alto = self.game_canvas.winfo_height() or 260

    self.game_canvas.delete("all")

    for x in range(0, ancho, 40):
      self.game_canvas.create_line(x, 0, x, alto, fill="#111111")
    for y in range(0, alto, 40):
      self.game_canvas.create_line(0, y, ancho, y, fill="#111111")

    nuevas_balas = []
    for bala in self.balas:
      bala["x"] += 16
      if bala["x"] < ancho:
        self.game_canvas.create_oval(
            bala["x"] - bala["r"],
            bala["y"] - bala["r"],
            bala["x"] + bala["r"],
            bala["y"] + bala["r"],
            fill="#00FFFF",
            outline="#FFFFFF",
        )
        nuevas_balas.append(bala)
    self.balas = nuevas_balas

    for obs in self.obstaculos:
      if obs["boom"] > 0:
        obs["boom"] -= 1
        self.game_canvas.create_oval(
            obs["x"] - 15,
            obs["y"] - 15,
            obs["x"] + obs["w"] + 15,
            obs["y"] + obs["h"] + 15,
            fill="#FF3300",
            outline="#FFFF00",
            width=4,
        )
        self.game_canvas.create_text(
            obs["x"] + 20,
            obs["y"] - 15,
            text="💥 ¡BOOM!",
            fill="#FFFF00",
            font=("Consolas", 11, "bold"),
        )
        if obs["boom"] == 0:
          obs["x"] = ancho + random.randint(50, 150)
          obs["y"] = random.randint(30, alto - 70)
        continue

      obs["x"] -= 4.0  # Incremento sutil de velocidad para mayor desafío
      if obs["x"] < -50:
        obs["x"] = ancho + random.randint(50, 150)
        obs["y"] = random.randint(30, alto - 70)

      # Colisión Letal Directa: Bug destruye al Jugador
      if (
          self.pos_x < obs["x"] + obs["w"]
          and self.pos_x + 38 > obs["x"]
          and self.pos_y < obs["y"] + obs["h"]
          and self.pos_y + 38 > obs["y"]
      ):
        self.juego_activo = False
        self.game_over = True
        self.lbl_viewport_info.configure(
            text="💀 GAME OVER: ¡Un BUG destruyó tu nave!",
            text_color="#FF3333",
        )
        self.game_canvas.delete("all")
        self.game_canvas.create_text(
            ancho / 2,
            alto / 2 - 15,
            text=(
                f"💀 GAME OVER 💀\nPuntuación Final: {self.puntuacion}\nEscribe"
                " 'jugar' o presiona el botón para revivir"
            ),
            fill="#FF3333",
            font=("Consolas", 13, "bold"),
            justify="center",
        )
        return

      bala_impactada = None
      for bala in self.balas:
        if (
            obs["x"] - 10 < bala["x"] < obs["x"] + obs["w"] + 10
            and obs["y"] - 10 < bala["y"] < obs["y"] + obs["h"] + 10
        ):
          bala_impactada = bala
          self.puntuacion += 100
          break

      if bala_impactada:
        if bala_impactada in self.balas:
          self.balas.remove(bala_impactada)
        obs["boom"] = 20
      else:
        self.game_canvas.create_rectangle(
            obs["x"],
            obs["y"],
            obs["x"] + obs["w"],
            obs["y"] + obs["h"],
            fill="#3a1111",
            outline="#FF4444",
            width=2,
        )
        self.game_canvas.create_text(
            obs["x"] + 20,
            obs["y"] - 10,
            text="BUG",
            fill="#FF4444",
            font=("Consolas", 8, "bold"),
        )

    self.game_canvas.create_rectangle(
        self.pos_x,
        self.pos_y,
        self.pos_x + 38,
        self.pos_y + 38,
        outline="#00FF66",
        fill="#0b2b18",
        width=2,
    )
    self.game_canvas.create_text(
        self.pos_x + 19,
        self.pos_y - 10,
        text="PLAYER",
        fill="#00FF66",
        font=("Consolas", 8, "bold"),
    )

    self.game_canvas.create_text(
        70,
        20,
        text=f"SCORE: {self.puntuacion}",
        fill="#00FF66",
        font=("Consolas", 11, "bold"),
    )

    self.after(16, self.bucle_juego)

  def ejecutar_comando_directo(self, comando):
    self.entry_msg.delete(0, "end")
    self.entry_msg.insert(0, comando)
    self.iniciar_proceso_envio()

  def iniciar_proceso_envio(self):
    texto = self.entry_msg.get().strip()
    if not texto:
      return
    self.entry_msg.delete(0, "end")

    if texto.lower() in ["limpiar", "clear"]:
      self.chat_log.configure(state="normal")
      self.chat_log.delete("1.0", "end")
      self.chat_log.configure(state="disabled")
      return

    self.mostrar_en_pantalla(f"tú > {texto}\n")
    self.btn_enviar.configure(state="disabled", text="...")
    threading.Thread(
        target=self.ejecutar_consulta_hilo, args=(texto,), daemon=True
    ).start()

  def ejecutar_consulta_hilo(self, texto):
    inicio = time.time()
    respuesta = ejecutar_comando_local(texto)
    duracion = round(time.time() - inicio, 2)
    self.after(0, lambda: self.finalizar_respuesta(respuesta, duracion))

  def finalizar_respuesta(self, respuesta, duracion):
    if respuesta == "LIMPIAR_PANTALLA_COMANDO":
      self.chat_log.configure(state="normal")
      self.chat_log.delete("1.0", "end")
      self.chat_log.configure(state="disabled")
    elif respuesta == "CERRAR_SISTEMA_COMANDO":
      self.destroy()
    elif respuesta == "ACTIVAR_VISOR_JUEGO":
      self.iniciar_juego()
      self.mostrar_en_pantalla(
          "ia > ⚠️ [SUPERVIVENCIA ACTIVA]: ¡Cuidado con los BUGS letales! Escribe"
          " 'jugar' para reiniciar si caes.\n\n"
      )
    elif respuesta == "DETENER_VISOR_JUEGO":
      self.detener_juego()
      self.mostrar_en_pantalla("ia > ⏹️ [JUEGO PAUSADO].\n\n")
    else:
      self.mostrar_en_pantalla(
          f"ia > {respuesta} <Latencia {duracion}s>\n\n"
      )
    self.btn_enviar.configure(state="normal", text="ENVIAR")

  def mostrar_en_pantalla(self, mensaje):
    self.chat_log.configure(state="normal")
    self.chat_log.insert("end", mensaje)
    self.chat_log.see("end")
    self.chat_log.configure(state="disabled")


if __name__ == "__main__":
  app = TerawareApp()
  app.mainloop()