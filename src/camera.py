


from pygame.locals import *
import pygame, math, numpy
import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *


class CameraController():
    def __init__(self):
        self.DEBUG = True

    def controls_3d(self,keys,mouse_button=1,w_key='w',s_key='s',a_key='a',\
                        d_key='d'):
        self.keys = keys
        self.speed = 0.5
        mouse_dx,mouse_dy = pygame.mouse.get_rel()
        if pygame.mouse.get_pressed()[mouse_button]:
            look_speed = .2
            buffer = glGetDoublev(GL_MODELVIEW_MATRIX)
            c = (-1 * numpy.mat(buffer[:3,:3]) * \
                numpy.mat(buffer[3,:3]).T).reshape(3,1)
            glTranslate(c[0],c[1],c[2])
            m = buffer.flatten()
            glRotate(mouse_dx * look_speed, m[1],m[5],m[9])
            glRotate(mouse_dy * look_speed, m[0],m[4],m[8])

            glRotated(-math.atan2(-m[4],m[5]) * \
                57.295779513082320876798154814105 ,m[2],m[6],m[10])
            glTranslate(-c[0],-c[1],-c[2])
        fwd = self.speed * (self.keys[w_key]-self.keys[s_key]) 
        strafe = self.speed * (self.keys[a_key]-self.keys[d_key])
        if abs(fwd) or abs(strafe):
            m = glGetDoublev(GL_MODELVIEW_MATRIX).flatten()
            glTranslate(fwd*m[2],fwd*m[6],fwd*m[10])
            glTranslate(strafe*m[0],strafe*m[4],strafe*m[8])


        keypress = pygame.key.get_pressed()

        if keypress[pygame.K_z]:
            self.DEBUG = True
            print("DEBUG MODE: ACTIVATED")

        if keypress[pygame.K_x]:
            self.DEBUG = False
            print("DEBUG MODE: DEACTIVTED")

        if keypress[pygame.K_w]:
            fwd = self.speed
        if keypress[pygame.K_s]:
            fwd = -self.speed
        if keypress[pygame.K_a]:
            strafe = self.speed
        if keypress[pygame.K_d]:
            strafe = -self.speed


            

        if abs(fwd) or abs(strafe):
            m = glGetDoublev(GL_MODELVIEW_MATRIX).flatten()
            glTranslate(fwd*m[2],fwd*m[6],fwd*m[10])
            glTranslate(strafe*m[0],strafe*m[4],strafe*m[8])

            



    
