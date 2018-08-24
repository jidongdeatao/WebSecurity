密码破解
参考密码破解工具：
https://github.com/jidongdeatao/Security-Tools-List
  破解密码工具：Medusa、THC-hydra、Hashcat
  
弱密码破解的前提是对外开放了SSH、FTP服务

1.SSH弱密码暴力破解


  
2.FTP弱密码暴力破解：
  使用命令：
  python3 ftpScanner.py -H 127.0.0.1 -f pwd.txt
  解释说明：
      ftpScanner.py是FTP弱密码破解的文件
      pwd.txt是自己选择的密码本：格式为username:password
（FTP暴力破解防御：http://www.freebuf.com/column/180296.html）
                        ||
                        \/
  FTP弱密码破解后渗透流程->在FTP服务器上搜索网页->在网页中加入恶意代码






3.Zip文件密码暴力破解：
  使用命令：
  python3 decodeZip.py -f 1.zip -w pwd.txt
  解释说明：
      decodeZip.py是Zip文件密码破解的py文件
      1.zip是加密的Zip文件：自己演示的时候可以使用zip -r 1.zip 1.txt -P 1314命令将1.txt文件压缩成加密的1.zip文件，密码为1314
      pwd.txt是自己选择的密码本
