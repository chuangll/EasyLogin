# EasyLogin.py

��requests��BeautifulSoup��һ����װ��д������������~

## ���Ȱ�װ��������֧��Python3

    pip3 install -U requests[socks] bs4 -i https://pypi.doubanio.com/simple/ --trusted-host pypi.doubanio.com
    
## ˵��

ֻ��Ҫ����EasyLogin.py�͹��ˣ�examples�ļ�����ʹ��EasyLogin������������

## �����Կ���~

���ȵ����������һ������

    from EasyLogin import EasyLogin
    a = EasyLogin()
    
Ȼ����һ������

    html = a.get("http://ip.cn") #����ҳԴ�����е�code��ǩ�ں���������Ҫ�� `�Լ���IP` �� `�Լ������ĵ���λ��`

����Ҫ�Ķ�����`<code>`��ǩ���棬���ǰ����ó���

���ģ���ִ����get��post��a.b����һ��BeautifulSoup����

    #find_all��BeautifulSoup�ķ��������� `��ǩ����` �� `��ǩ���Ե��ֵ�`
    code_tags = a.b.find_all("code",attrs={}) 
    myIP = code_tags[0].text
    mylocation = code_tags[1].text

> Ϊ�˼�����������ṩ��f��������ʵһ���ò��������������Ϊ����ȡ�������������б�ǩ���ı�����

>    myIP,mylocation = a.f("code",attrs={})

�����IP��location����print��~

    print(myIP) #������Լ���IP
    print(mylocation) #���硰�㽭ʡ������ ���š�

�һ���Ҫ��ҳ�г��ֵ�ͼƬ��CSS��JS�������Լ��ı�����Щ����Ҳ�����ã������ͺ�

    print(a.img())
    print(a.css())
    print(a.js())
    print(";".join(a.text()))

## �ĵ�

�����...
    
�򵥵�˵����get��post��self.b����BeautifulSoup�Ķ���

## ��������

> ����������ô�򵥵ر�д������

1. �����һ���ֶ��Ĳ����������̣��۲��������о�

2. ��Chrome�����߹��߻���Burp���鿴�ؼ��Ե������

3. д���ʼ���Ĵ��룬�������a=EasyLogin()

4. �����������ݣ�����ҳԴ������������������ҵ���˿����ƴ�ճ���ȷ�������

    ��һ����Ҳ����Ҫ��get����Դ����õ�token�Ĳ����͵õ�cookie
    
    ��EasyLogin���Լ������cookie��������ģ�

5. ����post���󣬷������ص�����

    �����Ǹ�json������x.json()
    
    һ����ܾ��Ǹ�ҳ�棬�Ǿ�a.b.find��
    
    ��a��EasyLogin�Ķ���a.b��BeautifulSoup�Ķ��󣬴���[����](http://cuiqingcai.com/1319.html)������BeautifulSoup��ô�ã�

6. ����������ȷ��Ӧ�ͻ�������������������ȡ�ɺ�������װ���ࡢ���ҷ���һ��Pull����