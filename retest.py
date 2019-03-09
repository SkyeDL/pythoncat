


# 需求：处理邮箱地址
# 126——> chenyuannjau@126.com  #小写字母+数字
# org|edu|net——>




# 标记——>@符号——>以该符号为分界线
# @前面的部分——>@符号——>163/126——>.点号——>com

import re
# 最重要的一步：根据刚才的分析——>规则——>满足规则的保留，不满足的过滤掉
reg_str = "[a-zA-Z0-9]+@[a-zA-Z0-9]+\.(com|org|edu|net)"    # 一次或者多次  元字符.——>具有特殊含义,需要使用转义字符（\n)
reg = re.compile(reg_str)   # 目的是什么？
# 要处理的字符串是什么？
a_str = 'chenyuan1128927@126_.com'
a_match = re.match(reg, a_str)   # 如果匹配成功
if a_match:
    print(a_match.group())
else:
    print("没有匹配上")




