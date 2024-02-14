import string
import random

length=int(input("enter the length of password: "))

lower=string.ascii_lowercase
upper=string.ascii_uppercase
num=string.digits
symbols=string.punctuation

all=lower + upper + num + symbols

temp=random.sample(all,length)

password="".join(temp)

print("Password:" ,password)

