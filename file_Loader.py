from tkinter import *
from PIL import ImageTk, Image

# Main페이지와 로그인 페이지의 배경 이미지 저장
mbg_image = Image.open(r"Image\\i_Krome_title.png")
mbg_image = mbg_image.resize((700, 350))

# 회원가입 페이지의 배경 저장
Sign_Up_Image = Image.open(r"Image\\회원가입.png")
# Sign_Up_Image = Sign_Up_Image.resize((300, 660))
