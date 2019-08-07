
#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
time: 2018.11.11
author: pqx
email:369030340@qq.com
"""
import re
import pyautogui
import smtplib
import datetime
from time import sleep
from  selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from email.mime.text import MIMEText

def Open(url):#打开浏览器 关闭更新 进入指定地址
    # ffpro=r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\rxgmslh7.default'
    # profile=webdriver.FirefoxProfile(ffpro)#文件夹 加载这个文件夹不更新浏览器
    # b=webdriver.Firefox(profile)#浏览器
    b=webdriver.Chrome()
    b.implicitly_wait(10)#隐式等待10秒  如果10秒之内完成则不等待进入下一步 如果10秒以后则进入下一步
    b.maximize_window()#最大化窗口
    sleep(1)
    b.get(url)
    return b  #返回b

def login(b,name,pwd):#登录
    b.find_element_by_class_name('login-hd-account').click()#用户密码登录
    b.implicitly_wait(10)
    sleep(1)
    b.find_element_by_id('J-userName').clear()
    b.find_element_by_id('J-userName').send_keys(name)#姓名
    b.find_element_by_id("J-password").clear()
    b.find_element_by_id("J-password").send_keys(pwd)  # 密码
    sleep(10)  # 验证码要手动
    b.find_element_by_id("J-login").click()  # 不用自己点登录
    b.implicitly_wait(10)
    sleep(2)
    while 1:#设置一个死循环 如果验证失败则重新登录
        try:
            personage_login = b.find_element_by_xpath('//*[@id="gerenzhongxin"]/h2/a')
            if personage_login.text=='个人中心':
                break#登录成功则跳出死循环
        except:
            login(b,name,pwd)

def check_tickets(b,fromStation,toStation,train_date,departure_time,train_type,set_type_list):#查票筛选
    b.implicitly_wait(10)
    sleep(3)
    e=b.find_element_by_link_text('车票')
    ActionChains(b).move_to_element(e).perform()#悬停在车票上显示下拉框
    sleep(1)
    b.implicitly_wait(10)
    b.find_element_by_link_text('单程').click()#这里选择的是单程
    b.implicitly_wait(10)
    sleep(1)

    js = 'document.getElementById("train_date").removeAttribute("readonly")'
    b.execute_script(js)
    b.find_element_by_id("train_date").clear()
    b.find_element_by_id("train_date").send_keys(train_date)#日历元素处理
    sleep(1)
    pyautogui.moveTo(764,347)
    pyautogui.click(764, 347)#日历框里面点一下 这几个 pyautogui 要根据不同的电脑、浏览器像素自己定位
    pyautogui.moveTo(21,361)
    pyautogui.click(21,361)#空白地方点一下 消掉日历弹出窗
    sleep(1)

    b.find_element_by_id('fromStationText').clear()
    b.find_element_by_id('fromStationText').send_keys(fromStation)  # 出发车站
    pyautogui.moveTo(275, 410)
    pyautogui.click(275, 410)  # 这里选的是第一个
    sleep(1)
    b.find_element_by_id('toStationText').clear()
    b.find_element_by_id('toStationText').send_keys(toStation)  # 到达车站
    pyautogui.moveTo(504, 410)
    pyautogui.click(504, 410)  # 这里选的是第一个
    sleep(1)


    b.find_element_by_xpath('//*[@id="auto_query"]').click()  # 自助查询
    s1 = Select(b.find_element_by_id('cc_start_time'))  # 实例化Select
    s1.select_by_visible_text(departure_time)    #发车时间 #00:00--24:00 00:00--06:00 06:00--12:00 12:00--18:00 18:00--24:00
    b.find_element_by_id('sf1_label').click()#普通 学生
    # b.find_element_by_xpath('//*[@id="checkbox_8KcrDAF3Vr"]').click()K
    # li[1] GC-高铁/城际  li[2] D-动车 li[3] Z-直达 li[4] T-特快 li[5] K-快速 li[6] 其他
    b.find_element_by_xpath('//*[@id="_ul_station_train_code"]/li[{}]/input'.format(train_type)).click()#这里选的是快速
    # p=b.find_element_by_xpath('//*[@id="_ul_station_train_code"]/li[5]/label').text
    # print(p)

    a=0
    while 1:#这里也写了一个死循环 反复查询
        try:
            b.find_element_by_link_text('查询').click()#点击查询
        except:
            b.find_element_by_link_text('停止查询').click()#重复查询时先点下停止
            sleep(1)
            b.find_element_by_link_text('查询').click()#再点查询
        b.implicitly_wait(10)
        ceci=b.find_elements_by_xpath('// *[ @ id = "queryLeftTable"]/tr[*]/td[1]/div/div[1]/div/a')#所有车次
        # print(p)
        # print('特座  一座  二座  高软  软卧  动卧  硬卧  软座  硬座  无座  其他  车次')
        x = 1
        for i in range(len(ceci)):
            dr =b.find_element_by_xpath('// *[ @ id = "queryLeftTable"]/tr[{}]'.format(x))#车次ID 标签
            ceci_id=dr.get_attribute('id').split('_')[1]#切片出车次id
            # print(ceci_id)
            x+=2#每次加2
            zuowei_list=[set_type_list]#座位类型  # zuowei_list=[['特座','TZ_'],['一座','ZY_',],['二座','ZE_'],['高软','GR_'],['软卧','RW_'],['动卧','SRRB_'],['硬卧','YW_'],['软座','RZ_'],['硬座','YZ_'],['无座','WZ_'],['其他','QT_']]
            for j in zuowei_list:
                f = b.find_element_by_xpath('//*[@id="float"]')#先滚动到车次列表标题
                b.execute_script("arguments[0].scrollIntoView();", f)
                zuoweixinxi=dr.find_element_by_xpath('//*[@id="{}{}"]'.format(j[1],ceci_id)).text#车次座位信息
                if zuoweixinxi!='无' and zuoweixinxi!='--'and zuoweixinxi!='':
                    print('座位类型：{}，余票：{}，车次：{}'.format(j[0], zuoweixinxi, ceci[i].text))
                    b.find_element_by_xpath('//*[@id="ticket_{}"]/td[13]/a'.format(ceci_id)).click()#找车次对应的预定链接
                    sleep(1)         #'//*[@id="ticket_650000K4460I"]/td[13]/a'
                    b.implicitly_wait(10)
                    a=1
                    break#跳出座位循环
            if a==1:
                break#跳出车次循环
        if a==1:
            break#跳出死循环

def reserve(b,people,seat):#预订
    peoples=b.find_elements_by_xpath('//*[@id="normal_passenger_id"]/li[*]/label')#找已经存在的乘客列表
    # // *[ @ id = "normalPassenger_0"] #     // *[ @ id = "normal_passenger_id"] / li[1] / label
    #     // *[ @ id = "normalPassenger_1"] #     // *[ @ id = "normal_passenger_id"] / li[2] / label
    #     // *[ @ id = "normalPassenger_2"]  #     // *[ @ id = "normal_passenger_id"] / li[3] / label
    for i in range(len(peoples)):
        if peoples[i].text==people:
            b.find_element_by_xpath('// *[ @ id = "normalPassenger_{}"]'.format(i)).click()#勾选乘客
            sleep(1)
            b.implicitly_wait(10)
    seats=b.find_element_by_xpath('//*[@id="ticket_con_id"]')#座位类型及票价
    ll=seats.text.split(' ')#切片形成列表
    for j in ll:
        if seat in j:
            seat_type='%s）'%j.split('）')[0]#座位类型票价 # print(seat,'%s）'%j.split('）')[0])
            s2 = Select(b.find_element_by_id("seatType_1"))  # 实例化Select
            s2.select_by_visible_text(seat_type)  # 选择座位类型
            sleep(1)
            b.implicitly_wait(10)
    b.find_element_by_id('submitOrder_id').click()#提交订单
    b.implicitly_wait(10)
    sleep(3)
    b.implicitly_wait(10)
    e=b.find_element_by_xpath('//*[@id="body_id"]/div[24]').text
    print(e)
    sleep(3)
    b.implicitly_wait(10)
    b.find_element_by_xpath('//*[@id="qr_submit_id"]').click()#确认订单
    sleep(5)
    b.implicitly_wait(10)
    print('预定完成请前往支付')
    b.close()
    b.quit()
    return  e

def send_mail(sender_mail,sender_pwd,receiver_address, content):
    """发送邮件通知"""
    # 连接邮箱服务器信息
    host = 'smtp.163.com'
    port = 25
    # 发件信息
    receiver = receiver_address
    body = '<h2>温馨提醒：</h2><p>' + content + '</p>'
    msg = MIMEText(body, 'html', _charset="utf-8")
    msg['subject'] = '抢票成功通知！'
    msg['from'] = sender_mail
    msg['to'] = receiver
    s = smtplib.SMTP(host, port)
    # 开始登陆邮箱，并发送邮件
    s.login(sender_mail, sender_pwd)
    s.sendmail(sender_mail, receiver, msg.as_string())

def main():
    # name, pwd, fromStation, toStation, train_date, departure_time, train_type, set_type_list, people, seat, sender_mail, sender_pwd, receiver_address
    #12306用户名，密码，出发站点，到达站点，出发日期，    出发时间，     列车类型，   座位列表  ，预订人    座位类型，发件人，    发件人密码，   收件人
    name = input('请输入12306账号：')
    while name == '':
        name = '88888888'  # 12306用户名，
        print('不做输入将使用默认用户名%s' % name)
    # print('12306账号：%s' % name)
    pwd = input('请输入12306密码：')
    while pwd == '':
        pwd = '88888888'  # 12306密码
        print('不做输入使用默认密码%s' % pwd)
    # print('12306密码：%s' % pwd)

    fromStation = input('请输入出发站点：')
    while fromStation == '':
        fromStation = '深圳'  # 出发站点
        print('不做输入使用默认起始站点：%s' % fromStation)
    # print('出发站点：%s' % fromStation)
    toStation = input('请输入目的站点：')
    while toStation == '':
        toStation = '吉安'  # 到达站点
        print('不做输入使用默认终点%s' % toStation)
    # print('目的站点：%s' % toStation)
    train_date = input('请输入出发日期(格式：2018-02-02)：')
    date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
    while train_date == '' or re.findall(date_pattern, train_date) == []:
        today = datetime.date.today()
        oneweek = datetime.timedelta(days=7)
        nextweekday = today + oneweek
        train_date = nextweekday.strftime('%Y-%m-%d')  # 出发日期
        print('不做输入使用默认7天后日期:%s' % train_date)
    # print('出发日期：%s' % train_date)
    departures_time = {'': '06:00--12:00',
                       '1': '00:00--24:00',
                       '2': '00:00--06:00',
                       '3': '06:00--12:00',
                       '4': '12:00--18:00',
                       '5': '18:00--24:00'}
    departure_time_choice = str(
        input('请选择发车时间：1： 00:00--24:00 2： 00:00--06:00 3： 06:00--12:00 4： 12:00--18:00 5: 18:00--24:00'))

    departure_time = departures_time[departure_time_choice]
    while departure_time_choice == '':
        departure_time_choice = '3'
        departure_time = departures_time[departure_time_choice]#发车时间
        print('不做输入将使用默认发车时间:%s' % departure_time)
    # print('发车时间：%s'%departure_time)
    trains_type = {
        '1': 'GC-高铁/城际', '2': 'D-动车', '3': 'Z-直达', '4': 'T-特快', '5': 'K-快速', '6': '其他'
    }
    train_type = str(input('请选择发车类型：1:GC-高铁/城际,2:D-动车,3:Z-直达,4:T-特快,5:K-快速,6:其他'))
    while train_type == '':
        train_type = '5'
        print('不做输入将使用默认发车类型:%s' % trains_type[train_type])
    # print('发车类型：%s' % trains_type[train_type])
    zuowei_list = {'1': ['特座', 'TZ_'], '2': ['一座', 'ZY_', ],
                   '3': ['二座', 'ZE_'], '4': ['高软', 'GR_'],
                   '5': ['软卧', 'RW_'], '6': ['动卧', 'SRRB_'],
                   '7': ['硬卧', 'YW_'], '8': ['软座', 'RZ_'],
                   '9': ['硬座', 'YZ_'], '10': ['无座', 'WZ_'],
                   '11': ['其他', 'QT_']}
    set_type = str(input('请选择座位类型：1:特座,2:一座,3:二座,4:高软,5:软卧,6:动卧,7:硬卧,8:软座,9:硬座,10:无座,11:其他'))
    while set_type == '':
        set_type = '9'  #9:硬座
        print('不做输入将使用默认座位类型:%s' % zuowei_list[set_type][0])
    # print('座位类型：%s' % zuowei_list[set_type][0])
    set_type_list = zuowei_list[set_type]#座位类型 及简写
    seat = zuowei_list[set_type][0]  # 座位类型
    people = input('请输入乘车人姓名：')
    while people == '':
        people = '彭启轩'  # 预定人
        print('不做输入使用默认姓名:%s' % people)
    # print('乘车人姓名：%s' % people)

    receiver_address = input('请输入收件人邮箱：')
    while receiver_address == '':
        receiver_address = '369030340@qq.com'  # 发件人
        print('不做输入使用默认收件人:%s' % receiver_address)
    # print('收件人邮箱：%s' %receiver_address)
    sender_mail = input('请输入发件人邮箱：')
    while sender_mail == '':
        sender_mail = '18218412817@163.com'  # 你的发件邮箱号码
        print('不做输入使用默认发件人:%s' % sender_mail)
    # print('发件人邮箱：%s' % receiver_address)
    sender_pwd = input('请输入发件人密码：')
    while sender_pwd == '':
        sender_pwd = '88888888'  # 不是登陆密码，是客户端授权密码
        print('不做输入使用默认发件人密码：%s' % sender_pwd)
    # print('发件人密码：%s' % receiver_address)


    login_url = 'https://kyfw.12306.cn/otn/resources/login.html'
    b=Open(login_url)
    login(b,name,pwd)#登录  12306用户名，密码
    check_tickets(b,fromStation,toStation,train_date,departure_time,train_type,set_type_list)#查票 出发站点，到达站点，出发日期
    send_mail(sender_mail,sender_pwd,receiver_address, reserve(b,people,seat))#发邮件（ 发件人，发件人密码，收件人订票（预定人，座位类型））

if __name__ == '__main__':
    main()

