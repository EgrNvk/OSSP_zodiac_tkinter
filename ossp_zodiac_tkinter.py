import tkinter as tk

root = tk.Tk()
root.title("Title")
root.geometry("400x500")
root.configure(bg="#f2f2f2")

label1 = tk.Label(root, text="Введите день рождения:", font=("Arial", 14), bg="#f2f2f2")
label1.pack(pady=(20, 5))
entry1 = tk.Entry(root, font=("Arial", 10), width=25, justify="center")
entry1.pack(pady=10)

label2 = tk.Label(root, text="Введите месяц рождения:", font=("Arial", 14), bg="#f2f2f2")
label2.pack(pady=(20, 5))
entry2 = tk.Entry(root, font=("Arial", 10), width=25, justify="center")
entry2.pack(pady=10)

label3 = tk.Label(root, text="Введите год рождения:", font=("Arial", 14), bg="#f2f2f2")
label3.pack(pady=(20, 5))
entry3 = tk.Entry(root, font=("Arial", 10), width=25, justify="center")
entry3.pack(pady=10)

img_label = tk.Label(root, bg="#f2f2f2")
img_label.pack(pady=10)

def btnClick1():
    day = int(entry1.get())
    month = int(entry2.get())

    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        zodiac = "Водолей"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        zodiac = "Рыбы"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        zodiac = "Овен"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        zodiac = "Телец"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        zodiac = "Близнецы"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        zodiac = "Рак"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        zodiac = "Лев"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        zodiac = "Дева"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        zodiac = "Весы"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        zodiac = "Скорпион"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        zodiac = "Стрелец"
    else:
        zodiac = "Козерог"

    label4.config(text=f"Ваш знак зодиака — {zodiac}")

    img = tk.PhotoImage(file=f"img/{zodiac}.png")
    img_label.config(image=img)
    img_label.image = img

button = tk.Button(root, text="Знак зодиака", font=("Arial", 14), command=btnClick1)
button.pack(pady=10)

label4 = tk.Label(root, text="Ваш знак зодиака - ", font=("Arial", 14), bg="#f2f2f2")
label4.pack(pady=(20, 5))

root.mainloop()