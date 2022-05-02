import csv
import pandas as pd
import justpy as jp



def readcsv(filename):
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        return data

def writecsv(filename,data):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

def main():
    search_string = "BOOK2"   
    data = readcsv('library.csv')

    print(data)

    for i, (code,title,status,who,since) in enumerate(data):
        if title == search_string:
            data[i][1] = 'Available'
            data[i][2] = '-'
            data[i][3] = '-'


    extracted_list = [list for lis in data for list in lis if search_string in lis]
    print(extracted_list)
    # print('BOOK2' in [j for i in data for j in i]) #Check if 'BOOK2' is in the list

    writecsv('library_out.csv',data)
    return data
# main()
data = main()

# def home():
#     wp = jp.WebPage()
#     wp.add(jp.P(text='ANCA Library', classes='text-lg m-4'))
#     wp.add(jp.P(text='Book Title: ', classes='text-base m-4'))

#     for i in data:
#         wp.add(jp.P(text=data[i][:]))

#     return wp

# jp.justpy(home)