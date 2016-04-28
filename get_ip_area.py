#-*- coding:utf-8 -*-
import urllib2
import json


def get_ip_area(ip):
    try:
        apiurl = "http://ip.taobao.com/service/getIpInfo.php?ip=%s" % ip
        content = urllib2.urlopen(apiurl).read()
        data = json.loads(content)['data']
        code = json.loads(content)['code']
        if code == 0:   # success
            if data['region'] == data['city']:
                return data['region']
            else:
                return data['region']+data['city']        
        else:  
            return "未知地区"  
    except Exception as ex:  
        return "未知地区"  
  
if __name__ == '__main__':  
    ip = '61.148.124.38'   
    print get_ip_area(ip)  
