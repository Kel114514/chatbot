import requests

def _yh_api():
    #backup setu api
    # from https://www.cnblogs.com/ghgxj/p/14219047.html
    url='http://www.dmoe.cc/random.php'
    params = {'return': 'json'}
    return requests.get(url, params=params).json()['imgurl']


def _lolicon_api(**kwargs):
    # from https://api.lolicon.app/#/setu
    url='https://api.lolicon.app/setu/v2'
    res=requests.get(url)
    return res.json()['data'][0]['urls']['original']


def get_setu():
    try:
        return f'[CQ:image,file={_lolicon_api()}]'
    except:
        return '色图寄了'