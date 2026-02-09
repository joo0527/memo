from tkinter import *
from tkinter.filedialog import *

# 텍스트창을 아무것도 안 쓰인 상태로!
def new_file():
    text_area.delete(1.0,END)

# 현재 쓰여진 내용을 파일로 저장하기
def save_file():
    f = asksaveasfile(mode = "w", defaultextension=".txt",filetypes=[('Text files', '.txt')])
    text_save = str(text_area.get(1.0, END))
    f.write(text_save)
    f.close()

# 누가 만들었는지 보여주는 창을 별도로 띄우기!
def maker():
    help_view = Toplevel(window) # 따로 메시지창 띄우기용
    help_view.geometry("300x50")
    help_view.title("만든이")
    lb = Label(help_view, text = "주성현이 만든 메모장입니다.")
    lb.pack()


window = Tk()
window.title("Notepad")
window.geometry("400x400")
window.resizable(True, True)

menu = Menu(window)
menu_1 = Menu(menu, tearoff=0)
menu_1.add_command(label="새파일", command=new_file)
menu_1.add_command(label="저장", command=save_file)
menu_1.add_separator()
menu_1.add_command(label="종료", command=window.destroy)
menu.add_cascade(label="파일", menu=menu_1)

menu_2 = Menu(menu, tearoff=0)
menu_2.add_command(label="만든이", command=maker)
menu.add_cascade(label="만든이", menu=menu_2)

text_area = Text(window)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky = N + E + S + W)

window.config(menu=menu)

window.mainloop()