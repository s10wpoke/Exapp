from auth import проверить_пароль
from gui import ГенераторВедомостиGUI

if __name__ == "__main__":
    if проверить_пароль():
        app = ГенераторВедомостиGUI()
        app.запустить()