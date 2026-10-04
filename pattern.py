import re

pattern = r"^(?:\+91)?[6-9][0-9]{9}$"
num = input("Enter the num")

if re.fullmatch(pattern, num):
    print("num is valid")
else:
    print("number is invalid")