## �������API

ʹ��EasyLogin��ɡ�������̡���¼���ϴ�������������ֱ����ȡһ����

### ʹ�÷���

����EasyLogin��ʹ��ʾ�������ȷ���https://github.com/zjuchenyuan/EasyLogin

���غ�EasyLogin.py�������������װ

    python3 run.py ���ϴ����ļ��� ѧ�� ͳһͨ��֤����

![screenshot](screenshot.png)

### ˵��

�����֮ǰ����û�з��ʹ�������̣���һ��ִ�п��ܻ�ʧ�ܣ�������һ�ξͺ���

��������Զ����桢�����¼״̬��fangcloud.status��ʹ��EasyLogin�ṩ��**save**��**load**������

������cookieû��ʧЧʱ�����ᷢ���¼����

#### ����˵��

```
login(xh,password) #ʹ��ͳһͨ��֤���û��������¼
islogin() #�Ƿ��Ѿ���¼,����Ѿ���¼����token������False
upload(token,filename,data) #�ϴ��ļ�������fileid
share(token,fileid) #�����ļ������ط����ַfile_unique_name
download(file_uniqe_name) #���ļ������ַ�õ�ֱ����������URL����������Ҫ���¼
```