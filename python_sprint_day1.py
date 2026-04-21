# 1. 写函数，统计列表里有几个数字同时满足：1是奇数 2大于 10
def count_numbers(lst):
    count = 0
    for i in lst:
        if i % 2 != 0 and i > 10:
            count += 1
    return count
# 2. 写函数，返回字符串里所有不是大写字母的字符组成的新字符串
def backwards_letters(s):
    new_s = ""
    for i in s:
        if not i.isupper():
            new_s += i
    return new_s
# 3. 写函数，返回列表里所有长度等于 4 的字符串组成的新列表
def backward_len4(lst):
    new_lst = []
    for i in lst:
        if len(i) == 4:
            new_lst.append(i)
    return new_lst
# 4. 写函数，统计字符串里有几个字符同时满足：1是数字字符 2是奇数
def count_odd_digits(s):
    count = 0
    for i in s:
        if i.isdigit() and int(i) % 2 != 0:
            count += 1
    return count
# 5. 写函数：先找出列表里所有小于 20 的偶数，再把它们加 5，最后返回新列表
def find_even_numbers(lst):
    new_lst = []
    for i in lst:
        if i % 2 ==0 and i < 20 :
            new_lst.append(i+5)
    return new_lst
# 6. 写函数：找出字符串里所有小写字母，把它们按原顺序组成新字符串，再全部变成大写返回
def find_lowercase_to_capitalize(s):
    new_s = ""
    for i in s:
        if i.islower():
            new_s += i.upper()
    return new_s

# 7. 写函数：统计一个列表里有几个字符串同时满足：1是回文字符串 2全部是小写字母
def count_palindrome_lower(lst):
    count = 0
    for i in lst:
        if i == i[::-1] and i.islower():
            count += 1
    return count
# 8. 写一个简单程序，不一定非要写成函数，也可以先直接写：
def analyze_string(s):
    digit_count = 0
    lower_count = 0
    upper_count = 0
    space_count = 0

    for i in s:
        if i.isdigit():
            digit_count += 1
        elif i.islower():
            lower_count += 1
        elif i.isupper():
            upper_count += 1
        elif i == " ":
            space_count += 1

    return digit_count, lower_count, upper_count, space_count
result = analyze_string("Abc 12 Xy")
print("数字个数:", result[0])
print("小写字母个数:", result[1])
print("大写字母个数:", result[2])
print("空格个数:", result[3])
# 8. 写一个简单程序，不一定非要写成函数，也可以先直接写：
def analyze_string(s):
    digit_count = 0
    lower_count = 0
    upper_count = 0
    space_count = 0

    for i in s:
        if i.isdigit():
            digit_count += 1
        elif i.islower():
            lower_count += 1
        elif i.isupper():
            upper_count += 1
        elif i == " ":
            space_count += 1

    return digit_count, lower_count, upper_count, space_count
result = analyze_string("Abc 12 Xy")
print("数字个数:", result[0])
print("小写字母个数:", result[1])
print("大写字母个数:", result[2])
print("空格个数:", result[3])
# 9写函数，统计列表里有几个字符串同时满足：长度大于 2首字母是小写字母
def count_to_s_len2and_islower(lst):
    count = 0
    for i in lst:
        if len(i) > 2 and i[0].islower():
            count += 1
    return count
# 10写函数，返回字符串里所有不是数字也不是空格的字符组成的新字符串
def backwards_not_num_blank(s):
    new_s = ""
    for i in s:
        if not i.isdigit() and i != " " :
            new_s += i
    return new_s
# 11写函数：先找出列表里所有奇数，再把这些奇数平方，最后返回新列表
def count_odd_num_and_square(lst):
    new_lst = []
    for i in lst:
        if i % 2 != 0 :
            new_lst.append(i**2)
    return new_lst
# 12写函数：统计一个列表里有几个字符串同时满足：
def count_it(lst):
    count = 0
    for i in lst:
        if i.islower() and len(i) == 3 and i.isalpha() :
            count += 1
    return count

# 全部是字母
# 全部是小写字母
# 长度等于 3
