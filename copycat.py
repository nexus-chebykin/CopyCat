import os
import time
from tkinter import filedialog, messagebox
import subprocess, pathlib
from tkinter import *
import ctypes


def addFolder():
    global sources_gui_text
    dir = filedialog.askdirectory(parent=root)
    if dir != '':
        sources_gui_text.set(sources_gui_text.get() + f'\n{dir}')
        source_folders.append(dir)

def setDestination():
    global dest
    dir = filedialog.askdirectory(parent=root)
    dest_gui_text.set(f'Destination: {dir}')
    dest = dir


def popupWindow():
    answer = messagebox.askquestion(title='Уверены?',
                                    message="Хотите продолжить?")
    if answer == 'yes':
        root.destroy()
        do()


def do():
    for folder in source_folders:
        print(f'Copying from {folder} to {dest}')
        s = subprocess.run(
            ['robocopy', folder, dest, '/E', f'/MT:{os.cpu_count()}', '/NFL', '/NDL', '/NJH',
             '/NJS'], capture_output=True)
        print(s)
    print('everything is done')
    time.sleep(100000)

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2) # if your windows version >= 8.1
except:
    ctypes.windll.user32.SetProcessDPIAware() # win 8.0 or less


source_folders = []
dest = ''
root = Tk(className='Выбор файлов')
add_folder_button = Button(text="Добавить папку", height=5, width=50,
                           command=addFolder)
sources_gui_text = StringVar(value='Sources:')
sources_list_gui = Label(textvariable=sources_gui_text)
dest_button = Button(text="Конечная папка", height=5, width=50,
                     command=setDestination)
dest_gui_text = StringVar(value='Destination:')
dest_gui = Label(textvariable=dest_gui_text)
copy_button = Button(text='Скопировать!', height=5, width=50,
                     command=popupWindow)
add_folder_button.pack()
dest_button.pack()
sources_list_gui.pack()
dest_gui.pack()
copy_button.pack()
root.mainloop()
