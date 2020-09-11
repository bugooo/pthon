### MAC 安装pip报错
urllib3.exceptions.ReadTimeoutError: HTTPSConnectionPool(host='files.pythonhosted.org', port=443): Read timed out

#### 解决办法：
1.在~目录下新建文件夹.pip  mkdir ~/.pip
2.新建配置文件 pip.conf
3.在pip.conf里配置国内源

```
[global]
index-url = http://pypi.douban.com/simple
trusted-host = pypi.douban.com           disable-pip-version-check = true
timeout = 120
```
