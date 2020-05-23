import requests
import hashlib
import time, random

# 使用hashlib进行md5解密
def md5(e):
    ua = '5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4128.3 Safari/537.36'
    bv = hashlib.md5(ua.encode('utf-8')).hexdigest()
    ts = str(int(time.time() * 1000))
    salt = ts + str(random.randint(0, 10))
    # 返回加密的参数
    return {
        'ts': ts,
        'bv': bv,
        'salt': salt,
        'sign': hashlib.md5(("fanyideskweb" + e + salt + "Nw(nmmbP%A-r6U3EUn]Aj").encode('utf-8')).hexdigest()
    }


def youdao(word):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    pwd = md5(word)
    data = {
        'i': word,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': pwd['salt'],
        'sign': pwd['sign'],
        'ts': pwd['ts'],
        'bv': pwd['bv'],
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME',
    }
    # cookie不可缺少
    headers = {
        "Cookie": '_ga=GA1.2.37083754.1581260484; OUTFOX_SEARCH_USER_ID_NCOO=122841041.90469362; OUTFOX_SEARCH_USER_ID="82816029@10.108.160.18"; JSESSIONID=aaarRYY4OhNgo96yPMIbx; ___rl__test__cookies=1582202548824',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '234',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'fanyi.youdao.com',
        'Origin': 'http://fanyi.youdao.com',
        'Referer': 'http://fanyi.youdao.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4128.3 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',

    }
    response = requests.post(url=url, headers=headers, data=data)
    print(response.json())


if __name__ == '__main__':
    print('输入exit退出程序')
    while True:
        word = input('请输入需要翻译的内容：')
        if word == '':
            print('请输入正确内容')
        if word == 'exit':
            print('程序已退出')
            break
        youdao(word)
