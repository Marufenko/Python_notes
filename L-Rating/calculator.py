import openpyxl
import xlsxwriter

# open xlsx
wb = openpyxl.load_workbook(filename = 'data.xlsx')
sheet = wb['Sheet1']

# read IDs
ids = []
for i in range(2,1001):
    ids.append(sheet['A' + str(i)].value)

# read market value
mv = []
for i in range(2,1001):
    mv.append(sheet['B' + str(i)].value)

# read lending value
lv = []
for i in range(2,1001):
    lv.append(sheet['C' + str(i)].value)

# read TOT_EXP value
tot_exp = []
for i in range(2,1001):
    tot_exp.append(sheet['D' + str(i)].value)

# calculate LV_RATIO
lv_ratio=[]
for i in range(999):
    if lv[i] < tot_exp[i]:
        lv_ratio.append(lv[i]/mv[i])
    else:
        lv_ratio.append(tot_exp[i]/mv[i])

# Create an new Excel file and add a worksheet for results
workbook = xlsxwriter.Workbook('result.xlsx')
worksheet = workbook.add_worksheet()
worksheet.set_column('A:A', 15)
worksheet.set_column('B:B', 15)

# write a results
worksheet.write(0, 0, 'PORTFOLIO_ID')
worksheet.write(0, 1, 'LV_RATIO')
for i in range(999):
    worksheet.write(i+1, 0, ids[i])
    worksheet.write(i+1, 1, lv_ratio[i])