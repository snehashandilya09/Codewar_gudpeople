import random
import math
from random import randint 

name = "Gud_People"

def moveTo(x, y, Pirate):
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return 0
    if position[0] == x:
        return (position[1] < y) * 2 + 1
    if position[1] == y:
        return (position[0] > x) * 2 + 2
    if random.randint(1, 2) == 1:
        return (position[0] > x) * 2 + 2
    else:
        return (position[1] < y) * 2 + 1
    
def movement_1(pirate, pirate_id, mapX, mapY):
    if (pirate_id%12==0):
        return moveTo(randint(0, math.floor(mapX/7)), randint(0, math.floor(mapY/7)), pirate)
    elif (pirate_id%12==1):
        return moveTo(randint(6*math.floor(mapX/7), mapX), randint(0, math.floor(mapY/7)), pirate)
    elif (pirate_id%12==2):
        return moveTo(randint(0, math.floor(mapX/7)), randint(6*math.floor(mapY/7), mapY), pirate)
    elif (pirate_id%12==3):
        return moveTo(randint(6*math.floor(mapX/7), mapX), randint(6*math.floor(mapY/7), mapY), pirate)
    elif (pirate_id%12==4):
        return moveTo(randint(2*math.floor(mapX/7), math.floor(mapX/2)), randint(0, math.floor(mapY/7)), pirate)
    elif (pirate_id%12==5):
        return moveTo(randint(math.floor(mapX/2), 5*math.floor(mapX/7)), randint(0, math.floor(mapY/7)), pirate)
    elif (pirate_id%12==6):
        return moveTo(randint(0, math.floor(mapX/7)), randint(2*math.floor(mapY/7), math.floor(mapY/2)), pirate)
    elif (pirate_id%12==7):
        return moveTo(randint(0, math.floor(mapX/7)), randint(math.floor(mapY/2), 5*math.floor(mapY/7)), pirate)
    elif (pirate_id%12==8):
        return moveTo(randint(2*math.floor(mapX/7), math.floor(mapX/2)), randint(6*math.floor(mapY/7), mapY), pirate)
    elif (pirate_id%12==9):
        return moveTo(randint(math.floor(mapX/2), 5*math.floor(mapX/7)), randint(6*math.floor(mapY/7), mapY), pirate)
    elif (pirate_id%12==10):
        return moveTo(randint(6*math.floor(mapX/7), mapX), randint(2*math.floor(mapY/7), math.floor(mapY/2)), pirate)
    elif (pirate_id%12==11):
        return moveTo(randint(6*math.floor(mapX/7), mapX), randint(math.floor(mapY/2), 5*math.floor(mapY/7)), pirate)
    
def movement_2(pirate, pirate_id, mapX, mapY):
    if (pirate_id%12==0):
        return moveTo(randint(0, math.floor(mapX/7)), randint(6*math.floor(mapY/7), mapY), pirate)
    elif (pirate_id%12==1):
        return moveTo(randint(0, math.floor(mapX/7)), randint(0, math.floor(mapY/7)), pirate)
    elif (pirate_id%12==2):
        return moveTo(randint(6*math.floor(mapX/7), mapX), randint(6*math.floor(mapY/7), mapY), pirate)
    elif (pirate_id%12==3):
        return moveTo(randint(6*math.floor(mapX/7), mapX), randint(0, math.floor(mapY/7)), pirate)
    elif (pirate_id%12==4):
        return moveTo(randint(2*math.floor(mapX/7), math.floor(mapX/2)), randint(6*math.floor(mapY/7), mapY), pirate)
    elif (pirate_id%12==5):
        return moveTo(randint(math.floor(mapX/2), 5*math.floor(mapX/7)), randint(6*math.floor(mapY/7), mapY), pirate)
    elif (pirate_id%12==6):
        return moveTo(randint(6*math.floor(mapX/7), mapX), randint(2*math.floor(mapY/7), math.floor(mapY/2)), pirate)
    elif (pirate_id%12==7):
        return moveTo(randint(6*math.floor(mapX/7), mapX), randint(math.floor(mapY/2), 5*math.floor(mapY/7)), pirate)
    elif (pirate_id%12==8):
        return moveTo(randint(2*math.floor(mapX/7), math.floor(mapX/2)), randint(0, math.floor(mapY/7)), pirate)
    elif (pirate_id%12==9):
        return moveTo(randint(math.floor(mapX/2), 5*math.floor(mapX/7)), randint(0, math.floor(mapY/7)), pirate)
    elif (pirate_id%12==10):
        return moveTo(randint(0, math.floor(mapX/7)), randint(2*math.floor(mapY/7), math.floor(mapY/2)), pirate)
    elif (pirate_id%12==11):
        return moveTo(randint(0, math.floor(mapX/7)), randint(math.floor(mapY/2), 5*math.floor(mapY/7)), pirate)
    
