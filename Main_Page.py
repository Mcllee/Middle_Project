from Window_set import *        # 윈도우 기본 설정
from file_Loader import *       # 이미지 파일 읽기
import Sign_Up_Page as sup      # 회원가입 페이지 이동
import Log_in_Page as lip       # 로그인 페이지 이동
import Sudoku_Page as sp        # 스도쿠 페이지 이동
import shelve                   # 회원정보 저장용

# 사용자 데이터 저장소
uif = shelve.open('userInf.dat')
# 사용하는 이미지 받기
main_win_back_image = ImageTk.PhotoImage(mbg_image)
bg_image = Label(win_root, image=main_win_back_image)
# 사용자 이름 저장 문자열
user_name = ''
# 윈도우 위젯 선언
id_in_txt = Entry(win_root)
pasw_in_txt = Entry(win_root)
Sign_Up_btn = Button(win_root, text='회원가입', command=lambda: all_delete_main(1))
Log_in_btn = Button(win_root, text='로그인', command=lambda: all_delete_main(2))
log_Out_btn = Button(win_root, text='로그아웃', command=lambda: [
                                                id_in_txt.delete(0, END),
                                                id_in_txt.insert(0, "아이디"),
                                                pasw_in_txt.delete(0, END),
                                                pasw_in_txt.insert(0, "비밀번호"),
                                                msgbox.showinfo("로그아웃", "정상적으로 로그아웃이 실행되었습니다.")])
Qite_btn = Button(win_root, text='종료', command=lambda: quit())
forward_page_btn = Button(win_root, text='앞으로')
back_page_btn = Button(win_root, text='뒤로가기')
page_address = Entry(win_root, width=800)
Main_page_btn = Button(win_root, text='⌂', command=lambda: [sp.delete_sp(),
                                                            sup.delete_all_sign_up(),
                                                            lip.delete_log_in_page(0)])


def all_delete_main(page_num):
    global user_name

    bg_image.place_forget()
    id_in_txt.place_forget()
    pasw_in_txt.place_forget()
    Sign_Up_btn.place_forget()
    Log_in_btn.place_forget()
    log_Out_btn.place_forget()
    Qite_btn.place_forget()

    match page_num:
        case 1:
            sup.set_sign_up_page()
        case 2:
            if id_in_txt.get() != '아이디':
                try:
                    user_pw = uif[id_in_txt.get()][0]   # shelve모듈을 이용해 입력된 정보 찾기
                    if user_pw == '비밀번호':          # 입력된 정보가 없을 경우 KeyError를 발생시킨다.
                        raise KeyError
                    else:                               # 제대로된 정보가 존재할 경우
                        lip.set_log_in_page(uif[id_in_txt.get()][1])
                except KeyError:                        # 정상적인 정보가 아닐 경우
                    msgbox.showinfo("로그인 오류", "잘못된 아이디 혹은 비밀번호 입니다!")
                    Main_Page_set()
            else:                                       # 엔트리에 입력된 정보가 없을 경우
                lip.set_log_in_page('아이디를 잊어버린 학생')
        case 3:
            sp.sudoku_creater.set_sp(user_name)


def Main_Page_set():
    global bg_image, id_in_txt, pasw_in_txt, Sign_Up_btn, log_Out_btn, Qite_btn

    # 메인 이미지
    bg_image.place(x=200, y=50)
    # 회원 아이디, 비밀번호 입력 엔트리
    id_in_txt.place(x=430, y=400, width=150, height=40)
    pasw_in_txt.place(x=430, y=450, width=150, height=40)
    # 회원 정보 조작 버튼
    Log_in_btn.place(x=430, y=500, width=70, height=40)
    Sign_Up_btn.place(x=430, y=545, width=150, height=30)
    log_Out_btn.place(x=510, y=500, width=70, height=40)
    Qite_btn.place(x=430, y=580, width=150, height=30)
    # 페이지 이동 버튼(앞으로가기, 뒤로가기, 메인으로)
    forward_page_btn.place(x=60, y=0, width=60, height=30)
    back_page_btn.place(x=0, y=0, width=60, height=30)
    Main_page_btn.place(x=960, y=0, width=40, height=30)
    # 페이지 주소창(http:/ www. ...)
    page_address.place(x=120, y=0, width=840, height=30)

    # 주소창 재설정
    page_address.delete(0, END)
    page_address.insert(0, 'https://www.Krome.com')
    # 페이지 이동버튼 재설정
    forward_page_btn.config(command=lambda: None)
    back_page_btn.config(command=lambda: None)

    # 회원정보 입력 초기화
    id_in_txt.delete(0, END)
    id_in_txt.insert(0, '아이디')
    pasw_in_txt.delete(0, END)
    pasw_in_txt.insert(0, '비밀번호')
