import csv

# with open("stock.csv",'r',encoding='gbk') as fp:
#     reader = csv.reader(fp)
#     for x in reader:
#         print(x[3])

# with open("stock.csv",'r',encoding='gbk') as fp:
#     reader = csv.DictReader(fp)
#     for x in reader:
#         print(x['secShortName'])

headers = ['name','age','height']
# students = [
#     ('张三',18,'180'),
#     ('李四',19,'185'),
#     ('王五',20,'190')]
# with open('students.csv','w',encoding='utf-8',newline='')as fp:
#     writer = csv.writer(fp)
#     writer.writerow(headers)
#     writer.writerows(students)

students = [
    {"name": "张三","age":18,"height":180},
    {"name": "李四","age":19,"height":185},
    {"name": "王五","age":20,"height":190}]

with open('students.csv','w',encoding='utf-8',newline='')as fp:
    writer = csv.DictWriter(fp,headers)
    # Although there is a header when dictwriter is created, if you want to write data in, you still need to call the writer.writeheader() method, otherwise, the header data will not be written in.
    writer.writeheader()
    writer.writerows(students)

# headers = ['name','age','classroom']
# values = [{"name":'wena',"age":20,"classroom":'222'},{"name":'abc',"age":30,"classsroom":'333'}]
# with open('test.csv','w',newline='')as fp:
#     writer = csv.DictWriter(fp,headers)
#     writer = csv.writeheader()
#     writer.writerow({'name':'zhiliao',"age":18,"classroom":'111'})
#     writer.writerows(values)