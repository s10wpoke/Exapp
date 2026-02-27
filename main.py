"""
main.py - Главный файл запуска приложения
"""

from gui import GUI
from exel_export import ExcelExport

def main():
    # Создаем GUI
    app = GUI()
    
    # Запуск интерфейса: получаем выбранные работы и настройки
    выбранные_работы, настройки = app.run()
    
    if not выбранные_работы:
        print("Работы не выбраны. Выход.")
        return

    # Создаем объект для экспорта
    excel = ExcelExport(настройки)
    
    # Сохраняем в Excel
    путь = excel.сохранить_в_excel(выбранные_работы)
    
    print(f"\n✅ Ведомость успешно сохранена: {путь}")

if __name__ == "__main__":
    main()