"""fahrsequenz_assistent controller."""

from controller import Robot, Keyboard
from vehicle import Driver
import pandas

print("Steuern Sie selber das Fahrzeug!")
print("'r' um eine Sequenz aufzunehmen bzw. zu stoppen")
print("'p' um die Sequenz wieder abzuspielen")

# Erzeuge einen "Roboter"-Controller
# Heute ist der Roboter ein Fahrzeug
robot = Robot()

timestep = 64

fname_sequence = "fahrsequenz1.csv"

keyboard = Keyboard()
keyboard.enable(timestep)

driver = Driver()

driving_sequence = []

speed = 0.0
angle = 0.0
recording = False
playing = False

def set_speed(new_speed, recording, time_seq, driving_sequence):
    driver.setCruisingSpeed(new_speed)
    if recording:
        driving_sequence.append( (time_seq, "speed", new_speed) )
    print("New speed:", new_speed)
    
def set_angle(new_angle, recording, time_seq, driving_sequence):
    driver.setSteeringAngle(new_angle)
    if recording:
        driving_sequence.append( (time_seq, "angle", new_angle) )
    print("New angle:", new_angle)
    
def start_stop_recording(rec):
    if rec==False:
        print("Starte Aufnahme der Sequenz")
        return True
    else:
        print("Stoppe Aufnahme der Sequenz")
        return False
        
def save_sequence( fname, driving_sequence ):
    t = pandas.DataFrame(driving_sequence,
                         columns=["time", "cmd", "value"])
    t.to_csv( fname, index=False )
    
# Am Anfang Räder des Fahrzeugs gerade aus stellen
# Auf der Stelle stehen bleiben
driver.setSteeringAngle(0.0)
driver.setCruisingSpeed(0.0)

wait_time = 0
time_seq = 0
while driver.step() != -1:
    key=keyboard.getKey()
    #print("key=",key)
    
    if key>0 and wait_time == 0:
       
        if chr(key)=='I': # Taste i
           speed += 2.0
           set_speed( speed, recording, time_seq, driving_sequence )
           
        if chr(key)=='J': # Taste j
           angle -= 0.05
           set_angle( angle, recording, time_seq, driving_sequence )
           
        if chr(key)=='K': # Taste k
           speed -= 2.0
           set_speed( speed, recording, time_seq, driving_sequence )
           
        if chr(key)=='L': # Taste l
           angle += 0.05
           set_angle( angle, recording, time_seq, driving_sequence )
           
        if chr(key)=='R': # Taste r wie record
           recording = start_stop_recording(recording)
           if recording:
               driving_sequence = []
               time_seq = 0
           if not recording:
               driving_sequence.append( (time_seq, "stop", "-1") )
               save_sequence( fname_sequence, driving_sequence )
               
        if chr(key)=='P': # Taste p wie play
            if not playing:
                print(f"Starte mit Abspielen der Sequenz {fname_sequence}")
                playing = True
                sequence_table = pandas.read_csv( fname_sequence )
                sequence_table.set_index("time", inplace=True)
                time_seq = 0
            else:
                playing = False
                print(f"Abspielen der Sequenz {fname_sequence} von Benutzer gestoppt!")
                      
        wait_time = 20
        
    if recording or playing:
        time_seq += 1
        
    if playing:
    
        # Wir spielen gerade eine Sequenz ab
        # D.h. wir müssen überprüfen, ob wir zum
        # aktuellen Zeitpunkt der Sequenz
        # nämlich <time_seq>
        # eine neue Aktion laut sequence_table ausführen
        # sollen.
        # Wenn nicht, gibt es keinen Eintrag in der Tabelle
        # und das führt zu einem KeyError, den wir hier
        # dann abfangen und dann nichts machen (pass).
    
        try:
            cmd, val = sequence_table.loc[ time_seq ]
            print( f"{time_seq} : {cmd} {val}" )
            if cmd=="speed":
                driver.setCruisingSpeed(val)
            if cmd=="angle":
                driver.setSteeringAngle(val)
            if cmd=="stop":
                print(f"Sequenz {fname_sequence} komplett abgespielt!")
                playing=False
                
        except KeyError:
            # Keine neue Aktion muss ausgeführt werden
            pass
       
    wait_time -= 1
    if wait_time < 0:
        wait_time = 0
       
 
