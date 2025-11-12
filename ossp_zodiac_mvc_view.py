import tkinter as tk

class ZodiacView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Title")
        self.root.geometry("400x500")
        self.root.configure(bg="white")

        self.label1 = tk.Label(self.root, text="Введите день рождения:", font=("Arial", 14), bg="#f2f2f2")
        self.label1.pack(pady=(20, 5))
        self.entry_day = tk.Entry(self.root, font=("Arial", 10), width=25, justify="center")
        self.entry_day.pack(pady=10)

        self.label2 = tk.Label(self.root, text="Введите месяц рождения:", font=("Arial", 14), bg="#f2f2f2")
        self.label2.pack(pady=(20, 5))
        self.entry_month = tk.Entry(self.root, font=("Arial", 10), width=25, justify="center")
        self.entry_month.pack(pady=10)

        self.label3 = tk.Label(self.root, text="Введите год рождения:", font=("Arial", 14), bg="#f2f2f2")
        self.label3.pack(pady=(20, 5))
        self.entry_year = tk.Entry(self.root, font=("Arial", 10), width=25, justify="center")
        self.entry_year.pack(pady=10)

        self.img_label = tk.Label(self.root, bg="#f2f2f2")
        self.img_label.pack(pady=10)
        self._img=None

        self.button = tk.Button(self.root, text="Ваш знак ", font=("Arial", 14), bg="#f2f2f2")
        self.button.pack(pady=10)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 14), bg="#f2f2f2")
        self.result_label.pack(pady=10)

    def get_day(self):
        return int(self.entry_day.get())

    def get_month(self):
        return int(self.entry_month.get())

    def set_on_calculate(self, callback):
        self.button.config(command=callback)

    def show_zodiac(self, zodiac: str):
        self.result_label.config(text=f"Ваш знак зодиака - {zodiac}")
        img = tk.PhotoImage(file=f"img/{zodiac}.png")
        self.img_label.config(image=img)
        self._img = img

    def mainloop(self):
        self.root.mainloop()