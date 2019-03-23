import RPi.GPIO as sb
import time
import serial
sb.setmode(sb.BOARD)
sb.setwarnings(False)
sb.setup(3,sb.OUT)
sb.setup(5,sb.OUT)
sb.setup(7,sb.IN)
rfid=7
m1=3
m2=5
a='Priyanshu'
b='Priyanshu'
c='aj1d35s'
global b

while(1):
    global data
    if(sb.input(rfid)==1):
        id=read_rfid()
        print("id")
        time.sleep(1)
        if(id==data):
            print("Welcome Screen")
            time.sleep(2)
            A=input("Enter Username- ")
            B=input("Enter Password- ")
            print(c)
            time.sleep(2)
            C=input("Enter Captcha- ")
            if(A==a):
                if(B==b):
                    if(C==c):
                        print("Login Sucecessful")
                        time.sleep(2)
                        sb.output(m1)==1
                        sb.output(m2)==0
                        time.sleep(2)
                        sb.output(m1)==0
                        sb.output(m2)==0
                        time.sleep(2)
                        sb.output(m1)==0
                        sb.output(m2)==1
                        time.sleep(2)
                        sb.output(m1)==0
                        sb.output(m2)==0
                        print("Authentic Entry")
                        time.sleep(2)
                        if(input("Z is pressed - Want to Change Password")=='Z'):
                            ChangePassword()
                    else:
                        print("Invalid Captcha")
                        time.sleep(2)
                else:
                    print("Invalid Password")
                    time.sleep(2)
            else:
                print("Invalid Username")
                time.sleep(2)
        else:
            print("Invalid Tag")
            time.sleep(2)
    else:
        print("No Tag Identified")
        time.sleep(2)

    def ChangePassword():
        global b
        B=input("Type Current Password- ")
        X=input("Type New Password- ")
        Y=input("Re-enter New Password- ")
        if(B==b):
            if(X==Y):
                b=X
                print("Password Changed Successfully")
                time.sleep(2)
            else:
                print("Password Does Not Match")
                time.sleep(2)
        else:
            print("Type Your Password Again")
            time.sleep(2)

    def read_rfid():
        global data
        ser=serial.Serial("/dev/ttyUSB0")
        ser.baudrate=9600
        data=ser.read(12)
        ser.close()
        return data
