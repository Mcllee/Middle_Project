from Window_set import *
from file_Loader import *
import Sign_Up_Page as sup
import Log_in_Page as lip

main_win_back_image = ImageTk.PhotoImage(mbg_image)
bg_image = Label(win_root, image=main_win_back_image)

user_name = ''


class Main_Page:
    user_id = ''
    user_password = ''


def all_delete_main(page_num):
    global user_name

    bg_image.place_forget()
    id_in_txt.place_forget()
    pasw_in_txt.place_forget()
    Sign_Up_btn.place_forget()
    Log_in_btn.place_forget()
    log_Out_btn.place_forget()
    Qite_btn.place_forget()
    forward_page_btn.place_forget()
    back_page_btn.place_forget()

    if page_num == 1:
        sup.set_sign_up_page()
    elif page_num == 2:
        if id_in_txt.get() != '아이디':
            lip.set_log_in_page(id_in_txt.get())
        else:
            lip.set_log_in_page('아이디를 잊어버린 학생')


def quit_win():
    exit()


def main_page_button():
    sup.delete_all_sign_up()
    lip.delete_log_in_page(0)


id_in_txt = Entry(win_root)
id_in_txt.insert(0, '아이디')

pasw_in_txt = Entry(win_root)
pasw_in_txt.insert(0, '비밀번호')

Sign_Up_btn = Button(win_root, text='회원가입', command=lambda: all_delete_main(1))

Log_in_btn = Button(win_root, text='로그인', command=lambda: all_delete_main(2))

log_Out_btn = Button(win_root, text='로그아웃')

Qite_btn = Button(win_root, text='종료', command=quit_win)

forward_page_btn = Button(win_root, text='뒤로가기', command=DISABLED)
back_page_btn = Button(win_root, text='앞으로', command=DISABLED)

page_address = Entry(win_root, width=800)
page_address.insert(0, 'https://www.Krome.com')

Main_page_btn = Button(win_root, text='⌂', command=main_page_button)


def Main_Page_set():
    global bg_image, id_in_txt, pasw_in_txt, Sign_Up_btn, log_Out_btn, Qite_btn

    page_address.delete(0, END)
    page_address.insert(0, 'https://www.Krome.com')

    bg_image.place(x=200, y=50)

    id_in_txt.place(x=430, y=400, width=150, height=40)

    pasw_in_txt.place(x=430, y=450, width=150, height=40)

    Log_in_btn.place(x=430, y=500, width=70, height=40)

    Sign_Up_btn.place(x=430, y=545, width=150, height=30)

    log_Out_btn.place(x=510, y=500, width=70, height=40)

    Qite_btn.place(x=430, y=580, width=150, height=30)

    forward_page_btn.place(x=0, y=0, width=60, height=30)

    back_page_btn.place(x=60, y=0, width=60, height=30)

    page_address.place(x=120, y=0, width=840, height=30)

    Main_page_btn.place(x=960, y=0, width=40, height=30)
