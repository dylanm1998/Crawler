import re

# Grouping
text = "apple price is $99, orange price is $88"
result = re.search('.+(\$\d+).+(\$\d+)',text)
print(result.group(0),result.group(1),result.group(2))
# group()/group(0): match the entire groups
# group(1): match first group
# group(2): match second group
# groups(): get all groups

# findall: Find all that meet the conditions.
text = "apple price is $99, orange price is $88"
result = re.findall(r'\$\d+',text)
print(result)

# sub: Replace other strings according to rules
text = "hello china, hello world"
# new_text = text.replace(" ","\n")
new_text = re.sub(r' |,','\n',text)
print(new_text)
html = """
<div class="job-detail">
    <p>1. 3年以上相关开发经验 ，全日制统招本科以上学历</p>
    <p>2. 精通一门或多门开发语言(Python,C,Java等)，其中至少有一门有3年以上使用经验</p>
    <p>3. 熟练使用ES/mysql/mongodb/redis等数据库；</p>
    <p>4. 熟练使用django、tornado等web框架，具备独立开发 Python/Java 后端开发经验；</p>
    <p>5. 熟悉 Linux / Unix 操作系统&nbsp;</p>
    <p>6. 熟悉 TCP/IP，http等网络协议</p>
    <p>福利：</p>
    <p>1、入职购买六险一金（一档医疗+公司全额购买商业险）+开门红+全额年终奖（1年13薪，一般会比一个月高）</p>
    <p>2、入职满一年有2次调薪调级机会</p>
    <p>3、项目稳定、团队稳定性高，团队氛围非常好（汇合员工占招行总员工比例接近50%）；</p>
    <p>4、有机会转为招商银行内部员工；</p>
    <p>5、团队每月有自己的活动经费，法定节假日放假安排；</p>
    <p>6、办公环境优良，加班有加班费（全额工资为计算基数，加班不超过晚上10点，平日加班为时薪1.5倍，周末加班为日薪2倍，周末加班也可优先选择调休，管理人性化）。</p>
</div>
"""
new_html = re.sub(r'<.+?>',"",html)
print(new_html)
# split: Split strings according to rules
text = "hello china,hello world"
result = re.split(r' |,',text)
print(result)

# compile: Compile regular expression
text = "apple price is 34.56"
r = re.compile(r"""
\d+ # integer part
\.? # decimal point
\d* # decimal part
""",re.VERBOSE)

result = re.search(r"""
\d+ # integer part
\.? # decimal point
\d* # decimal part
""",text,re.VERBOSE)
#result = re.search(r,text)
print(result.group())