import requests,json,time

class download:
    def __init__(self):
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36','authorization':'Bearer SEV0001MTUyODA5Njg1MXxLRy02MkRtRDhucnpHYS13QldtX2o3Nm9URnU3dXhQUi1QQkxwLXhoMU1pbWZfdTZYbW1sTE1tN0FFLXRHaXB4cGljMjVMd0tIUklwVjdyUU42UkdsQ3FrMzdEYW1IVGIweUd6UGM2RFZ2ODNWalV5a28za0ZGUTI5aGNmRmpMdmUwNW0xLUFmNk1BQnBpd3FBcUdteHExTXVuQzRCUjk2QTdiT3BTZlFZTVVhaVhJPXynsDsuLyanQx3JAuJWcEmTvmQVvZjWum7bdKi6eEgEag=='}
        self.proxie={}
    def download(self,url):
        try:
            # proxies={'http':'http://'+ip[1]+':'+ip[2]}
            proxies=''
            content=requests.get(url,headers=self.headers,proxies=proxies)
            if content.status_code==200:
                text=content.content.decode('utf-8')
                text=json.loads(text)
                return text
            else:
                print(url)
                print(content)
        except Exception as e:
            # proxies={'http':'http://'+ip[1]+':'+ip[2]}
            print('download error')
            time.sleep(100)
            proxies=''
            content=requests.get(url,headers=self.headers,proxies=proxies)
            if content.status_code==200:
                text=content.content.decode('utf-8')
                text=json.loads(text)
                return text

            raise e
            # joom post  show more 返回dict字典包含商品id和网址
    def post(self,newUrl,itemsId):
        url=newUrl[0]
        pageToken=newUrl[1]
        # itemsId="1473502936226769818-70-2-118-2760164976"
        headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
        'content-type':'application/json',
        'origin':'https://www.joom.com',
        'authorization':'Bearer SEV0001MTUyODA5Njg1MXxLRy02MkRtRDhucnpHYS13QldtX2o3Nm9URnU3dXhQUi1QQkxwLXhoMU1pbWZfdTZYbW1sTE1tN0FFLXRHaXB4cGljMjVMd0tIUklwVjdyUU42UkdsQ3FrMzdEYW1IVGIweUd6UGM2RFZ2ODNWalV5a28za0ZGUTI5aGNmRmpMdmUwNW0xLUFmNk1BQnBpd3FBcUdteHExTXVuQzRCUjk2QTdiT3BTZlFZTVVhaVhJPXynsDsuLyanQx3JAuJWcEmTvmQVvZjWum7bdKi6eEgEag=='
        }
        data={ 
            "count":48,
            "filters":
                [
                    {
                    "id":"categoryId",
                    "value":
                        {
                        "items":[{"id": itemsId}],
                        "type":"categories"
                        }
                    }
                ]
            }
        if pageToken is None:
            pass
        else:
            data['pageToken']=pageToken

        try:
            content=requests.post(url,headers=headers,data=json.dumps(data),proxies=self.proxie)
            # print(json.loads(content.content)['contes'])
            if content.status_code==200:
                text=json.loads(content.content)
                return text
            else:
                time.sleep(60)
                content=requests.post(url,headers=headers,data=json.dumps(data),proxies=self.proxie)
                # print(json.loads(content.content)['contes'])
                if content.status_code==200:
                    text=json.loads(content.content)
                    return text
        except Exception as e:
            
            time.sleep(60)
            content=requests.post(url,headers=headers,data=json.dumps(data),proxies=self.proxie)
            # print(json.loads(content.content)['contes'])
            if content.status_code==200:
                text=json.loads(content.content)
                return text
            raise e

    # 设置代理
    def setProxie(self,proxie):
        self.proxie=proxie

# d=download()
# h=d.post('https://api.joom.com/1.1/search/products?language=en-US&currency=USD&_=jh5us5lu',None)
# print(h)