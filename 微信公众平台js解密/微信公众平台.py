import requests
import execjs


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


def weixingzh(account, password):
    url = 'https://mp.weixin.qq.com/cgi-bin/bizlogin?action=startlogin'
    pwd = get_js_function('微信公众平台.js', 'md5', password)

    data = {
        'username': account,
        'pwd': pwd,
        'imgcode': '',
        'f': 'json',
        'userlang': 'zh_CN',
        'redirect_url': '',
        'token': '',
        'lang': 'zh_CN',
        'ajax': '1',
    }

    headers = {

        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-length': '129',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://mp.weixin.qq.com',
        'referer': 'https://mp.weixin.qq.com/',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    response = requests.post(url=url, headers=headers, data=data)
    # print(data)
    # print(response.text)
    # with open('微信公众平台.html', 'w', encoding='utf-8') as fp:
    #     fp.write(response.text)

if __name__ == '__main__':
    account = input('请输入账号：')
    password = input('请输入密码：')
    weixingzh(account, password)