def movement_3(pirate, pirate_id, mapX, mapY):
    if (pirate_id%12==0):
        return moveTo(randint(6*math.floor(mapX/7), mapX), randint(0, math.floor(mapY/7)), pirate)
    elif (pirate_id%12==1):
        return moveTo(randint(6*math.floor(mapX/7), mapX), randint(6*math.floor(mapY/7), mapY), pirate)
    elif (pirate_id%12==2):
        return moveTo(randint(0, math.floor(mapX/7)), randint(0, math.floor(mapY/7)), pirate)
    elif (pirate_id%12==3):
        return moveTo(randint(0, math.floor(mapX/7)), randint(6*math.floor(mapY/7), mapY), pirate)
    elif (pirate_id%12==4):
        return moveTo(randint(2*math.floor(mapX/7), math.floor(mapX/2)), randint(0, math.floor(mapY/7)), pirate)
    elif (pirate_id%12==5):
        return moveTo(randint(math.floor(mapX/2), 5*math.floor(mapX/7)), randint(0, math.floor(mapY/7)), pirate)
    elif (pirate_id%12==6):
        return moveTo(randint(0, math.floor(mapX/7)), randint(2*math.floor(mapY/7), math.floor(mapY/2)), pirate)
    elif (pirate_id%12==7):
        return moveTo(randint(0, math.floor(mapX/7)), randint(math.floor(mapY/2), 5*math.floor(mapY/7)), pirate)
    elif (pirate_id%12==8):
        return moveTo(randint(2*math.floor(mapX/7), math.floor(mapX/2)), randint(6*math.floor(mapY/7), mapY), pirate)
    elif (pirate_id%12==9):
        return moveTo(randint(math.floor(mapX/2), 5*math.floor(mapX/7)), randint(6*math.floor(mapY/7), mapY), pirate)
    elif (pirate_id%12==10):
        return moveTo(randint(6*math.floor(mapX/7), mapX), randint(2*math.floor(mapY/7), math.floor(mapY/2)), pirate)
    elif (pirate_id%12==11):
        return moveTo(randint(6*math.floor(mapX/7), mapX), randint(math.floor(mapY/2), 5*math.floor(mapY/7)), pirate)
    
def attack_island(pirate):
    if pirate.getTeamSignal() != "":
            s = pirate.getTeamSignal()
            l = s.split(",")
            x = int(l[0][1:])
            y = int(l[1])

            position = pirate.getPosition()

            if (pirate.investigate_up()[0][:-1] == "island" and pirate.investigate_down()[0][:-1] == "island" and pirate.investigate_left()[0][:-1] == "island" and pirate.investigate_right()[0][:-1] == "island"):

                x = position[0]
                y = position[1]

                if (pirate.investigate_nw()[0][:-1] == "island" and pirate.investigate_nw()[1] == "enemy"):
                    return moveTo(x-1, y-1, pirate)
                if (pirate.investigate_ne()[0][:-1] == "island" and pirate.investigate_ne()[1] == "enemy"):
                    return moveTo(x+1, y-1, pirate)
                if (pirate.investigate_sw()[0][:-1] == "island" and pirate.investigate_sw()[1] == "enemy"):
                    return moveTo(x-1, y+1, pirate)
                if (pirate.investigate_se()[0][:-1] == "island" and pirate.investigate_se()[1] == "enemy"):
                    return moveTo(x+1, y+1, pirate)
                if (pirate.investigate_up()[0][:-1] == "island" and pirate.investigate_up()[1] == "enemy"):
                    return moveTo(x, y-1, pirate)
                if (pirate.investigate_down()[0][:-1] == "island" and pirate.investigate_down()[1] == "enemy"):
                    return moveTo(x, y+1, pirate)
                if (pirate.investigate_left()[0][:-1] == "island" and pirate.investigate_left()[1] == "enemy"):
                    return moveTo(x-1, y, pirate)
                if (pirate.investigate_right()[0][:-1] == "island" and pirate.investigate_right()[1] == "enemy"):
                    return moveTo(x+1, y, pirate)

            else:
                return moveTo(x, y, pirate)
            
    else:
        return 0
    
    


