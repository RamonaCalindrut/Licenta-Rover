import socket
from threading import *
import wiringpi
OUTPUT = 1

M1_PWM1 = 4
M1_PWM2 = 3

M2_PWM1 = 5
M2_PWM2 = 6

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.43.237"
port = 3000
print (host)
print (port)
serversocket.bind((host, port))


def initPins():

    wiringpi.wiringPiSetup()
    wiringpi.pinMode(M1_PWM1,OUTPUT)
    wiringpi.pinMode(M1_PWM2,OUTPUT)
    wiringpi.pinMode(M2_PWM1,OUTPUT)
    wiringpi.pinMode(M2_PWM2,OUTPUT)


    wiringpi.softPwmCreate(M1_PWM1,0,100) # Setup PWM using Pin, Initial Value and Range parameters
    wiringpi.softPwmCreate(M1_PWM2,0,100)
    wiringpi.softPwmCreate(M2_PWM1,0,100)
    wiringpi.softPwmCreate(M2_PWM2,0,100)

def go(leftSpeed, rightSpeed):
    if leftSpeed>0:
        wiringpi.softPwmWrite(M1_PWM1,leftSpeed) # Change PWM duty cycle
        wiringpi.softPwmWrite(M1_PWM2,0)
    else:
        wiringpi.softPwmWrite(M1_PWM1,0) # Change PWM duty cycle
        wiringpi.softPwmWrite(M1_PWM2,-leftSpeed)
        
        
    if rightSpeed>0:
        wiringpi.softPwmWrite(M2_PWM1,rightSpeed) # Change PWM duty cycle
        wiringpi.softPwmWrite(M2_PWM2,0)
    else:
        wiringpi.softPwmWrite(M2_PWM1,0) # Change PWM duty cycle
        wiringpi.softPwmWrite(M2_PWM2,-rightSpeed)
        
class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while 1:
            direction = ''
            direction = self.sock.recv(1024).decode()
            #print('Client sent:', direction)
            self.sock.send(b'Oi you sent something to me')
            
            if 'FORWARD' in direction:
                print('Rover is moving FORWARD')
                go(80,80)
            if 'BACK' in direction:
                print('Rover is moving BACK')
                go(-80,-80)
            if 'LEFT' in direction:
                print('Rover is moving LEFT')
                go(-80,80)
            if 'RIGHT' in direction:
                print('Rover is moving RIGHT')
                go(80,-80)
            if 'STOP' in direction:
                print('STOP')
                #reset to 0
                wiringpi.softPwmWrite(M1_PWM1,0) # Change PWM duty cycle
                wiringpi.softPwmWrite(M1_PWM2,0)
                wiringpi.softPwmWrite(M2_PWM1,0)
                wiringpi.softPwmWrite(M2_PWM2,0)

initPins()
serversocket.listen(5)
print ('server started and listening')
while 1:
    clientsocket, address = serversocket.accept()
    client(clientsocket, address)