#每个字符串，不夹杂空格或者特殊符号，默认开启intern机制，会自动放入字符串池中，
#如果字符串池中存在，则直接引用，否则放入池中
str1 = 'hello'
str2 = 'hello'
print(str1 is str2) #True
print(id(str1) == id(str2)) #True