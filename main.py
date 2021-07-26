try:
    import tkinter as tk
    from tkinter import *
    from tkinter import filedialog as fd
    from tkinter import ttk
    from tkinter import messagebox as msg
    import onetimepad
    import plyer
    import threading
    import time
    import os
except ImportError as e:
    print('no named module Found')
            

win = tk.Tk()
win.title('Encrypt/Decrypt Text')
win.geometry('1590x1200+0+0')
win.wm_iconbitmap('favicon.ico')
image1 = tk.PhotoImage(file='2.png')
lbl_img = tk.Label(win,image=image1)
lbl_img.pack(pady=250)

#------------------Backend Functions--------------

def exit_func(event=None):
    exit = tk.messagebox.askyesno("Exit",'Do you want to really close the program!')
    try:
        if exit is True:
            win.destroy()
        else:
            return
    except:
        return
    
def show_time():
    get_time = time.asctime()
    return get_time

def notification_me():
    while True:
        plyer.notification.notify(
            title='Cryptography',
            message='Cryptography is art of communication between two users via coded message and it is the art of conceling the message to introduce privacy and sececy',
            timeout=2,
            app_icon='favicon.ico'
        )
        time.sleep(30)

def encrypt():
    txt = entry2.get()
    enc_txt = onetimepad.encrypt(txt,'random')
    lbxo.insert(tk.END,enc_txt)

def decrypt():
    txt = entry1.get()
    dec_txt = onetimepad.decrypt(txt,'random')
    lbxo1.insert(tk.END,dec_txt)
    

def rev_cipher():
    txt = entry2.get()
    translated = ''
    i = len(txt)-1
    while i >= 0:
        translated += txt[i]
        i -= 1
    lbxo.insert(tk.END,translated)

def ceaser_cipher():
    txt = entry2.get()
    s = 6
    result = ''
    for i in range(len(txt)):
        const = txt[i]
        if const.isupper():
            result += chr((ord(const)+ s-65) % 26 + 65)
        else:
            result += chr((ord(const)+ s-97) % 26 + 97)
    lbxo.insert(tk.END,result)

def ceaser_cipher_dec():
    txt = entry2.get()
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for key in range(len(LETTERS)):
        translated = ''
        for symbol in txt:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num -= key
                if num < 0:
                    num += len(LETTERS)
                translated += LETTERS[num]
            else:
                translated += symbol
        get_txt = '-->%s: %s' %(key,translated)
        lbxo1.insert(tk.END,get_txt)         

th1 = threading.Thread(target=notification_me)
th1.setDaemon(True)
th1.start()

#------------------------------------------------
#------------------Menu Bar---------------------

menu_bar = Menu(win)
win.config(menu=menu_bar)
edit_menu = Menu(menu_bar,tearoff=False)
edit_menu.add_command(label='Exit',compound=tk.LEFT,accelerator='ctrl+X',command=lambda:exit_func.event_generate("<Control x>"))
menu_bar.add_cascade(label='Edit',menu=edit_menu)

#-----------------------GUI--------------------------
f = ('sans_serif',15,'bold')
f1 = ('helvetica',13,'bold')
#----------------------------Frame 1--------------------------

frm1 = tk.Frame(win,bd=5,relief='ridge')
frm1.place(x=10,y=10,width=650,height=650)

frm_2 = tk.Frame(frm1,bd=5,relief='ridge')
frm_2.place(x=10,y=400,width=420,height=230)

title = tk.Label(frm_2,text='-Decryption-',font=('times new roman',30,"bold"))
title.pack(side='top',fill="x",padx=10,pady=10)
title.configure(background='black',foreground='white')

lbl = ttk.Label(frm_2,text='Enter Text:--',font=('times new roman',15,"bold"))
lbl.pack()

entry1= ttk.Entry(frm_2,width=17,font=('times new roman',18,"bold"),cursor='dot',show='*')
entry1.pack(pady=5)

frm_3 = tk.Frame(frm1,bd=5,relief='ridge')
frm_3.place(x=15,y=10,width=420,height=360)

title = tk.Label(frm_3,text='-Encryption-',font=('times new roman',30,"bold"))
title.pack(side='top',fill="x",padx=10,pady=10)
title.configure(background='black',foreground='white')

lbl = ttk.Label(frm_3,text='Enter Text:--',font=('times new roman',15,"bold"))
lbl.pack()

entry2= ttk.Entry(frm_3,width=17,font=('times new roman',18,"bold"),cursor='dot')
entry2.pack(pady=5)

frm_1 = tk.Frame(frm1,bd=5,relief='ridge')
frm_1.place(x=450,y=10,width=180,height=620)

btn1 = tk.Button(frm_1,bd=3,width=10,text='Encrypt',command=encrypt)
btn1.pack(pady=10,padx=10,fill='both')

btn2 = tk.Button(frm_1,bd=3,width=10,text='Decrypt',command=decrypt)
btn2.pack(pady=10,padx=10,fill='both')

btn3 = tk.Button(frm_1,bd=3,width=10,text='Reverse/Cipher',command=rev_cipher)
btn3.pack(pady=10,padx=10,fill='both')

btn4 = tk.Button(frm_1,bd=3,width=10,text='caesar Cipher',command=ceaser_cipher)
btn4.pack(pady=10,padx=10,fill='both')

btn5 = tk.Button(frm_1,bd=3,width=10,text='Ceaser Cipher Decrypt',command=ceaser_cipher_dec)
btn5.pack(pady=10,padx=10,fill='both')

#---------------------------Frame 2-------------------------------

frm2 = tk.Frame(win,bd=5,relief='ridge',bg='orange')
frm2.place(x=880,y=10,width=310,height=650)

lbxo = tk.Listbox(frm2,height=15,width=15,bg='#7d7e80',activestyle='dotbox',font = f1)
lbxo.pack(fill='both',padx=15,pady=15)

lbxo1 = tk.Listbox(frm2,height=15,width=15,bg='#7d7e80',activestyle='dotbox',font = f1)
lbxo1.pack(fill='both',padx=15,pady=15)

#----------------------------Frame 4----------------------------------

frm4 = tk.Frame(win,bd=5,relief='ridge')
frm4.place(x=1230,y=10,width=292,height=650)

lblfrm1 = tk.LabelFrame(frm4,text='Current_time',height=200,bd=5,fg='red',cursor='dot',font=f)
lblfrm1.pack(padx=10,pady=10,fill='both')

lbl_frm = tk.Label(lblfrm1,text=show_time(),font=f)
lbl_frm.grid()

lbl_2 = tk.Label(frm4,text='Earlier cryptography \n was effectively \n synonymous with \n encryption but nowadays \n cryptography is mainly based on \n mathematical\n theory and computer \n science practice.Modern \n cryptography concerns with.\n Confidentiality - Information cannot be understood \n by anyone \n Integrity -\n Information cannot be altered. \n Non-repudiation \n- Sender cannot deny his/her \n intentions in the \n transmission of the information at \n a later stage \n Authentication - Sender and \n receiver can confirm each \n Cryptography is used in many \n applications like banking \n transactions cards, computer passwords,\n  and e- commerce \n transactions.',font=('sans-serif',10,'bold'))
lbl_2.pack(padx=10,pady=10)

#-----------------------------------------Frame 3--------------------------------

frm3 = tk.Frame(win,bd=9,relief='ridge',bg='skyblue')
frm3.place(x=10,y=670,width=1510,height=148)

win.bind("<Control-x>",exit_func)

win.mainloop()

