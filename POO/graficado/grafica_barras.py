from bokeh.io import output_file,show
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.plotting import figure
from bokeh.transform import factor_cmap

output_file('studies.html')
schools = ['Java', 'C#', 'Python', 'PHP','Javascript','Go']
counts = [40,50,40,20,10,0]

data_source = ColumnDataSource(data=dict(schools=schools, counts=counts))

graphic = figure(x_range=schools,plot_height=500, plot_width=1000, toolbar_location=None,
                 title="Porcentaje de conocimiento de lenguajes")
graphic.vbar(x='schools', top='counts',width=0.9, source=data_source, legend_field="schools",
             line_color='white', fill_color=factor_cmap('schools', palette=Spectral6,factors=schools))

graphic.xgrid.grid_line_color = None
graphic.y_range.start = 0
graphic.y_range.end = 100
graphic.legend.orientation = "horizontal"
graphic.legend.location = "top_center"
show(graphic)