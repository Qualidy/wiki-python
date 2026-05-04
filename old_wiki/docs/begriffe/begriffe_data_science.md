# Begriffssammlung Data Science


# Einführung in Data Science

| Begriff        | Kurzerklärung                                               | Link zur Referenz                                      |
|----------------|-------------------------------------------------------------|--------------------------------------------------------|
| Data Science   | Eine Fachdisziplin, um aus Daten neues Wissen zu generieren | [Referenz](https://de.wikipedia.org/wiki/Data_Science) |

# Pandas: Einführung

| Begriff                   | Kurzerklärung                                                         | Link zur Referenz                                                                   |
|---------------------------|-----------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| `DataFrame`               | Datenstruktur in Pandas, die eine Tabelle speichert                   | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)      |
| `Series`                  | Datenstruktur in Pandas, die eine Folge von Werten speichert          | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.Series.html)         |
| `Index`                   | Die Beschriftung der Zeilen einer Pandas Tabelle                      | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.Index.html)          |
| `.loc[]`                  | Zugriff auf eine Zeile in einer Pandas Tabelle über Zeilenbezeichnung | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html)  |
| `concat()`                | Zusammenfügen mehreren DataFrames oder Series'                        | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.concat.html)         |
| 

# Pandas: Import/Export von Daten

| Begriff                   | Kurzerklärung                                                         | Link zur Referenz                                                                        |
|---------------------------|-----------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| `read_csv()`              | Liest eine `.csv` (comma separated values) Datei ein (eine Tabelle)   | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)            |
| `to_csv()`                | Speichert eine Pandas Tabelle als `.csv`-Datei                        | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html)    |
| `to_dict()`               | Wandelt eine Tabelle in ein Python Dictionary um                      | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html)   |
| `read_pickle()`           | Liest eine Pandas Tabelle aus einer pickle-Datei                      | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.read_pickle.html)         |
| `to_pickle()`             | Speichert eine Pandas Tabelle im pickle-Dateiformat (Binärdatei)      | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_pickle.html) |
| `to_sql()`                | Speichert eine Pandas Tabelle in einer SQL-Datenbank                  | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html)    |
| `read_sql_query()`        | Führt einen SQL-Befehl aus einer SQL-Datenbank aus. Ergebnis: Tabelle | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.read_sql_query.html)      |


# Pandas: Fehlende Werte

| Begriff                   | Kurzerklärung                                                                | Link zur Referenz                                                                          |
|---------------------------|------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| `NaN`                     | Steht für "Not a Number". Im Kontext von Tabellen meint dies eine Datenlücke | [Referenz](https://de.wikipedia.org/wiki/NaN)                                              |
| Imputation                | Einfügen von Werten in Datenlücken                                           | [Referenz](https://de.wikipedia.org/wiki/Imputation_(Statistik))                           |
| `isnull()`                | Hilfsfunktion, um fehlende Werte in Pandas DataFrames/Series zu detektieren  | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.isnull.html)                |
| `dropna()`                | Entfernt unvollständige Zeilen oder Spalten in einer Tabelle bzw. Series     | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html)      |
| `fillna()`                | Füllt Datenlücken (`NaN`) mit Werten                                         | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html)      |
| `median()`                | Berechnet den Median über Zeilen oder Spalten (je nach Einstellung)          | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.median.html)      |
| `interpolate()`           | Füllt Datenlücken mit Hilfe von benachbarten Werten (Randwerten)             | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.interpolate.html) |


# NumPy: Einführung und NumPy Arrays

