


# 1 写函数，找出列表里最短的字符串
def try_found_the_shortest_str_in_list(list1):
    the_shortest_str = list1[0]
    for i in list1:
        if len(i) < len(the_shortest_str):
            the_shortest_str = i
    return the_shortest_str

# 2 写函数，把列表里每个字符串倒过来返回
# def try_backwards_the_str_in_list(list2):         # 修改前版本
#     new_list2 = []
#     for i in list2:
#         i = i[::-1]
#         new_list2.append(i)
#     return new_list2
def try_backwards_the_str_in_list(list2):           # 简化后的版本
    new_list2 = []
    for i in list2:
        new_list2.append(i[::-1])
    return new_list2
# 3 写函数，把列表里大于10的数字找出来，组成一个新列表返回
# def found_num_more_than_10(list3):              # 做了多余的处理，题目已经说了列表中是数字
#     new_list3 = []
#     new_finally_list3= []
#     for i in list3:
#         if i.isdigit():
#             new_list3.append(i)
#     for i in new_list3:
#         if i > 10 :
#             new_finally_list3.append(i)
#     return new_finally_list3
def found_num_more_than_10(list3):
    new_list3 = []
    for i in list3:
        if i > 10:
            new_list3.append(i)
    return new_list3

# 4写函数，把列表里的偶数找出来，组成一个新列表返回
def func_for_find_even_number_in_List(list4):
    new_list4 =[]
    for i in list4:
        if i %2 == 0:
            new_list4.append(i)
    return new_list4

# 5写函数，把列表中每个数字都乘 2，组成一个新列表返回
def func_for_every_num_to_time_two(list5):
    new_list5 = []
    for i in list5:
        i *= 2
        new_list5.append(i)
    return new_list5


# 6写函数，统计列表里有几个大写字母开头的字符串
def func_for_find_capitalize_word_str(list6):
    count6 = 0
    for i in list6:
        if i[0].isupper():
            count6 += 1
    return count6

# 7写函数，删除字符串中所有的空格
def func_for_delete_space_in_str(str7):
    return str7.replace(" ", "")
print(func_for_delete_space_in_str("a b c d"))
# 8写函数，统计一个列表里有几个素数
def is_prime(num):
    if num <2 :
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def func_for_sum_prime_numin_list(list8):
    count8 = 0
    for i in list8:
        if is_prime(i):
            count8 += 1
    return count8
# 9. 写函数，找出列表里最短的字符串长度
def func_to_find_shortest_str_in_list(list9):
    shortest_str = list9[0]
    for i in list9:
        if len(i) < len(shortest_str):
            shortest_str = i
    return len(shortest_str)
# 10. 写函数，把列表里所有大于 10 的数字都乘 2 后返回新列表
def func_to_more_than_10_num_time_2(list10):
    new_list10 = []
    for i in list10:
        if i >10:
            new_list10.append(i*2)
    return new_list10

# 11. 写函数，找出字符串中数字字符的个数
def func_to_find_num_nums_ins_str(str11):
    count11 = 0
    for i in str11:
        if i.isdigit():
            count11 += 1
    return count11
# 12写函数，把列表里所有偶数都乘 3 后返回新列表
def even_num_time3(lst):
    new_lst = []
    for i in lst:
        if i % 2 == 0:
            new_lst.append(i * 3)
    return new_lst
# 13写函数，统计字符串里有几个大写字母
def count_capital_letters(s):
    count = 0
    for i in s:
        if i[0].isupper():
            count += 1
    return count








