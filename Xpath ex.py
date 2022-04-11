# # method 1
# from lxml import etree
# text ='''
# <div>
#     <ul>
#           <li class="item-0"><a href="link1.html">first item</a></li>
#           <li class="item-1"><a href="link2.html">second item</a></li>
#           <li class="item-inactive"><a href="link3.html">third item</a></li>
#           <li class="item-1"><a href="link4.html">fourth item</a></li>
#           <li class="item-0"><a href="link5.html">fifth item</a></li>
#     </ul>
# </div>
# '''
# # Parse string to html file
# html = etree.HTML(text)
# #print(html)
# result = etree.tostring(html) .decode('utf-8')
# print(result)

# method 2
# from lxml import etree
# html = etree.parse('hello.html')
# result = etree.tostring(html,pretty_print=True).decode('utf-8')
# print(result)

from lxml import etree
html = etree.parse('hello.html')
# Get all li tags:
# result = html.xpath('//li')
# print(result)
# for i in result:
#     print(etree.tostring(i).decode('utf-8'))

# Get the value of all class attributes under all li elements:
# result = html.xpath('//li/@class')
# print(result)

# Get the a tag whose href is www.baidu.com under the li tag:
# result = html.xpath('//li/a[@href="www.baidu.com"]')
# print(result)

# Get all span tags under the li tag:
# result = html.xpath('//li//span')
# print(result)
# for i in result:
#     print(etree.tostring(i))

# Get all the classes in the a tag under the li tag
# result = html.xpath('//li/a//@class')
# print(result)

# Get the value corresponding to the href attribute of the last li
result = html.xpath('//li[last()]/a/@href')
print(result)

# Get the content of the penultimate(second last) li element
# result = html.xpath('//li[last()-1]/a')
# print(result)
# print(result[0].text)

# The second way to get the content of the penultimate li element
result = html.xpath('//li[last()-1]/a/text()')
print(result)