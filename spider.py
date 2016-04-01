#-*- coding:utf-8 -*-
import re
import requests


class Spider(object):

    def __init__(self, url):
        self._url = url

    def get_sourcecode(self):
        '''取地址的源代码'''
        con = requests.get(self._url)
        try:
            code = unicode(con.content, con.encoding).encode("utf8")
        except Exception, e:
            code = con.text.encode("utf8")
        finally:
            return code

    def save_content(self, url, path, name, headers={}):
        '''将网页内容保存到指定路径'''
        try:
            con = requests.get(url, headers=headers)
            fp = open(path+"\\"+name, 'wb')
            fp.write(con.content)
            fp.close()
            return True
        except Exception, e:
            print(e)
            return False

# 爬取腾牛个性网http://www.qqtn.com/tx/haokantx_1.html头像
# 未加防盗链网站，requests的headers为空即可直接爬取


def foo1():
    print('爬取腾牛个性网http://www.qqtn.com/tx/haokantx_1.html头像')
    url1 = 'http://www.qqtn.com/tx/haokantx_1.html'
    j = 1
    for i in range(1, 19):
        p_url = re.sub('haokantx_1', 'haokantx_'+str(i), url1)
        a = Spider(p_url)
        urllist = re.findall(
            'src="(http://pic.*?.[jpg|png|gif])"', a.get_sourcecode(), re.S)
        for url in urllist:
            print('正在下载第{0}张图片...'.format(j))
            if(a.save_content(url, 'D:\\test1', str(j)+'.jpg')):
                j += 1
    print('下载完毕，共下载{0}张图片。'.format(j-1))

# 爬个性网qq头像http://www.gexing.com/qqtouxiang/new/1 （1-274）
# 该网站加了防盗链，不能直接爬取，需要伪造下Referer加入headers中


def foo2():
    print('爬个性网qq头像http://www.gexing.com/qqtouxiang/new/1 （1-274）')
    url2 = 'http://www.gexing.com/qqtouxiang/new/1'
    j = 1
    for i in range(1, 274):
        p_url = re.sub('1', str(i), url2)
        a = Spider(p_url)
        urllist = re.findall(
            '<li data-pid(.*?)</li>', a.get_sourcecode(), re.S)
        for url in urllist:
            url = re.findall('src="(http.*?)"', url, re.S)
            print('正在下载第{0}张图片...'.format(j))
            # 在此伪造下Referer，即为源代码的网址
            headers = {"Referer": p_url}
            if(a.save_content(url[0], 'E:\\test3', str(j)+'.jpg', headers)):
                j += 1
    print('下载完毕，共下载{0}张图片。'.format(j-1))


if __name__ == '__main__':
    foo1()
    # foo2()
