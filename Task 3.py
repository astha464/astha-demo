import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbol = "@_!#$%^&*()/?."
string = lower + upper + symbol + numbers
length = 8
password = "".join(random.sample(string,length))
print("Your genereated password is :"+password)
