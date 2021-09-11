# -*- coding: utf-8 -*-
#import requirement libs

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
from datetime import datetime, time
from time import sleep
import winsound
import threading


stop_tread = False
#search: how to a program runs back ground or runs even if the program close.
#search: how to a program send a notification 
alarms = []

def alarmm():
    while 1:
        sleep(1)
        current_time = datetime.now()
        now = current_time.strftime('%H:%M:%S')
        print(now, current_time)
        if now in alarms:
            print('time to wake up!')
            winsound.PlaySound(r'C:\Users\asus\Desktop\python_projects\alarm-clock\sounds\mixkit-scanning-sci-fi-alarm-905.wav', winsound.SND_FILENAME)


class Alarm:

    def __init__(self) -> None:
        self.alarms = dict()

    def remaning_time(self):
        pass

    def play_sound(self):
        pass

    def create_alarm(self, hour:str, min:str, sec:str, days:tuple):

        if len(hour) == 1:
            hour = '0' + hour
        if len(min) == 1:
            min = '0' + min
        if len(sec) == 1:
            sec = '0' + sec
        
        if len(self.alarms) == 10:
            raise ValueError('You have been reached max alarm number!')
        else:
            self.alarms.update(
                    {
                        f'alarm{len(self.alarms)+1}':{
                            'time':f'{hour}:{min}:{sec}', 
                            'days':days
                            }
                    }
                )
        
        print(self.alarms)

#layout
class AlarmClock(tk.Tk):

    def __init__(self, ala: object, className) -> None:
        super().__init__(className=className)
        self.ala = ala
        
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
        self.file_menu.add_command(label='Saved Times')
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
        self.hours = [str(i) for i in range(0, 24)]
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

        #checkboxes for weekdays
        self.days_list = ['mon', 'tue', 'wed','thur', 'fri', 'sat', 'sun']
        
        self.sd_mon = tk.StringVar()
        self.sd_tue = tk.StringVar()
        self.sd_wed = tk.StringVar()
        self.sd_thu = tk.StringVar()
        self.sd_fri = tk.StringVar()
        self.sd_sat= tk.StringVar()
        self.sd_sun = tk.StringVar()
        self.check_monday = ttk.Checkbutton(self, text='mon', variable=self.sd_mon, onvalue='mon', offvalue=None)
        self.check_tuesday = ttk.Checkbutton(self, text='tue', variable=self.sd_tue, onvalue='tue', offvalue=None)
        self.check_wed = ttk.Checkbutton(self, text='wed', variable=self.sd_wed, onvalue='wed', offvalue=None)
        self.check_thursday = ttk.Checkbutton(self, text='thu', variable=self.sd_thu, onvalue='thu', offvalue=None)
        self.check_friday = ttk.Checkbutton(self, text='fri', variable=self.sd_fri, onvalue='fri', offvalue=None)
        self.check_saturday = ttk.Checkbutton(self, text='sat', variable=self.sd_sat, onvalue='sat', offvalue=None)
        self.check_sunday = ttk.Checkbutton(self, text='sun', variable=self.sd_sun, onvalue='sun', offvalue=None)
        self.check_monday.place(x=30, y=90)
        self.check_tuesday.place(x=80, y=90)
        self.check_wed.place(x=130, y=90)
        self.check_thursday.place(x=180, y=90)
        self.check_friday.place(x=230, y=90)
        self.check_saturday.place(x=280, y=90)
        self.check_sunday.place(x=330, y=90) 

        #buttons
        self.btn_sound = tk.Button(self, text='Set Sound', bg='#264653',fg='white', width=15)
        self.btn_save = tk.Button(self, text='Set Alarm', bg='#2a9d8f',fg='white', width=15, command=self.set_alarm)
        self.btn_sound.place(x=150, y=130)
        self.btn_save.place(x=150, y=170)
        self.btn_reset = tk.Button(self, text='Reset', bg='#e76f51', fg='white', command=self.reset)
        self.btn_reset.place(x=70, y=220)

        #remaning time label
        self.lbl_remaning_time = tk.Label(self, text='Remaning Time: 2h 3m 2s', fg='green')
        self.lbl_remaning_time.place(x=160, y=220)

    def set_alarm(self):
        days = (
        self.sd_mon.get(),
        self.sd_tue.get(),
        self.sd_wed.get(),
        self.sd_thu.get(),
        self.sd_fri.get(),
        self.sd_sat.get(),
        self.sd_sun.get()
        )
        if self.combobox_hour.get() and self.combobox_min.get() and self.combobox_sec.get() and any(days):
            hour,min,sec = self.combobox_hour.get(),self.combobox_min.get(),self.combobox_sec.get()
            self.ala.create_alarm(hour, min, sec, days)
        else:
            showerror(title='Error', message='You have to fill hour, min, sec and at least one day sections!')


    def set_sound(self):
        #TODO open a box and show including sounds and besides user sets a music from own music!
        ...

    def reset(self):
        self.combobox_hour.set('')
        self.combobox_min.set('')
        self.combobox_sec.set('')
        self.sd_mon.set(''), self.sd_tue.set(''), self.sd_wed.set(''), self.sd_thu.set(''), self.sd_fri.set(''), self.sd_sat.set(''), self.sd_sun.set('') 



def main():
    thread = threading.Thread(target = alarmm)
    thread.daemon = True
    thread.start()
    alarm = Alarm()
    alarm_app = AlarmClock(alarm, className='Alarm Clock')
    alarm_app.mainloop()


if __name__ == '__main__':
    main()