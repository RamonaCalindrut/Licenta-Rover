# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 13:12:47 2018

@author: uidq9144
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot

import numpy as np
from PIL import ImageGrab
import cv2
import time
import socket
import os
 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'Licenta Rover '
        self.left = 10
        self.top = 10
        self.width = 564
        self.height = 564
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        # Create widget
        label = QLabel(self)
        pixmap = QPixmap('image2.jpg')
        label.setPixmap(pixmap)
        #self.resize(pixmap.width(),pixmap.height())
            
        #Create Button
        button = QPushButton('Start Stream', self)
        button.setToolTip('This is an example button')
        button.move(150,500) 
        button.clicked.connect(self.on_click_button_stream)
        
        button2 = QPushButton('Autonomous Mode', self)
        button2.setToolTip('This is an example button')
        button2.move(10,500) 
        button2.clicked.connect(self.on_click_button2)
        
        button_up = QPushButton('UP', self)
        button_up.setToolTip('This is an example button')
        button_up.move(90,400) 
        button_up.clicked.connect(self.on_click_button2)
        
        button_down = QPushButton('DOWN', self)
        button_down.setToolTip('This is an example button')
        button_down.move(90,450) 
        button_down.clicked.connect(self.on_click_button2)
        
        button_left= QPushButton('LEFT', self)
        button_left.setToolTip('This is an example button')
        button_left.move(10,450) 
        button_left.clicked.connect(self.on_click_button2)
        
        button_right = QPushButton('RIGHT', self)
        button_right.setToolTip('This is an example button')
        button_right.move(170,450) 
        button_right.clicked.connect(self.on_click_button2)
 
        self.show()
 
    @pyqtSlot()
    
    def on_click_button(self):
        print('Start Stream')
        last_time = time.time()
        while(True):
            # 800x600 windowed mode
            printscreen =  np.array(ImageGrab.grab(bbox=(0,40,320,240)))
            print('loop took {} seconds'.format(time.time()-last_time))
            last_time = time.time()
            cv2.imshow('window',cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
        #split_sheets()
        #add_error()
            
    def on_click_button_stream(self):
        print('Start Stream')
        self.server_socket = socket.socket()
        self.server_socket.bind(('192.168.43.20', 4000))
        self.server_socket.listen(0)

        # accept a single connection
        self.connection = self.server_socket.accept()[0].makefile('rb')
        self.send_inst = True
        #self.collect_image()
        
        # collect images for training
        print ('Start streaming images...')
        #e1 = cv2.getTickCount()
        # stream video frames one by one
        try:
            
            stream_bytes = b''
            #frame = 1
            while self.send_inst:
                stream_bytes += self.connection.read(1024)
                first = stream_bytes.find(b'\xff\xd8')
                last = stream_bytes.find(b'\xff\xd9')
                if first != -1 and last != -1:
                    jpg = stream_bytes[first:last + 2]
                    stream_bytes = stream_bytes[last + 2:]
                    image = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.IMREAD_GRAYSCALE)
                    cv2.imshow('image', image)
                    if cv2.waitKey(25) & 0xFF == ord('q'):
                        cv2.destroyAllWindows()
                        break
            print("Finished")
            
        finally:
            self.connection.close()
            self.server_socket.close()

    def on_click_button2(self):
        print('Autonomous Mode')
       # CRC_Calc()
    
    def getText(self):
        text, okPressed = QInputDialog.getText(self, "Get text","Your name:", QLineEdit.Normal, "")
        if okPressed and text != '':
            print(text)
            
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
 