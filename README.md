# EasyLogin

## Requirements ���Ȱ�װ����

    pip3 install -U requests[socks] -i https://pypi.doubanio.com/simple
    pip3 install bs4 -i https://pypi.doubanio.com/simple
    
## Note ˵��

Useful thing is only `EasyLogin.py`. All directories are examples, not needed for running.

ֻ��Ҫ����EasyLogin.py�͹��ˣ�examples�ļ�����ʹ��EasyLogin������������

## Quickstart �����Կ���~

Using EasyLogin is very EASY!

First, import it and create an object:  ���ȵ����������һ������

    from EasyLogin import EasyLogin
    a = EasyLogin()
    
Then, make a get request or post request: ����һ������

    a.get("http://ip.cn")

Finally, I need the `code` tag: ����Ҫ�Ķ�����`<code>`��ǩ���棬���ǰ����ó���

    IP,location = a.f("code",attrs={})
    print(IP)
    print(location)

Moreover, I also need img, css, js and text: �һ���Ҫ��ҳ�г��ֵ�ͼƬ��CSS��JS�������Լ��ı�

    print(a.img())
    print(a.css())
    print(a.js())
    print(";".join(a.text()))

## Documentation �ĵ�

�����...
    
�򵥵�˵����get��post��self.b����BeautifulSoup�Ķ���