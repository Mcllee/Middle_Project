from tkinter import *
from Window_set import *
import Main_Page as mp

import file_creater as fc


def set_log_in_page(user_name):
    mp.page_address.delete(0, END)
    mp.page_address.insert(0, '...//어서오세요! ' + str(user_name) + '님! 원하시는 작업을 선택해주세요!')

    # mp.forward_page_btn.config(command=lambda: [delete_log_in_page(0)])
    # mp.back_page_btn.config(command=DISABLED)

    file_btn.place(x=430, y=500, width=140, height=40)
    mail_btn.place(x=430, y=550, width=140, height=40)
    object_viewer_btn.place(x=430, y=600, width=140, height=40)


def delete_log_in_page(next_page):
    file_btn.place_forget()
    mail_btn.place_forget()
    object_viewer_btn.place_forget()

    match(next_page):
        case 0:
            mp.Main_Page_set()
        case 1:
            fc.file_creater()
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass

file_btn = Button(win_root, text='파일 제작하기', command=lambda: [delete_log_in_page(1)])
mail_btn = Button(win_root, text='메일 보내기')
object_viewer_btn = Button(win_root, text='3D 모델 보기')

