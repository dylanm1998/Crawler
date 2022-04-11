import xlrd

workbook = xlrd.open_workbook("成绩表.xlsx")

# # Get all sheet name:
# print(workbook.sheet_names())
#
# # Get the specified sheet object according to the index
# sheet = workbook.sheet_by_index(1)
# print(sheet.name)
#
# # Get the specified sheet object according to the name
# sheet = workbook.sheet_by_name("2班")
# print(sheet.name)
#
# # Get all sheet objects
# sheets = workbook.sheets()
# for sheet in sheets:
#     print(sheet.name)
#
# # Get the specified sheet rows and columns
# sheet = workbook.sheet_by_index(0)
# print({"rows":sheet.nrows,"cols":sheet.ncols})

###################################################
from xlrd.sheet import Cell
# sheet = workbook.sheet_by_index(0)
# cell = sheet.cell(1,1)
# print(type(cell))
#
# cells = sheet.row_slice(1,1,4)
# for cell in cells:
#     print(cell.value)

# cells = sheet.col_slice(0,1,sheet.nrows)
# for cell in cells:
#     print(cell.value)

# cell_value = sheet.cell_value(0,1)
# print(cell_value)
#
# cell_values = sheet.col_values(1,1,sheet.nrows)
# print(cell_values)
#
# cell_values = sheet.row_values(1,1,sheet.ncols)
# print(cell_values)

#####################################################
sheet = workbook.sheet_by_index(0)
cell = sheet.cell(0,0)
print(cell.ctype)
print(xlrd.XL_CELL_TEXT)

cell = sheet.cell(1,1)
print(cell.ctype)
print(xlrd.XL_CELL_NUMBER)

cell = sheet.cell(19,0)
print(cell.ctype)
print(xlrd.XL_CELL_DATE)

cell = sheet.cell(20,0)
print(cell.ctype)
print(xlrd.XL_CELL_BOOLEAN)

cell = sheet.cell(19,1)
print(cell.ctype)
print(xlrd.XL_CELL_EMPTY)