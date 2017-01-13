# EasyLogin.py

��requests��BeautifulSoup��һ����װ��д������������~

## Requirements ���Ȱ�װ��������֧��Python3

    pip3 install -U requests[socks] bs4 -i https://pypi.doubanio.com/simple/ --trusted-host pypi.doubanio.com
    
## Note ˵��

Useful thing is only `EasyLogin.py`. All directories are examples, not needed for running.

ֻ��Ҫ����EasyLogin.py�͹��ˣ�examples�ļ�����ʹ��EasyLogin������������

## Quickstart �����Կ���~

Using EasyLogin is very EASY!

First, import it and create an object:  ���ȵ����������һ������

    from EasyLogin import EasyLogin
    a = EasyLogin()
    
Then, make a get request or post request: ����һ������

    html = a.get("http://ip.cn") #����ҳԴ�����е�code��ǩ�ں���������Ҫ�� `�Լ���IP` �� `�Լ������ĵ���λ��`

Finally, I need the `code` tag: ����Ҫ�Ķ�����`<code>`��ǩ���棬���ǰ����ó���

A general method is use `a.b` as a BeautifulSoup object: ��ִ����get��post��a.b����һ��BeautifulSoup����

    code_tags = a.b.find_all("code",attrs={}) #find_all��BeautifulSoup�ķ��������� `��ǩ����` �� `��ǩ���Ե��ֵ�`
    myIP = code_tags[0].text
    mylocation = code_tags[1].text

> To simplify this, I created a `f` method, return text of all tags that match tag name and attrs: 

> Ϊ�˼�����������ṩ��f��������ʵһ���ò��������������Ϊ����ȡ�������������б�ǩ���ı�����

>    myIP,mylocation = a.f("code",attrs={})

Finally, just print them~ �����IP��location����print��~

    print(myIP) #������Լ���IP
    print(mylocation) #���硰�㽭ʡ������ ���š�

Moreover, I also need img, css, js and text: �һ���Ҫ��ҳ�г��ֵ�ͼƬ��CSS��JS�������Լ��ı�

��Щ����Ҳ�����ã������ͺ�

    print(a.img())
    print(a.css())
    print(a.js())
    print(";".join(a.text()))

## Documentation �ĵ�

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