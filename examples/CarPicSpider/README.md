A simple mimic of https://github.com/FindHao/CarPicSpider/blob/master/spider.py

## ֱ������

ֱ�����н����������ļ���`record.txt`��`download_command.bat`

    record.txt�ĸ�ʽΪ��Ʒ����\t��������\tͼƬurl

    download_command.bat������curl.exeִ����������

`result.zip`�ṩ�������ļ���**����ǰ����Star����Ŀ**

# Cache����

��exampleʹ����`Cache=True`��������ʾ��`md5(url)`��Ϊ`�����ļ����ļ���`

�ṩ`cache_files.zip`����ѹ����Ŀ¼�󼴿ɲ������κ���������ʵ�ֿ���ѭ��

# ����˵��

## gethot

    ������֮�ҹ����ֻ���������Ʒ��

    ����һ��dict��{ Ʒ������:[����url��Ʒ��ƴ��]}

## getbrand(url):

    ����һ��Ʒ�Ƶ�url����url���Դ�gethot�������

    �������飬��Ԫ��Ϊ��[���ƣ��۸����ͣ�ͼƬurl������url��id]

    ����ͼƬurl�����滻�������Ϊ640x480����֪����壩��ͼƬurl

## morepic(id):

    ��һ�����͵õ�����ĳ���ͼƬ��id����getbrand���������

    ����ͼƬurl������

    ����url�����滻�������Ϊ640x480����֪����壩��ͼƬurl

