from Window_set import *
from file_Loader import *
import Main_Page as mp


sign_win_back_image = ImageTk.PhotoImage(Sign_Up_Image)
bg_image = Label(win_root, image=sign_win_back_image)


def delete_all_sign_up():
    forward_page_btn.place_forget()
    back_page_btn.place_forget()
    bg_image.place_forget()
    page_address.place_forget()


def move_main_page():
    delete_all_sign_up()
    mp.Main_Page_set()

forward_page_btn = Button(win_root, text='뒤로가기', command=move_main_page)
back_page_btn = Button(win_root, text='앞으로', command=DISABLED)

page_address = Entry(win_root, width=800)


def set_sign_up_page():
    global bg_image

    page_address.delete(0, END)
    page_address.insert(0, 'https://www.Krome.com//회원가입')

    bg_image.place(x=0, y=0, width=1000, height=700)
    forward_page_btn.place(x=0, y=0, width=60, height=30)
    back_page_btn.place(x=60, y=0, width=60, height=30)
    page_address.place(x=120, y=0, width=840, height=30)



