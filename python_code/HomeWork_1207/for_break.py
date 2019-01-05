# -*-coding:utf-8-*-
# @Time       :2018/12/21 6:17
# @Autor      :DA BAI CAI
# @Email      :icewong401@163.com
# @File       :for_break.py
# @Software   :PyCharm
l=['for,','w','for','y','any']
for i in l:
    print("xunhuanlimiande dongxi ",i)
    if i == 'for':
        print("找到啦{}！".format(i))
        break

print("-_--------------------------------------")
l=['w','y','for']
for i in l:
    print("xunhuanlimiande dongxi ",i)
    if i == 'for':
        print("找到啦{}！".format(i))
    break
