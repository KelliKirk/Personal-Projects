import time
import os

def draw_tree():
    tree_height = 10  # Kuusepuu kõrgus
    tree_width = 2 * tree_height - 1
    trunk_height = 3

    # Loopi abil kuusepuu joonistamine
    for i in range(tree_height):
        stars = '*' * (2 * i + 1)
        print(' ' * (tree_height - i - 1) + stars)

    # Joonista puu tüvi
    for _ in range(trunk_height):
        print(' ' * (tree_height - 1) + '|')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_tree():
    t = 0
    while True:
        clear_screen()
        draw_tree()
        t += 0.2
        time.sleep(0.3)

animate_tree()
