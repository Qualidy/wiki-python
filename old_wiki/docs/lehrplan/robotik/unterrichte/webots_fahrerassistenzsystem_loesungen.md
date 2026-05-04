# Lösungen

### A1: Sequenzen aufnehmen können [120 min] 🌶️🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/SuDZetKPkLM?si=UOUTSCmGOgxeXRUz" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Erweitern Sie jetzt den Tastatur-Controller (der es einem Benutzer erlaubt das Fahrzeug über die Tastatur zu steuern) so, dass die aufgenommenen Steuersignale an das Auto (den "Roboter") mit einer zeitlichen Information in einer Pandas Tabelle gespeichert werden, wenn der Benutzer die Aufnahme mit "r" (record start) startet und mit "r" (record stop" wieder beendet.

Die zeitliche Information / das Timing ist später sehr wichtig um die Sequenz auch zeitlich korrekt wieder zu geben!

Zum Beispiel könnte das Fahrmanöver "Rückwärts ausparken und langsames anfahren" sinngemäßg aus der folgenden Sequenz von Steuersignalen bestehen:

    Zeitpunkt 0: START DER AUFNAHME DER SEQUENZ
    Zeitpunkt 10: Geschwindigkeit auf -5 km/h
    Zeitpunkt 35: Lenkwinkel auf -0.2° setzen
    Zeitpunkt 70: Geschwindigkeit auf 0 km/h
    Zeitpunkt 75: Lenkwinkel auf 0.0° setzen
    Zeitpunkt 90: Geschwindigkeit auf +5 km/h
    Zeitpunkt 110: Geschwindigkeit auf +10 km/h
    Zeitpunkt 130: Geschwindigkeit auf +15 km/h
    Zeitpunkt 150: ENDE DER AUFNAHME DER SEQUENZ

Überlegen Sie sich dazu auch einen geeigneten Aufbau der Pandas-Tabelle.

Die erzeugte Pandas-Tabelle soll dann in einer Datei fahrsequenz1.csv gespeichert werden, sobald der Benutzer die Fahrsequenzaufnahme mit "r" beendet.

Lösung? Siehe bei Lösung für A2

### A2: Sequenzen abspielen können [120 min] 🌶️🌶️🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/IYVGXMK6edI?si=a6B2Fm3D2YI_lrKI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

Das Ergebnis von Aufgabe 1 ist, dass der Benutzer nun ein Fahrzeug steuern kann und die Steuersequenz als Tabelle in einer Datei wie z.B. fahrsequenz1.csv speichern kann.

Wenn der Benutzer nun "p" drückt (wie "play"), soll diese Sequenztabelle aus der Datei wieder eingelesen werden und die Sequenz abgespielt werden.

Überlegen Sie sich hierzu, wie Sie das Timing der Steuerkommandos für das Fahrzeug, das in der Tabelle auch gespeichert ist möglichst einfach bei dem Wiederabspielen der Steuerkommandos berücksichtigen.

Ziel ist es hier, eine möglichst kompkakte, leicht verständliche und wartbare Lösung in Python zu programmieren!

Lösung: Hier der Lösungscode für A1+A2:


```python
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
```

### A3: Test des Fahrsequenz-Assistenten bei Einparkvorgang [60 min] 🌶️🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/LnjXPwlIZxo?si=JjewjTilWI6jmYfq" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Erstellen Sie jetzt ein Webot Welt, in der Sie neue andere Fahrzeuge aus Webots, mit denen wir bisher nicht gearbeitet haben, an den Straßenrand stellen. Lassen Sie dabei eine gute Parklücke Platz!

Stellen Sie "Ihr" Fahrzeug auf die Straße etwas vor die Parklücke.

Dann nehmen Sie den von Ihnen entwickelten Fahrsequenz-Assistenten und nehmen einen Ihrer erfolgreichen Einpark-Vorgänge auf.

Testen Sie dann den Einparkassistenten: kann der Assistent beim Wiederabspielen der Einparksequenz das Fahrzeug erfolgreich in die Parklücke einparken?

Finden Sie heraus wie Sie in Webots ein Video erstellen können und nehmen Sie den Test Ihres Einparkassistenten als Video auf!

Lösung:

Der Autor dieses Skriptteiles ist nicht besonders gut beim Einparken.

Aber eine Einparksequenz hat er aufgenommen und dann wieder abgespielt.

Hier die aufgenommene Sequenz als Tabelle:


```python
import pandas
sequence_table = pandas.read_csv("webots_loesungen/strassen_welt/controllers/fahrsequenz_assistent/fahrsequenz1.csv")
sequence_table
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>time</th>
      <th>cmd</th>
      <th>value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>49</td>
      <td>speed</td>
      <td>-2.000000e+00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>91</td>
      <td>speed</td>
      <td>-4.000000e+00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>423</td>
      <td>speed</td>
      <td>-2.000000e+00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>469</td>
      <td>speed</td>
      <td>0.000000e+00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>548</td>
      <td>angle</td>
      <td>5.000000e-02</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>89</th>
      <td>4164</td>
      <td>angle</td>
      <td>1.387779e-17</td>
    </tr>
    <tr>
      <th>90</th>
      <td>4184</td>
      <td>angle</td>
      <td>-5.000000e-02</td>
    </tr>
    <tr>
      <th>91</th>
      <td>4204</td>
      <td>speed</td>
      <td>-2.000000e+00</td>
    </tr>
    <tr>
      <th>92</th>
      <td>4224</td>
      <td>speed</td>
      <td>0.000000e+00</td>
    </tr>
    <tr>
      <th>93</th>
      <td>4631</td>
      <td>stop</td>
      <td>-1.000000e+00</td>
    </tr>
  </tbody>
</table>
<p>94 rows × 3 columns</p>
</div>



Und hier ein Video, was in etwa als finale Lösung herauskommen könnte:

<iframe width="560" height="315" src="https://www.youtube.com/embed/ZDcYn0_F6KE?si=bL3uIOjk-H4GcIrx" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

