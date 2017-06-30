## 浙大云盘API

使用EasyLogin完成[浙大云盘](https://pan.zju.edu.cn)登录、上传、分享、下载直链获取

### 使用方法

这是EasyLogin的使用示例，请先访问https://github.com/zjuchenyuan/EasyLogin

下载好EasyLogin.py，并完成依赖安装

    python3 panzju.py 待上传的文件名 学号 浙江大学统一通行证密码

![screenshot](screenshot.jpg)

### 说明

本程序会自动保存、载入登录状态到panzju.status（使用EasyLogin提供的**save**与**load**函数）

所以在cookie没有失效时，不会发起登录请求，此时可以不提供用户名密码参数

#### 函数说明

```
login(xh, password) #使用统一通行证的用户名密码登录
islogin() #是否已经登录,如果已经登录返回token，否则False
upload(token, filename, data, filesize) #上传文件，返回fileid，data为文件二进制数据或者block函数产生的generator， 建议传入filesize
share(token, fileid) #分享文件，返回分享地址file_unique_name
download(file_uniqe_name) #从文件分享地址得到直接下载链接URL，本函数不要求登录，也不会使用登录状态
block(fp) #使用分块上传解决大文件传输的内存问题
```

