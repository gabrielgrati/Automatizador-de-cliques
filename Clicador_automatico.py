import pyautogui
import time

# Posição na tela de onde o mouse irá clicar
x, y = 869, 790

# Número de cliques que quero que o programa ruealize
num_clicks = 700

# Tempo para começar os cliques
time.sleep(5)

# Realizando os cliques
for _ in range(num_clicks):
    pyautogui.click(x, y)
    time.sleep(0.001)  # segundos entre os cliques

