from tkinter import *
from Window_set import *
import Main_Page as mp

import random


def delete_sp():
    # place_forget
    for hei in range(0, 9):
        for wid in range(0, 9):
            txt[hei][wid].place_forget()
    map_clear_btn.place_forget()
    new_game_btn.place_forget()
    check_game_btn.place_forget()
    mp.Main_Page_set()
    level_1_btn.place_forget()
    level_2_btn.place_forget()
    level_3_btn.place_forget()


def clear_all():
    for hei in range(0, 9):
        for wid in range(0, 9):
            txt[hei][wid].delete("1.0", END)


quest = 0
level = 1
quest_position = []

sdFont = tkFont.Font(family="Arial", size=16, weight="bold", slant="italic")
label = [[0] * 9 for _ in range(9)]


def game_level(input_level):
    global quest_position
    quest_position.clear()

    match input_level:
        case 1:
            for i in range(10):
                quest_position.append([random.randint(0, 8), random.randint(0, 8)])
        case 2:
            for i in range(40):
                quest_position.append([random.randint(0, 8), random.randint(0, 8)])
        case 3:
            for i in range(70):
                quest_position.append([random.randint(0, 8), random.randint(0, 8)])


def new_game(input_level):
    global sdFont
    global label
    global quest
    global level
    global quest_position

    if level != input_level:
        level = input_level
    quest = 0

    beg = 0
    beg_stack = 0
    for hei in range(0, 9):
        for wid in range(0, 9):
            label[hei][wid].configure(text=(' ' + str((beg + wid) % 9 + 1)))
            label[hei][wid].place(x=(380 + wid * 30), y=(200 + hei * 30), height=28, width=28)
        beg += 3
        if beg - beg_stack == 9:
            beg_stack += 1
            beg = beg_stack

    game_level(level)
    for i in range(0, 10*level):
        label[quest_position[i][1]][quest_position[i][0]].place_forget()
        txt[quest_position[i][1]][quest_position[i][0]].delete("1.0", END)
        txt[quest_position[i][1]][quest_position[i][0]].place(x=(380 + quest_position[i][0] * 30),
                                                              y=(200 + quest_position[i][1] * 30))
        quest += 1  # 문제 수 증가


def check_game():
    beg = 0
    beg_stack = 0
    success = 0
    for hei in range(0, 9):
        for wid in range(0, 9):
            if txt[hei][wid].get("1.0", END) != '\n':
                input_num = int(txt[hei][wid].get("1.0", END))
                check = ((beg + wid) % 9 + 1)
                if input_num == check:
                    success += 1
            else:
                continue
        beg += 3
        if beg - beg_stack == 9:
            beg_stack += 1
            beg = beg_stack

    if success == quest:
        msgbox.showinfo("성공!", "정답입니다!\n축하합니다!")
    else:
        msgbox.showinfo("실패!", f"아쉽군요! {success}개만 정답입니다.\n다시 도전하세요!")

#  윈도우 위젯 선언
txt = [[0] * 9 for _ in range(9)]
map_clear_btn = Button(win_root, text="모두 지우기", command=clear_all)
new_game_btn = Button(win_root, text="새 게임", command=lambda: new_game(level))
check_game_btn = Button(win_root, text="정답 확인", command=check_game)

level_1_btn = Button(win_root, text="Level 1", command=lambda: new_game(1))
level_2_btn = Button(win_root, text="Level 2", command=lambda: new_game(2))
level_3_btn = Button(win_root, text="Level 3", command=lambda: new_game(3))


class sudoku_creater:
    global sdFont

    for hei in range(0, 9):
        for wid in range(0, 9):
            txt[hei][wid] = Text(win_root, width=2, height=1, padx=1, pady=1)
            txt[hei][wid].configure(font=sdFont)

            label[hei][wid] = Label(win_root)
            label[hei][wid].config(font=sdFont)


    # beg = 0
    # beg_stack = 0
    # for hei in range(0, 9):
    #     for wid in range(0, 9):
    #         txt[hei][wid].insert(END, (beg + wid) % 9 + 1)
    #     beg += 3
    #     if beg - beg_stack == 9:
    #         beg_stack += 1
    #         beg = beg_stack


    @staticmethod
    def set_sp(input_name):
        mp.page_address.delete(0, END)
        mp.page_address.insert(0, f"스도쿠 게임을 시작합니다! {input_name}님!")

        # mp.back_page_btn.config(command=delete_sp)
        for hei in range(0, 9):
            for wid in range(0, 9):
                txt[hei][wid].place(x=380 + wid * 30, y=200 + hei * 30)
                txt[hei][wid].delete("1.0", END)


        map_clear_btn.place(x=610, y=510)
        new_game_btn.place(x=410, y=510)
        check_game_btn.place(x=510, y=510)

        level_1_btn.place(x=700, y=300)
        level_2_btn.place(x=700, y=400)
        level_3_btn.place(x=700, y=500)
