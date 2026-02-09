import tkinter
from tkinter import *
from tkinter.filedialog import *

#텍스트 창 함수
def new_file():
    text_area.delete("1.0", END)

#파일 저장함수
def save_file():
    f = asksaveasfile(mode='w', defaultextension='.txt',filetypes=[('text files', '.txt')])
    text_save = str(text_area.get("1.0", END))
    f.write(text_save)
    f.close()

def marker():
    help_view = Toplevel(window)
    help_view.geometry("200x50")
    help_view.title("만든이")
    lb = Label(help_view,text = "주성현의 메모장")
    lb.pack()

window = Tk()
window.title("Notepad")
window.geometry("400x400")
window.resizable(True, True)

menu = Menu(window) # 최상위 메뉴
menu_1 = Menu(menu, tearoff=0) # 하위 메뉴
menu_1.add_command(label="새파일",command=new_file)
menu_1.add_command(label="저장",command=save_file)
menu_1.add_separator() # 구분선
menu_1.add_command(label="종료", command=window.destroy)
menu.add_cascade(label="파일", menu=menu_1)

menu_2 = Menu(menu, tearoff=0)
menu_2.add_command(label="만든이",command=marker)
menu.add_cascade(label="만든이", menu=menu_2)

text_area = Text(window)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

#텍스트 입력창으로 가득 채운다
text_area.grid(sticky = N + E + S + W)

window.config(menu=menu)
window.mainloop()