| Begriff                   | Kurzerklärung                                                          | Link zur Referenz                                                                             |
|---------------------------|------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| `numpy.array()`           | Ein n-dimensionales Array. Wird sehr effizient gespeichert             | [Referenz](https://numpy.org/doc/stable/reference/generated/numpy.array.html)                 |
| `arange()`                | Erzeugt ein NumPy Array in einem angegebenen Bereich                   | [Referenz](https://numpy.org/doc/stable/reference/generated/numpy.arange.html)                |
| `sum()`                   | Bildet die Zeilen- oder Spaltensummen eines Arrays                     | [Referenz](https://numpy.org/doc/stable/reference/generated/numpy.sum.html)                   |
| `max()`                   | Berechnet das Zeilen- oder Spaltenmaximum eines Arrays                 | [Referenz](https://numpy.org/doc/stable/reference/generated/numpy.max.html)                   |
| `multiply()`              | Multipliziert zwei Arrays elementweise (keine Matrizenmultiplikation!) | [Referenz](https://numpy.org/doc/stable/reference/generated/numpy.multiply.html)              |
| `randint()`               | Erzeugt ein Array mit zufälligen ganzen Zahlen aus einem Intervall     | [Referenz](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html) |
| `transpose()`             | Wandelt Zeilen einer Matrix in Spalten um ("kippt" die Matrix)         | [Referenz](https://numpy.org/doc/stable/reference/generated/numpy.transpose.html)             |


# Numpy: Slicing

| Begriff                   | Kurzerklärung                                                                   | Link zur Referenz                                                                                      |
|---------------------------|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| Slicing                   | Bei Python-Listen, NumPy-Arrays oder Tabellen Teile "herrauschneiden"           | [Referenz](https://www.geeksforgeeks.org/slicing-indexing-manipulating-and-cleaning-pandas-dataframe/) |
| Boolean Indexing          | Rausschneiden von Teilen eines NumPy-Arrays, das gewissen Bedingungen "genügt"  | [Referenz](https://numpy.org/doc/stable/user/basics.indexing.html)                                     |
| `diagonal()`              | Liefert die Diagonalwerte einer Matrix                                          | [Referenz](https://numpy.org/doc/stable/reference/generated/numpy.diagonal.html)                       |
| `reshape()`               | Wandelt die Werte eines NumPy-Arrays in einer andere Form (Dimensionalität) um  | [Referenz](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html)                        |


# Matplotlib: Linienplots

| Begriff                   | Kurzerklärung                                                                     | Link zur Referenz                                                                                      |
|---------------------------|-----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| `plot()`                  | Plottet (x,y)-Punkte mit Markern und/oder verbindet diese mit Linien (Linienplot) | [Referenz](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)                      |
| Marker                    | Visualisiert einzelne Datenpunkte über Kreise, Dreiecke, Sterne, etc.             | [Referenz](https://matplotlib.org/stable/api/markers_api.html)                                         |
| `annotate()`              | Erlaubt es Anmerkungen zu einzelnen Datenpunkte über Pfeile+Text hinzuzufügen     | [Referenz](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.annotate.html)                  |
| `plt.legend()`            | Fügt einem Diagramm eine Legende zu, die zeigt, was die einzelnen Linien bedeuten | [Referenz](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html)                    |
| `plt.grid()`              | Zeigt Gitterlinien im Diagramm an. Erhöht die Lesbarkeit                          | [Referenz](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html)                      |


# Matplotlib: Subplots

| Begriff                   | Kurzerklärung                                                                   | Link zur Referenz                                                                                      |
|---------------------------|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| Subplot                   | Ein Unterdiagramm in einem großen Diagramm                                      | [Referenz](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html)         |
| `plt.subplot()`           | Fügt einen neuen einzelnen Subplot (Unterdiagramm) hinzu                        | [Referenz](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html)                   |
| `plt.subplots()`          | Erzeugt eine ganze Menge (ein Gitter) von Subplots                              | [Referenz](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html)                  |
| `tight_layout()`          | Optimiert die Abstände zwischen und um Subplots herum                           | [Referenz](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html)              |
| `subplots_adjust()`       | Erlaubt es horizontale und vertikale Abstände zwischen Subplots zu definieren   | [Referenz](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html)           |
| `subplot2grid()`          | Erlaubt es Subplots über mehrere Zeilen/Spalten des Subplotgitters zu erzeugen  | [Referenz](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot2grid.html)              |


# Seaborn: Einführung


| Begriff                   | Kurzerklärung                                                                   | Link zur Referenz                                                                                      |
|---------------------------|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| `violinplot()`            | Plot, der die Verteilung von Daten und einen Boxplot gleichzeitig visualisiert  | [Referenz](https://seaborn.pydata.org/generated/seaborn.violinplot.html)                               |
| `countplot()`             | Balkendiagramm, das zeigt, wie oft bestimmte Kategorien auftreten               | [Referenz](https://seaborn.pydata.org/generated/seaborn.countplot.html)                                |
| `boxplot()`               | Visualiert Median, Quartile, Spannweiter und Ausreißer in einem Diagramm        | [Referenz](https://seaborn.pydata.org/generated/seaborn.boxplot.html)                                  |
| FacetGrid                 | Plot, der es erlaubt schnell bedingte Abhängigkeiten zwischen Daten zu erkennen | [Referenz](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html)                                |
| `jointplot()`             | Kombination von Scatterplot und Histogramm-Plots                                | [Referenz](https://seaborn.pydata.org/generated/seaborn.jointplot.html)                                |
| `kdeplot()`               | Zeigt Verteilungen von Daten über Isokonturlinien ("Höhenlinien") an            | [Referenz](https://seaborn.pydata.org/generated/seaborn.kdeplot.html)                                  |


# Matplotlib: Ticks

| Begriff                             | Kurzerklärung                                                                                             | Link zur Referenz                                                                           |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| Ticks (bei Matplotlib Diagrammen)   | Ticks sind die Markierungen auf den Achsen eines Matplotlib-Diagramms, die die Skalenwerte repräsentieren | [Referenz](https://matplotlib.org/stable/users/explain/axes/axes_ticks.html)                |
| `xticks()`                          | Definiert, wo die Ticks auf der x-Achse gesetzt werden                                                    | [Referenz](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html)         |
| `yticks()`                          | Definiert, wo die Ticks auf der y-Achse gesetzt werden                                                    | [Referenz](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html)         |
| `xscale()`                          | Setzt die Skala (linear, logarithmisch) für die x-Achse                                                   | [Referenz](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xscale.html)         |
| `yscale()`                          | Setzt die Skala (linear, logarithmisch) für die y-Achse                                                   | [Referenz](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yscale.html)         |
| `tick_params()`                     | Erlaubt es z.B. die Farbe der Ticks zu ändern                                                             | [Referenz](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html) |


# Pandas: Multiindex

| Begriff                   | Kurzerklärung                                                                                             | Link zur Referenz                                                                                      |
|---------------------------|-----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| Multiindex                | Ein Multiindex in Pandas ermöglicht es, mehrere Indexebenen in einem DataFrame oder einer Series zu haben | [Referenz](https://pandas.pydata.org/docs/user_guide/advanced.html)                                    |
| `Multiindex()`            | Erzeugung eines Multiindex                                                                                | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.html)                        |
| `from_arrays()`           | Erzeugt einen Multiindex aus Arrays                                                                       | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_arrays.html)            |
| `from_product()`          | Erzeugt einen Multiindex aus dem Produkt von Mengen                                                       | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_product.html)           |


# Pandas: Gruppieren und Pivotisieren

| Begriff                   | Kurzerklärung                                                                         | Link zur Referenz                                                                                            |
|---------------------------|---------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| `groupby()`               | Erzeugt aus einem DataFrame Gruppen-Objekte (unterteilt das DataFrame in Gruppen)     | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html)                       |
| Aggregationsfunktion      | Eine Funktion, die auf den Gruppen angewendet wird (z.B. `min`, `mean`, etc.)         | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.aggregate.html) |
| `pivot_table()`           | Erzeugt eine neue Tabelle aus einer bestehenden Tabelle, gruppiert nach einem Merkmal | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.pivot_table.html)                             |


# Pandas & Matplotlib: Zeitreihenanalyse

| Begriff                   | Kurzerklärung                                                                         | Link zur Referenz                                                                                          |
|---------------------------|---------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| Zeitreihe                 | Eine zeitlich geoordnete Folge von Werten, Bsp: Sensorwerte oder Umsatzzahlen         | [Referenz](https://de.wikipedia.org/wiki/Zeitreihenanalyse)                                                |
| `rolling()`               | Erzeugt ein gleitendes Fenster, z.B. um einen gleitenden Mittelwert zu berechnen      | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rolling.html)                     |
| `resample()`              | Erzeugt eine neue zeitliche Sicht auf eine Zeitreihe                                  | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.resample.html)                    |
| Lineare Regression        | Verfahren, das Datenpunkte versucht durch eine Gerade zu beschreiben                  | [Referenz](https://de.wikipedia.org/wiki/Lineare_Regression)                                               |
| scikit-learn              | Python Bibliothek mit sehr vielen Machine-Learning-Verfahren, u.a. Lineare Regression | [Referenz](https://scikit-learn.org/stable/)                                                               |
| `LinearRegression`        | Klasse aus scikit-learn, um eine lineare Regression zu lernen                         | [Referenz](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)   |


# Pandas: Outlier (Ausreißer)

| Begriff                  | Kurzerklärung                                                                                                                                                | Link zur Referenz                                                                                      |
|------------------------ -|--------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| IQR                      | Der Interquartilbereich (IQR) ist die Differenz zwischen dem 75. und 25. Perzentil eines Datensatzes und wird verwendet, um Ausreißer zu identifizieren      | [Referenz](https://de.wikipedia.org/wiki/Interquartilsabstand_(deskriptive_Statistik))                 |
| Z-Score                  | Der Z-Score ist eine statistische Maßzahl, die angibt, wie viele Standardabweichungen ein Datenpunkt vom Mittelwert der Datenmenge entfernt ist              | [Referenz](https://help.tableau.com/current/pro/desktop/de-de/calculating_z_scores.htm)                |
| Winsorizing              | Winsorizing ist eine Methode zur Reduzierung von Ausreißern, indem extrem hohe und niedrige Werte auf einen bestimmten Perzentilwert gesetzt werden          | [Referenz](https://en.wikipedia.org/wiki/Winsorizing)                                                  |
| Quantil                  | Ein Quantil ist ein Wert, der einen Datensatz in gleich große, aufeinanderfolgende Teile teilt, wobei das 50. Perzentil beispielsweise dem Median entspricht | [Referenz](https://de.wikipedia.org/wiki/Empirisches_Quantil)                                          |
| Standardabweichung       | Die Standardabweichung ist ein Maß für die Streuung der Werte in einem Datensatz, wobei höhere Werte auf eine größere Variabilität hinweisen                 | [Referenz](https://de.wikipedia.org/wiki/Stichprobenvarianz_(Sch%C3%A4tzfunktion))                     |
| `zscore()`               | Funktion zur Berechnung des Z-Scores                       | [Referenz](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.zscore.html)           |
| `quantile()`             | Berechnet Quantile, z.B. zur Berechnung des 95% Perzentils | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.quantile.html)            |
| `winsorize()`            | Funktion zur Begrenzung von Ausreißern                     | [Referenz](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mstats.winsorize.html) |


# Pandas & Matplotlib: DateTime (Zeitstempel)

| Begriff                  | Kurzerklärung                                                                                       | Link zur Referenz                                                                                      |
|--------------------------|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| datetime                 | Modul aus der Python Standard-Bibliothek, um Zeitstempel (Datum-Uhrzeit) zu speichern               | [Referenz](https://docs.python.org/3/library/datetime.html#module-datetime)                            |
| `date_range()`           | Erzeugt ein Intervall von Zeitstempeln                                                              | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.date_range.html)                        |
| `dt.day`                 | Liefert den Tag eines datetime Objektes zurück                                                      | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.day.html)                     |
| `dt.month`               | Liefert den Monat eines datetime Objektes zurück                                                    | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.month.html)                   |
| `dt.year`                | Liefert das Jahr eines datetime Objektes zurück                                                     | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.year.html)                    |
| `dt.dayofweek`           | Liefert den Wochentag eines datetime Objektes zurück                                                | [Referenz](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.dayofweek.html)               |
