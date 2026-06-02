import sorting_visualizer as sv


def simple_sort(elements):
    n = len(elements)
    for i in range(n):
        for j in range(n - i - 1):
            if elements[j] > elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]

            # Visualisiere den momentanen Zustand
            color = sv.create_color_list(n=n, indexed_color={j: 'red', j + 1: 'yellow'})
            sv.add_frame(elements=elements, color=color)


# Erstelle zufällig sortierte Aufsteigende Liste
shuffled_list = sv.create_shuffled_list(12)

# Sortiere die Liste
simple_sort(shuffled_list)

# Starte Animation
sv.plot_animation()
