# Pulsates an LED connected to GPIO pin 1 with a suitable resistor 4 times using softPwm
# softPwm uses a fixed frequency
import wiringpi
OUTPUT = 1

M1_PWM1 = 4
M1_PWM2 = 3

M2_PWM1 = 5
M2_PWM2 = 6

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
'''
for time in range(0,4):
	for brightness in range(0,100): # Going from 0 to 100 will give us full off to full on
		wiringpi.softPwmWrite(M1_PWM1,brightness) # Change PWM duty cycle
		wiringpi.softPwmWrite(M1_PWM2,brightness)
		wiringpi.softPwmWrite(M2_PWM1,brightness)
		wiringpi.softPwmWrite(M2_PWM2,brightness)
		
		wiringpi.delay(10) # Delay for 0.2 seconds
	for brightness in reversed(range(0,100)):
		wiringpi.softPwmWrite(M1_PWM1,brightness)
		wiringpi.softPwmWrite(M1_PWM2,brightness)
		wiringpi.softPwmWrite(M2_PWM1,brightness)
		wiringpi.softPwmWrite(M2_PWM2,brightness)
		
		wiringpi.delay(10)
'''

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
        
def main():
    initPins()
    go(70,70)
    wiringpi.delay(5000)
    go(-70,-70)
    wiringpi.delay(5000)
    go(70,-70)
    wiringpi.delay(5000)
    go(-70,70)
    wiringpi.delay(5000)
    
    #reset to 0
    wiringpi.softPwmWrite(M1_PWM1,0) # Change PWM duty cycle
    wiringpi.softPwmWrite(M1_PWM2,0)
    wiringpi.softPwmWrite(M2_PWM1,0)
    wiringpi.softPwmWrite(M2_PWM2,0)
    
main()