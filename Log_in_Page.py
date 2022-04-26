from Window_set import *
import Main_Page as mp
import file_creater as fc
import Mail_Page as mc
import Sudoku_Page as sp        # 스도쿠 페이지 이동

# Main Page에서 받아온 사용자의 이름
save_name = ''
# 윈도우 위젯 선언
file_btn = Button(win_root, text='파일 제작하기', command=lambda: [delete_log_in_page(1)])
mail_btn = Button(win_root, text='메일 보내기', command=lambda: [delete_log_in_page(2)])
object_viewer_btn = Button(win_root, text='스도쿠 게임하기', command=lambda: [delete_log_in_page(3)])


def set_log_in_page(user_name):
    global save_name
    save_name = user_name   # delete에서 다른 페이지로 넘어갈 때 넘겨준다.

    # 위젯 배치 설정
    file_btn.place(x=430, y=500, width=140, height=40)
    mail_btn.place(x=430, y=550, width=140, height=40)
    object_viewer_btn.place(x=430, y=600, width=140, height=40)
    # 주소창 초기화
    mp.page_address.delete(0, END)
    mp.page_address.insert(0, '...//어서오세요! ' + str(user_name) + '님! 원하시는 작업을 선택해주세요!')
    # 페이지 이동 버튼 재설정
    mp.back_page_btn.config(command=lambda: [delete_log_in_page(0)])
    mp.forward_page_btn.config(command=DISABLED)


def delete_log_in_page(next_page):
    file_btn.place_forget()
    mail_btn.place_forget()
    object_viewer_btn.place_forget()

    match(next_page):
        case 0:
            mp.Main_Page_set()
        case 1:
            fc.file_creater.set_fc(save_name)
        case 2:
            mc.mail_creater.set_mc(save_name)
        case 3:
            sp.sudoku_creater.set_sp(save_name)
