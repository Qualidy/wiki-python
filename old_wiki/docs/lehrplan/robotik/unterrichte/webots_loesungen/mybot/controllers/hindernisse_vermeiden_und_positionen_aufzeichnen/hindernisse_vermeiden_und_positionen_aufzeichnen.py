# Hindernisse vermeiden + Positionen aufzeichnen Controller.


from controller import Robot, Motor
import pandas as pd
import numpy as np

print("Controller Hindernisse vermeiden + Positionen aufzeichnen gestartet!")

TIME_STEP = 64
MAX_MOTOR_SPEED = 6.28

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

leftMotor.setVelocity (0)
rightMotor.setVelocity(0) 

# Zugriff auf Sensoren ds0-ds1 vorbereiten
ds0 = robot.getDevice("ds0")
ds1 = robot.getDevice("ds1")
ds0.enable(TIME_STEP)
ds1.enable(TIME_STEP)

# Zugriff auf GPS vorbereiten
gpsSensor = robot.getDevice("gps")
gpsSensor.enable(TIME_STEP)

SPEED = 6
randomize = True

fname = "koordinaten.csv"
coords = []

# Hauptsimulationsschleife
# Wird ausgeführt, bis Webots den Robotcontroller stoppt
while robot.step(TIME_STEP) != -1:

    ds0_value = ds0.getValue()
    ds1_value = ds1.getValue()
    #print(ds0_value, ds1_value)
    gpsCoords = gpsSensor.getValues()
    print(gpsCoords)
    coords.append( tuple(gpsCoords) )
    
    t = pd.DataFrame(coords, columns=["x", "y", "z"])
    t.to_csv( fname, index=False )

    if ds1_value > 500:
      
      #
      # If both distance sensors are detecting something, this means that
      # we are facing a wall. In this case we need to move backwards.
      #
      if ds0_value > 200:
        left_speed = -SPEED
        right_speed = -SPEED / 2
        
      else:
        #
        # We turn proportionnaly to the sensors value because the
        # closer we are from the wall, the more we need to turn.
        #
        left_speed = -ds1_value / 100
        right_speed = (ds0_value / 100) + 0.5

    elif ds0_value > 500:
    
      left_speed = (ds1_value / 100) + 0.5
      right_speed = -ds0_value / 100
      
    else:
    
      #
      # If nothing was detected we can move forward at maximal speed.
      #
      left_speed = SPEED
      right_speed = SPEED
      
    # Randomisiere die Bewegung (damit der Roboter keine festen Schleifen fährt)?
    if randomize:
        left_speed +=  np.random.uniform(-1.5, 1.5)
        right_speed +=  np.random.uniform(-1.5, 1.5)
    
    # Setze Motorgeschwindigkeiten
    leftMotor.setVelocity (left_speed)
    rightMotor.setVelocity(right_speed)
    
