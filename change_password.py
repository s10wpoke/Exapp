"""
change_password.py - Утилита для смены пароля
"""

import hashlib

def создать_новый_пароль():
    print("=" * 60)
    print("        ГЕНЕРАТОР ХЭША ПАРОЛЯ")
    print("=" * 60)
    print("\nЭта утилита генерирует хэш SHA-256 для вашего пароля.")
    print("Скопируйте полученный хэш в файл config.py")
    print("-" * 60)
    
    while True:
        print("\nВведите новый пароль (или Enter для отмены):")
        пароль = input("> ")
        
        if пароль == "":
            print("Отмена.")
            return
        
        подтверждение = input("Повторите пароль: ")
        
        if пароль != подтверждение:
            print("\n❌ Пароли не совпадают! Попробуйте снова.")
            continue
        
        # Генерируем хэш
        хэш = hashlib.sha256(пароль.encode()).hexdigest()
        
        print("\n" + "=" * 60)
        print("✅ ХЭШ УСПЕШНО СОЗДАН!")
        print("=" * 60)
        print(f"\nВаш пароль: {пароль}")
        print(f"Хэш SHA-256: {хэш}")
        print("\nЗамените строку в файле config.py на:")
        print(f'ПАРОЛЬ_ХЭШ = "{хэш}"')
        print("\n" + "=" * 60)
        
        # Предлагаем автоматически обновить config.py
        обновить = input("\nОбновить config.py автоматически? (y/n): ")
        if обновить.lower() == 'y':
            try:
                with open('config.py', 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Ищем и заменяем старый хэш
                lines = content.split('\n')
                new_lines = []
                for line in lines:
                    if line.strip().startswith('ПАРОЛЬ_ХЭШ ='):
                        new_lines.append(f'ПАРОЛЬ_ХЭШ = "{хэш}"')
                    else:
                        new_lines.append(line)
                
                with open('config.py', 'w', encoding='utf-8') as f:
                    f.write('\n'.join(new_lines))
                
                print("✅ config.py успешно обновлен!")
            except Exception as e:
                print(f"❌ Ошибка обновления config.py: {e}")
                print("Обновите файл вручную.")
        
        break

if __name__ == "__main__":
    создать_новый_пароль()
    input("\nНажмите Enter для выхода...")
