from Window_set import *
from file_Loader import *
import Main_Page as mp
import shelve

sign_win_back_image = ImageTk.PhotoImage(Sign_Up_Image)
bg_image = Label(win_root, image=sign_win_back_image)


def make_new_inf():
    mp.uif[new_id_ent.get()] = new_pd_ent.get()


def delete_all_sign_up():
    forward_page_btn.place_forget()
    back_page_btn.place_forget()
    bg_image.place_forget()
    page_address.place_forget()

    new_id_ent.place_forget()
    new_pd_ent.place_forget()
    create_in_btn.place_forget()


def move_main_page():
    delete_all_sign_up()
    mp.Main_Page_set()


forward_page_btn = Button(win_root, text='뒤로가기', command=move_main_page)
back_page_btn = Button(win_root, text='앞으로', command=DISABLED)

page_address = Entry(win_root, width=800)

new_id_ent = Entry(win_root, width=800)
new_pd_ent = Entry(win_root, width=800)
create_in_btn = Button(win_root, text="회원가입", bg='yellow', fg='black', command=make_new_inf)

def set_sign_up_page():
    global bg_image

    page_address.delete(0, END)
    page_address.insert(0, 'https://www.Krome.com//회원가입')

    bg_image.place(x=0, y=0, width=1000, height=700)
    forward_page_btn.place(x=0, y=0, width=60, height=30)
    back_page_btn.place(x=60, y=0, width=60, height=30)
    page_address.place(x=120, y=0, width=840, height=30)

    new_id_ent.place(x=350, y=255, width=300, height=40)
    new_pd_ent.place(x=350, y=325, width=300, height=40)

    create_in_btn.place(x=350, y=410, width=300, height=50)



