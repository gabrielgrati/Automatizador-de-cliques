import pyautogui
import time

# Tempo pra iniciar
time.sleep(5)

# Coordenada do mouse
x, y = pyautogui.position()
print(f'Coordenadas do cursor do mouse: x={x}, y={y}')

# impressao da coordenada
pyautogui.click(x, y)