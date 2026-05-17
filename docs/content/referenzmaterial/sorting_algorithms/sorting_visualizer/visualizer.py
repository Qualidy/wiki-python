import doctest
import matplotlib.pyplot as plt


def add_frame(elements, color='blue', pause=0.1):
    """
    Erstellt eine Animation für einen Sortieralgorithmus. Eine Liste Elements wird mit Balken dargestellt,
    die eingefärbt werden können.

    ⚠ WICHTIG: Führe am Ende des Files plot_animation() aus.

    Args:
        elements: Liste mit y-Wert der Balken.
        color: Farbe der Balken. Kann eine einzelne Farbe sein (englische Bezeichnung 'blue' oder Hexadezimalwert '#0000FF') oder eine Liste, die für jedes Elemente die Farbe angibt.
        pause: Zeit, bis zum nächsten Animationsschritt.
    """
    plt.clf()
    plt.bar(range(len(elements)), elements, color=color)
    plt.pause(pause)


def create_color_list(n, default_color='blue', indexed_color=None):
    """
    Gibt eine Liste der Länge n von Farben zurück. Dabei wird immer die Defaultfarbe verwendet, außer
    es ist anders im indexed_color dictionary hinterlegt.

    Args:
        n: Länge der Liste.
        default_color: Standardfarbe, die genutzt wird, wenn nicht abweichend im indexed_color notiert. Englische Bezeichnungen ('blue') oder Hexadezimalwerte ('#0000FF') sind erlaubt.
        indexed_color: dictionary, in dem die Schlüssel einen Index Darstellen und die Values die jeweiligen Farben an der Position.

    Returns: Liste von Farben.

    >>> create_color_list(6, 'blue', {2: 'red', 4: 'yellow'})
    ['blue', 'blue', 'red', 'blue', 'yellow', 'blue']
    >>> create_color_list(2, 'red')
    ['red', 'red']
    >>> create_color_list(3)
    ['blue', 'blue', 'blue']
    """
    indexed_color = indexed_color or dict()

    colors = [default_color] * n

    for index, color in indexed_color.items():
        colors[index] = color

    return colors


def plot_animation():
    """
    Shorthand für `plt.show()`, um Animation anzuzeigen. Führe dies am Ende der Datei aus.
    """
    plt.show()


if __name__ == "__main__":
    doctest.testmod()
