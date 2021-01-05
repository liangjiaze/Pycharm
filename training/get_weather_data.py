import requests
import json
import time
from bs4 import BeautifulSoup
import random
import io
import sys
import pymysql
import datetime
import json
# import cx_Oracle  # 导入包
import psycopg2
import smtplib  # 加载smtplib模块
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import csv

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'way.weatherdt.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

# 获取气象局数据

citys = ['101090303', '101090410', '101090506']

citys_dict = {'101090303': '张北', '101090410': '围场', '101090506': '乐亭'}


def send_mail():
    sender = 'lirui_cd@163.com'  # 发件人邮箱账号
    # receive = ['renmuda@163.com', '32130185@qq.com']  # 收件人邮箱账号
    receive = ['renmuda@163.com']  # 收件人邮箱账号
    # receive = ['32130185@qq.com']  # 收件人邮箱账号
    passwd = 'Lirui123456'
    mailserver = 'smtp.163.com'
    port = '25'

    db = psycopg2.connect(database="jbgf", user="postgres", password="123456", host="127.0.0.1", port="5432")
    cur = db.cursor()
    cur_date = time.strftime("%Y%m%d")
    cur_time = time.strftime("%Y-%m-%d %H:%M:%S")
    print(cur_time)
    sql = "select city_no, max(d000),max(d0001),sum(float(d002)) fz from weather_fz where stat_date = '{0}' group by city_no".format(cur_date)
    cur.execute(sql)
    rows = cur.fetchall()
    sub = cur_time + '辐照数据'
    send_msg = '当前已经收集到:{0},最后发布时间:{1}\n'.format(rows[0][1], rows[0][2])
    for row in rows:
        send_msg = send_msg + row[0] + '({0}):{1}\n'.format(citys_dict[row[0]], int(row[3] * 36 / 100 + 0.5))
    send_msg = send_msg + '\n\n天气数据:\n'
    sql = "select stat_date,city_no,avg(float(d002)),sum(float(d006)) from weather_obverse where stat_date = '{0}' group by city_no,stat_date  order by city_no".format(cur_date)
    cur.execute(sql)
    rows = cur.fetchall()
    # send_msg = send_msg + 'city_no,city_name,father_city,stat_date,max(d002),min(d002),max(d005),min(d005)\n'
    for row in rows:
        send_msg = send_msg + "insert into llys.fc_gc_weather(data_date,station,precipitation,temperature )values('{0}','{1}','{2}','{3}')\n".format(row[0], row[1], row[3], row[2])
    send_msg = send_msg + '\n\n辐照明细:\n'
    sql = "select * from weather_fz where stat_date = '{0}' order by city_no,d000".format(cur_date)
    cur.execute(sql)
    rows = cur.fetchall()
    send_msg = send_msg + 'city_no,d000,d0001,stat_date,d001,d002,d003,d004,d005,d006,d007\n'
    for row in rows:
        send_msg = send_msg + '{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}\n'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])

    try:
        msg = MIMEMultipart('related')
        msg['From'] = formataddr([sender, sender])  # 发件人邮箱昵称、发件人邮箱账号
        # msg['To'] = formataddr(['32130185@qq.com','495219428@qq.com'])  # 收件人邮箱昵称、收件人邮箱账号
        msg['To'] = ','.join(receive)
        msg['Subject'] = sub
        # 文本信息
        txt = MIMEText(send_msg, 'plain', 'utf-8')
        # txt = MIMEText(msg, 'plain')
        msg.attach(txt)

        server = smtplib.SMTP(mailserver, port)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(sender, passwd)  # 发件人邮箱账号、邮箱密码
        server.sendmail(sender, receive, msg.as_string())  # 发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()
        print('success')
    except Exception as e:
        print(e)


