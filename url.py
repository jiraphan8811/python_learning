from logging import exception
from datetime import datetime
import justpy as jp
import csv
import pandas as pd

session_data = {}


def read_file(filename):
    wm_df = pd.read_csv(filename).round(2)
    wm_df_search = wm_df.set_index('CODE')

    return wm_df


def open_dialog(self, msg):
    self.dialog.value = True


def index():
    wm_df = read_file('library.csv')
    headers = list(wm_df.columns)
    table_data = wm_df.to_numpy().tolist()
    table_data.insert(0, headers)
    wp = jp.WebPage()
    wp.add(jp.P(text='Welcome to ANCA Library', classes='text-2xl m-4 text-decoration-line: underline font-weight: 700'))
    wp.add(jp.P(text='Below is the list of all the books we have. Please scan the qr code on the book or type /CODE in the url to borrow the book outside the department.', classes='text-base m-4'))
    d = jp.Div(classes='w-7/8 m-2 p-3 border rounded-lg item-start', a=wp)
    grid = wm_df.jp.ag_grid(a=d)
    for i in range(4):
      grid.options.columnDefs[i].cellStyle = ['justify-self-start']

    return wp


def writecsv(filename,data):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)


def bookView(request):
    wm_df = read_file('library.csv')
    headers = list(wm_df.columns)
    table_data = wm_df.to_numpy().tolist()
    table_data.insert(0, headers)
    wp = jp.WebPage()
    url = request.path_params["code"].upper()
    loadcount = 0
    n = 0
    

    def submit_form(self, msg):
                session_data[msg.session_id] = msg.form_data
                for d in msg.form_data:
                    print(d["value"])
                    user = d["value"]
                    if user == '':
                        pass
                    elif user == 'Click to Return':
                        msg.page.redirect = '/'
                        table_data[n][2] = 'Available'
                        table_data[n][3] = '-'
                        table_data[n][4] = '-'
                    else:
                        msg.page.redirect = '/'    
                        table_data[n][2] = 'Unavailable'
                        table_data[n][3] = user
                        table_data[n][4] = datetime.now().strftime('%d/%m/%Y')
                    break
                print(table_data[n])
                writecsv('library.csv',table_data)

                
    for i, (code,title,status,who,since) in enumerate(table_data):
        # print(i)
        if code == url:

            #Render HTML Components
            wp.add(jp.P(text=f'Book Title: {table_data[i][1]}', classes='text-base m-2 font-bold'))
            wp.add(jp.P(text=f'Book Code: {table_data[i][0]}', classes='text-base m-2'))
            wp.add(jp.P(text=f'Status: {table_data[i][2]}', classes='text-base m-2'))
            wp.add(jp.P(text=f'Checked out by: {table_data[i][3]}', classes='text-base m-2'))
            wp.add(jp.P(text=f'Since: {table_data[i][4]}', classes='text-base m-2'))
            wp.add(jp.Br())
            form1 = jp.Form(a=wp, classes='border m-1 p-1 w-72')
            if table_data[i][2] == 'Available':
                
                user_label = jp.Label(text='Enter your name before clicking button', classes='m-2 block uppercase tracking-wide text-gray-700 text-xs mb-2', a=form1)
                in1 = jp.Input(placeholder='Enter your name', a=form1, classes='form-input m-2 w-56')
                submit_button = jp.Input(value='Click to Borrow', type='submit', a=form1, classes='m-2 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 rounded w-56 text-center')
            else:
                
                submit_button2 = jp.Input(value='Click to Return', type='submit', a=form1, classes='m-2 bg-red-500 hover:bg-red-700 text-white font-bold py-2 rounded w-56 text-center')
            loadcount +=1
            #Transfer index from enumerate to use in submit_form method
            n = i
            form1.on('submit', submit_form)

    if loadcount == 0:
        wp.add(jp.P(text='NO URL!', classes='text-2xl m-2'))
    wp.add(jp.A(text='Book list', href='/', classes='m-2 text-base text-blue-600 underline'))
    return wp

jp.Route('/{code}', bookView)
jp.Route('/', index)
jp.justpy()