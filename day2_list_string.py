

# 1 求列表中最小值
test_list= [8,3,15,2,9]
min_num = test_list[0]
for i in test_list:
    if min_num >i :
        min_num = i
print(min_num)

# 2计算列表中所有元素的和
test_list2 = [1,2,3,4,5]
count2 = 0
for i in test_list2:
    count2 += i
print(count2)

# 3统计列表中偶数的个数
test_list3 = [1,2,4,7,8,11]
count3 = 0
for i in test_list3:
    if i%2==0:
        count3 += 1
print(count3)

# 4输出1到100能被3整除的数
for i in range(1,101):
    if i%3==0:
        print(i)

# 5判断一个数是不是回文数
num = input("请输入一个数字：")
if num == num[::-1]:
    print("是回文数")
else:
    print("不是回文数")
# 6找出列表中的最大值最小值
test_list6 = [5,12,3,9,21,1]
max_num6 = test_list6[0]
mini_num6 = test_list6[0]
for i in test_list6:
    if i>max_num6:
        max_num6 = i
    if i < mini_num6:
        mini_num6 = i
print(max_num6)
print(mini_num6)
# 7 写函数判断一个数是不是偶数

def is_even(num):
    if num%2==0:
        return True
    else:
        return False


# 8 写函数，返回列表中大于10的数字个数
def confirm_num(list_num):
    count8 = 0
    for i in list_num:
        if i >10:
            count8 += 1
    return count8

# 9写函数，返回列表中最小值
def confirm_mini_num(list_num):
    mini_num9 = list_num[0]
    for i in list_num:
        if i < mini_num9:
            mini_num9 = i
    return mini_num9
# 10写函数，计算列表所有元素之和
def calculate_sum(list_num10):
    count10 = 0
    for i in list_num10:
        count10 += i
    return count10
# 11输入一个数，判断是不是素数
def is_prime(num):
    if num < 2:
        return "不是素数"
    for i in range(2, num):
        if num % i == 0:
            return "不是素数"
    return "是素数"
num11 = int(input("请输入一个数："))
print(is_prime(num11))


# 12函数，返回列表中的最大值
def confirm_list_max_num12(test_list12):
    max_num12 = test_list12[0]
    for i in test_list12:
        if i>max_num12:
            max_num12=i
    return max_num12
# 13写函数，判断一个列表里有几个偶数
def confirm_list_num_is2(test_list13):
    count13 = 0
    for i in test_list13:
        if i%2 == 0:
            count13 += 1
    return count13
# 14写函数，返回 1 到 n 的和
def confirm_list_num_sum14(n):
    sum14 = 0
    for i in range(1,n+1):
        sum14 += i
    return sum14
# 15写函数，统计字符串长度
def cofirm_str_length(str15):
    length15 = len(str15)
    return length15
print(cofirm_str_length("asldfhae"))
# 16写函数，统计字符串里有几个字母 a
def cofirm_str_have_a_numbs(str16):
    have_a_numbs = 0
    for i in str16:
        if i == "a" :
            have_a_numbs += 1
    return have_a_numbs
cofirm_str_have_a_numbs("dasdasdadakjsdu")

# 17写函数，判断字符串是不是回文
def confirm_str_is_huiwen(str17):
    if str17 == str17[::-1]:
        return True
    else:
        return False


# 18写函数，把字符串全部变成大写
def try_capitalize_str(str18):
    return str18.upper()

print(try_capitalize_str("abcde"))
# 19写函数，统计字符串里有几个数字
def confirm_str_numbs(str19):
    count19 = 0
    for i in str19:
        if i.isdigit():
            count19 += 1
    return count19

print(confirm_str_numbs("a1b2c3"))
# 20写函数，把字符串倒过来返回
def str_backwars(str20):
    str20 = str20[::-1]
    return str20
def str_backwars(str20):
    return str20[::-1]


# 21写函数，统计字符串里有几个小写字母
def sum_word_num(str21):
    sum21 = 0
    for i in str21:
        if i.islower():
            sum21 += 1
    return sum21

# 22写函数，把字符串全部变成小写
def try_lower_str(str22):
    str22 = str22.lower()
    return str22
# 23写函数，去掉字符串两边的空格
def str_strip(str23):
    str23 = str23.strip(" ")
    return str23

# 24写函数，统计列表里一共有几个字符串
def confirm_str_in_list(list24):
    count24 = 0
    for i in list24:
        if isinstance(i, str):
            count24 += 1
    return count24
# 25写函数，找出列表里最长的字符串
def confirm_str_in_list25_longest(list25):
    longest =len(list25[0])
    for i in list25:
        if len(i) > longest:
            longest = i
    return longest
# 26写函数，把列表里每个字符串都变成大写


def try_super_str_in_list(list26):
    new_list26 = []
    for i in list26:
        new_list26.append(i.upper())
    return new_list26






