import time
from pynput.keyboard import Controller, Key
from pynput import keyboard as kb
import win32gui
import sys

# Настройки
TARGET_KEY = "e"  # Клавиша для нажатия
ROBLOX_WINDOW_TITLE = "Roblox"  # Заголовок окна Roblox
PRESS_INTERVAL = 30.0  # Интервал между нажатиями (в секундах)

# Проверяем, активно ли окно Roblox
def is_roblox_focused():
    window = win32gui.GetForegroundWindow()
    window_title = win32gui.GetWindowText(window)
    return ROBLOX_WINDOW_TITLE in window_title

# Основной цикл
def main():
    keyboard = Controller()
    start_time = time.time()
    print(f"Скрипт запущен. Нажимаю '{TARGET_KEY}' каждые {PRESS_INTERVAL} сек.")
    print("Нажмите ESC в консоли, чтобы остановить.")

    def on_press(key):
        if key == kb.Key.esc:
            print("\nОстановлено пользователем.")
            return False  # Останавливаем listener

    # Слушаем ESC в консоли для остановки
    listener = kb.Listener(on_press=on_press)
    listener.start()

    try:
        while listener.is_alive():
            if is_roblox_focused():  # Если Roblox в фокусе
                keyboard.press(TARGET_KEY)
                time.sleep(0.05)
                keyboard.release(TARGET_KEY)
                
                elapsed_time = time.time() - start_time
                print(f"Нажал {TARGET_KEY}. Прошло: {elapsed_time:.2f} сек.", end="\r")
            
            time.sleep(PRESS_INTERVAL)  # Задержка между нажатиями

    except Exception as e:
        print(f"\nОшибка: {e}")
    finally:
        listener.stop()

if __name__ == "__main__":
    main()