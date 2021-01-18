from openpyxl import chart, utils
from openpyxl.chart import layout
from openpyxl.worksheet import table

def add_table(
    worksheet,
    name,
    start_cell,
    num_rows,
    num_columns,
):
    worksheet.add_table(table.Table(
        displayName=name,
        ref='{}:{}{}'.format(
            start_cell,
            utils.get_column_letter(num_columns),
            num_rows,
        ),
        tableStyleInfo=table.TableStyleInfo(
            name='TableStyleMedium9',
            showFirstColumn=True,
            showLastColumn=False,
            showRowStripes=True,
            showColumnStripes=False,
        ),
    ))

# TODO: Add support to add this for a table note defined at top left of sheet
def add_graph(
    worksheet,
    start_cell,
    title,
    chart_length,
    x_axis_label='',
    y_axis_label='',
):
    area_chart = chart.AreaChart()
    area_chart.title=title
    area_chart.style = 42
    area_chart.x_axis.scaling.orientation = "maxMin"
    area_chart.x_axis.title = x_axis_label
    # Makes the y axis labels vertical instead of slanted so they all fit
    area_chart.y_axis.title = y_axis_label
    area_chart.x_axis.tickLblSkip = 1
    # put legend on the bottom which allows the graph to be wider
    area_chart.legend.position = 'b'
    # not sure exactly how this works but this makes the graph bigger within the space alotted 
    area_chart.layout = layout.Layout(
        layout.ManualLayout(
            x=0, y=0,
            h=.9, w=.9,
        ),
    )

    yaxis_dates = chart.Reference(
        worksheet,
        min_col=2,
        max_col=chart_length + 1,
        min_row=1,
        max_row=1,
    )
    xaxis_data = chart.Reference(
        worksheet,
        min_col=1,
        max_col=chart_length + 1,
        min_row=2,
        max_row=5,
    )
    area_chart.add_data(xaxis_data, titles_from_data=True, from_rows=True)
    area_chart.set_categories(yaxis_dates)
    worksheet.add_chart(area_chart, start_cell)
