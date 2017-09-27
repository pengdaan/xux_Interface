# -*- coding: utf-8 -*-
__author__ = 'leo'

#后台登录
adminName=['name,username','admin']     #账号输入框
adminPwd=['name,password','admin1234'] #密码密码输入框
login_submit=('class_name,button')      #登录按钮

#登录成功后起始页面
headerframe=('id,header-frame')         #头部iframe
Personal_center=("xpath,//*[@id='submenu-div']/ul/li[2]/a") #个人中心设置

#后台左侧菜单页面
menu_frame=('name,menu-frame')
List_goods=("xpath,//*[@id='menu-ul']/li[2]/ul/li[1]/a")   #商品列表

#后台右侧内容页
main_frame=('id,main-frame')

#商品列表页查询
classification=('s,a.textbox-icon.combo-arrow')
Gcontent=('id,_easyui_combobox_i2_63')
Buttion=("xpath,//input[@value=' 搜索 ']")
Good_Title=("xpath,//*[@id='listDiv']/table[1]/tbody/tr[3]/td[3]/span")
