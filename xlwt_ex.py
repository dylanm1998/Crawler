import random
import xlwt

workbook = xlwt.Workbook()
sheet = workbook.add_sheet("sheet1")
headers = ['姓名','语文','数学','英语']
for index,header in enumerate(headers):
    sheet.write(0,index,header)

names = ['张三','李四','王五']
for index,name in enumerate(names):
    sheet.write(index+1,0,name)

for row in range(1,4):
    for col in range(1,4):
        sheet.write(row,col,random.randint(0,100))

workbook.save("成绩表1.xls")