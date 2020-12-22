from tkinter import *
from tkinter import ttk

import smtplib
import webbrowser

root = Tk()
root.title("mail text message")
root.geometry('600x450')
root.iconbitmap('gmail.ico')
root.resizable(0, 0)


def sendemail():
    try:
        sender = acct.get()
        password = passwd.get()
        recipients = reciv.get()
        subject = sub.get()
        msg = msg_entry.get(1.0, 'end')
        finalmsg = f'Subject:{subject}\n\n{msg}'

        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.starttls()
        mail.login(sender, password)
        mail.sendmail(sender, recipients, finalmsg)
        mail.close()
        ttk.Label(mainframe, text="email sent successfully").grid(column=4, row=9, sticky='w')
        reset()
    except Exception as e:
        ttk.Label(mainframe, text="Check Mail ID or PassWord").grid(column=4, row=9, sticky='w')
        reset()


def setup(event):
    webbrowser.open_new(r"https://www.gmail.com")


def reset():
    acct_entry.delete(0, 'end')
    passwd_entry.delete(0, 'end')
    reciv_entry.delete(0, 'end')
    sub_entry.delete(0, 'end')
    msg_entry.delete(1.0, 'end')


mainframe = ttk.Frame(root, padding="4 4 13 13")
mainframe.grid(column=0, row=0, sticky='nsew')
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

acct = StringVar()
passwd = StringVar()
reciv = StringVar()
sub = StringVar()

lbl = Label(mainframe, text="send mail via gmail", fg='blue', cursor="hand2", font=('algerian', 15))
lbl.grid(columnspan=2, column=0, row=0, sticky='w')
lbl.bind("<Button-1>", setup)

Label(mainframe, text="FROM:", font=('britannic', 12)).grid(column=0, row=2, sticky='w')
acct_entry = Entry(mainframe, width=30, textvariable=acct, font=('bold'))
acct_entry.grid(column=4, row=2, sticky='we')

Label(mainframe, text="Your Password", font=('britannic', 12)).grid(column=0, row=3, sticky='w')
passwd_entry = Entry(mainframe, show="*", width=30, textvariable=passwd, font=('bold'))
passwd_entry.grid(column=4, row=3, sticky='we')

Label(mainframe, text="TO:", font=('britannic', 12)).grid(column=0, row=4, sticky='w')
reciv_entry = Entry(mainframe, width=30, textvariable=reciv, font=('bold'))
reciv_entry.grid(column=4, row=4, sticky='we')

Label(mainframe, text="Subject:", font=('britannic', 12)).grid(column=0, row=5, sticky='w')
sub_entry = Entry(mainframe, width=30, textvariable=sub, font=('bold'))
sub_entry.grid(column=4, row=5, sticky='we')

Label(mainframe, text="Message:", font=('britannic', 12)).grid(column=0, row=6, sticky='w')
msg_entry = Text(mainframe, width=30, height=10)
msg_entry.grid(column=4, row=6, sticky='we')

Button(mainframe, text="send Email ", command=sendemail).grid(column=4, row=7)

Button(mainframe, text='Reset', command=reset).grid(column=4, row=7, sticky='w')
Button(mainframe, text='Close', command=root.destroy).grid(column=4, row=7, sticky='e')

for child in mainframe.winfo_children(): child.grid_configure(padx=5,pady=5)
acct_entry.focus()




Label(mainframe, text="~~created by ABHISHEK and AMRIT", fg='skyblue', font=('bradley hand itc', 10)).grid(row=0,column=4,sticky='e',padx=5)
root.mainloop()
