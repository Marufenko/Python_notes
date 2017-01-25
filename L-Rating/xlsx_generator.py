import xlsxwriter
import random

# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('data.xlsx')
worksheet = workbook.add_worksheet()

# Generate Market Value
worksheet.set_column('A:A', 15)       # prepare column
worksheet.write(0, 0, 'PORTFOLIO_ID') # write column title
for i in range(1, 1000):
    worksheet.write(i, 0, 'BRL731' + str(i+1000))          # generate and write ID values

# Generate Market Value
worksheet.set_column('B:B', 15)       # prepare column
worksheet.write(0, 1, 'MARKET_VALUE') # write column title
for i in range(1, 1000):
    a = random.uniform(1,1000000)     # generate random values
    worksheet.write(i, 1, a)          # write random values

# Generate Lending Value
worksheet.set_column('C:C', 15)        # prepare column
worksheet.write(0, 2, 'LENDING_VALUE') # write column title
for i in range(1, 1000):
    a = random.uniform(1,1000000)      # generate random values
    b = random.uniform(1,1000)
    worksheet.write(i, 2, a-b)         # write random values

# Generate TOT_EXP
worksheet.set_column('D:D', 15)        # prepare column
worksheet.write(0, 3, 'TOT_EXP') # write column title
for i in range(1, 1000):
    a = random.uniform(1,1000000)      # generate random values
    worksheet.write(i, 3, a)         # write random values