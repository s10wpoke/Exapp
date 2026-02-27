import tkinter as tk
from tkinter import ttk, messagebox
from generator import создать_ведомость
from works_data import РаботыБаза

class Приложение:
    def __init__(self, root):
        self.root = root
        self.root.title("Генератор ведомости работ")
        self.база = РаботыБаза()

        self.создать_widgets()

    def создать_widgets(self):
        frm = ttk.Frame(self.root, padding=10)
        frm.grid(row=0, column=0, sticky="nsew")

        # Настройки окна
        ttk.Label(frm, text="Тип окна:").grid(row=0, column=0, sticky="w")
        self.тип_окна_var = tk.StringVar(value=self.база.тип_окна)
        тип_окна_options = ["двухстворчатое", "одностворчатое", "триплекс"]
        ttk.OptionMenu(frm, self.тип_окна_var, self.база.тип_окна, *тип_окна_options).grid(row=0, column=1, sticky="ew")

        ttk.Label(frm, text="Ширина окна (м):").grid(row=1, column=0, sticky="w")
        self.ширина_окна_var = tk.DoubleVar(value=self.база.ширина_окна)
        ttk.Entry(frm, textvariable=self.ширина_окна_var).grid(row=1, column=1, sticky="ew")

        ttk.Label(frm, text="Высота окна (м):").grid(row=2, column=0, sticky="w")
        self.высота_окна_var = tk.DoubleVar(value=self.база.высота_окна)
        ttk.Entry(frm, textvariable=self.высота_окна_var).grid(row=2, column=1, sticky="ew")

        # Настройки плитки
        ttk.Label(frm, text="Размер плитки (мм):").grid(row=3, column=0, sticky="w")
        self.размер_плитки_var = tk.StringVar(value=self.база.размер_плитки)
        ttk.Entry(frm, textvariable=self.размер_плитки_var).grid(row=3, column=1, sticky="ew")

        # Отклонения стен и дверей
        ttk.Label(frm, text="Отклонение откосов окна (м):").grid(row=4, column=0, sticky="w")
        self.откос_окна_var = tk.DoubleVar(value=self.база.откос_окна)
        ttk.Entry(frm, textvariable=self.откос_окна_var).grid(row=4, column=1, sticky="ew")

        ttk.Label(frm, text="Отклонение откосов двери (м):").grid(row=5, column=0, sticky="w")
        self.откос_двери_var = tk.DoubleVar(value=self.база.откос_двери)
        ttk.Entry(frm, textvariable=self.откос_двери_var).grid(row=5, column=1, sticky="ew")

        ttk.Label(frm, text="Высота помещения (м):").grid(row=6, column=0, sticky="w")
        self.высота_помещения_var = tk.DoubleVar(value=self.база.высота_помещения)
        ttk.Entry(frm, textvariable=self.высота_помещения_var).grid(row=6, column=1, sticky="ew")

        # Кнопка создания Excel
        ttk.Button(frm, text="Создать Excel", command=self.собрать_данные).grid(row=7, column=0, columnspan=2, pady=10)

        # Настройка растяжки колонок
        frm.columnconfigure(1, weight=1)

    def собрать_данные(self):
        # Обновляем базу
        self.база.тип_окна = self.тип_окна_var.get()
        self.база.ширина_окна = self.ширина_окна_var.get()
        self.база.высота_окна = self.высота_окна_var.get()
        self.база.размер_плитки = self.размер_плитки_var.get()
        self.база.откос_окна = self.откос_окна_var.get()
        self.база.откос_двери = self.откос_двери_var.get()
        self.база.высота_помещения = self.высота_помещения_var.get()

        try:
            создать_ведомость(self.база)
            messagebox.showinfo("Готово", "Excel успешно создан!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка при создании Excel:\n{e}")

def запустить_gui():
    root = tk.Tk()
    app = Приложение(root)
    root.mainloop()

if __name__ == "__main__":
    запустить_gui()