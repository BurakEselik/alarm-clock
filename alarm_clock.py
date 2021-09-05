#install requirement libs

import tkinter as tk 


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

if __name__ == '__main__':
    alarm = AlarmClock(className='Alarm Clock')
    alarm.mainloop()