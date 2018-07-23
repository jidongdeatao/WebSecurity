深度研究XSS

  1.XSS简介
  2.XSS分类
    1）反射
    2）存储
    3）DOM
  3.XSS常用的测试方法
    1）输出点为HTML标签的文本区域，如<textarea></textarea>
        考虑先闭合,如使用</textarea><script>aler(1)</script>
    2）输出点为HTML标签的属性值，如<input type="text" name="address" value="输出点">
        如果input标签输入的字符串会在value项中输出，考虑的情况,
          1.使用引号结束字符串，引人该标签所支持的事件处理器 “onfocus="alert(1)
          2.使用引号结束字符串，再结束前面的标签，引人弹框脚本 "><script>alert(1)</script>
    3）输出点为JavaScript脚本中的字符串，如<script> var a=“输出点”;</script>时，
        可考虑使用引号和分号终止前面点语句，引人弹框脚本，用其他语句衔接后面的语句，或
        使用引号和分号终止前面点语句，引人弹框脚本，用其他语句注释后面的语句
        如将输出点替换为 ";alert(1);b="
    4）输出点为URL位置的属性值，如
        <a href="输出点“>click here</a>
        <embed src=“输出点">
        <iframe src=“输出点">
        <object data=“输出点”>
        可以使用伪协议，如javascript:alert(1);
    5）绕过客户端对特定字符串过滤的限制
        使用burpsuite抓包进行请求拦截，修改参数，然后重新发送
    6）输入点与输出点在不同的模块
        主要针对存储型XSS，寻找输入点与输出点点关联点然后按照上述方式进行判断
    7）输入点在http头字段
        X-Forwarded-For，简称XFF头，它代表客户端，也就是HTTP的请求端真实的IP，只有在通过了
        HTTP代理或者负载均衡服务器才会添加该项。系统有可能会通过该字段获取IP信息记录到页面上来。
        这样只要在该字段的值输入XSS脚本来验证是否存在XSS攻击
        步骤：使用burpsuite工具拦截修改该字段为XSS脚本重新发送报文即可
 4.XSS危害
 5.XSS防护
  输入点进行特殊字符过滤（要放在服务器端进行过滤），输出点进行特殊字符转义
    
            
