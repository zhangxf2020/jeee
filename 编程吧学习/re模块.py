import re
str2 = r'eva egon yuan'
print(re.findall('a',str2))#>>['a', 'a'] 返回所有满足匹配条件的结果,放在列表里
print(re.search('a|eg', str2).group())#得到匹配的字符串,如果没有,则返回None,加上group只返回第一个查到的结果
print(re.match('e', str2).group())#同上,只不过从字符串开头匹配
print(re.split('[ab]', 'abcd'))# 先按'a'分割得到''和'bcd',在对''和'bcd'分别按'b'分割
print(re.sub('\d', 'H', 'eva3egon4yuan5',4))#将数字替换为'H',参数表示替换几次
