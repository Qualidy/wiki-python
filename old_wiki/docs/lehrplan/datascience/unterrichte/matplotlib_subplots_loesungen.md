# Lösungen

### A1: Subplot mit 3x2 Anordnung mittels plt.subplot() 🌶️🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/s7UfvewUcZE?si=kNFf6Y-yvWeoedwq" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

Erstelle ein Subplot mit 3 Zeilen und 2 Spalten und den gleichen Plot in allen 6 Subplots.

Benutze dabei den Befehl plt.subplot().


```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

for i in range(1,7):
    plt.subplot(3, 2, i)
    plt.plot(x, y)
    plt.title('Sinuskurve')

plt.tight_layout()
plt.show()
```


    
![png](matplotlib_subplots_loesungen_files/matplotlib_subplots_loesungen_2_0.png)
    


### A2: Subplot mit 3x2 Anordnung mittels plt.subplot()s 🌶️🌶️🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/K_xLFccB7TU?si=o02nbembDzz8mJrp" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

Erstelle ein Subplot mit 3 Zeilen und 2 Spalten und den gleichen Plot in allen 6 Subplots.

Benutze dabei den Befehl `plt.subplots()` (ja! den mit dem s am Ende)

Versuche alle 6 Subplots im Rahmen einer Schleife zu erzeugen!


```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

fig, axs = plt.subplots(3, 2)

for i in range(0,6):
    zeile  = i%3
    spalte = i%2
    print((zeile,spalte))
    axs[zeile, spalte].plot(x,y)
    axs[zeile, spalte].set_title("Sinus")   
    
plt.tight_layout()
plt.show()
```

    (0, 0)
    (1, 1)
    (2, 0)
    (0, 1)
    (1, 0)
    (2, 1)



    
![png](matplotlib_subplots_loesungen_files/matplotlib_subplots_loesungen_4_1.png)
    


### A3: Anpassen der Subplot-Abstände 🌶️🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/bXrS5XtAcaM?si=xwuVeZlr3NGLuKIc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

Erstelle vier Subplots in einem Gitter und passe die Abstände zwischen ihnen an.

Der Abstand soll vertikal und horizontal geregelt werden können.


```python
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

fig, axs = plt.subplots(2, 2)

axs[0, 0].plot(x, y)
axs[0, 1].plot(x, y)
axs[1, 0].plot(x, y)
axs[1, 1].plot(x, y)

plt.subplots_adjust(wspace=1.5, hspace=0.5)

plt.show()
```


    
![png](matplotlib_subplots_loesungen_files/matplotlib_subplots_loesungen_6_0.png)
    


### A4: Ein großer und zwei kleine Subplots 🌶️🌶️🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/UoqdLcs5iZY?si=E1cTwOwHuYwL-lQR" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

Erstelle ein Layout mit einem großen Subplot oben und zwei kleineren Subplots unten.

Lese hierzu vorher in der Dokumentation den Befehl `subplot2grid()` nach!


```python
import matplotlib.pyplot as plt

fig = plt.figure()

ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)

# Beispieldaten plotten
ax1.plot([1, 2, 3], [10,  20, 30])
ax2.plot([1, 2, 3], [15, 100, 90])
ax3.plot([1, 2, 3], [60,  70, 70])

plt.tight_layout()
plt.show()
```


    
![png](matplotlib_subplots_loesungen_files/matplotlib_subplots_loesungen_8_0.png)
    


### A5: Subplots in L-Form 🌶️🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/uEmCP8qsT4Y?si=nONd0HFXXejeEcz9" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

Erstelle ein Subplot-Layout in L-Form, bei dem sich ein vertikales Subplot links und ein horizontales Subplot unten befinden.


```python
fig = plt.figure()

ax1 = plt.subplot2grid((3, 3), (0, 0), rowspan=2)
ax2 = plt.subplot2grid((3, 3), (2, 0), colspan=3)

# Beispieldaten plotten
ax1.plot([1, 2, 3], [1, 2, 3])
ax2.plot([1, 2, 3], [3, 2, 1])

plt.tight_layout()
plt.show()
```


    
![png](matplotlib_subplots_loesungen_files/matplotlib_subplots_loesungen_10_0.png)
    


### A6: Schachbrett-Layout 🌶️🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/flIpcC72dxY?si=vOujAykA0_Wbn7eh" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

Erstelle ein 3x3 Schachbrett-Layout, wobei abwechselnd Subplots und leere Räume sind.


```python
fig = plt.figure()

for i in range(3):
    for j in range(3):
        if (i + j) % 2 == 0:
            ax = plt.subplot2grid((3, 3), (i, j))
            ax.plot([1, 2, 3], [10, 30, -5])  # Beispieldaten

plt.tight_layout()
plt.show()
```


    
![png](matplotlib_subplots_loesungen_files/matplotlib_subplots_loesungen_12_0.png)
    


### A7: Zwei Horizontale Subplots Nebeneinander 🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/0bpj4U3y1fg?si=AbXevzmkCb75FLeW" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

Erstelle zwei horizontale Subplots nebeneinander, wobei der linke Subplot doppelt so breit ist wie der rechte.


```python
fig = plt.figure()

ax1 = plt.subplot2grid((1, 3), (0, 0), colspan=2)
ax2 = plt.subplot2grid((1, 3), (0, 2))

# Beispieldaten plotten
ax1.plot([1, 2, 3], [10, 20, 5])
ax2.plot([1, 2, 3], [3, 2, 9])

plt.tight_layout()
plt.show()
```


    
![png](matplotlib_subplots_loesungen_files/matplotlib_subplots_loesungen_14_0.png)
    


### A8: T-förmiges Layout 🌶️🌶️
<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/pG4NCkvnXAg?si=NmnB2SRrCBCjPRRV" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>



Erstelle ein T-förmiges Layout mit drei Subplots.


```python
fig = plt.figure()

ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
ax2 = plt.subplot2grid((3, 3), (1, 1), rowspan=2)

# Beispieldaten plotten
ax1.plot([1, 2, 3], [1, 2, 3])
ax2.plot([1, 2, 3], [3, 2, 1])

plt.tight_layout()
plt.show()
```


    
![png](matplotlib_subplots_loesungen_files/matplotlib_subplots_loesungen_16_0.png)
    

