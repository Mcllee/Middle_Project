from Window_set import *
from tkinter.ttk import *            # UpGrade tkinter
from tkinter import *

import Main_Page as mp
import Log_in_Page as lip

import smtplib
from email.mime.text import MIMEText  # 메일 제목과 내용을 설정하는 모듈
from tkinter.scrolledtext import ScrolledText

# 폰트 생성
bsFont = tkFont.Font(family="Arial", size=11, weight="bold")
sdFont = tkFont.Font(family="Arial", size=15, weight="bold")
sd_btn_Font = tkFont.Font(family="Arial", size=20, weight="bold")
# 위젯 선언
sender_frame = LabelFrame(win_root, text='송신자 정보', width=300, height=120, bg="gray", font=sdFont)
sender_id_ent = Entry(sender_frame, width=25, font=sdFont)
sender_pw_ent = Entry(sender_frame, width=25, show="●", font=sdFont)
# 수신자 정보 위젯
Recipient_frame = LabelFrame(win_root, text='수신자 정보', width=300, height=60, bg="gray", font=sdFont)
Recipient_id_ent = Entry(Recipient_frame, width=30, font=bsFont)
# 메일 제목 위젯
mail_title_frame = LabelFrame(win_root, text='메일 제목', width=300, height=60, bg="gray", font=sdFont)
mail_title = Entry(mail_title_frame, width=30, font=bsFont)
# 메일 송신 버튼
send_message_btn = Button(win_root, text="메일 보내기", font=sd_btn_Font, fg="red")
# 메일 내용 위젯
message_text_frame = LabelFrame(win_root, text='메일 내용', width=850, height=500, bg="gray", font=sdFont)
message_text = ScrolledText(message_text_frame, width=100, height=25, font=bsFont)

# 송신자의 비밀번호를 가릴지 선택하는 함수
def check():
    if order.get():
        sender_pw_ent.config(show="")
    else:
        sender_pw_ent.config(show="●")

# 송신자의 비밀번호 가림여부 연택기
order = IntVar()
show_pw = Checkbutton(sender_frame, variable=order, command=check, bg="white")


# 메일 발송 함수
def send_message():
    sender_id = sender_id_ent.get()
    sender_pw = sender_pw_ent.get()

    # 수신자 혹은 송신자 정보가 잘못 됬을 경우 반환함.
    if sender_id.find('@') == -1:
        msgbox.showinfo("송신 실패!", "송신자의 정보를 입력해주세요!")
        return

    if Recipient_id_ent.get().find('@') == -1:
        msgbox.showinfo("송신 실패!", "수신자의 정보를 입력해주세요!")
        return

    smtp_server = "smtp." + sender_id_ent.get().split('@')[1]

    smtp_info = {
        "smtp_server": smtp_server,     # SMTP 서버 주소
        "smtp_user_id": sender_id,      # 메일 아이디
        "smtp_user_pw": sender_pw,      # 메일 비밀 번호
        "smtp_port": 587                # SMTP 서버 포트
    }

    to = Recipient_id_ent.get()
    title = mail_title.get()

    msg = MIMEText(message_text.get("1.0", END), _charset="utf8")   # 메일 내용 입력

    msg['Subject'] = title
    msg['From'] = smtp_info['smtp_user_id']
    msg['To'] = to

    smtp = smtplib.SMTP(smtp_info['smtp_server'], smtp_info['smtp_port'])
    smtp.ehlo()
    smtp.starttls()
    smtp.login(sender_id, sender_pw)

    smtp.sendmail(msg['From'], msg['To'].split(','), msg.as_string())

    smtp.quit()


# 메일 페이지 위젯을 가리고 다음 페이지를 생성한다.
def delete_mc(next_page):
    sender_id_ent.place_forget()
    sender_pw_ent.place_forget()
    Recipient_id_ent.place_forget()
    mail_title.place_forget()
    send_message_btn.place_forget()
    message_text.place_forget()
    show_pw.place_forget()
    sender_frame.place_forget()
    Recipient_frame.place_forget()
    mail_title_frame.place_forget()
    message_text_frame.place_forget()

    match (next_page):  # 이동 횟수(깊이)에 따라 넘버링
        case 1:
            lip.set_log_in_page(lip.save_name)
        case 2:
            mp.Main_Page_set()
        case 3:  # 페이지 기록 리스트에서 하나씩 꺼내어 이전 페이지로 돌아간다.
            try:
                mp.page_list.pop(-1)        # 페이지 생성시 현재 페이지가 리스트에 추가되었으므로 제거
                move_to = mp.page_list[-1]  # 이전 페이지를 임시 변수에 저장
                mp.page_list.pop(-1)        # 이전 페이지로 이동할 것이므로 리스트에서 제거

                match move_to:              # 다음 페이지로 이동한다.
                    case "Log_in":
                        lip.set_log_in_page(lip.save_name)
            except IndexError:              # 이전 페이지가 없을 만큼 기록이 짧은 경우
                print("범위 오류")


# 메일 페이지 위젯 생성 클래스
class mail_creater:
    #  윈도우 위젯 선언

    @staticmethod
    def set_mc(input_name):
        mp.page_list.append("Mail")

        mp.page_address.delete(0, END)
        mp.page_address.insert(0, f"메일 시스템에 어서오세요! {input_name}님!")

        mp.back_page_btn.config(command=lambda: [delete_mc(1)])
        mp.forward_page_btn.config(command=lambda: [delete_mc(3)])
        mp.Main_page_btn.config(command=lambda: [delete_mc(2)])
        send_message_btn.config(command=send_message)

        #송신자 정보 출력
        sender_frame.place(x=80, y=40)
        sender_id_ent.place(x=10, y=15)
        sender_pw_ent.place(x=10, y=55)
        show_pw.place(x=260, y=57)

        Recipient_frame.place(x=420, y=40)
        Recipient_id_ent.place(x=10, y=5)
        mail_title_frame.place(x=420, y=100)
        mail_title.place(x=10, y=5)

        message_text_frame.place(x=80, y=180)
        message_text.place(x=10, y=10)
        send_message_btn.place(x=750, y=80)

        sender_id_ent.delete(0, END)
        sender_pw_ent.delete(0, END)
        Recipient_id_ent.delete(0, END)
        mail_title.delete(0, END)

        sender_id_ent.insert(0, "송신자 메일 아이디")
        sender_pw_ent.insert(0, "송신자 비밀 번호")
        Recipient_id_ent.insert(0, "수신자 메일 아이디")
        mail_title.insert(0, "제목을 입력해주세요.")
