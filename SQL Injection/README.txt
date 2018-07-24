SQL Injection

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
        
        
          
    2）黑盒测试：
      神器——sqlmap工具检测
      
