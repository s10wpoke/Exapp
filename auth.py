"""
auth.py - Авторизация пользователя
Пароль хранится внутри приложения (в виде SHA256 хэша)
"""

import hashlib
import tkinter as tk
from tkinter import simpledialog, messagebox

# Хэш пароля по умолчанию (admin123)
ХЭШ_ПАРОЛЯ = "93ed7071a1c6e55a1ccd873dedc710776895e8faa5ef2cd647d4ba09c30aca3d"

def проверить_пароль():
    root = tk.Tk()
    root.withdraw()  # скрываем главное окно

    for попытка in range(3):
        введенный = simpledialog.askstring("Авторизация", "Введите пароль:", show="*")
        if введенный is None:
            return False

        хэш_введенного = hashlib.sha256(введенный.encode("utf-8")).hexdigest()

        if хэш_введенного == ХЭШ_ПАРОЛЯ:
            return True
        else:
            messagebox.showerror("Ошибка", f"Неверный пароль ({попытка + 1}/3)")
    
    return False