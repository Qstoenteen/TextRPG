import pyautogui
import time
print ('Антиафк включен, чтобы отключить - закройте это окно')
x = 0.0
while True:
    pyautogui.press('up')  # Нажимаем на клавишу "A"
    pyautogui.press('down')  # Нажимаем на клавишу "A"
    time.sleep(30)  # Пауза в 60 секунд (1 минута)a
    x += 0.5
    print ('Прошло', x, 'минут.')