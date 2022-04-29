from Window_set import *
import Main_Page as mp
import file_creater as fc
import Mail_Page as mc
import Sudoku_Page as sp        # 스도쿠 페이지 이동
from tkinter import *

# Main Page에서 받아온 사용자의 이름
save_name = ''

sdFont = tkFont.Font(family="Arial", size=20, weight="bold")
# 윈도우 위젯 선언
buttons_frame = LabelFrame(win_root, text='Krome의 기능', bg="gray", width=800, height=150, font=sdFont)
file_btn = Button(buttons_frame, text='파일 제작하기', command=lambda: [delete_log_in_page(1)], font=sdFont, fg="deep sky blue")
mail_btn = Button(buttons_frame, text='메일 보내기', command=lambda: [delete_log_in_page(2)], font=sdFont, fg="gold2")
object_viewer_btn = Button(buttons_frame, text='스도쿠 게임하기', command=lambda: [delete_log_in_page(3)], font=sdFont, fg="IndianRed1")


# 페이지 이동 함수
def move_page():
    try:
        mp.page_list.pop(-1)
        move_to = mp.page_list[-1]
        mp.page_list.pop(-1)

        match move_to:
            case "Main":
                delete_log_in_page(0)
            case "File":
                delete_log_in_page(1)
            case "Mail":
                delete_log_in_page(2)
            case "Sudoku":
                delete_log_in_page(3)
    except IndexError:
        print("범위 오류")


# 로그인 페이지 생성 함수
def set_log_in_page(user_name):
    mp.page_list.append("Log_in")

    global save_name
    save_name = str(user_name)   # delete에서 다른 페이지로 넘어갈 때 넘겨준다.

    # 위젯 배치 설정
    buttons_frame.place(x=100, y=450)
    file_btn.place(x=40, y=25, width=200, height=70)
    mail_btn.place(x=300, y=25, width=200, height=70)
    object_viewer_btn.place(x=560, y=25, width=200, height=70)
    # 주소창 초기화
    mp.page_address.delete(0, END)
    mp.page_address.insert(0, '...//어서오세요! ' + str(user_name) + '님! 원하시는 작업을 선택해주세요!')
    # 페이지 이동 버튼 재설정
    mp.back_page_btn.config(state=NORMAL, command=lambda: [delete_log_in_page(0)])
    mp.Main_page_btn.config(state=NORMAL, command=lambda: [delete_log_in_page(0)])

    if len(mp.page_list) <= 2:
        mp.forward_page_btn.config(state=DISABLED)
    else:
        mp.forward_page_btn.config(state=NORMAL, command=lambda: [move_page])

    mp.bg_image.place(x=160, y=50)


# 로그인 페이지 위젯 가리고 다음 페이지 이동 함수
def delete_log_in_page(next_page):
    buttons_frame.place_forget()
    file_btn.place_forget()
    mail_btn.place_forget()
    object_viewer_btn.place_forget()

    mp.bg_image.place_forget()

    match(next_page):
        case 0:
            mp.Main_Page_set()
        case 1:
            fc.file_creater.set_fc(save_name)
        case 2:
            mc.mail_creater.set_mc(save_name)
        case 3:
            sp.sudoku_creater.set_sp(save_name)
