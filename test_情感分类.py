import requests
import json


def main2():    # 使用鉴权方法，调用 （扫码登录）
    url = "https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify?access_token=24.d9ca570077810a660d12abdc44d664ef.2592000.1704019154.282335-44111758&charset=GBK"

    payload = json.dumps({
        "text": "炒你妈"
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)




import requests
import json

API_KEY = "Nu06pS9LxGQq9n8m8cEdHtTG"
SECRET_KEY = "KNNDIWm7ghPS2ZOQE3XjKPdAsQpCjHUB"


def main(): # 使用HTTP方法调用  所以需要API——key，SECRET_KEY（就像账号，密码要匹配才能进入）
    url = "https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify?charset=GBK&access_token=" + get_access_token()

    payload = json.dumps({
        "text": "炒你妈"
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


if __name__ == '__main__':
    main()
    # main2()