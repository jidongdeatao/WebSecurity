SQL Injection

最常见的检测SQL注入的方法是通过在输入处添加一个单引号(&#039;)并且期待（系统）返回一个错误，有些应用程序并不会返回错误。这个时候我们就会利用true/false语句来检查是否这个应用程序会受到SQL注入的攻击。

为了随机的找到还有SQL注入的脆弱性的网站，你能够使用如下格式的语句利用google dork：inurl:news.php id =1?将会出现一堆google dork的数据并且为你过滤你搜索得到的结果提供了可能。
google dork的列表：
https://github.com/jidongdeatao/Security-Tools-List/tree/master/Google%20Hacking

SQL注入：
  测试思路：
    1）白盒测试：
      通过WEB源代码审计，查看是否使用预编译绑定变量（参数化接口查询）来杜绝SQL注入漏洞
      测试依据：是否正确使用预编译语句类型化SQL参数
      jAVA安全编码规则：禁止采用未经校验的输入参数直接串联来构造可执行SQL语句
        说明：例如：
        String sql = "select status from Uers where Username = "" + txtUserName.Text + "";
        这种方式很容易被SQL注入攻击；
        对于Java/JSP语言，使用预编译语句PreparedStatement代替直接执行的语句执行Statement。
        使用预编译语句Prepared Statement，类型化SQL参数将检查输入的类型，确保输入值在数据库中当作字符串、数字、日期、或boolen等值
        而不是可执行代码进行处理，从而防止SQL注入攻击，而且由于PreparedStatement对象已经预编译过，所以执行速度要
        比Statement对象快，还可以提高效率。
        
        测试步骤：
        1.关键字查找
          可使用Search and replace 或 PowerGREP 工具查找源码中的关键字
            关键字如下：
              PHP语言关键字：prepare 、execute
              JAVA语言关键字：PreparedStatement
        2.分析代码
          考虑到测试人员的代码水平不一，如果不确定可找开发帮忙定位分析。当通过关键字定位到具体代码段段时候，查看当前是否使用如下方式类型化SQL参数：
            String selectStatement = “Select * From Uer where userId = ?";
            PreparedStatement prepstmt = con.prepareStatement(selectStatement);
            prepStmt setString(1,userId);
            ResultSet rs = prepStmt.executeQuery();
        
              
    2）黑盒测试：
      神器——sqlmap工具检测
      sqlmap的安装这里不进行展开。
      由于测试环境一般都需要登录认证，建议使用burpsuite截取包含认证cookie的报文进行SQL注入测试，截取整个request请求报文参数测试覆盖参数更加全面。
      步骤1: 
          使用burpsuite截取需要测试的request请求
          然后将截取的request请求报文全部保存到一个txt文档中，如：inject.txt
      步骤2:
          检测目标API是否存在注入点。
          通过执行命令：
          sqlmap.py -r C;\inject.txt -b
            参数说明：-r 表示读取本地文件，后面加上文件的路径
                    -b 表示探测目标系统的数据库和操作系统的版本信息
          如果中请求中发现sql注入点，结果会显示目标数据库及目标系统的版本信息。
      步骤3:
          探测目标数据库
          通过执行命令：
          sqlmap.py -r C;\inject.txt --dbs
      步骤4:
          探测目标数据库的tables信息
          通过执行命令：
          sqlmap.py -r C;\inject.txt -D XXX --tables
            参数说明：-D 表示探测指定的数据库信息，后面加数据库名称
                    --tables 表示探测数据库中的表信息
      步骤5:
          探测目标数据库的columns
          通过执行命令：
          sqlmap.py -r C;\inject.txt -D XXX -T YYY --columns
            参数说明：-D 表示探测指定的数据库信息，后面加数据库名称
                    -T 表示探测指定的table中的信息
                    --columns 表示列出table中的columns信息
      步骤6:
          探测目标数据库的字段信息
          通过执行命令：
          sqlmap.py -r C;\inject.txt -D XXX -T YYY --columns -dump
            参数说明：--dump 表示列出表中的字段信息      
      
     
      sqlmap+burpsuite自动化测试：参见文档sqlmap+burpsuite.txt
