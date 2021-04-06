from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import font,messagebox,filedialog,colorchooser
import os 

win=tk.Tk()
win.geometry('1280x800')
win.title('YRpad editor')

# part 1
mainmenu=tk.Menu()

url=''
def new():
    global url
    url=''
    text_editor.delete(1.0,tk.END)

def open_1(event=None):
    global url
    url=filedialog.askopenfilename(initialdir=os.getcwd(),title='select file',filetypes=(('Text File','*.txt'),('All files','*.*')))
    try:
        with open(url,'r')as r:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,r.read())
    except:
        return
    win.title(os.path.basename(url))

def save_1(even=None):
    global url
    try:
        if url:
            content=str(text_editor.get(1.0,tk.END))
            with open(url,'w',encoding='utf-8')as r:
              r.write(content)
        else:
            url=filedialog.asksaveasfile(mode='w',defaultextension=".txt",  filetypes=(('Text File','*.txt'),('All files','*.*')))
            content2=str(text_editor.get(1.0,tk.END))
            url.write(content2)
    except:
        return


def saveas_1(even=None):
    global url
    try:
        content=text_editor.get(1.0,tk.END)
        url=filedialog.asksaveasfile(mode='w',defaultextension=".txt",  filetypes=(('Text File','*.txt'),('All files','*.*')))
        url.write(content)
        url.close()
    except:
        return

def exit_1(even=None):
    mbox=messagebox.askyesno('Warning','Do you want to exit')
    if mbox is True:
        win.destroy()
    elif mbox is False:
        pass

file=tk.Menu(mainmenu,tearoff=False)
file.add_command(label='New',accelerator='Ctrl+N',command=new)
file.add_command(label='Open',accelerator='Ctrl+O',command=open_1)
file.add_command(label='Save',accelerator='Ctrl+S',command=save_1)
file.add_command(label='Save as',accelerator='Ctrl+Alt+S',command=saveas_1)
file.add_command(label='Exit',accelerator='Ctrl+Q',command=exit_1)

Edit=tk.Menu(mainmenu,tearoff=False)
Edit.add_command(label='copy',accelerator='Ctrl+C',command=lambda:text_editor.event_generate('<Control c>'))
Edit.add_command(label='past',accelerator='Ctrl+V',command=lambda:text_editor.event_generate('<Control v>'))
Edit.add_command(label='cut',accelerator='Ctrl+X',command=lambda:text_editor.event_generate('<Control x>'))
Edit.add_command(label='find',accelerator='Ctrl+F')
Edit.add_command(label='clear all',command=lambda:text_editor.delete(1.0,tk.END))




mainmenu.add_cascade(label='file',menu=file)
mainmenu.add_cascade(label='edit',menu=Edit)


# part 2

tool_bar=ttk.Label(win)
tool_bar.pack(side=tk.TOP,fill=tk.X)

font_t=tk.font.families()
font_family=tk.StringVar()
font_box=ttk.Combobox(tool_bar,width=30,textvariable=font_family,state='read only')
font_box['values']=font_t
font_box.current(font_t.index('Arial'))
font_box.grid(row=0,column=0,padx=5)

# ?part 2.1

size_bar=tk.IntVar()
font_size=ttk.Combobox(tool_bar,width=14,textvariable=size_bar,state='readonly')
font_size['values']=tuple(range(8,81))
font_size.current(4)
font_size.grid(row=0,column=1 ,padx=5)

# ?bold button

bold_btn1=ttk.Button(tool_bar,text='Bold')
bold_btn1.grid(row=0,column=2,padx=5)
bold_btn2=ttk.Button(tool_bar,text='italic')
bold_btn2.grid(row=0,column=3,padx=5)
bold_btn3=ttk.Button(tool_bar,text='Underline')
bold_btn3.grid(row=0,column=4,padx=5)
bold_btn4=ttk.Button(tool_bar,text='colour')
bold_btn4.grid(row=0,column=5,padx=5)

# text editor

text_editor=tk.Text(win)
text_editor.config(wrap='word',relief=tk.FLAT)

# scrolbar

scbar=tk.Scrollbar(win)
scbar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.focus_set()
text_editor.pack(fill=tk.BOTH,expand=True)
scbar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scbar.set)


# font size
curent_font_family='Arial'
curent_font_size=12
def change_font(win):
    global curent_font_family
    curent_font_family=font_family.get()
    text_editor.config(font=(curent_font_family,curent_font_size))

def change_font_size(win):
    global curent_font_size
    curent_font_size=size_bar.get()
    text_editor.config(font=(curent_font_family,curent_font_size))

font_box.bind('<<ComboboxSelected>>',change_font)
font_size.bind('<<ComboboxSelected>>',change_font_size)

text_editor.config(font=('Arial',12))

# for bold
def change_bold(event):
    text_bold=tk.font.Font(font=text_editor['font'])
    if text_bold.actual()['weight']=='normal':
        text_editor.config(font=(curent_font_family,curent_font_size,'bold'))
    if text_bold.actual()['weight']=='bold':
        text_editor.config(font=(curent_font_family,curent_font_size,'normal'))

bold_btn1.bind('<Button-1>',change_bold)


# for italic?
def change_italic(event):
    text_bold=tk.font.Font(font=text_editor['font'])
    if text_bold.actual()['slant']=='roman':
        text_editor.config(font=(curent_font_family,curent_font_size,'italic'))
    if text_bold.actual()['slant']=='italic':
        text_editor.config(font=(curent_font_family,curent_font_size,'roman'))

bold_btn2.bind('<Button-1>',change_italic)

# for underline
def change_underline(event):
    text_bold=tk.font.Font(font=text_editor['font'])
    if text_bold.actual()['underline']==0:
        text_editor.config(font=(curent_font_family,curent_font_size,'underline'))
    if text_bold.actual()['underline']==1:
        text_editor.config(font=(curent_font_family,curent_font_size,'normal'))

bold_btn3.bind('<Button-1>',change_underline)

# for color
def change_color(event):
    color_var=tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])
bold_btn4.bind('<Button>',change_color)


# statusbar
sbar=ttk.Label(win,text='statusbar')
sbar.pack(side=tk.BOTTOM)

def count(event=None):
    if text_editor.edit_modified():
         
        words=len(text_editor.get(1.0,'end-1c').split())
        characters=len(text_editor.get(1.0,'end-1c'))
        sbar.configure(text=f'words:{words} characters:{characters}')
    text_editor.edit_modified(False)
text_editor.bind('<<Modified>>',count)  

win.config(menu=mainmenu)
win.mainloop()
