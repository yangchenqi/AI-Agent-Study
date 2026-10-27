# float类型:是有精度损失的，如果存在精度问题，可以使用decimal模块
num1=0.1;
num2=0.2;
print(num1+num2) # 0.30000000000000004  精度损失
 

from decimal import Decimal
print(Decimal('0.1')+Decimal('0.2')) # 0.3

# bool类型:True和False,true为1,false为0
# 所有的true都是同一个对象，所有的false都是同一个对象

print(1>2) # False
print(1<2) # True
 
b1 = True
b2=True
print(b1==b2) # True比较值
print(b1 is b2) # True比较内存地址

# false:0,空字符串,空列表,空字典,空元组,空集合，None
print(bool(0)) # False
print(bool('')) # False
print(bool([])) # False
print(bool({})) # False
print(bool(())) # False
print(bool(set())) # False
print(bool(None)) # False

# str类型:字符串类型
# 任何被单引号或双引号包裹的内容都是字符串
str1='hello'
str2="hello"
str3='''hello'''
str4="""hello"""  # 三引号可以换行
print(str1,str2,str3,str4) # hello hello hello hello

print('hello'+'world') # helloworld  字符串的拼接
print('hello'*3) # hellohellohello 字符串的重复

