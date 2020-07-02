from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource

import bokeh.sampledata
bokeh.sampledata.download()
output_file('puntos.html')
source = ColumnDataSource(data={
    'x' : [1, 2, 3, 4, 5],
    'y' : [3, 7, 8, 5, 1],
})
p = figure(plot_width=400, plot_height=400)
p.circle('x', 'y', size=20, source=source)
show(p)