"""benutzer_steuert_fahrzeug controller."""

from controller import Robot, Keyboard
from vehicle import Driver

print("Steuern Sie selber das Fahrzeug!")

# Erzeuge einen "Roboter"-Controller
# Heute ist der Roboter ein Fahrzeug
robot = Robot()

timestep = 64

keyboard = Keyboard()
keyboard.enable(timestep)

driver = Driver()

speed = 0.0
angle = 0.0

def set_speed(new_speed):
    driver.setCruisingSpeed(new_speed)
    print("New speed:", new_speed)
    
def set_angle(new_angle):
    driver.setSteeringAngle(new_angle)
    print("New angle:", new_angle)

wait_time = 0
while driver.step() != -1:
    key=keyboard.getKey()
    
    if wait_time == 0:
       
        if key==73: # Taste i
           speed += 2.0
           set_speed( speed )
           wait_time = 10
           
        if key==74: # Taste j
           angle -= 0.05
           set_angle( angle )
           wait_time = 10
           
        if key==75: # Taste k
           speed -= 2.0
           set_speed( speed )
           wait_time = 10
           
        if key==76: # Taste l
           angle += 0.05
           set_angle( angle )
           wait_time = 10
       
    wait_time -= 1
    if wait_time < 0:
        wait_time = 0
 
