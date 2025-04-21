import os, sys
from os import environ
from os.path import exists
import random, time, math
import pickle

import pygame
from pygame.locals import *

from objloader import OBJ
from camera import CameraController

import speech_recognition as sr
import pyttsx3

import threading

from responseAdapter import ResponseAdapter

from OpenGL.GL import *
from OpenGL.GLU import *



pygame.init()


class Animation():
    def __init__(self, animation_dir):
        self.frames = self.getAnimations(animation_dir)
        self.current_frame_index = 0
        self.current_frame = None
        self.isAnimating = False


    def getAnimations(self, location):
        frames = []
        for file in os.listdir(location):
            if file.endswith(".obj"):
                print(os.path.join(location, file))
                frames.append(OBJ(os.path.join(location, file)))
        return frames
    def play(self):
        self.isAnimating = True

    def update(self, speed=0.8):

        if self.isAnimating == True:

            self.current_frame_index += 0.8
            
            if self.current_frame_index >= len(self.frames):
                self.current_frame_index = 0
                self.isAnimating = False
            
            self.current_frame = self.frames[int(self.current_frame_index)]
            self.current_frame == self.frames[int(self.current_frame_index)].render()

                
        


class MM350():
    def __init__(self):
        self.scale = 10
        self.ears = sr.Recognizer()
        self.voice = pyttsx3.init()
        self.isTalking = False

        self.animations = []

        if exists("animations.pickle") and 1 == 2:
            with open('animations.pickle', 'rb') as handle:
                self.animations = pickle.load(handle)

                print(self.animations)
        else:

            self.animations = [
                Animation("3Dmodels//Avatar//animations//talk//"),
                Animation("3Dmodels//Avatar//animations//blink//")
                ]

            with open('animations.pickle', 'wb') as handle:
                pickle.dump(self.animations, handle, protocol=pickle.HIGHEST_PROTOCOL)

                

        self.idle_actions = [self.animations[1]]

        self.response_adapter = ResponseAdapter()
        self.response_adapter.loadCorpus("Corpus//")


    


    def play_idle_action(self):
        action_selection = random.randint(0, 200)
        if action_selection < len(self.idle_actions):
            self.idle_actions[action_selection].play()

        else:
            pass



    def update(self):
        glPushMatrix()
        glRotatef(0,1,0, 90)
        glScalef(self.scale, self.scale, self.scale)
        self.levitate()

        if any(x.isAnimating == True for x in self.animations):
            for animation in self.animations:
                if self.isTalking == True:
                    self.animations[0].update()
                    break
                else:
                    animation.update()

        else:
            self.animations[0].frames[0].render()
            

            
        glPopMatrix()

        self.play_idle_action()

    def levitate(self):
        glTranslatef(0,0.03*math.cos(0.5*pygame.time.get_ticks()*0.0025),0)



    def listen(self):

        print("Listening...")
        with sr.Microphone() as source:
            self.ears.adjust_for_ambient_noise(source)
            audio_text = self.ears.listen(source)
            try:
                text = self.ears.recognize_google(audio_text)
                return text
            except:
                return "FAILED"

    def say(self, text):
        self.voice.say(text)
        self.voice.runAndWait()


    def listen_and_respond(self):
        while True:
            text = self.listen()

            response = self.response_adapter.generateResponse(text)

            if response == "POOR_CONFIDENCE":
                self.isTalking = False #True
                self.say("Sorry, I don't understand. How should I respond to: " + text + " Next time?")
                self.isTalking = False
                while True:
                    new_response = self.listen()
                    if new_response != "FAILED":
                        break

                with open("Corpus//custom_conversations.txt", "a") as file:
                    file.write("* " + text + "\n")
                    file.write("- " + new_response + "\n")

                self.response_adapter.loadCorpus("Corpus//")
                self.isTalking = True
                self.say("OK. Registered: " + new_response)
                self.isTalking = False
            else:
                self.isTalking = True
                self.say(response)
            
            self.isTalking = False


    def talking(self):
        while True:
            if self.isTalking == True:
                self.animations[0].play()
                


    
















class Window():
    def __init__(self, dim=(500,500), title="MM350 (AlterEGO)", fov= 45):
        self.window = pygame.display.set_mode(dim, DOUBLEBUF | OPENGL | RESIZABLE)
        pygame.display.set_caption(title)
        self.width = dim[0]
        self.height = dim[1]
        self.fov = fov
        gluPerspective(self.fov, (dim[0]/dim[1]), 0.1, 100000)

        with open('code.txt', 'rb') as f:
            self.code = f.read()
        glTranslatef(0,0, -15)



        self.AlterEgo = MM350()




    def drawText(self, position, textString):     
        font = pygame.font.Font (None, 64)
        textSurface = font.render(textString, True, (255,255,255,255), (0,0,0,0))     
        textData = pygame.image.tostring(textSurface, "RGBA", True)     
        glRasterPos3d(0,0,0)     
        glDrawPixels(textSurface.get_width(), textSurface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, textData)


	

    def set_lights(self):
        light_ambient  = [0.5, 0.5, 0.5, 1.0]                                                       
        light_diffuse  = [0.9, 0.9, 0.9, 1.0]                                                       
        light_specular = [ 1.0, 1.0, 1.0, 1.0]
        light_position = [ 100.0, 100.0, -100.0, 1.0]

        mat_ambient    = [0.5, 0.5, 0.5, 1.0]
        mat_diffuse    = [0.8, 0.8, 0.8, 1.0]
        mat_specular   = [1.0, 1.0, 1.0, 1.0]
        high_shininess = [100.0]

        glEnable(GL_LIGHT0)
        glEnable(GL_NORMALIZE)
        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glShadeModel(GL_SMOOTH)

        glLightfv(GL_LIGHT0, GL_AMBIENT,  light_ambient)
        glLightfv(GL_LIGHT0, GL_DIFFUSE,  light_diffuse)
        glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
        glLightfv(GL_LIGHT0, GL_POSITION, light_position)

        glMaterialfv(GL_FRONT, GL_AMBIENT,   mat_ambient)
        glMaterialfv(GL_FRONT, GL_DIFFUSE,   mat_diffuse)
        glMaterialfv(GL_FRONT, GL_SPECULAR,  mat_specular)
        glMaterialfv(GL_FRONT, GL_SHININESS, high_shininess)

        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)

        glClearColor(0, 0, 0, 1)
    



    def run(self):

        self.set_lights()

        speech_thread = threading.Thread(target=self.AlterEgo.listen_and_respond).start()
        talking_animation_thread = threading.Thread(target = self.AlterEgo.talking).start()
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()



                if event.type == pygame.KEYDOWN:  

                    if event.key == pygame.K_x:
                        self.AlterEgo.animations[0].play()

                    if event.key == pygame.K_z:
                        self.AlterEgo.animations[1].play()
                        

                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()


                        
                        




            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            self.AlterEgo.update()
            #self.drawText((1,0,0),self.code)

            #glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
            glEnable(GL_TEXTURE_2D)
            pygame.display.flip()
            pygame.time.wait(10)





Window(dim=(1500,800), fov=20).run()