def ActPirate(pirate):


    pirate_id = int(pirate.getID())

    mapX = int(pirate.getDimensionX())
    mapY = int(pirate.getDimensionY())


    up = pirate.investigate_up()[0]
    down = pirate.investigate_down()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]
    nw = pirate.investigate_nw()[0]
    ne = pirate.investigate_ne()[0]
    sw = pirate.investigate_sw()[0]
    se = pirate.investigate_se()[0]

    x, y = pirate.getPosition()
    pirate.setSignal("")
    s = pirate.trackPlayers()


    if (
        (up == "island1" and s[0] != "myCaptured")
        or (up == "island2" and s[1] != "myCaptured")
        or (up == "island3" and s[2] != "myCaptured")
    ):
        
        if (nw[:-1] == "island" and ne[:-1] != "island"):
            s = up[-1] + str(x-1) + "," + str(y - 2)

        if (nw[:-1] == "island" and ne[:-1] == "island"):
            s = up[-1] + str(x) + "," + str(y - 2)

        if (nw[:-1] != "island" and ne[:-1] == "island"):
            s = up[-1] + str(x+1) + "," + str(y - 2)

        pirate.setTeamSignal(s)

    elif (
        (down == "island1" and s[0] != "myCaptured")
        or (down == "island2" and s[1] != "myCaptured")
        or (down == "island3" and s[2] != "myCaptured")
    ):
        if (sw[:-1] == "island" and se[:-1] != "island"):
            s = down[-1] + str(x-1) + "," + str(y + 2)

        if (sw[:-1] == "island" and se[:-1] == "island"):
            s = down[-1] + str(x) + "," + str(y + 2)

        if (sw[:-1] != "island" and se[:-1] == "island"):
            s = down[-1] + str(x+1) + "," + str(y + 2)

        pirate.setTeamSignal(s)

    elif (
        (left == "island1" and s[0] != "myCaptured")
        or (left == "island2" and s[1] != "myCaptured")
        or (left == "island3" and s[2] != "myCaptured")
    ):
        if (nw[:-1] == "island" and sw[:-1] != "island"):
            s = left[-1] + str(x-2) + "," + str(y - 1)

        if (nw[:-1] == "island" and sw[:-1] == "island"):
            s = left[-1] + str(x-2) + "," + str(y)

        if (nw[:-1] != "island" and sw[:-1] == "island"):
            s = left[-1] + str(x-2) + "," + str(y + 1)

        pirate.setTeamSignal(s)

    elif (
        (right == "island1" and s[0] != "myCaptured")
        or (right == "island2" and s[1] != "myCaptured")
        or (right == "island3" and s[2] != "myCaptured")
    ):
        if (ne[:-1] == "island" and se[:-1] != "island"):
            s = right[-1] + str(x+2) + "," + str(y - 1)

        if (ne[:-1] == "island" and se[:-1] == "island"):
            s = right[-1] + str(x+2) + "," + str(y)

        if (ne[:-1] != "island" and se[:-1] == "island"):
            s = right[-1] + str(x+2) + "," + str(y + 1)

        pirate.setTeamSignal(s)

    elif (
        (nw == "island1" and s[0] != "myCaptured")
        or (nw == "island2" and s[1] != "myCaptured")
        or (nw == "island3" and s[2] != "myCaptured")
    ):
        s = nw[-1] + str(x - 2) + "," + str(y - 2)

        pirate.setTeamSignal(s)

    elif (
        (ne == "island1" and s[0] != "myCaptured")
        or (ne == "island2" and s[1] != "myCaptured")
        or (ne == "island3" and s[2] != "myCaptured")
    ):
        s = ne[-1] + str(x + 2) + "," + str(y - 2)

        pirate.setTeamSignal(s)

    elif (
        (sw == "island1" and s[0] != "myCaptured")
        or (sw == "island2" and s[1] != "myCaptured")
        or (sw == "island3" and s[2] != "myCaptured")
    ):
        s = sw[-1] + str(x - 2) + "," + str(y + 2)


    elif (
        (se == "island1" and s[0] != "myCaptured")
        or (se == "island2" and s[1] != "myCaptured")
        or (se == "island3" and s[2] != "myCaptured")
    ):
        s = se[-1] + str(x + 2) + "," + str(y + 2)

        pirate.setTeamSignal(s)



    time = int(pirate.getCurrentFrame())

    if (time <= 115):
        return movement_1(pirate, pirate_id, mapX, mapY)
        

    if (time >115 and time <=162):
        return movement_2(pirate, pirate_id, mapX, mapY)

        
    elif (time > 162 and time<=260):
        if (attack_island(pirate) != 0):
            return attack_island(pirate)
        return movement_3(pirate, pirate_id, mapX, mapY)
        


    elif (time > 260 and time<=360):
        if (attack_island(pirate) != 0):
            return attack_island(pirate)   
        return movement_1(pirate, pirate_id, mapX, mapY)
            

        
        
    
    elif (time > 360 and time<=420):
        if (attack_island(pirate) != 0):
            return attack_island(pirate) 
        return movement_2(pirate, pirate_id, mapX, mapY)
            

        
        

    elif(time > 420 and time <= 460):
        # if (attack_island(pirate) != 0):
        #     return attack_island(pirate)
        return movement_3(pirate, pirate_id, mapX, mapY)
            
        
        
    elif (time > 460 and time <= 495):

        # if (attack_island(pirate) != 0):
        #     return attack_island(pirate)
        return movement_1(pirate, pirate_id, mapX, mapY)
        


    elif (time > 495 and time<=605):
        if (attack_island(pirate) != 0):
            return attack_island(pirate)
        return movement_2(pirate, pirate_id, mapX, mapY)
        

    elif (time > 605 and time<=745):
        if (attack_island(pirate) != 0):
            return attack_island(pirate)
        return movement_3(pirate, pirate_id, mapX, mapY)
        

    elif (time >745 and time <= 790):

        # if (attack_island(pirate) != 0):
        #     return attack_island(pirate)
        return movement_1(pirate, pirate_id, mapX, mapY)
        

    elif (time > 790 and time<=820):
        #if (attack_island(pirate) != 0):
         #   return attack_island(pirate)  
        return movement_2(pirate, pirate_id, mapX, mapY)
        

    elif (time > 820 and time<=960):
        if (attack_island(pirate) != 0):
            return attack_island(pirate)
        return movement_3(pirate, pirate_id, mapX, mapY)
        
    elif (time > 960 and time<=1070):
        if (attack_island(pirate) != 0):
            return attack_island(pirate)  
        return movement_1(pirate, pirate_id, mapX, mapY)
    
    elif (time > 1070 and time<=1115):
        #if (attack_island(pirate) != 0):
            #return attack_island(pirate)
        return movement_2(pirate, pirate_id, mapX, mapY)
            
    elif(time > 1115 and time <= 1145):
        #if (attack_island(pirate) != 0):
           # return attack_island(pirate)
        return movement_3(pirate, pirate_id, mapX, mapY)

    elif (time > 1145 and time<=1255):
        if (attack_island(pirate) != 0):
            return attack_island(pirate) 
        return movement_1(pirate, pirate_id, mapX, mapY)
    
    elif (time > 1255 and time<=1395):
        if (attack_island(pirate) != 0):
            return attack_island(pirate) 
        return movement_2(pirate, pirate_id, mapX, mapY)

    elif(time > 1395 and time <= 1440):
        #if (attack_island(pirate) != 0):
            #return attack_island(pirate)
        return movement_3(pirate, pirate_id, mapX, mapY)
        
    elif (time > 1440 and time<=1470):
        #if (attack_island(pirate) != 0):
           # return attack_island(pirate)
        return movement_1(pirate, pirate_id, mapX, mapY)
            
    elif (time > 1470 and time<=1580):
        if (attack_island(pirate) != 0):
            return attack_island(pirate)
        return movement_2(pirate, pirate_id, mapX, mapY)
            
    elif(time > 1580 and time <= 1720):
        if (attack_island(pirate) != 0):
            return attack_island(pirate)
        return movement_3(pirate, pirate_id, mapX, mapY)
    
    elif (time > 1720 and time<=1765):
        #if (attack_island(pirate) != 0):
            #return attack_island(pirate)
        return movement_1(pirate, pirate_id, mapX, mapY)
     
    elif (time > 1765 and time<=1795):
        #if (attack_island(pirate) != 0):
            #return attack_island(pirate)
        return movement_2(pirate, pirate_id, mapX, mapY)
        
    elif(time > 1795 and time <= 1935):
        if (attack_island(pirate) != 0):
            return attack_island(pirate)
        return movement_3(pirate, pirate_id, mapX, mapY)
        
    elif (time > 1935 and time<=2045):
        if (attack_island(pirate) != 0):
            return attack_island(pirate)
        return movement_1(pirate, pirate_id, mapX, mapY)
     
    elif (time > 2045 and time<=2100):
        #if (attack_island(pirate) != 0):
            #return attack_island(pirate)
        return movement_2(pirate, pirate_id, mapX, mapY)
      
    elif(time > 2100 and time <= 2130):
        #if (attack_island(pirate) != 0):
            #return attack_island(pirate)    
        return movement_3(pirate, pirate_id, mapX, mapY)
        
    elif (time > 2130 and time<=2240):
        if (attack_island(pirate) != 0):
            return attack_island(pirate)
        return movement_1(pirate, pirate_id, mapX, mapY)
     
    elif (time > 2240 and time<=2380):
        if (attack_island(pirate) != 0):
            return attack_island(pirate)
        return movement_2(pirate, pirate_id, mapX, mapY)
      
    elif(time > 2380 and time <= 2425):
        #if (attack_island(pirate) != 0):
            #return attack_island(pirate)
        return movement_3(pirate, pirate_id, mapX, mapY)
        
    elif (time > 2425 and time<=2455):
        #if (attack_island(pirate) != 0):
            #return attack_island(pirate)
        return movement_1(pirate, pirate_id, mapX, mapY)
      
    elif (time > 2455 and time<=2565):
        if (attack_island(pirate) != 0):
            return attack_island(pirate)   
        return movement_2(pirate, pirate_id, mapX, mapY)
       
    elif(time > 2565 and time <= 2705):
        if (attack_island(pirate) != 0):
            return attack_island(pirate)
        return movement_3(pirate, pirate_id, mapX, mapY)
        
    elif (time > 2705 and time<=2750):
        #if (attack_island(pirate) != 0):
            #return attack_island(pirate) 
        return movement_1(pirate, pirate_id, mapX, mapY)
            
    elif (time > 2750 and time<=2780):
        #if (attack_island(pirate) != 0):
            #return attack_island(pirate)
        return movement_2(pirate, pirate_id, mapX, mapY)
            
    elif(time > 2780):
        if (attack_island(pirate) != 0):
            return attack_island(pirate)
        return movement_3(pirate, pirate_id, mapX, mapY)


def ActTeam(team):
    l = team.trackPlayers()
    s = team.getTeamSignal()

    team.buildWalls(1)
    team.buildWalls(2)
    team.buildWalls(3)
    # print(team.getTeamSignal())
    # print(team.trackPlayers())
    if s:
        island_no = int(s[0])
        signal = l[island_no - 1]
        if signal == "myCaptured":
            team.setTeamSignal("")
