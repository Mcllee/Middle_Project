import os
import pygame
from OpenGL.GL import *
from Window_set import *

import Main_Page as mp
import Log_in_Page as lip

import smtplib
from email.mime.text import MIMEText  # 메일 제목과 내용을 설정하는 모듈


def delete_mc(next_page):
    sender_id_ent.place_forget()
    sender_pw_ent.place_forget()
    Recipient_id_ent.place_forget()
    mail_title.place_forget()

    send_message_btn.place_forget()
    message_text.place_forget()

    match (next_page):  # 이동 횟수(깊이)에 따라 넘버링
        case 1:
            lip.set_log_in_page(lip.save_name)
        case 2:
            mp.Main_Page_set()


def send_message():
    sender_id = sender_id_ent.get()
    sender_pw = sender_pw_ent.get()

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


message_text = Text(win_root, width=115, height=40)
send_message_btn = Button(win_root, text="메일 보내기", command=send_message)

sender_id_ent = Entry(win_root, width=30)
sender_id_ent.insert(0, "송신자 메일 아이디")

sender_pw_ent = Entry(win_root, width=30)
sender_pw_ent.insert(0, "송신자 비밀 번호")

Recipient_id_ent = Entry(win_root, width=30)
Recipient_id_ent.insert(0, "수신자 메일 아이디")

mail_title = Entry(win_root, width=30)
mail_title.insert(0, "제목을 입력해주세요.")


class mail_creater:
    #  윈도우 위젯 선언

    @staticmethod
    def set_mc(input_name):
        mp.page_address.delete(0, END)
        mp.page_address.insert(0, f"메일 시스템에 어서오세요! {input_name}님!")

        mp.back_page_btn.config(command=lambda: [delete_mc(1)])
        mp.forward_page_btn.config(command=DISABLED)

        sender_id_ent.place(x=100, y=40)
        sender_pw_ent.place(x=100, y=80)
        Recipient_id_ent.place(x=400, y=40)
        mail_title.place(x=400, y=80)

        message_text.place(x=100, y=100)
        send_message_btn.place(x=800, y=60)
