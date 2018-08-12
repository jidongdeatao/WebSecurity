File Inclusion:文件包含漏洞

，是指当服务器开启allow_url_include选项时，
就可以通过php的某些特性函数（include()，require()和include_once()，require_once()）利用url去动态包含文件，
此时如果没有对文件来源进行严格审查，就会导致任意文件读取或者任意命令执行。
文件包含漏洞分为本地文件包含漏洞与远程文件包含漏洞，
远程文件包含漏洞是因为开启了php配置中的allow_url_fopen选项（选项开启之后，服务器允许包含一个远程的文件）。
