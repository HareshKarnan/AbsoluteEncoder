import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

PIN_CLK = 2
PIN_DAT = 3
PIN_CS  = 4
delay = 0.0000005
# totally 10 bits to be extracted from SSI signal
bitcount = 16

# pin setup done here
try:
    GPIO.setup(PIN_CLK,GPIO.OUT)
    GPIO.setup(PIN_DAT,GPIO.IN)
    GPIO.setup(PIN_CS,GPIO.OUT)
    GPIO.output(PIN_CS,1)
    GPIO.output(PIN_CLK,1)
except:
    print "ERROR. Unable to setup the configuration requested"

#wait some time to start
time.sleep(0.5)

print "GPIO configuration enabled"

def clockup():
    GPIO.output(PIN_CLK,1)
def clockdown():
    GPIO.output(PIN_CLK,0)
def MSB():
    # Most Significant Bit
    clockdown()
    clockup()

def readpos():
    GPIO.output(PIN_CS,0)
    time.sleep(delay)
    #MSB()
    data = 0
    for i in range(0,bitcount):
        if i<10:
            #print i
            data<<=1
            clockdown()
            clockup()
            data|=GPIO.input(PIN_DAT)
        else:
            for k in range(0,6):
                clockdown()
                clockup()
    GPIO.output(PIN_CS,1)
    return data 

try:
    while(1):
        print readpos()
        #break
        
finally:
    print "cleaning up GPIO"
    GPIO.cleanup()
