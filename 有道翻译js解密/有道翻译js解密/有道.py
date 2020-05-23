import execjs
import requests

def get_js_function(js_path, func_name, func_args):
    '''
    获取指定目录下的js代码, 并且指定js代码中函数的名字以及函数的参数。
    :param js_path: js代码的位置
    :param func_name: js代码中函数的名字
    :param func_args: js代码中函数的参数
    :return: 返回调用js函数的结果
    '''

    with open(js_path, encoding='utf-8') as fp:
        js = fp.read()
        ctx = execjs.compile(js)
        return ctx.call(func_name, func_args)


def youdao(word):
    '''
    有道翻译
    :param word: 传入的待翻译的词汇
    :return: 返回的翻译后的内容
    '''
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    pwd = get_js_function('有道.js', 'youdao', word)
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
    response = requests.post(url, data=data, headers=headers)
    return response.json()


if __name__ == '__main__':
    print('输入exit退出程序')
    while True:
        word = input('请输入需要翻译的内容：')
        if word == '':
            print('请输入正确内容')
        if word == 'exit':
            print('程序已退出')
            break
        print(youdao(word))