def get_fz_data():
    file_path = "E:\spider\log{0}.txt".format(time.strftime("%Y%m%d"))
    file_obj = open(file_path, "a+")
    db = psycopg2.connect(database="jbgf", user="postgres", password="123456", host="127.0.0.1", port="5432")
    cur = db.cursor()
    battch_no = ''
    flag = 0
    for city in citys:
        response = None
        while response == None:
            try:
                response = requests.get(
                    'http://way.weatherdt.com/apimall/basic/grid.htm?station={0}&type=raid1h&key=da501d6a4e89eb65365149f15183d537'
                        .format(city), headers=headers)
            except:
                print("net work connect failed, wait 10 second and connect again")
                time.sleep(10)
        # print(response.json())
        r_json = response.json();
        # r_json = json.loads(response.json());
        # print(r_json['result']['raid1h'][city][0])
        cur.execute("select * from weather_fz where city_no = '{0}' and d0001 = '{1}'"
                    .format(city, r_json['result']['raid1h'][city][0]['0001']))
        rows = cur.fetchall()
        if (len(rows) == 0):
            sql = '''insert into weather_fz(city_no,d000,d0001,stat_date,d001,d002,d003,d004,d005,d006,d007)
                                  values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}')''' \
                .format(city,
                        r_json['result'][
                            'raid1h'][
                            city][0][
                            '000'] \
                        ,
                        r_json['result'][
                            'raid1h'][
                            city][
                            0][
                            '0001'],
                        r_json['result'][
                            'raid1h'][
                            city][0][
                            '000'][0:8],
                        r_json['result'][
                            'raid1h'][
                            city][
                            0][
                            '001'] \
                        ,
                        r_json['result'][
                            'raid1h'][
                            city][
                            0][
                            '002'],
                        r_json['result'][
                            'raid1h'][
                            city][
                            0][
                            '003'],
                        r_json['result'][
                            'raid1h'][
                            city][
                            0][
                            '004'] \
                        ,
                        r_json['result'][
                            'raid1h'][
                            city][
                            0][
                            '005'],
                        r_json['result'][
                            'raid1h'][
                            city][
                            0][
                            '006'],
                        r_json['result'][
                            'raid1h'][
                            city][
                            0][
                            '007'])
            cur.execute(sql);
            cur.execute('commit');
            log = time.strftime("%H:%M:%S") + ' | insert [{0},{1}] success' \
                .format(city, r_json['result']['raid1h'][city][0]['000'])
            print(log)
            file_obj.writelines(log + '\n')
            flag = 1
        else:
            log = time.strftime("%H:%M:%S") + ' | data [{0},{1}] has been inserted' \
                .format(city,
                        r_json['result']['raid1h'][
                            city][0]['000'])
            print(log)
            file_obj.writelines(log + '\n')
        battch_no = r_json['result']['raid1h'][city][0]['000']
    cur.close()
    db.close()
    file_obj.close()
    cur_date = time.strftime("%Y%m%d")
    if ((battch_no == cur_date + '16' or battch_no == cur_date + '17' or battch_no == cur_date + '18') and flag == 1):
        send_mail()


def get_weather_data():
    cur_date = time.strftime("%Y%m%d")
    file_path = "E:\spider\log{0}.txt".format(time.strftime("%Y%m%d"))
    file_obj = open(file_path, "a+")
    city_dict = {}
    with open('E:\spider\city_list.csv', 'r') as f:  # 采用b的方式处理可以省去很多问题
        reader = csv.reader(f)
        for row in reader:
            city_dict[row[0]] = [row[0], row[2], row[3]]

    db = psycopg2.connect(database="jbgf", user="postgres", password="123456", host="127.0.0.1", port="5432")
    cur = db.cursor()
    i = 0
    citystr = ''
    cur_citys = []
    j = 0
    n = 0
    for city in city_dict.values():
        cur_citys.append(city[0])
        i = i + 1
        n = n + 1
        if i <= 19 and n < len(city_dict):
            citystr = citystr + city[0] + '|'
        else:
            citystr = citystr + city[0]
            response = None
            while response == None:
                try:
                    response = requests.get(
                        'http://api.weatherdt.com/common/?area={0}&type=observe&key=23bb09b1353b80d890c8723aa4b2b731'.format(
                            citystr), headers=headers)
                except:
                    print("net work connect failed, wait 10 second and connect again")
                    time.sleep(10)
            r_json = response.json();
            cur.execute(
                "select * from weather_obverse where stat_date = '{0}' and substr(d000,1,2) = '{1}'"
                    .format(cur_date,
                            r_json[
                                'observe'][
                                cur_citys[
                                    0]][
                                '1001002'][
                                '000'][
                            0:2]))
            rows = cur.fetchall()
            if (len(rows) == 0 or j == 1):
                j = 1
                for row in cur_citys:
                    sql = '''insert into weather_obverse(city_no,city_name,father_city,stat_date,d000,d002,d003,d004,d005,d006,d007)
                         values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}')''' \
                        .format(row,
                                city_dict[
                                    row][
                                    1],
                                city_dict[
                                    row][
                                    2],
                                cur_date,
                                r_json[
                                    'observe'][
                                    row][
                                    '1001002'][
                                    '000'] \
                                , r_json[
                                    'observe'][
                                    row][
                                    '1001002'][
                                    '002'],
                                r_json[
                                    'observe'][
                                    row][
                                    '1001002'][
                                    '003'],
                                r_json[
                                    'observe'][
                                    row][
                                    '1001002'][
                                    '004'] \
                                , r_json[
                                    'observe'][
                                    row][
                                    '1001002'][
                                    '005'],
                                r_json[
                                    'observe'][
                                    row][
                                    '1001002'][
                                    '006'],
                                r_json[
                                    'observe'][
                                    row][
                                    '1001002'][
                                    '007'], )
                    cur.execute(sql);
                    cur.execute('commit');
                    log = time.strftime("%H:%M:%S") + ' | insert [{0},{1}] success'.format(row, r_json['observe'][row][
                        '1001002']['000'])
                    print(log)
                    file_obj.writelines(log + '\n')
            else:
                log = time.strftime("%H:%M:%S") + ' | data [{0}] has been inserted'.format(
                    r_json['observe'][cur_citys[0]]['1001002']['000'])
                print(log)
                file_obj.writelines(log + '\n')
                break
            i = 0
            citystr = ''
            cur_citys = []
    cur.close()
    db.close()
    file_obj.close()


if __name__ == '__main__':
    get_weather_data()
    get_fz_data()
