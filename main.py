# main.py
import tkinter as tk
from auth import проверить_пароль
from gui import GUI

def main():
    # Проверка пароля перед запуском GUI
    пароль_введенный = False
    попытки = 0
    макс_попыток = 3  # можно вынести в auth или параметры
    
    while not пароль_введенный and попытки < макс_попыток:
        пароль = tk.simpledialog.askstring("Вход", "Введите пароль:", show="*")
        if пароль is None:
            # Пользователь отменил ввод
            return
        if проверить_пароль(пароль):
            пароль_введенный = True
            break
        else:
            попытки += 1
            tk.messagebox.showerror("Ошибка", f"Неверный пароль. Попытка {попытки} из {макс_попыток}")
    
    if not пароль_введенный:
        tk.messagebox.showerror("Ошибка", "Превышено количество попыток. Программа завершает работу.")
        return

    # Запуск GUI
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()