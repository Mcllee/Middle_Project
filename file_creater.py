from OpenGL.GL import *         # OpenGL 파일
from OpenGL.GLU import *        # ''
from Object import *            # 오브젝트 내용
from pygame.locals import *     # 파이게임 파일

import random
import pygame
import os

from Window_set import *    # 기본 윈도우 파일
import Main_Page as mp      # 메인 페이지 파일
import Log_in_Page as lip   # 로그인 페이지 파일

def CubeMesh():
    glBegin(GL_QUADS)
    for face in cube_faces_vector4:
        x = 0
        for vertex in face:
            x+=1
            glColor3fv(colors[x])
            glVertex3fv(cube_verticies_vector3[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in cube_edges_vector2:
        for vertex in edge:
            glVertex3fv(cube_verticies_vector3[vertex])
    glEnd()


def ChairMesh():
    glBegin(GL_QUADS)
    for face in chair_faces_vector4:
        x = 0
        for vertex in face:
            x+=1
            glColor3fv(colors[x])
            glVertex3fv(chair_verticies_vector3[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in chair_edges_vector2:
        for vertex in edge:
            glVertex3fv(chair_verticies_vector3[vertex])
    glEnd()


def random_color():
    x = random.randint(0, 255) / 255
    y = random.randint(0, 255) / 255
    z = random.randint(0, 255) / 255
    color = (x, y, z)
    return color

colors_list= []

for n in range(len(chair_faces_vector4)):
    colors_list.append(random_color())


def main():
    pygame.init()
    display = (1000, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    # 투영 변환

    glTranslatef(0.0, 0.0, -20)
    # 평행 이동

    glRotatef(-90, 2, 0, 0)
    # 회전


def delete_fc(next_page):
    pass  # place_forget

    match (next_page):  # 이동 횟수(깊이)에 따라 넘버링
        case 1:
            lip.set_log_in_page(lip.save_name)
        case 2:
            mp.Main_Page_set()


class file_creater:
    #  윈도우 위젯 선언

    @staticmethod
    def set_fc(input_name):
        mp.page_address.delete(0, END)
        mp.page_address.insert(0, f"파일 제작소에 어서오세요! {input_name}님!")

        mp.back_page_btn.config(command=lambda: [delete_fc(1)])

        main()

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # 프로그램 종료 조건
                    run = False
            glRotatef(4, 3, -10, -45)
            # (4, 3, -10) 벡터로 -45도씩 회전

            # 모델 다시 그리기
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            ChairMesh()
            pygame.display.flip()
            pygame.time.wait(2)

        pygame.quit()
