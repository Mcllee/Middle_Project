import os
import pygame
from OpenGL.GL import *
from Window_set import *

import Main_Page as mp
import Log_in_Page as lip


def delete_fc(next_page):
    pass  # place_forget

    match (next_page):  # 이동 횟수(깊이)에 따라 넘버링
        case 1:
            lip.set_log_in_page(lip.save_name)
        case 2:
            mp.Main_Page_set()


class file_creater:
    #  윈도우 위젯 선언

    @staticmethod
    def set_fc(input_name):
        mp.page_address.delete(0, END)
        mp.page_address.insert(0, f"파일 제작소에 어서오세요! {input_name}님!")

        mp.back_page_btn.config(command=lambda: [delete_fc(1)])
