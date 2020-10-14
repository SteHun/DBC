if __name__ == "__main__":
    raise RuntimeError("This is a librairy, don't run this as __main__")


import blessed
from math import floor,ceil
from time import sleep
term = blessed.Terminal()

def prompt(message, title=None, height=term.height - 2, width=term.width - 2):
    if height > term.height or width > term.width:
        raise RuntimeError("the menu is larger than the terminal emulator. ")
    if height <= 0  or width <= 0:
        raise RuntimeError("the menu size can not be 0 or smaller")
    with term.fullscreen(), term.cbreak():
        if title != None:
            if not isinstance(title, str):
                raise TypeError("the title argument must only be None or a string. ")
            titlebar_x_start_pos = floor((term.width - width) / 2)
            titlebar_y_start_pos = floor((term.height - height) / 2)
            title_start_pos = floor((width - len(title))/2)
            title_end_pos = title_start_pos + len(title)
            to_print = ""
            for x in range(width):
                if x >= title_start_pos and x < title_end_pos:
                    to_print += title[x-title_start_pos]
                else:
                    to_print += " "
            print(f"{term.move_xy(titlebar_x_start_pos, titlebar_y_start_pos)}{term.black_on_yellow}{to_print}")
            sleep(10)

