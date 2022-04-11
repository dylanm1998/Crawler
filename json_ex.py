import json

# books = [{'title': '钢铁是怎样炼成的', 'price': 9.8}, {'titie': '红楼梦', 'price': 9.9}]
# json_str = json.dumps(books, ensure_ascii=False)
# print(json_str)

# dumps& dump
books = [
    {'title': '钢铁是怎样炼成的',
     'price': 9.8
     },
    {'titie': '红楼梦',
     'price': 9.9
     }
]
result = json.dumps(books, ensure_ascii=False)
print(result)
print(type(result))

fp = open("books.json",'w',encoding='utf-8')
json.dump(books,fp,ensure_ascii=False)
fp.close()

# loads& load
json_str = '[{"title": "钢铁是怎样炼成的", "price": 9.8}, {"titie": "红楼梦", "price": 9.9}]'

print(type(json_str))
result = json.loads(json_str)
print(result)
print(type(result))

with open("books.json",'r',encoding='utf-8') as fp:
    result = json.load(fp)
    print(result)
    print(type(result))


# Python object -> JSON string -> Python object