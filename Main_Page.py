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
bg_image = Label(win_root, image=main_win_back_image, borderwidth=0, relief="flat")
# 사용자 이름 저장 문자열
user_name = ''
user_id = ''
sdFont = tkFont.Font(family="Arial", size=11, weight="bold")
# 윈도우 위젯 선언
inf_frame = LabelFrame(win_root, text='로그인 하기', width=200, height=250, bg="gray", font=sdFont)
id_in_txt = Entry(inf_frame, font=sdFont)
pasw_in_txt = Entry(inf_frame, show="●", font=sdFont)
Sign_Up_btn = Button(inf_frame, text='회원가입', command=lambda: all_delete_main(1), font=sdFont)
Log_in_btn = Button(inf_frame, text='로그인', command=lambda: all_delete_main(2), font=sdFont)
log_Out_btn = Button(inf_frame, text='로그아웃', command=lambda: [
                                                id_in_txt.delete(0, END),
                                                id_in_txt.insert(0, "아이디"),
                                                pasw_in_txt.delete(0, END),
                                                pasw_in_txt.insert(0, "비밀번호"),
                                                msgbox.showinfo("로그아웃", "정상적으로 로그아웃이 실행되었습니다.")], font=sdFont)
Qite_btn = Button(inf_frame, text='종료', command=lambda: quit(), font=sdFont)
forward_page_btn = Button(win_root, text='앞으로')
back_page_btn = Button(win_root, text='뒤로가기')
page_address = Entry(win_root, width=800)
Main_page_btn = Button(win_root, text='⌂', command=lambda: [sp.delete_sp(),
                                                            sup.delete_all_sign_up(),
                                                            lip.delete_log_in_page(0)])


# 비밀번호를 가릴 것인지 보여줄 것인지 선택하는 함수
def check():
    if order.get():
        pasw_in_txt.config(show="")
    else:
        pasw_in_txt.config(show="●")


# 비밀번호를 가리기위한 변수와 체크박스
order = IntVar()
show_pw = Checkbutton(inf_frame, bg='gray', variable=order, command=check)

page_list = []  # 페이지 리스트


# 메인 페이지의 위젯들을 지우고 다음 페이지를 호출하는 함수
def all_delete_main(page_num):
    global user_name
    global user_score

    inf_frame.place_forget()
    bg_image.place_forget()
    id_in_txt.place_forget()
    pasw_in_txt.place_forget()
    Sign_Up_btn.place_forget()
    Log_in_btn.place_forget()
    log_Out_btn.place_forget()
    Qite_btn.place_forget()
    show_pw.place_forget()
    
    # 다음 페이지 match-case 선택기 (1: 회원가입 페이지, 2: 로그인 페이지)
    match page_num:
        case 1:
            sup.set_sign_up_page()
        case 2:
            if id_in_txt.get() != '아이디':
                try:
                    user_pw = uif[id_in_txt.get()][0]   # shelve모듈을 이용해 입력된 정보 찾기
                    if user_pw == pasw_in_txt.get():    # 제대로된 정보가 존재할 경우
                        lip.set_log_in_page(uif[id_in_txt.get()][1])
                    else:                               # 입력된 정보가 없을 경우 KeyError를 발생시킨다.
                        raise KeyError
                except KeyError:                        # 정상적인 정보가 아닐 경우
                    msgbox.showinfo("로그인 오류", "잘못된 아이디 혹은 비밀번호 입니다!")
                    Main_Page_set()
            else:                                       # 엔트리에 입력된 정보가 없을 경우
                msgbox.showinfo("로그인 오류", "아이디 혹은 비밀번호를 입력해주세요!")
                Main_Page_set()


# 아이디, 비밀번호 모두 입력 완료시 enter키를 누르면 입력을 받아준다.
def push_enter(event):
    all_delete_main(2)


# 비밀번호 text를 binding한다.
pasw_in_txt.bind("<Return>", push_enter)


# 메인 페이지 초기화 함수
def Main_Page_set():
    global bg_image, id_in_txt, pasw_in_txt, Sign_Up_btn, log_Out_btn, Qite_btn

    # 페이지 방문 기록 초기화 및 추가
    page_list.clear()
    page_list.append("Main")

    # 메인 이미지
    bg_image.place(x=160, y=50)

    # 회원 아이디, 비밀번호 입력 엔트리
    inf_frame.place(x=420, y=390)
    id_in_txt.place(x=10, y=10, width=170, height=35)
    pasw_in_txt.place(x=10, y=60, width=150, height=35)
    show_pw.place(x=165, y=65)

    # 회원 정보 조작 버튼
    Log_in_btn.place(x=10, y=105, width=80, height=35)
    log_Out_btn.place(x=105, y=105, width=80, height=35)
    Sign_Up_btn.place(x=10, y=150, width=178, height=35)
    Qite_btn.place(x=10, y=190, width=178, height=35)

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
    forward_page_btn.config(state=DISABLED)
    back_page_btn.config(state=DISABLED)
    Main_page_btn.config(state=DISABLED)

    # 회원정보 입력 초기화
    id_in_txt.delete(0, END)
    id_in_txt.insert(0, '아이디')
    pasw_in_txt.delete(0, END)
    pasw_in_txt.insert(0, '비밀번호')

