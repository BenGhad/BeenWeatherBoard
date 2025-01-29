import tkinter as tk
import requests


class WeatherGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Weather GUI")

        # Enter Location
        self.location_label = tk.Label(master, text="Location:")
        self.location_label.pack()
        self.location_entry = tk.Entry(master)
        self.location_entry.pack()

        # Enter Unit
        self.unit_label = tk.Label(master, text="Unit (metric/imperial):")
        self.unit_label.pack()
        self.unit_entry = tk.Entry(master)
        self.unit_entry.pack()

        # Get Weather:
        self.get_button = tk.Button(master, text="Get Weather", command=self.get_weather)
        self.get_button.pack()
        # Result:
        self.result_label = tk.Label(master, text="")  # we update this with fetched data
        self.result_label.pack()

    def get_weather(self):
        location = self.location_entry.get()
        unit = self.unit_entry.get() or "metric"
        url = f"http://127.0.0.1:8000/weather?location={location}&unit={unit}"
        try:
            response = requests.get(url)
            data = response.json()
            if (response.status_code == 200):
                self.result_label.config(text=str(data))
            else:
                self.result_label.config(text="Error: " + data["detail"])
        except Exception as e:
            self.result_label.config(text="Exception: " + str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherGUI(root)
    root.mainloop()
