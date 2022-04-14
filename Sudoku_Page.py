from tkinter import *
from Window_set import *
import Main_Page as mp


def delete_sp():
    # place_forget

    mp.Main_Page_set()


class sudoku_creater:
    #  윈도우 위젯 선언

    @staticmethod
    def set_sp(input_name):
        mp.page_address.delete(0, END)
        mp.page_address.insert(0, f"스도쿠 게임을 시작합니다! {input_name}님!")

        # mp.back_page_btn.config(command=delete_sp)
        pass
