"""
Created on May 22 00:40:38 2022
"""
import sys
import tkinter as tk

from earth import Earth


def main():

    ###################################################################################
    # Initialization
    ###################################################################################

    # set the width and height of the original window
    _w, _h = 640, 240
    # main is the master name in which all work is going to be done
    root_window = tk.Tk()
    # set the title of the GUI window
    root_window.title('[Enter appropriate name here]')
    # set the size of the GUI window
    root_window.geometry(f'{_w}x{_h}')
    # do not let it be resized smaller than it already is
    root_window.minsize(_w, _h)

    ###################################################################################
    # Function
    ###################################################################################

    # def change_units(window, entry_widget, option):
    #     change_win = tk.Toplevel(window)
    #     change_win.title(' ')
    #
    #     change_win.geometry('100x100')
    #     change_win.resizable(False, False)
    #
    #     get_val = tk.IntVar(change_win, 1)
    #
    #     values = {'kg': '1',
    #               'Msun': '2'}
    #
    #     for (text, value) in values.items():
    #         tk.Radiobutton(master=change_win,
    #                        text=text,
    #                        variable=get_val,
    #                        value=value).pack(side=tk.TOP)
    #
    #     but = tk.Button(master=change_win, text='Save', command=change_win.destroy)
    #     but.place(x=50, y=75, anchor=tk.CENTER)
    #
    #     if get_val.get() == '1':
    #         entry_widget.insert(0, option.convert_mass('Msun'))

    def show_earth(window):
        def change_value():
            mass_entry.delete(0, 'end')
            if get_value.get() == 'kg':
                mass_entry.insert(0, earth_.mass)
            elif get_value.get() == 'Msun':
                mass_entry.insert(0, earth_.convert_mass('Msun'))

        earth_window = tk.Toplevel(window)
        earth_window.title('Earth')

        _f_w, _f_h = window.winfo_width(), window.winfo_height()
        earth_window.geometry(f'{_f_w}x{_f_h}')

        earth_ = Earth()

        mass_label = tk.Label(master=earth_window, text='Mass of Earth')
        mass_label.place(x=50, y=20, anchor=tk.CENTER)

        mass_entry = tk.Entry(master=earth_window, width=30)
        mass_entry.insert(0, f'{earth_.mass}')
        mass_entry.place(x=200, y=20, anchor=tk.CENTER)

        get_value = tk.StringVar()

        mass_radio_button = {'kg': ['kg', 325],
                             'solMass': ['Msun', 375]}

        for (text, value) in mass_radio_button.items():
            tk.Radiobutton(master=earth_window,
                           text=text,
                           variable=get_value,
                           value=value[0],
                           command=lambda: change_value()).place(x=value[1],
                                                                 y=20,
                                                                 anchor=tk.CENTER)

    ##################################################################################
    # Working
    ##################################################################################

    welcome_label = tk.Label(master=root_window,
                             text='Welcome to Solar Explorer.\nPlease select a '
                                  'button.')
    welcome_label.place(x=_w / 2, y=25, anchor=tk.CENTER)

    earth_button = tk.Button(master=root_window, text='Earth',
                             command=lambda: show_earth(root_window))
    earth_button.place(x=_w / 2, y=75, anchor=tk.CENTER)

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
