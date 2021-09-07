#install requirement libs

import tkinter as tk
from tkinter import ttk


#layout
class AlarmClock(tk.Tk):

    def __init__(self, className) -> None:
        super().__init__(className=className)

        #set geometry
        self.title('Alarm Clock App')
        self.resizable(0,0)
        self.geometry('400x300')

        #set icon
        self.icon =  tk.PhotoImage(file='images/alarm-clock.png')
        self.iconphoto(False, self.icon)

        #menubar
        self.menubar = tk.Menu(self, bg='light blue')
        self.config(menu=self.menubar)
        self.file_menu = tk.Menu(self.menubar, tearoff=False)
        self.file_menu.add_command(label='Save Time')
        self.file_menu.add_separator()
        #submenu
        self.sub_menu = tk.Menu(self.file_menu, tearoff=0)
        self.sub_menu.add_command(label='Keyboard Shortcuts')
        self.sub_menu.add_command(label='Color Themes')
        self.file_menu.add_cascade(label='Preferences', menu=self.sub_menu)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Exit', command=self.destroy)
        self.menubar.add_cascade(label='Alarm', menu=self.file_menu, underline=0)

        self.help_menu = tk.Menu(self.menubar, tearoff=0)
        self.help_menu.add_command(label='Welcome')
        self.help_menu.add_command(label='About..')
        self.menubar.add_cascade(label='Help', menu=self.help_menu)

        self.lbl_1 = tk.Label(self, text='When to wake you up?')
        self.lbl_1.pack(pady=15)

        #combobox for hours
        self.lbl_hour = tk.Label(self, text='Hour:')
        self.lbl_hour.place(x=50, y=50)
        self.widget_var_hour = tk.StringVar()
        self.combobox_hour = ttk.Combobox(self, textvariable=self.widget_var_hour, width=5)
        self.hours = [str(i) for i in range(0, 13)]
        self.combobox_hour['values'] = tuple(self.hours)
        self.combobox_hour['state'] = 'readonly'
        self.combobox_hour.place(x=90, y=50)

        #combobox for minutes
        self.lbl_minute = tk.Label(self, text='Min:')
        self.lbl_minute.place(x=150, y=50)
        self.widget_var_min = tk.StringVar()
        self.combobox_min = ttk.Combobox(self, textvariable=self.widget_var_min, width=5)
        self.mins = [str(i) for i in range(0, 60)]
        self.combobox_min['values'] = tuple(self.mins)
        self.combobox_min['state'] = 'readonly'
        self.combobox_min.place(x=190, y=50)

        #combobox for seconds
        self.lbl_seconds = tk.Label(self, text='Sec:')
        self.lbl_seconds.place(x=250, y=50)
        self.widget_var_sec = tk.StringVar()
        self.combobox_sec = ttk.Combobox(self, textvariable=self.widget_var_sec, width=5)
        self.secs = [str(i) for i in range(0, 60)]
        self.combobox_sec['values'] = tuple(self.secs)
        self.combobox_sec['state'] = 'readonly'
        self.combobox_sec.place(x=290, y=50)


if __name__ == '__main__':
    alarm = AlarmClock(className='Alarm Clock')
    alarm.mainloop()