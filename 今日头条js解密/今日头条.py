import requests
from urllib import parse
import json
import execjs

url = 'https://www.toutiao.com/api/pc/feed/?'
headers = {

    'accept': 'text/javascript, text/html, application/xml, text/xml, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'ttcid=a5c8f56494de4901a555d17a88123fce15; WEATHER_CITY=%E5%8C%97%E4%BA%AC; SLARDAR_WEB_ID=be6b6c99-8293-4cae-afe5-c14c8f1711d6; csrftoken=cae9681bae00ecd857863ac443630123; tt_webid=6833569956723230216; s_v_web_id=verify_kaxaq47g_tgkusbGW_iZvM_4prQ_BFfn_gwvgXV8mJNQa; __tasessionId=voyskfdc71591064504394; tt_webid=6833569956723230216; tt_scid=cFTy5bPKZLje8heEnIKh1u1l.vqOmIgXoBYEMGnhVjkzf4s7YAhBNJdMjH.IJmMa2768',
    'referer': 'https://www.toutiao.com/',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',

}
with open('今日头条.js', 'r', encoding='utf-8') as f:
    code = f.read()
    ctx = execjs.compile(code)
    res = ctx.call('md5s')

parmas = {
    'max_behot_time': '',  # next['max_behot_time']
    'category': '__all__',
    'utm_source': 'toutiao',
    'widen': '1',
    'tadrequire': 'true',
    'as': res['as'],
    'cp': res['cp'],
    '_signature': res['_signature'],


}

url = url + parse.urlencode(parmas)
print(url)
response = requests.get(url=url, headers=headers ,params=parmas)

print(response.text)

