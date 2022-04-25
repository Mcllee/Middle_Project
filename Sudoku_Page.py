from Window_set import *
import Main_Page as mp
import random

quest = 0
level = 1
quest_position = []

#  윈도우 위젯 선언
sdFont = tkFont.Font(family="Helvetica", size=35)
label = [[0] * 9 for _ in range(9)]
txt = [[0] * 9 for _ in range(9)]
map_clear_btn = Button(win_root, text="모두 지우기")
new_game_btn = Button(win_root, text="새 게임", command=lambda: new_game(level))
check_game_btn = Button(win_root, text="정답 확인")
level_1_btn = Button(win_root, text="Level 1", command=lambda: new_game(1))
level_2_btn = Button(win_root, text="Level 2", command=lambda: new_game(2))
level_3_btn = Button(win_root, text="Level 3", command=lambda: new_game(3))


def delete_sp():
    for hei in range(0, 9):
        for wid in range(0, 9):
            txt[hei][wid].place_forget()
            label[hei][wid].place_forget()
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
            txt[hei][wid].delete(0, END)


def new_game(input_level):
    global sdFont
    global label
    global quest
    global level
    global quest_position

    # 사용하지 않는 칸을 전부 지운다.
    clear_all()

    if level != input_level:
        level = input_level
    quest = 0

    beg = 0
    beg_stack = 0
    for hei in range(0, 9):
        for wid in range(0, 9):
            label[hei][wid].configure(text=(str((beg + wid) % 9 + 1).center(3, ' ')), relief='solid')
            label[hei][wid].place(x=(100 + wid * 58), y=(100 + hei * 58), height=58, width=58)
        beg += 3
        if beg - beg_stack == 9:
            beg_stack += 1
            beg = beg_stack

    quest_position.clear()

    match level:
        case 1:
            for i in range(10):
                quest_position.append([random.randint(0, 8), random.randint(0, 8)])
        case 2:
            for i in range(40):
                quest_position.append([random.randint(0, 8), random.randint(0, 8)])
        case 3:
            for i in range(70):
                quest_position.append([random.randint(0, 8), random.randint(0, 8)])

    for i in range(0, 10*level):
        label[quest_position[i][1]][quest_position[i][0]].place_forget()
        txt[quest_position[i][1]][quest_position[i][0]].delete(0, END)
        txt[quest_position[i][1]][quest_position[i][0]].place(x=(100 + quest_position[i][0] * 58),
                                                              y=(100 + quest_position[i][1] * 58))
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




class sudoku_creater:
    global sdFont

    for hei in range(0, 9):
        for wid in range(0, 9):
            txt[hei][wid] = Entry(win_root, width=2, foreground='red', justify=CENTER)
            txt[hei][wid].configure(font=sdFont)

            label[hei][wid] = Label(win_root)
            label[hei][wid].config(font=sdFont)


    @staticmethod
    def set_sp(input_name):
        mp.page_address.delete(0, END)
        mp.page_address.insert(0, f"스도쿠 게임을 시작합니다! {input_name}님!")

        mp.back_page_btn.config(command=delete_sp)
        mp.forward_page_btn.config(command=delete_sp)

        for hei in range(0, 9):
            for wid in range(0, 9):
                txt[hei][wid].place(x=100 + wid * 58, y=100 + hei * 58)
                txt[hei][wid].delete(0, END)

        map_clear_btn.place(x=610, y=510)
        new_game_btn.place(x=410, y=510)
        check_game_btn.place(x=510, y=510)

        level_1_btn.place(x=900, y=300, width=100, height=50)
        level_2_btn.place(x=900, y=400)
        level_3_btn.place(x=900, y=500)

        map_clear_btn.config(command=clear_all)
        check_game_btn.config(command=check_game)
