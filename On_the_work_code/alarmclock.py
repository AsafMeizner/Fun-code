from tkinter import *
import datetime
import time
import winsound
from threading import *
 
root = Tk()
 
root.geometry("400x200")
 
def Threading():
    t1=Thread(target=alarm)
    t1.start()
 
def alarm():

    while True:

        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

        time.sleep(1)
 
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time,set_alarm_time)

        Label(root,text="Time until alarm",font=("Helvetica 15 bold")).pack()
        Label(root,text=f"{hour.get()}:{minute.get()}:{second.get()}",font=("Helvetica 15 bold")).pack()

        
        if current_time == set_alarm_time:
            print("Time to Wake up")

            root2=Tk()
            root2.title("Alarm")
            root2.geometry("400x200")
            Label(root2,text="Wake Up",font=("Helvetica 20 bold"),fg="red").pack(pady=10)
            Label(root2,text="Wake Up",font=("Helvetica 20 bold"),fg="red").pack(pady=10)
            Button(root2,text="Stop",font=("Helvetica 15 bold"),command=root2.destroy).pack(pady=10)
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            root2.mainloop()

Label(root,text="Alarm Clock",font=("Helvetica 20 bold"),fg="red").pack(pady=10)
Label(root,text="Set Time",font=("Helvetica 15 bold")).pack()
 
frame = Frame(root)
frame.pack()
 
hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24'
        )
hour.set(hours[0])
 
hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)
 
minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
minute.set(minutes[0])
 
mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)
 
second = StringVar(root)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
second.set(seconds[0])
 
secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)
 
Button(root,text="Set Alarm",font=("Helvetica 15"),command=Threading).pack(pady=20)

root.mainloop()

#change the input to text and not multiple options
#add the ability to set the alarm to a specific date
#add the ability to add multiple alarms and delete them
#add the ability to add a custom sound
#add the ability to add a custom message insead of "time to wake up"
#add below the set time button a button that says "show all alarms" and when clicked it will show all the alarms that are set and the time until they go off and a button to delete them
#remember the settings of the alarm clock when you close the program and open it again
#add the ability to minimize the program to the taskbar and when you click it it will open the program again and right click the icon and you will have the option to close the program
