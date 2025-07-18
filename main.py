def show_exception_and_exit(exc_type, exc_value, tb):
    import traceback
    traceback.print_exception(exc_type, exc_value, tb)
    input("Press key to exit.")
    sys.exit(-1)

import sys
sys.excepthook = show_exception_and_exit



import tkinter as tk
from tkinter import ttk
from tkinter import font



#______ Main Window Configuration _______

main = tk.Tk()
main.title("Assembly Word Database")
main_width = 1000
main_height = 700

def center_window(window, width, height):

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    
    window.geometry(f"{width}x{height}+{x}+{y}")

center_window(main, main_width, main_height)



#______ Style _______

s = ttk.Style(main)
#('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
s.theme_use('clam')
s.configure('TLabel', background='#F0F0F0')




#______ Main Frames _______


main_frame=tk.Frame(main, bg='#F0F0F0', height=1000, width=800)
main_frame.pack()

title=tk.Label(main_frame, font=('@Malgun Gothic', 36), padx=50, pady=30, text='Assembly Word Database')
title.grid()

sub_frame=tk.Frame(main_frame, bg='#F0F0F0')
sub_frame.grid()



#______ Properties Search _______

tk.Frame(sub_frame, bg='#F0F0F0', height=30, width=550).grid()

f=tk.Frame(sub_frame, bg='#F0F0F0')
f.grid(sticky=tk.W)

ttk.Label(f, text= 'Filter Properties: ', font='helvetica 12')grid(column=0, row=0)
ttk.Label(f, text= 'chose the desired properties below',font='helvetica 12').grid(column=1, row=0)

tk.Frame(sub_frame, bg='#F0F0F0', height=10, width=550).grid()


properties_search_border=tk.Frame(sub_frame, bg='grey', height=100, width=200,padx=3, pady=3)
properties_search_border.grid()
properties_search=tk.Frame(properties_search_border, bg='#F0F0F0', height=100, width=200,padx=10, pady=10)
properties_search.pack()

text_pad_x=10
text_pad_y=5


#column0
ttk.Label(properties_search, text='Size:').grid(column=0, row=0, padx=text_pad_x, pady=text_pad_y, sticky=tk.W)
ttk.Label(properties_search, text='Assembly Number:').grid(column=0, row=1, padx=text_pad_x, pady=text_pad_y, sticky=tk.W)


#column1
size_val=[str(i) for i in range(1,8)]
size_val.insert(0,'')
an_val=[str(i) for i in range(1,4)]
an_val.insert(0,'')

size_chosen=ttk.Combobox(properties_search, values=size_val, width=5)
size_chosen.grid(column=1, row=0, padx=text_pad_x, pady=text_pad_y, sticky=tk.W)
an_chosen=ttk.Combobox(properties_search, values=an_val, width=5)
an_chosen.grid(column=1, row=1, padx=text_pad_x, pady=text_pad_y, sticky=tk.W)


#column2
ttk.Label(properties_search, text='').grid(column=2, row=0, ipadx=text_pad_x+30, ipady=text_pad_y, sticky=tk.W)


#column3
ttk.Label(properties_search, text='Palindromic:').grid(column=3, row=0, padx=text_pad_x, pady=text_pad_y, sticky=tk.W)
ttk.Label(properties_search, text='Weakly Irriducible:').grid(column=3, row=1, padx=text_pad_x, pady=text_pad_y, sticky=tk.W)
ttk.Label(properties_search, text='Strongly Irriducible:').grid(column=3, row=2, padx=text_pad_x, pady=text_pad_y, sticky=tk.W)


#column4
f0=ttk.Frame(properties_search)
f0.grid(column=4, row=0, padx=text_pad_x, pady=text_pad_y)
f1=ttk.Frame(properties_search)
f1.grid(column=4, row=1, padx=text_pad_x, pady=text_pad_y)
f2=ttk.Frame(properties_search)
f2.grid(column=4, row=2, padx=text_pad_x, pady=text_pad_y)

pal=tk.StringVar()
w_i=tk.StringVar()
s_i=tk.StringVar()

pal_chosen=ttk.Radiobutton(f0, text = 'Any', value='0', variable=pal)
pal_chosen.grid(column=0, row=0)
pal_chosen.invoke()
ttk.Radiobutton(f0, text = 'Yes', value='1', variable=pal).grid(column=1, row=0)
ttk.Radiobutton(f0, text = 'No', value='2', variable=pal).grid(column=2, row=0) 

w_i_chosen=ttk.Radiobutton(f1, text = 'Any', value='0', variable=w_i)
w_i_chosen.grid(column=0, row=0)
w_i_chosen.invoke()
ttk.Radiobutton(f1, text = 'Yes', value='1', variable=w_i).grid(column=1, row=0)
ttk.Radiobutton(f1, text = 'No', value='2', variable=w_i).grid(column=2, row=0) 

s_i_chosen=ttk.Radiobutton(f2, text = 'Any', value='0', variable=s_i)
s_i_chosen.grid(column=0, row=0)
s_i_chosen.invoke()
ttk.Radiobutton(f2, text = 'Yes', value='1', variable=s_i).grid(column=1, row=0)
ttk.Radiobutton(f2, text = 'No', value='2', variable=s_i).grid(column=2, row=0) 



#______ Submittion Buttons _______

tk.Frame(sub_frame, bg='#F0F0F0', height=30, width=550).grid()

sumbit=tk.Frame(sub_frame, bg='grey', height=100, width=600)
sumbit.grid(sticky=tk.E)


def handle_search(): 
    size=size_chosen.get()
    an=an_chosen.get()
    

def handle_clear(): 
    size_chosen.current(newindex=0)
    an_chosen.current(newindex=0)
    pal_chosen.invoke()
    w_i_chosen.invoke()
    s_i_chosen.invoke()
    

def handle_quit(): 
    main.destroy()

tk.Button(
    sumbit, 
    text='Search', 
    font='helvetica 10',
    width=10,
    command=handle_search).grid(column=0, row=0, sticky=tk.W, padx=3, pady=3)
tk.Button(
    sumbit, 
    text='Clear', 
    font='helvetica 10',
    width=10,
    command=handle_clear).grid(column=1, row=0, sticky=tk.W, padx=3, pady=3)
tk.Button(
    sumbit, 
    text='Quit', 
    font='helvetica 10',
    width=10,
    command=handle_quit).grid(column=2, row=0, sticky=tk.W, padx=3, pady=3)




main.mainloop()