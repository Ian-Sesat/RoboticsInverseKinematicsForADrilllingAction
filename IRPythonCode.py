from numpy import *
from time import *

a1=5.0    #link 1 length
a2=2.5    #link 2 length

#creating the home Position function that brings the robot arm to its home position
def homePos():
    global theta1
    global theta2
    theta1=90
    theta2=90
    print('Homing............')
    sleep(3)

# Making an inverse kinematics function that Calculates the angles theta1 and theta2
def inverseKine(x,y):
    theta2=arccos((x**2+y**2-a1**2-a2**2)/(2*a1*a2))                 #calculating the theta1 in radians
    theta1=arctan(y/x)+arctan((a2*sin(theta2))/(a1+a2*cos(theta2)))
    anglesArray=[]    #calculating the theta2 in radians 
    #Converting the radians theta1 and theta2 to degrees                                         
    theta1=rad2deg(theta1)
    theta2=rad2deg(theta2)
    anglesArray.append((theta1,theta2))
    return anglesArray
def drillingAnglesArray(xPos,yPos,theta1Desired, theta2Desired):
    xPosNew=xPos+drillDistance
    yPosNew=yPos
    endDrillPositionArray=inverseKine(xPosNew,yPosNew)
    theta1New=endDrillPositionArray[0][0]
    theta2New=endDrillPositionArray[0][1]
    print('Your drilling theta 1 value at end of the drilling process is therefore: ', theta1New)
    print('Your drilling theta 2 value at end of the drilling process is therefore: ', theta2New)
    theta1Delta=theta1New-theta1Desired
    theta2Delta=theta2New-theta2Desired
    theta1Divisions=theta1Delta/100
    theta2Divisions=theta2Delta/100
    myServoAngles=[]
    drillAngles=[]
    for i in linspace(1,100,100):
        theta1Desired=theta1Desired+theta1Divisions
        theta2Desired=theta2Desired+theta2Divisions
        drillAngles.append((theta1Desired,theta2Desired))
    #print('The 100 used drilling angles are:',drillAngles)
    retractionAngles=[]
    for i in linspace(100,1,100):
        theta1Desired=theta1Desired-theta1Divisions
        theta2Desired=theta2Desired-theta2Divisions
        retractionAngles.append((theta1Desired,theta2Desired))
    #print('The 100 used retraction angles are:',retractionAngles)
    myServoAngles.append((drillAngles,retractionAngles))
    myServoAngles=myServoAngles[0]
    return myServoAngles

homePos()

#finding our x, y values for the end effector before drilling by asking the user for the end effector values 
xPos=float(input('Boss, what is your desired x position? '))
yPos=float(input('And what is your desired y position? '))
print('Your x value is',xPos)
print('Your y value is',yPos)

#finding the x,y values of the desired position
desiredPositionArray=inverseKine(xPos,yPos)
theta1Desired=desiredPositionArray[0][0]
theta2Desired=desiredPositionArray[0][1]

print('Your theta 1 at position to start drill value is: ',theta1Desired)
print('Your theta 2 at position to start drill value is: ',theta2Desired)
#asking the user for the drilling length
drillDistance=float(input('Drilling distance required (maximum distance=3): '))
if drillDistance >3:
    print('ERROR!!!!!..... Drilling distance given more than the drilling distance limit')
myDrillingProcessAngles=drillingAnglesArray(xPos,yPos,theta1Desired, theta2Desired)
myDrillingAngles=myDrillingProcessAngles[0]
myRetractionAngles=myDrillingProcessAngles[1]
print()
print()
print('Drilling.............................')
i=0
for myDrillingAngle in myDrillingAngles:
    #print(myDrillingAngle)
    theta1=myDrillingAngle[0]
    print('My '+str(i)+'th theta1 is ',theta1)
    theta2=myDrillingAngle[1]
    print('My '+str(i)+'th theta2 is ',theta2)
    i=i+1
    if i==100:
        theta1=myDrillingAngle[0]
        print('Your END OF DRILL POSITION theta1 is ',theta1)
        theta2=myDrillingAngle[1]
        print('Your END OF DRILL POSITION theta2 is ',theta2)
sleep(3)       #assuming Drilling takes place at 3 seconds
print()
print()
print('Retracting..................................')
i=0
for myRetractionAngle in myRetractionAngles:
    #print(myRetractionAngle)
    theta1=myRetractionAngle[0]
    print('My '+str(i)+'th theta1 is ',theta1)
    theta2=myRetractionAngle[1]
    print('My '+str(i)+'th theta2 is ',theta2)
    i=i+1
    if i==100:
        theta1=myRetractionAngle[0]
        print('Your START OF DRILL POSITION theta1 is ',theta1)
        theta2=myRetractionAngle[1]
        print('Your START OF DRILL POSITION theta2 is ',theta2)
sleep(3)          #Assuming retraction after drilling takes place at 3 seconds
print() 
print()     
homePos()
print()
print('The End😉😉😉😉😉😉😉😉.............')


