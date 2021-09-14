from vpython import *
canvas(width=1500, height=720, center=vector(00,70,0), background=color.white, range=150)
sphere( pos=vector(0,0,0), radius=2, color=color.red)                 # Origin of the orthonormal coordinate system

for i in range(-150,150,10):                                          # Drawing floor
    for j in range(-150,150,10):                                      #
        sphere( pos=vector(i,0,j), radius=0.3, color=color.black)     #

H =curve()    # Diamond diagonal 
CL=curve()    # Diamond left top side
CR=curve()    # Diamond right top side
AL=curve()    # Diamond left bottom side
AR=curve()    # Diamond right bottom side

def IK(x,y,z):

    global H
    global CL
    global CR
    global AL
    global AR

    H.clear()
    CL.clear()
    CR.clear()
    AL.clear()
    AR.clear()

    d=Ay-y                   # X Y diagonal calculations
    e=x                      #
    h=sqrt((e*e)+(d*d))      #
    E=acos(d/h)              #
    if(e<0):                 #
        E=(-E)               #
    X=sin(E)*h               #
    Y=cos(E)*h               #

    G=acos(h/(2*c))          # diamond sides calculations
    Clx=sin(E-G)*c           #
    Cly=cos(E-G)*c           #
    Crx=sin(E+G)*c           #
    Cry=cos(E+G)*c           #
        
    dz=h                     # Z diagonal calculations
    ez=z                     #
    hz=sqrt((ez*ez)+(dz*dz)) #
    D=acos(dz/hz)            #
    if(ez<0):                #
        D=(-D)               #
    Z=sin(D)*hz              #
        
    H =curve( A.pos, vector(X,Ay-Y,Z), radius=0.1, color=color.magenta, retain=30 )        # diagonal line
    CL=curve( A.pos, vector(Clx,Ay-Cly,Z/2), radius=2, color=color.yellow )                # top left side line of the diamond
    CR=curve( A.pos, vector(Crx,Ay-Cry,Z/2), radius=2, color=color.green )                 # top right side line of the diamond
    AL=curve( vector(X,Ay-Y,Z), vector(Clx,Ay-Cly,Z/2), radius=2, color=color.yellow )     # bottom left side line of the diamond
    AR=curve( vector(X,Ay-Y,Z), vector(Crx,Ay-Cry,Z/2), radius=2, color=color.green )      # bottom right side line of the diamond

################ Start Zigzag ################
c=112                  # length of diamond side 
Ay=200                 # coordinates of the main axis
Ax=0                   #
Az=0                   #
A=sphere( pos=vector(Ax,Ay,0), radius=4, color=color.red)     # main paw axis

Pz=[-70,-70,-70,-70,-70,-70,-70,-70,-70,-70,-70,-70,-70,-70,-70,-60,-50,-40,-30,-20,-10,  0, 10, 20, 30, 40, 50, 60, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70]
Py=[ 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
Px=[-70,-60,-50,-40,-30,-20,-10,  0, 10, 20, 30, 40, 50, 60, 70, 60, 50, 40, 30, 20, 10,  0,-10,-20,-30,-40,-50,-60,-70,-60,-50,-40,-30,-20,-10,  0, 10, 20, 30, 40, 50, 60, 70]

for i in range(0, 43,1):
    rate(20)
    sphere( pos=vector(Px[i],Py[i],Pz[i]), radius=1.5, color=color.red)        # Path drawing with ball targets

while True:
    for i in range(0, 43, 1):
        rate(20)
        IK(Px[i],Py[i],Pz[i])
    for i in range(42,-1, -1):
        rate(20)
        IK(Px[i],Py[i],Pz[i])
################ End Zigzag ################
