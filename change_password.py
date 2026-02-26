"""
change_password.py - Утилита для смены пароля
Меняет хэш прямо в auth.py
"""

import hashlib
import os

AUTH_FILE = "auth.py"

def создать_новый_пароль():
    print("=" * 60)
    print("        ГЕНЕРАТОР ХЭША ПАРОЛЯ (auth.py)")
    print("=" * 60)

    while True:
        пароль = input("Введите новый пароль (Enter для отмены): ")
        if пароль == "":
            print("Отмена.")
            return

        подтверждение = input("Повторите пароль: ")
        if пароль != подтверждение:
            print("❌ Пароли не совпадают, попробуйте снова.")
            continue

        хэш = hashlib.sha256(пароль.encode()).hexdigest()
        print(f"✅ Новый хэш: {хэш}")

        # Обновляем auth.py
        try:
            with open(AUTH_FILE, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            with open(AUTH_FILE, 'w', encoding='utf-8') as f:
                for line in lines:
                    if line.strip().startswith("ХЭШ_ПАРОЛЯ ="):
                        f.write(f'ХЭШ_ПАРОЛЯ = "{хэш}"\n')
                    else:
                        f.write(line)

            print("✅ auth.py успешно обновлен с новым паролем!")
        except Exception as e:
            print(f"❌ Ошибка обновления auth.py: {e}")
        
        break

if __name__ == "__main__":
    создать_новый_пароль()
    input("Нажмите Enter для выхода...")