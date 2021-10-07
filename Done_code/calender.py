from tkinter import *
from tkinter import ttk
import calendar


class main:
    def __init__(self, master):
        self.master = master
        self.month = IntVar()
        self.year = IntVar()
        self.months = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
        self.widgets()

    def getcal(self):
        # Day/Month/Year Computations
        m = self.month.get()
        y = self.year.get()

        # Fill current month label
        self.current['text'] = calendar.month_name[m] + ' ' + str(y)

        # Remove text from all buttons
        for ii in range(6):
            for jj in range(7):
                self.area[ii][jj]['text'] = ''

        # Loop over monthcalendar matrix and fill button text
        for ii, week in enumerate(calendar.monthcalendar(y, m)):
            for jj, day in enumerate(week):
                if day != 0:
                    self.area[ii][jj]['text'] = day

    def click(self, event):
        print(event.widget.cget('text'))

    def widgets(self):
        # Main Heading
        Label(self.master, text='Calendar', font=('freesansbold', 30), bd=10).pack()
        f = Frame(self.master, pady = 10, padx=10)

        # Month Label:
        Label(f, text='Month: ', font=('freesansbold', 13)).grid()

        # Month Dropdown Selector
        mon = ttk.Combobox(f, width=7, font=('freesansbold', 15), values=self.months, textvariable = self.month)
        mon.grid(row=0, column=1)
        mon.current(0)

        # Year Label:
        Label(f, text='Year: ', font=('freesansbold', 13)).grid(row=0, column=2)

        # Year Entry Box:
        ttk.Entry(f, width=7, font = ('freesansbold', 13), textvariable=self.year).grid(row=0, column=3)
        self.year.set(2010)
        f.pack()

        # Label for currently displayed month
        self.current = Label(self.master, text='', font=('freesansbold', 13))
        self.current.pack()

        # Calendar Display area:
        f2 = Frame(self.master, pady = 10, padx=10)

        # Add day indicators
        for i, day in enumerate(calendar.day_abbr):
            Label(f2, text=day, font=('freesansbold', 13)).grid(row=0, column=i)

        # Create empty matrix
        self.area = [ [ 0 for i in range(7) ] for j in range(6) ]
        # Fill matrix with buttons
        for ii in range(6):
            for jj in range(7):
                self.area[ii][jj] = Button(f2, text='', font=('freesansbold', 15, 'bold'), width=4, height=1, bd=0)
                self.area[ii][jj].bind("<Button-1>", self.click)
                self.area[ii][jj].grid(row=ii+1, column=jj)

        f2.pack()

        # Get Calendar button
        Button(self.master, command = self.getcal, text='Get Calendar', font=('freesansbold', 15, 'bold'), bd=10).pack()


if __name__ == '__main__':
    root = Tk()
    main(root)
    root.title('Calendar')
    root.mainloop()