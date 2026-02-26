import tkinter as tk
from tkinter import ttk, filedialog, messagebox

from generator import ГенераторВедомости
from exel_export import сохранить_в_excel


class Приложение(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Генератор ведомости работ")
        self.geometry("900x600")

        self.generator = ГенераторВедомости()

        self.помещения = []

        self._создать_интерфейс()

    # =========================
    # СОЗДАНИЕ ИНТЕРФЕЙСА
    # =========================

    def _создать_интерфейс(self):

        # ===== Верхняя панель =====
        верхний_фрейм = ttk.Frame(self)
        верхний_фрейм.pack(fill="x", padx=10, pady=5)

        ttk.Label(верхний_фрейм, text="Название помещения:").pack(side="left")

        self.entry_помещение = ttk.Entry(верхний_фрейм, width=30)
        self.entry_помещение.pack(side="left", padx=5)

        ttk.Button(
            верхний_фрейм,
            text="Добавить помещение",
            command=self.добавить_помещение
        ).pack(side="left", padx=5)

        ttk.Button(
            верхний_фрейм,
            text="Создать Excel",
            command=self.создать_excel
        ).pack(side="right")

        # ===== Список помещений =====
        self.tree = ttk.Treeview(self, columns=("room",), show="headings")
        self.tree.heading("room", text="Помещения")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

    # =========================
    # ЛОГИКА GUI
    # =========================

    def добавить_помещение(self):
        название = self.entry_помещение.get().strip()

        if not название:
            messagebox.showwarning("Ошибка", "Введите название помещения")
            return

        self.помещения.append({
            "название": название,
            "работы": []  # сюда позже добавим выбранные работы
        })

        self.tree.insert("", "end", values=(название,))
        self.entry_помещение.delete(0, tk.END)

    def создать_excel(self):
        if not self.помещения:
            messagebox.showwarning("Ошибка", "Нет помещений")
            return

        try:
            строки = self.generator.создать_ведомость(self.помещения)

            путь = filedialog.asksaveasfilename(
                defaultextension=".xlsx",
                filetypes=[("Excel files", "*.xlsx")]
            )

            if not путь:
                return

            сохранить_в_excel(строки, путь)

            messagebox.showinfo("Успех", "Файл успешно сохранён")

        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка при создании файла:\n{e}")