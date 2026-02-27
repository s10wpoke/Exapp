# gui.py
import tkinter as tk
from tkinter import ttk, messagebox
from generator import ГенераторВедомости
from exel_export import сохранить_в_excel  # предполагаем, что exel_export.py уже есть и работает

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Ведомость работ")

        self.параметры = {
            'тип_окна': 'двухстворчатое',
            'размер_плитки': '60х60',
            'откос_окна': 0.2,
            'откос_двери': 0.2,
            'высота_помещения': 2.5
        }

        self.создать_виджеты()

    def создать_виджеты(self):
        # Фрейм параметров
        frame = ttk.Frame(self.root, padding=10)
        frame.pack(fill=tk.BOTH, expand=True)

        # Тип окна
        ttk.Label(frame, text="Тип окна:").grid(row=0, column=0, sticky=tk.W)
        self.тип_окна = ttk.Combobox(frame, values=["двухстворчатое", "одностворчатое"], width=20)
        self.тип_окна.set(self.параметры['тип_окна'])
        self.тип_окна.grid(row=0, column=1, pady=5)

        # Размер плитки
        ttk.Label(frame, text="Размер плитки (см):").grid(row=1, column=0, sticky=tk.W)
        self.размер_плитки = ttk.Entry(frame, width=10)
        self.размер_плитки.insert(0, self.параметры['размер_плитки'])
        self.размер_плитки.grid(row=1, column=1, pady=5)

        # Откос окна
        ttk.Label(frame, text="Откос окна (м):").grid(row=2, column=0, sticky=tk.W)
        self.откос_окна = ttk.Entry(frame, width=10)
        self.откос_окна.insert(0, str(self.параметры['откос_окна']))
        self.откос_окна.grid(row=2, column=1, pady=5)

        # Откос двери
        ttk.Label(frame, text="Откос двери (м):").grid(row=3, column=0, sticky=tk.W)
        self.откос_двери = ttk.Entry(frame, width=10)
        self.откос_двери.insert(0, str(self.параметры['откос_двери']))
        self.откос_двери.grid(row=3, column=1, pady=5)

        # Высота помещения
        ttk.Label(frame, text="Высота помещения (м):").grid(row=4, column=0, sticky=tk.W)
        self.высота_помещения = ttk.Entry(frame, width=10)
        self.высота_помещения.insert(0, str(self.параметры['высота_помещения']))
        self.высота_помещения.grid(row=4, column=1, pady=5)

        # Кнопка создания Excel
        btn = ttk.Button(frame, text="Создать Excel", command=self.создать_excel)
        btn.grid(row=5, column=0, columnspan=2, pady=10)

    def создать_excel(self):
        # Обновляем параметры из GUI
        self.параметры['тип_окна'] = self.тип_окна.get()
        self.параметры['размер_плитки'] = self.размер_плитки.get()
        try:
            self.параметры['откос_окна'] = float(self.откос_окна.get().replace(',', '.'))
            self.параметры['откос_двери'] = float(self.откос_двери.get().replace(',', '.'))
            self.параметры['высота_помещения'] = float(self.высота_помещения.get().replace(',', '.'))
        except ValueError:
            messagebox.showerror("Ошибка", "Откосы и высота помещения должны быть числами")
            return

        генератор = ГенераторВедомости(self.параметры)
        работы = генератор.получить_работы()

        # Сохраняем Excel
        try:
            сохранить_в_excel(работы)
            messagebox.showinfo("Готово", "Excel файл успешно создан!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось создать Excel файл:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()