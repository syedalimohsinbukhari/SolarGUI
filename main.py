"""
Created on May 22 00:40:38 2022
"""
import sys
import tkinter as tk

from functions import show_earth


def main():

    ###################################################################################
    # Initialization
    ###################################################################################

    # set the width and height of the original window
    _w, _h = 960, 240
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
    welcome_label.place(y=20, relx=.5, anchor=tk.CENTER)

    earth_button = tk.Button(master=root_window, text='Earth',
                             command=lambda: show_earth(root_window))
    earth_button.place(y=60, relx=.5, anchor=tk.CENTER)
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
