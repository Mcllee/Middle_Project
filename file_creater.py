from Window_set import *    # 기본 윈도우 파일
import Main_Page as mp      # 메인 페이지 파일
import Log_in_Page as lip   # 로그인 페이지 파일

import datetime             # 텍스트 현재시간 기록
import os                   # 파일 디렉토리 접근


def delete_fc(next_page):
    memo_txt.place_forget()
    save_btn.place_forget()
    open_btn.place_forget()

    match (next_page):  # 이동 횟수(깊이)에 따라 넘버링
        case 1:
            lip.set_log_in_page("")
        case 2:
            mp.Main_Page_set()


def save_txt():
    save_file = open("저장.txt", 'w')

    ctime = os.path.getctime(os.path.abspath(".\\저장.txt"))  # 생성 시간 획득
    cdate = datetime.datetime.fromtimestamp(ctime).strftime('%Y년 %m월 %d일\n%H시 %M분에 기록 되었습니다.\n\n')
    save_file.write(cdate)

    save_file.write(memo_txt.get("1.0", END))


def open_txt():
    save_file = open("저장.txt", 'r')

    memo_txt.delete("1.0", END)
    if os.path.getsize(".\\저장.txt") == 52:          # 기본 날짜만 저장 되었을 경우 크기 == 52
        memo_txt.insert(END, "저장.txt가 비어있습니다!")
    else:                                            # 파일에 저장된 내용이 있을 경우 memo에 출력한다.
        memo_txt.insert(END, save_file.read())


memo_txt = Text(win_root, width=115, height=40)
save_btn = Button(win_root, text="저장하기", command=save_txt)
open_btn = Button(win_root, text="열어보기", command=open_txt)


class file_creater:
    #  윈도우 위젯 선언

    @staticmethod
    def set_fc(input_name):
        mp.page_address.delete(0, END)
        mp.page_address.insert(0, f"파일 제작소에 어서오세요! {input_name}님!")

        mp.back_page_btn.config(command=lambda: [delete_fc(1)])  # 작동 오류: Log-in page의 back_page에서 변경하지 못함

        memo_txt.place(x=100, y=100)

        save_btn.place(x=100, y=70)
        open_btn.place(x=160, y=70)


