import xlrd

libro = xlrd.open_workbook('m.xlsx')
hoja = libro.sheet_by_index(0)


for i in range(2):
    for j in range(2):
        print(hoja.cell_value(i,j), end='t')
    print ('')