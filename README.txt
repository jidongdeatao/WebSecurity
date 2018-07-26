
WEB安全分为四大模块：
  一、操作系统安全（常见企业级操作系统为Linux：CentOS）
     这部分安全规范 已归纳到GitHub：https://github.com/jidongdeatao/LinuxSafty
     
     这部分安全检测已有自动化脚本：
     https://github.com/jidongdeatao/LinuxTest/tree/master/NewVerson/SecurityTest/TestCase/systemSafe
        检查功能项包括：
        1.所有非root用户的文件权限：
        1）含有敏感信息的文件不得大于600（rw------）对于多个OS用户都需要访问敏感文件的场景都不得大于640（rw-r-----），如：数据库备份恢复
        2）日志文件不得大于640（rw-r-----）
        3）不可执行文件不得大于640（rw-r-----）
        4）可执行文件不得大于750（rwxr-x---）
        5）目录不得大于750（rwxr-x---），有时候目录要求不能大于700（rwx------）"
        2.检查系统中不能安装调试工具：make|gcc|gcc-c++|cpp|gdb|binutils|glibc_devel|flex|tcpdump|mirror|glibc-devel|dexdump|toolbox|Netcat|Wireshark|ethereal
        3.检查系统中的无属主文件
        4.检查进程越权，产品进程是否用root账号启动
        5.检查进程中的敏感信息，关键字："pass|password|passwd|pswd|mima|key|pwd|PINNUMBER|secret|X-Auth-Token|Authorization|sessionID|token|email"
        6.检查进程中是否不允许使用的服务："bootps|pure-ftpd|pppoe|sendmail|isdn|zebra|cupsd|cups-config-daemon|hplip|hpiod|hpssd|bluetooth|hcid|hidd|sdpd|dund|pand|rsh|telnet"
        7.检查系统中是否含有不需要的账号
        8.检查系统账号的的密码加密安全（比如不能用Base64加密）
        9.运行数据库进程的帐号权限应该遵循最小权限原则，要使用操作系统的非管理员权限帐号来运行数据库
        10.检查是否安装了不安全的服务
     
  二、数据库安全（常见企业数据库为MySQL、Redis）
     这部分安全规范 已归纳到GitHub：https://github.com/jidongdeatao/Database/tree/master/DatabaseSafty
     
     MySQL安全检测已有自动化脚本：
     
  三、Docker容器安全
  
  
  四、WEB应用安全
  
  
     
