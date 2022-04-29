from Window_set import *
from file_Loader import *
import Main_Page as mp

import re

# 회원가입 정보 입력시 영어 대문자/소문자, 숫자만 입력하도록 함
checking_input = re.compile('[a-zA-Z0-9]+')

# 배경 이미지
sign_win_back_image = ImageTk.PhotoImage(Sign_Up_Image)
bg_image = Label(win_root, image=sign_win_back_image)

# 윈도우 위젯
forward_page_btn = Button(win_root, text='뒤로가기')
back_page_btn = Button(win_root, text='앞으로', command=DISABLED)
page_address = Entry(win_root, width=800)
new_id_ent = Entry(win_root, width=800)
new_pd_ent = Entry(win_root, width=800)
new_name_ent = Entry(win_root, width=800)
create_in_btn = Button(win_root, text="회원가입", bg='yellow', fg='black')
sign_in_btn = Button(win_root, text="로그인", bg='white', relief="flat", fg='goldenrod3',
                                command=lambda: [delete_all_sign_up(), mp.Main_Page_set()])
overlap_btn = Button(win_root, text="중복확인", bg='white', relief="flat", fg='goldenrod3',
                                command=lambda: overlap_check_uif())

overlap_checker = False

# 중복된 아이디가 파일에 저장되어있는지 확인하는 함수
def overlap_check_uif():
    global overlap_checker
    try:
        if mp.uif[new_id_ent.get()][0] != '':
            msgbox.showinfo("잘못된 입력!", "이미 존재하는 아이디 입니다!")
            overlap_checker = False
        else:
            raise KeyError
    except KeyError:
        overlap_checker = True
        msgbox.showinfo("중복확인", "가입 가능한 아이디 입니다!")


# 새로운 사용자의 정보를 파일에 추가하는 함수
def make_new_inf():  # 회원 정보 저장
    global overlap_checker
    if overlap_checker is False:
        msgbox.showinfo("아이디 중복확인", "아이디의 중복을 확인해주세요!")
    elif checking_input.findall(new_id_ent.get()) and checking_input.findall(new_pd_ent.get()):
        mp.uif[new_id_ent.get()] = [new_pd_ent.get(), new_name_ent.get()]
        msgbox.showinfo("회원가입 성공!", "회원가입이 정상적으로 진행되었습니다!")
    else:
        msgbox.showinfo("잘못된 입력", "아이디 혹은 비밀번호는\n소문자, 대문자, 숫자만 입력해주세요.")
        new_id_ent.delete(0, END)
        new_pd_ent.delete(0, END)


# 회원가입 페이지 위젯들을 가리고 다음 페이지를 호출하는 함수
def delete_all_sign_up():
    forward_page_btn.place_forget()
    back_page_btn.place_forget()
    bg_image.place_forget()
    page_address.place_forget()

    sign_in_btn.place_forget()
    overlap_btn.place_forget()

    new_id_ent.place_forget()
    new_pd_ent.place_forget()
    new_name_ent.place_forget()
    create_in_btn.place_forget()


# 회원가입 페이지를 초기화하는 함수
def set_sign_up_page():
    mp.page_list.append("Sign_Up")

    global bg_image

    page_address.delete(0, END)
    page_address.insert(0, 'https://www.Krome.com//회원가입')

    bg_image.place(x=0, y=0, width=1000, height=700)
    forward_page_btn.place(x=0, y=0, width=60, height=30)
    back_page_btn.place(x=60, y=0, width=60, height=30)
    page_address.place(x=120, y=0, width=840, height=30)

    sign_in_btn.place(x=560, y=195, width=100, height=30)
    overlap_btn.place(x=460, y=225, width=100, height=20)

    new_id_ent.delete(0, END)
    new_id_ent.insert(0, "아이디를 입력해주세요.")
    new_id_ent.place(x=350, y=255, width=300, height=40)
    new_pd_ent.delete(0, END)
    new_pd_ent.insert(0, "비밀번호를 입력해주세요.")
    new_pd_ent.place(x=350, y=300, width=300, height=40)
    new_name_ent.delete(0, END)
    new_name_ent.insert(0, "닉네임을 입력해주세요.")
    new_name_ent.place(x=350, y=345, width=300, height=40)

    create_in_btn.place(x=350, y=410, width=300, height=50)

    forward_page_btn.config(command=lambda: [delete_all_sign_up(),
                                             mp.Main_Page_set()])
    create_in_btn.config(command=make_new_inf)

    mp.back_page_btn.config(state=NORMAL, command=lambda: [delete_all_sign_up(),
                                                            mp.Main_Page_set()])
    mp.Main_page_btn.config(state=NORMAL, command=lambda: [delete_all_sign_up(),
                                                            mp.Main_Page_set()])
    mp.page_address.delete(0, END)
    mp.page_address.insert(0, "※회원가입※")
