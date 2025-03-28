import curses
import math
import time

def wave_animation(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(50)

    height, width = stdscr.getmaxyx()
    t = 0

    while True:
        stdscr.clear()
        for x in range(width):
            y = int(height // 2 + math.sin(x / 5.0 + t) * 10)
            if 0 < y < height:
                stdscr.addstr(y, x, "*")
        stdscr.refresh()
        t += 0.2
        time.sleep(0.05)

curses.wrapper(wave_animation)
