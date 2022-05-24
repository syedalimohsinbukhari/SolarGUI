"""
Created on May 22 00:40:38 2022
"""
import sys
import tkinter as tk

from show.show_earth import show_earth
from tk_functions import planet_button


def main():

    ###################################################################################
    # Initialization
    ###################################################################################

    # set the width and height of the original window
    _w, _h = 800, 240
    # main is the master name in which all work is going to be done
    root_window = tk.Tk()
    # set the title of the GUI window
    root_window.title('[Enter appropriate name here]')
    # set the size of the GUI window
    root_window.geometry(f'{_w}x{_h}')
    # do not let it be resized smaller than it already is
    root_window.minsize(_w, _h)

    ##################################################################################
    # Working
    ##################################################################################

    welcome_label = tk.Label(master=root_window,
                             text='Welcome to Solar Explorer.\nPlease select a '
                                  'button.')
    welcome_label.grid(row=0, column=0, columnspan=9)

    planet_button(window=root_window, text='Sun', function=show_earth, column=0)

    planet_button(window=root_window, text='Mercury', function=show_earth, column=1)

    planet_button(window=root_window, text='Venus', function=show_earth, column=2)

    planet_button(window=root_window, text='Earth', function=show_earth, column=3)

    planet_button(window=root_window, text='Mars', function=show_earth, column=4)

    planet_button(window=root_window, text='Jupiter', function=show_earth, column=5)

    planet_button(window=root_window, text='Saturn', function=show_earth, column=6)

    planet_button(window=root_window, text='Uranus', function=show_earth, column=7)

    planet_button(window=root_window, text='Neptune', function=show_earth, column=8)

    ##################################################################################
    # Show it
    ##################################################################################
    root_window.mainloop()


# taken from
# https://chriswarrick.com/blog/2014/09/15/python-apps-the-right-way-entry_points-and
# -scripts/
if __name__ == '__main__':
    try:
        sys.exit(main())
    except TypeError:
        pass
