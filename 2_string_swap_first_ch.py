str1 = "hello"
str2 = "world"
if len(str1) >= 2 and len(str2) >= 2:
    new_str1 = str1[0] + str2[1] + str1[2:]
    new_str2 = str2[0] + str1[1] + str2[2:]
else:
    new_str1 = str1
    new_str2 = str2
result = new_str1 + " " + new_str2
print(result)
