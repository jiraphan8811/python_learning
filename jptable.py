import justpy as jp
import pandas as pd

wm_df = pd.read_csv('https://elimintz.github.io/women_majors.csv').round(2)

def grid_test():
    wp = jp.WebPage()
    grid = wm_df.jp.ag_grid(a=wp)
    grid.options.pagination = True
    grid.options.paginationAutoPageSize = True
    grid.options.columnDefs[0].cellClass = ['text-white', 'bg-blue-500', 'hover:bg-blue-200']
    for col_def in grid.options.columnDefs[1:]:
        col_def.cellClassRules = {
            'font-bold': 'x < 20',
            'bg-red-300': 'x < 20',
            'bg-yellow-300': 'x >= 20 && x < 50',
            'bg-green-300': 'x >= 50'
        }
    return wp

jp.justpy(grid_test)