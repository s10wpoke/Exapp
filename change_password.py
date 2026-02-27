"""
change_password.py - Утилита для смены пароля в auth.py
"""

import hashlib
import os

AUTH_FILE = "auth.py"

def создать_новый_пароль():
    print("=" * 60)
    print("        ГЕНЕРАТОР ХЭША ПАРОЛЯ")
    print("=" * 60)
    print("\nЭта утилита генерирует хэш SHA-256 для вашего пароля и обновляет auth.py.")
    print("-" * 60)
    
    while True:
        пароль = input("\nВведите новый пароль (или Enter для отмены):\n> ")
        if пароль == "":
            print("Отмена.")
            return
        
        подтверждение = input("Повторите пароль:\n> ")
        if пароль != подтверждение:
            print("\n❌ Пароли не совпадают! Попробуйте снова.")
            continue
        
        # Генерируем хэш
        хэш = hashlib.sha256(пароль.encode()).hexdigest()
        
        print("\n✅ ХЭШ УСПЕШНО СОЗДАН!")
        print(f"Ваш пароль: {пароль}")
        print(f"Хэш SHA-256: {хэш}\n")
        
        # Обновляем auth.py
        if not os.path.exists(AUTH_FILE):
            print(f"❌ Файл {AUTH_FILE} не найден!")
            return
        
        try:
            with open(AUTH_FILE, "r", encoding="utf-8") as f:
                lines = f.readlines()
            
            new_lines = []
            заменено = False
            for line in lines:
                if line.strip().startswith("ПАРОЛЬ_ХЭШ"):
                    new_lines.append(f'ПАРОЛЬ_ХЭШ = "{хэш}"\n')
                    заменено = True
                else:
                    new_lines.append(line)
            
            if not заменено:
                # Если строки с паролем нет, добавляем в начало
                new_lines.insert(0, f'ПАРОЛЬ_ХЭШ = "{хэш}"\n')
            
            with open(AUTH_FILE, "w", encoding="utf-8") as f:
                f.writelines(new_lines)
            
            print(f"✅ auth.py успешно обновлён с новым паролем!")
        
        except Exception as e:
            print(f"❌ Ошибка обновления auth.py: {e}")
        
        break

if __name__ == "__main__":
    создать_новый_пароль()
    input("\nНажмите Enter для выхода...")