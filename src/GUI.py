import tkinter as tk
from tkinter.constants import LEFT, NW, NO

class TemperatureController:
    def __init__(self):
        self.current_temperature = 20  # Beispielwert für die Starttemperatur

    def start_heat(self):
        # Logik zum Starten der Heizung
        print("Heizung gestartet.")

    def read_current_temperature(self):
        # Hier kannst du die Logik zum Lesen der aktuellen Temperatur integrieren
        return self.current_temperature  # Beispielwert zurückgeben

class TemperatureGUI:
    def __init__(self, master):
        self.master = master
        self.controller = TemperatureController()  # Controller instanziieren

        self.master.title("Temperature Control")
        self.setup_ui()

        self.controller.start_heat()  # Heizung starten
        self.refresh_temperature()

    def setup_ui(self):
        WIDTH, HEIGHT = 500, 300
        self.canvas = tk.Canvas(self.master, width=WIDTH, height=HEIGHT)
        self.canvas.pack()

        self.temperature = tk.StringVar()

        self.aktTemp = tk.Label(self.master, textvariable=self.temperature, fg="red", font=("Helvetica", 16))
        self.aktTemp.pack()

        # Header Elements (Typ, Artikel, Datum)
        TypLabel = tk.Label(self.master, text="Typ")
        TypLabel.pack(side=LEFT)

        self.TypEntry = tk.Entry(self.master, width=10)
        self.TypEntry.pack(side=LEFT, anchor=NW, expand=NO)

        ArtikelLabel = tk.Label(self.master, text="Artikel")
        ArtikelLabel.pack(side=LEFT)

        self.ArtikelEntry = tk.Entry(self.master, width=10)
        self.ArtikelEntry.pack(side=LEFT)

        DatumLabel = tk.Label(self.master, text="Datum")
        DatumLabel.pack(side=LEFT)

        self.DatumEntry = tk.Entry(self.master, width=10)
        self.DatumEntry.pack(side=LEFT)

        # Body Elements (Start, End..)
        setWantedTempLabel = tk.Label(self.master, text="Starttemperatur")
        setWantedTempLabel.pack()

        self.setWantedTempEntry = tk.Entry(self.master, width=5)
        self.setWantedTempEntry.pack()

        setWantedIncLabel = tk.Label(self.master, text="Temperatur erhöhen um")
        setWantedIncLabel.pack()

        self.setWantedIncEntry = tk.Entry(self.master, width=5)
        self.setWantedIncEntry.pack()

        setZielTempLabel = tk.Label(self.master, text="Zieltemperatur")
        setZielTempLabel.pack()

        self.setWantedSecsEntry = tk.Entry(self.master, width=5)
        self.setWantedSecsEntry.pack()

    def refresh_temperature(self):
        current_temp = self.controller.read_current_temperature()
        self.temperature.set(f"{current_temp} °C")
        self.master.after(1000, self.refresh_temperature)

if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureGUI(root)
    root.mainloop()
