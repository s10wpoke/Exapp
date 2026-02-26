from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter


def сохранить_в_excel(строки, путь_к_файлу):
    wb = Workbook()
    ws = wb.active
    ws.title = "Ведомость"

    # ===== СТИЛИ =====
    жирный = Font(bold=True)
    выравнивание_центр = Alignment(horizontal="center", vertical="center", wrap_text=True)

    тонкая_граница = Border(
        left=Side(style="thin"),
        right=Side(style="thin"),
        top=Side(style="thin"),
        bottom=Side(style="thin")
    )

    # Цвета (можешь заменить на свои)
    цвет_помещение = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")
    цвет_раздел = PatternFill(start_color="EFEFEF", end_color="EFEFEF", fill_type="solid")

    # ===== ШИРИНА КОЛОНОК =====
    ширины = [5, 50, 15, 10]
    for i, ширина in enumerate(ширины, start=1):
        ws.column_dimensions[get_column_letter(i)].width = ширина

    # ===== ЗАПИСЬ ДАННЫХ =====
    for row_index, строка in enumerate(строки, start=1):
        for col_index, значение in enumerate(строка, start=1):
            cell = ws.cell(row=row_index, column=col_index, value=значение)
            cell.border = тонкая_граница
            cell.alignment = Alignment(vertical="center")

        # Простейшая логика форматирования (если ты передаёшь тип строки)
        if isinstance(строка, dict):
            тип = строка.get("type")

            if тип == "room":
                for col in range(1, 5):
                    cell = ws.cell(row=row_index, column=col)
                    cell.fill = цвет_помещение
                    cell.font = жирный

            elif тип == "section":
                for col in range(1, 5):
                    cell = ws.cell(row=row_index, column=col)
                    cell.fill = цвет_раздел
                    cell.font = жирный

    # ===== АВТОВЫРАВНИВАНИЕ =====
    for row in ws.iter_rows():
        for cell in row:
            cell.alignment = Alignment(vertical="center", wrap_text=True)

    wb.save(путь_к_файлу)