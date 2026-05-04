"""zufaelliges_rumfahren controller.

Der Roboter fährt hier zufällig herum
Wenn wir anstoßen, stoßen wir halt an ...
"""

from controller import Robot, Motor

print("Controller: Zufälliges Rumfahren gestartet.")

TIME_STEP = 64
MAX_SPEED = 6.28

# Eine Robotercontrollerinstanz erzeugen
robot = Robot()

# Handles für den Motor holen
leftMotor = robot.getDevice('left wheel motor')
rightMotor = robot.getDevice('right wheel motor')

# Zielposition der Räder auf Unendlich setzen
# D.h. so viel wie: Wir steuern jetzt gleich über
# die Geschwindigkeitskontrolle der Räder und geben
# NICHT eine Zielposition für die Räder vor
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))

# Hauptsimulationsschleife
# Wird ausgeführt, bis Webots den Robotcontroller stoppt
import random

# Startzustand: Nach vorne fahren
zustand = 3
counter = 50

zustandsdic = {1 : "Drehe nach links",
               2 : "Drehe nach rechts",
               3 : "Fahre vorwärts",
               4 : "Fahre rückwärts"}

# Geschwindigkeit der Motoren definieren
# 0.0: Motor steht
# 1.0: Motoren drehen sich maximal schnell
speed = 0.4

while robot.step(TIME_STEP) != -1:

    # Wenn die Zeit für die vorherige
    # Verhaltensweise abgelaufen ist,
    # setze einen neuen zufälligen Zustand
    # (Verhaltensweise) und wähle
    # eine zufällige Zeitdauer hierfür aus
    if counter==0:
                
        if zustand==1 or zustand==2:
            # Nach drehen: nach vorne oder rückwärts fahren
            zustand=random.randint(3,4)
            
            # Zeitdauer fürs nach vorne oder rückwärts fahren
            counter=random.randint(50,80)
            
        elif zustand==3 or zustand==4:
            # Nach vorne/rückwärts fahren: drehen
            zustand=random.randint(1,2)
            
            # Zeitdauer fürs Drehen
            counter=random.randint(15,50)
                        
        name_zustand = zustandsdic[zustand]
        print(f"Neuer Zustand #{zustand}/{name_zustand} für {counter} Schritte.")
    else:
        counter -= 1
        
    #print(zustand, counter)
    if zustand==1:
        leftMotor.setVelocity (-speed * MAX_SPEED)
        rightMotor.setVelocity(+speed * MAX_SPEED)        
    if zustand==2:
        leftMotor.setVelocity (+speed * MAX_SPEED)
        rightMotor.setVelocity(-speed * MAX_SPEED)
    if zustand==3:
        leftMotor.setVelocity (+speed * MAX_SPEED)
        rightMotor.setVelocity(+speed * MAX_SPEED)
    if zustand==4:
        leftMotor.setVelocity (-speed * MAX_SPEED)
        rightMotor.setVelocity(-speed * MAX_SPEED)
        
      
