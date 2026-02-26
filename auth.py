import os
import hashlib
import tkinter as tk
from tkinter import simpledialog, messagebox


def получить_путь_к_файлу(имя_файла):
    """
    Работает и в .py, и в .exe (PyInstaller)
    """
    if getattr(__import__("sys"), 'frozen', False):
        base_path = os.path.dirname(__import__("sys").executable)
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, имя_файла)


def проверить_пароль():
    root = tk.Tk()
    root.withdraw()

    try:
        путь = получить_путь_к_файлу("password.txt")

        if not os.path.exists(путь):
            messagebox.showerror("Ошибка", "Файл password.txt не найден")
            return False

        with open(путь, "r", encoding="utf-8") as f:
            сохраненный_хэш = f.read().strip()

        введенный = simpledialog.askstring(
            "Авторизация",
            "Введите пароль:",
            show="*"
        )

        if введенный is None:
            return False

        хэш_введенного = hashlib.sha256(
            введенный.encode("utf-8")
        ).hexdigest()

        if хэш_введенного == сохраненный_хэш:
            return True
        else:
            messagebox.showerror("Ошибка", "Неверный пароль")
            return False

    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка авторизации:\n{e}")
        return False